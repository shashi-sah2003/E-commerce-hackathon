from django.shortcuts import render , redirect
from . models import Message
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def send(response):
    message = response.POST['message']
    reciever = response.POST['username']
    sender = response.user
    msg = Message(sender = sender , reciever = reciever , messageText = message)
    msg.save()
    return HttpResponse('Message sent successfully')

def getMessages(response):
    message = Message.objects.all()
    listMessages = list(message.values())
    messages = []
    for i in range(len(listMessages)):
        if listMessages[i]['sender'] == response.user.username:
            messages.append(listMessages[i])
        elif listMessages[i]['reciever'] == response.user.username:
            messages.append(listMessages[i])
        else:
            pass
            
    return JsonResponse({"messages" : messages})