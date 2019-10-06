from django.db import models
from data_entry.models import OwnerInfo


def payment():
    owner = OwnerInfo
    owner
    if owner.objects.get(contact_type) == 'Active':
        owner.payments = 250
        owner.save(update_fields=['payments'])
        print("yes")
        # return owner.payments
    else:
        owner.payments = models.IntegerField(default=0)
        print("nope")
        return owner.payments
