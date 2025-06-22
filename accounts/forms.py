from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields= ['username','email','phone_number', 'role', 'password1', 'password2']

class UserProfileForm(ModelForm):
    class Meta:
        model= UserProfile
        fields = ['profile_img', 'full_name', 'gender', 'address']