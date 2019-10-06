from django import forms
from .models import OwnerInfo , ProspectiveOwner


class OwnerInfoForm(forms.ModelForm):

    class Meta:
        model = OwnerInfo
        fields = (
            'first_name', 'last_name', 'personal_email', 'corp_email',
            'phone_1', 'phone_2', 'home_address', 'old_home_address',
            'ssn', 'corp_name', 'second_corp', 'referral', 'date_of_birth',
            'contact_type', 'account_manager', 'gdrive',
        )

class IntakeForm(forms.ModelForm):

        class Meta:
            model = ProspectiveOwner
            fields = (
                'first_name', 'last_name', 'personal_email', 'home_address',
                'contact_date', 'referred_by', 'notes',
            )