from django.http import HttpResponse
from django.shortcuts import render
from .models import CorpInfo
from django.contrib.auth.decorators import login_required

@login_required
def Data(request):
    corps = CorpInfo.objects.all()
    return render(request,'data_entry/owner_list.html',{'corps': corps})

@login_required
def OwnerPage(request, corp_id):
    owner = CorpInfo.objects.get(pk=corp_id)
    return render(request, 'data_entry/owner_info.html', {'owner': owner})

@login_required
def OwnerPageRestricted(request, corp_id):
    owner = CorpInfo.objects.get(pk=corp_id)
    return render(request, 'data_entry/owner_info_restricted.html', {'owner': owner})