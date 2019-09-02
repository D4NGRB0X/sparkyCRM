from django.http import HttpResponse
from django.shortcuts import render
from .models import OwnerInfo
from .forms import CorpInfoForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def Data(request):
    corps = OwnerInfo.objects.all()
    return render(request,'data_entry/owner_list.html',{'corps': corps})

@login_required
@permission_required('users.is_appstaff')
def OwnerPage(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info.html', {'owner': owner})

@login_required
def OwnerPageRestricted(request, owner_id):
    owner = OwnerInfo.objects.get(pk=owner_id)
    return render(request, 'data_entry/owner_info_restricted.html', {'owner': owner})

@login_required
def NewOwner(request):
    form = CorpInfoForm()
    return render(request,'new_owner_form.html',{'form': form})