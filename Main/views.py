from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from . forms import CreateNewList
from django.contrib.auth.models import User
from register.models import Profile
import git

# Create your views here.
def home(response):
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(Profile.objects.filter(Retailer = True))
        for user in users:
            if str(user) == str(username):
                retail = True
                break
            else:
                retail = False
    return render(response , 'main/home.html' , {"retail":retail})

def start(response):
    return render(response , 'main/start.html')

def profile(response):
    username = None
    retail =False
    if response.user.is_authenticated:
        username = response.user.username
        users = list(Profile.objects.filter(Retailer = True))
        for user in users:
            if str(user) == str(username):
                retail = True
                break
            else:
                retail = False
    return render(response , 'main/profile.html' , {'retail':retail , 'username':username , 'email':response.user.email})

def Webhook(response):
    if response.method == 'POST':
            repo = git.Repo('https://github.com/Hackathon-team-aps-dk/ecommerce-hackathon')
            origin = repo.remotes.origin
            origin.pull()
            return HttpResponse('Success' , status = 200)
    else:
        return HttpResponse(f'Failed {response}' , status=400)