from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.CharField(max_length = 100)
    reciever = models.CharField(max_length = 100)
    messageText = models.CharField(max_length = 250)

    def __str__(self):
        return self.messageText