from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True,unique=True)
    is_active = models.BooleanField(default=True)
    firstuser = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="firstuser")
    seconduser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="seconduser")
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)