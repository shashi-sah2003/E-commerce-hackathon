from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Messages.views import send , getMessages

urlpatterns = [
   path("home/" , views.home , name = 'home'),
   path("" , views.start , name = 'start'),
   path("profile/" , views.profile  , name = 'profile'),
   path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='main/change-password.html',
            success_url = '/profile'
        ),
        name='change_password'
    ),
    path("update/" , views.Webhook , name='update'),
    path('send', send, name='send'),
    path('getMessages', getMessages, name='getMessages'),
]