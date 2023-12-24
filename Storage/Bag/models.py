from django.db import models
from datetime import datetime

# Create your models here.
class Features(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=300)
class posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=3000)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
class Room(models.Model):
    room  = models.CharField(max_length=500)
class Message(models.Model):
    value = models.CharField(max_length=2000000)
    user = models.CharField(max_length=200)
    room = models.CharField(max_length=2000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    