from django.db import models
# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
'''
username
password
first name
last name 
email
'''
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phon_number=models.CharField(max_length=15,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    price=models.CharField( max_length=10,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)


