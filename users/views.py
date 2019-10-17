from django.shortcuts import render, redirect
from .models import CustomUser
from data_entry.models import OwnerInfo

def login(request):
    return render(request, 'users/login.html')

def login_success(request):
        return redirect("/owner")
#     if request.user.has_perm('users.is_appstaff'):
#         return redirect("/owner")
# #     """
# #     Redirects users based on whether they are in the admins group
# #     """
# #     if CustomUser.has_perm('users.is_admin'):
# #         # user is an admin
# #         return redirect("/admin")
    
# #     elif CustomUser.has_perm('users.is_appstaff'):
# #     #     # user is an application staff
# #         return redirect("/owner")
#     else:
        
