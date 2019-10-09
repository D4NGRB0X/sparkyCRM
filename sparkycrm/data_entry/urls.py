from django.urls import path
from . import views


urlpatterns = [
    path('', views.Data, name='crm_data'),
    path('<int:owner_id>', views.OwnerPage, name='owner'),
    path('restricted/<int:owner_id>', views.OwnerPageRestricted, name='restricted'),
    path('newowner', views.NewOwner, name='newowner'),
    path('update_owner', views.OwnerUpdate, name='update_owner'),
    path('newprospect', views.NewProspect, name='newprospect'),
    path('prospects', views.Prospects, name='prospects'),
    path('prospect/<int:id>', views.ProspectPage, name='prospect'),
    path('update_prospect', views.ProspectUpdate, name='update_prospect'),
]
