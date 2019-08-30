from django.urls import path
from . import views


urlpatterns = [
    path('', views.Data, name='crm_data'),
    path('<int:corp_id>', views.OwnerPage, name='owner_info'),
    path('restricted/<int:corp_id>', views.OwnerPageRestricted, name='owner_restricted')
]
