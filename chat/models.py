from django.db import models
from django.contrib.auth import get_user_model
from notify.models import Notification
from django.db.models.signals import post_save
from study.models import Study

User = get_user_model()


class Room(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True,unique=True)
    is_active = models.BooleanField(default=True)
    firstuser = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="firstuser",null=True)
    seconduser = models.ForeignKey(User, on_delete=models.CASCADE,related_name="seconduser",null=True)
    joinUser = models.IntegerField(default=0,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

def room_action(sender, **kwargs):
    if kwargs['created']:
        room = kwargs['instance']
        content = f'채팅방을 생성하셨습니다.'
        noti = Notification.objects.create(sender=room.firstuser,receiver=room.seconduser,content=content)

post_save.connect(room_action, sender=Room)


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    is_read = models.BooleanField(default=False)
    content = models.CharField(max_length=200,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

