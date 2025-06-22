from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect ('category_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})
        
    return render (request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect ('category_list')

def register_user(request):
    if request.method == "POST":
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            return redirect ('category_list')
    else:
            form= CustomUserCreationForm()
    return render (request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    user_profile= request.user.user_profile

    return render(request, 'profile.html', {'user_profile':user_profile})

def edit_profile(request):
    user_profile= request.user.user_profile
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form= UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})