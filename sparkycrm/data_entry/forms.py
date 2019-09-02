from django import forms
from .models import OwnerInfo

class CorpInfoForm(forms.ModelForm):
    model = OwnerInfo
    