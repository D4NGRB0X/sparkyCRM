from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import OwnerInfo, ProspectiveOwner
from .forms import OwnerInfoForm, ProspectForm, OwnerUpdateForm, ProspectUpdateForm
from django.contrib.auth.decorators import login_required, permission_required
from data_entry.payments import payment

#Owner Views
@login_required
def Data(request):
    corps = OwnerInfo.objects.all()
    return render(request, 'data_entry/owner_list.html', {'corps': corps})


@login_required
@permission_required('users.is_appstaff')
def OwnerPage(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info.html', {'owner': owner})


@login_required
def OwnerPageRestricted(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info_restricted.html', {'owner': owner})


#Prospective Owner views
@login_required
@permission_required('user.is_admin')
def Prospects(request):
    prospect = ProspectiveOwner.objects.all()
    return render(request, 'data_entry/prospect_list.html', {'prospect': prospect})


@login_required
@permission_required('users.is_admin')
def ProspectPage(request, id):
    prospect = ProspectiveOwner.objects.get(pk=id)
    return render(request, 'data_entry/prospect_info.html', {'prospect': prospect})


#Forms
@login_required
@permission_required('user.is_admin')
def NewOwner(request):
    if request.method == 'POST':
        form = OwnerInfoForm(request.POST)
        if form.is_valid():
            form.save()
    form = OwnerInfoForm()
    return render(request, 'data_entry/new_owner_form.html', {'form': form})

@login_required
@permission_required('user.is_admin')
def OwnerUpdate(request):
    if request.method == 'POST':
        form = OwnerUpdateForm(request.POST, instance=request.owner)
        if form.is_valid():
            form.save()
            messages.success(request, f'Owner Info Updated')
            return redirect('owner')
    form = OwnerUpdateForm()
    return render(request, 'data_entry/owner_update_form.html', {'form': form})

@login_required
@permission_required('user.is_admin')
def NewProspect(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            form.save()
    form = ProspectForm()
    return render(request, 'data_entry/new_prospect_form.html', {'form': form})

@login_required
@permission_required('user.is_admin')
def ProspectUpdate(request):
    if request.method == 'POST':
        form = ProspectUpdateForm(request.POST, instance=request.ProspectiveOwner)
        if form.is_valid():
            form.save()
            messages.success(request, f'Prospect Updated')
            return redirect('prospect')
    form = ProspectUpdateForm()
    return render(request, 'data_entry/prospect_update_form.html', {'form': form})