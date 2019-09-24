from django.db import models
# from .models import CorpInfo


def payment(self, contact_type):
    if contact_type.choices == 'Active':
        payments = models.IntegerField(default=250)
        return payments
    else:
        payments = models.IntegerField(default=0)
        return payments
