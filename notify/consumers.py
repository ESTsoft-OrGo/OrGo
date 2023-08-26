import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
####
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification
from notify.serializers import NotificationSerializer
from user.serializers import UserSerializer
####

User = get_user_model()

class NotifyConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        
        user = self.scope["user"]
        if not user.is_authenticated:
            self.close()
            
        # 파라미터 값으로 채팅 룸을 구별
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.user_group_name = 'notify_%s' % self.user_id

        # 룸 그룹에 참가
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # 룸 그룹 나가기
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )
        
    # 룸 그룹으로부터 메세지 받음
    async def notify(self, event):
        message = event['message']
        # 웹소켓으로 메세지 보냄
        await self.send(text_data=json.dumps({
            'message': message,
        }))

@receiver(post_save, sender=Notification)
def notification_post_save(sender, instance, **kwargs):
    notifications = Notification.objects.filter(receiver=instance.receiver)
    new_notifications = []
    for notification in notifications:
        notify_serializer = NotificationSerializer(notification)
        user_serializer = UserSerializer(notification.sender)
        info = {
            'notify': notify_serializer.data,
            'sender': user_serializer.data
        }
        new_notifications.append(info)
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(f'notify_{instance.receiver.id}', {
        'type': 'notify',
        'message': new_notifications,
    })