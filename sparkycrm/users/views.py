from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

def login(request):
    return render(request, 'user_interface/login.html')

def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_admin:
        # user is an admin
        return redirect("/admin")
    
    elif request.user.is_appstaff:
        # user is an application staff
        return redirect("/owner")
    else:
        return redirect("/restricted")