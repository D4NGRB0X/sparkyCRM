from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_admin = models.BooleanField('Admin', default=False)
    is_appstaff = models.BooleanField('AppStaff', default=False)
    is_rep = models.BooleanField('OutsideRep', default=False)

    #  models.ForeignKey('AccessLevel', on_delete=models.CASCADE,
    #                              related_name='Admin', related_query_name='accesslevel')

class AccessLevel(models.Model):
    ACCESS_LEVEL = [
    ('Admin','Admin'),
    ('AppStaff','AppStaff'),
    ('OutsideRep','Rep')
    ]
    
    user = models.OneToOneField(CustomUser, verbose_name=("Access Level"), on_delete=models.CASCADE)
    access_level = models.CharField(("Set Access Level"), max_length=50, choices=ACCESS_LEVEL, default='OutsideRep')

    def __str__(self):
        return self.access_level
    
    def set_access(self, access_level):
        if access_level == 'Admin':
            CustomUser.is_admin = True
            return CustomUser
        elif access_level == 'AppStaff':
            CustomUser.is_appstaff = True
            return CustomUser
        else:
            CustomUser.is_rep = True
            return CustomUser