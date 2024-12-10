from django.db import models
from django.contrib.auth.model import User


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Create your models here.
class Room(models.Model):
    host=user=models.ForeignKey(User,on_delete=model.CASCADE)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name= models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    #participants=
    updated= models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user=models.ForeignKey(User,on_delete=model.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.textField()
    updated=models.DateTimeField(auto_now=True)
    created=DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
