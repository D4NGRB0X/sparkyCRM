from django.urls import path
from . import views


urlpatterns = [
    path('', views.Data, name='crm_data'),
    path('<int:owner_id>', views.OwnerPage, name='owner'),
    path('restricted/<int:owner_id>', views.OwnerPageRestricted, name='restricted'),
    path('newowner', views.NewOwner, name='newowner'),
]
