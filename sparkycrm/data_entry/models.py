from django.db import models 
# from .payments import payment

class OwnerInfo(models.Model):

   
    CONTACT_TYPE = [
        ('On boarding', 'On boarding'),
        ('Active', 'Active Paid'),
        ('Former', 'Former')
    ]

    ACCOUNT_MNGR = [
        ('Thomas','Thomas'),
        ('Patrick','Patrick')
    ]

    owner_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personal_email = models.EmailField(max_length=255)
    corp_email = models.EmailField(max_length=255)
    phone_1 = models.CharField(("ex. 123-123-4567"), max_length=20)
    phone_2 = models.CharField(("ex. 123-123-4567"), max_length=20, blank=True)#(optional)
    home_address = models.CharField(max_length=255)
    old_home_address = models.CharField( max_length=255, blank=True) #(optional)
    ssn = models.CharField(max_length=9)#(secured field)
    corp_name = models.CharField(max_length=255) 
    second_corp = models.CharField(max_length=255, blank=True) #(optional)
    referral = models.URLField(max_length=200,blank=True) #(link back to referring owner)
    date_of_birth = models.DateField()
    contact_type = models.CharField(max_length=255, choices=CONTACT_TYPE)
    account_manager = models.CharField(max_length=255, choices=ACCOUNT_MNGR)
    gdrive = models.URLField(max_length=200)
    payments = models.IntegerField(default=0)
    
    def __str__(self):
        return self.first_name

    # def __init__(self, contact_type):
    #     self.contact_type = contact_type.choice
    
    
