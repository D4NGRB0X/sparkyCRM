from django.db import models
from django.db.models import F, Q, When, Case


class OwnerInfo(models.Model):

    CONTACT_TYPE = [
        ('On boarding', 'On boarding'),
        ('Active', 'Active Paid'),
        ('Former', 'Former')
    ]

    ACCOUNT_MNGR = [
        ('Thomas', 'Thomas'),
        ('Patrick', 'Patrick')
    ]

    owner_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personal_email = models.EmailField(max_length=255)
    corp_email = models.EmailField(max_length=255)
    phone_1 = models.CharField(("Phone ex. 123-123-4567"), max_length=20)
    # (optional)
    phone_2 = models.CharField(
        ("Alt Phone ex. 123-123-4567"), max_length=20, blank=True)
    home_address = models.CharField(max_length=255)
    # (optional)
    old_home_address = models.CharField(
        ("Previous Address"), max_length=255, blank=True)
    # (secured field)
    ssn = models.CharField(max_length=9)
    corp_name = models.CharField(max_length=255)
    # (optional)
    second_corp = models.CharField(max_length=255, blank=True)
    # (link back to referring owner)
    referral = models.URLField(max_length=200, blank=True)
    date_of_birth = models.DateField()
    contact_type = models.CharField(max_length=255, choices=CONTACT_TYPE)
    account_manager = models.CharField(max_length=255, choices=ACCOUNT_MNGR)
    gdrive = models.URLField(max_length=200)
    payments = models.IntegerField(default=0)
    # Case(
    #         When(contact_type='Active', then=250), default=0,
    #         output_field=models.PositiveIntegerField
    #         )

    def __str__(self):
        return self.first_name

    # def __init__(self, contact_type):
    #     self.contact_type = contact_type.choice

class ProspectiveOwner(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personal_email = models.EmailField(max_length=255)
    phone_1 = models.CharField(("Phone ex. 123-123-4567"), max_length=20)
    home_address = models.CharField(max_length=255)
    contact_date = models.DateField()
    referred_by = models.CharField(max_length=255)
    notes = models.TextField()

    def __str__(self):
       return self.first_name