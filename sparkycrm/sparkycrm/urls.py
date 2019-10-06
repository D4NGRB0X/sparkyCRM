"""sparkycrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as ui
from django.contrib.auth import views as auth_views
from data_entry import views as data
urlpatterns = [
    path('backend/', admin.site.urls),
    # data.OwnerPage, name='owner'),
    path('owner/', include('data_entry.urls'), name='owner'),
    path('restricted/', data.OwnerPageRestricted, name='restricted'),
    path('newowner', data.NewOwner, name='newowner'),
    path('', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    path('login_success/', ui.login_success, name='login_success'),
    path('prospect/', data.ProspectiveOwner, name='prospect')
]
