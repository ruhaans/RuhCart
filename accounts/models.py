from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email= models.EmailField(unique=True)
    phone_number= models.CharField(max_length=15 ,unique=True)
    
    ROLE_CHOICES = [
    ('customer', 'Customer'),
    ('seller', 'Seller'),
    ]

    role= models.CharField(max_length=10, choices=ROLE_CHOICES, default= 'customer')


class UserProfile(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    username= User.username
    profile_img= models.ImageField(upload_to='users/', blank=True, null=True)
    full_name= models.CharField(max_length=30)
    gender= models.CharField(max_length=8)
    address= models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name or self.user.username
