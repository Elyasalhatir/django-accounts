from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

    

# Create your models here.
'''
username
password
first name
last name 
email
'''
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phon_number=models.CharField(max_length=15,null=True,blank=True)
    address=models.CharField(max_length=20,null=True,blank=True)
    price=models.CharField( max_length=10,null=True,blank=True)
    
    def __str__(self):
        return str(self.user)
@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


