from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   
    is_admin=models.BooleanField('Admin', default=False)
    is_appstaff=models.BooleanField('AppStaff', default=False)
    is_rep=models.BooleanField('OutsideRep', default=False)
    
    class Meta:
        permissions = (
            ('is_admin','Admin'),
            ('is_appstaff','AppStaff'),
            ('is_rep','OutsideRep')
           )

        #  models.ForeignKey('AccessLevel', on_delete=models.CASCADE,
        #                              related_name='Admin', related_query_name='accesslevel')


class AccessLevel(models.Model):
    ACCESS_LEVEL = [
        ('Admin', 'Admin'),
        ('AppStaff', 'AppStaff'),
        ('OutsideRep', 'Rep')
    ]

    user = models.OneToOneField(CustomUser, verbose_name=(
        "Access Level"), on_delete=models.CASCADE)
    access_level = models.CharField(
        ("Set Access Level"), max_length=50, choices=ACCESS_LEVEL, default='OutsideRep')

    def __str__(self):
        return self.access_level

    def set_access(self, access_level, request):
        if access_level == 'Admin':
            user = request.user.has_perm('users.is_admin')
            return user
        elif access_level == 'AppStaff':
            user = request.user.has_perm('users.is_appstaff')
            return user
        else:
            user = request.user.has_perm('users.is_rep')
            return user
            
