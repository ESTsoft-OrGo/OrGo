from django.db import models
from django.contrib.auth import get_user_model
from notify.models import Notification
from django.db.models.signals import post_save

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
    
# def message_action(sender, **kwargs):
#     if kwargs['created']:
#         message = kwargs['instance']
#         room = message.room
        
#         if room.firstuser == message.writer:
#             receiver = room.seconduser
#         else:
#             receiver = room.firstuser
            
#         content = f'메시지를 보내셨습니다.'
#         noti = Notification.objects.create(sender=message.writer,receiver=receiver,content=content)

# post_save.connect(message_action, sender=Message)