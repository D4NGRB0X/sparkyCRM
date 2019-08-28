from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, AccessLevel

class CustomUserInline(admin.StackedInline):
    model = AccessLevel
    can_delete = False
    verbose_name_plural = 'Access Level'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username', 'email',]
    inlines = [CustomUserInline]

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
