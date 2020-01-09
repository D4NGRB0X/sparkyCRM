from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from sparkycrm.decorator import login_check
from .models import OwnerInfo, ProspectiveOwner
from .forms import OwnerInfoForm, ProspectForm, OwnerUpdateForm, ProspectUpdateForm
from django.contrib.auth.decorators import login_required, permission_required
from data_entry.payments import payment


# Owner Views
# @login_check
@login_required
def Data(request):
    corps = OwnerInfo.objects.all()
    return render(request, 'data_entry/owner_list.html', {'corps': corps})


# @login_check
@login_required
@permission_required('users.is_appstaff')
def OwnerPage(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info.html', {'owner': owner})


# @login_check
@login_required
def OwnerPageRestricted(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info_restricted.html', {'owner': owner})


# Prospective Owner views
# @login_check
@login_required
@permission_required('users.is_admin')
def Prospects(request):
    prospect = ProspectiveOwner.objects.all()
    return render(request, 'data_entry/prospect_list.html', {'prospect': prospect})


# @login_check
@login_required
@permission_required('users.is_admin')
def ProspectPage(request, id):
    prospect = ProspectiveOwner.objects.get(pk=id)
    return render(request, 'data_entry/prospect_info.html', {'prospect': prospect})


# Forms
# @login_check
@login_required
@permission_required('users.is_admin')
def NewOwner(request):
    if request.method == 'POST':
        form = OwnerInfoForm(request.POST)
        if form.is_valid():
            form.save()
    form = OwnerInfoForm()
    return render(request, 'data_entry/new_owner_form.html', {'form': form})


# @login_check
@login_required
@permission_required('users.is_admin')
def OwnerUpdate(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    if request.method == 'POST':
        form = OwnerUpdateForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('/owner')
    form = OwnerUpdateForm(instance=owner)
    return render(request, 'data_entry/owner_update_form.html', {'form': form, 'owner': owner})


# @login_check
@login_required
@permission_required('users.is_admin')
def NewProspect(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
    form = ProspectForm()
    return render(request, 'data_entry/new_prospect_form.html', {'form': form})


# @login_check
@login_required
@permission_required('users.is_admin')
def ProspectUpdate(request, id):
    prospect = ProspectiveOwner.objects.get(pk=id)
    if request.method == 'POST':
        form = ProspectUpdateForm(request.POST, instance=prospect)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Prospect Updated')
            return redirect('/prospects')
    form = ProspectUpdateForm(instance=prospect)
    return render(request, 'data_entry/prospect_update_form.html', {'form': form, 'prospect': prospect})
