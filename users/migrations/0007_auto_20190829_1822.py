# Generated by Django 2.2.4 on 2019-08-30 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_accesslevel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('is_admin', 'Admin'), ('is_appstaff', 'AppStaff'), ('is_rep', 'OutsideRep'))},
        ),
    ]
