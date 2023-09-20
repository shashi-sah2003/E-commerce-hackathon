from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from . forms import RegisterForm , UserProfileForm
from register import models
# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        profileForm = UserProfileForm(response.POST)
        if form.is_valid() and profileForm.is_valid():
            user = form.save()
            profile = profileForm.save(commit = False)
            profile.user = user
            profile.save()
            return redirect('/home')
    else:
        form = RegisterForm()
        profileForm = UserProfileForm()
    return render(response , 'main/register.html' , {"form" : form , "profileForm" : profileForm})