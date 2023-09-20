from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label=mark_safe('<br/> Email Id'))

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Retailer',)