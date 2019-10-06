from django.http import HttpResponse
from django.shortcuts import render
from .models import OwnerInfo
from .forms import OwnerInfoForm, IntakeForm
from django.contrib.auth.decorators import login_required, permission_required
from data_entry.payments import payment


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
    return render
    (request, 'data_entry/owner_info_restricted.html', {'owner': owner})

@login_required
def Prospect(request):
    prospect = ProspectiveOwner.objects.all()
    return render(request, 'data_entry/owner_list.html', {'prospect': prospect})

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
def ProspectiveOwner(request):
    if request.method == 'POST':
        form = IntakeForm(request.POST)
        if form.is_valid():
            form.save()
    form = IntakeForm()
    return render(request, 'data_entry/new_owner_form.html', {'form': form})