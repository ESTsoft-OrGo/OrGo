from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from user.serializers import UserSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

User = get_user_model()


class NotifyList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        notifications = Notification.objects.filter(receiver=user,is_read=False)

        new_notifications = []
        for notification in notifications:
            notification.is_read = True
            notification.save()
            notify_serializer = NotificationSerializer(notification)
            user_serializer = UserSerializer(notification.sender)
            info = {
                'notify': notify_serializer.data,
                'sender': user_serializer.data
            }
            new_notifications.append(info)
        datas = {
            'notify': new_notifications
        }
        return Response(datas, status=status.HTTP_200_OK)


class MessageNotify(APIView):
    def post(self, request):
        
        instance = get_object_or_404(Notification,pk=request.data['notify_id'])
        notifications = Notification.objects.filter(receiver=instance.receiver,is_read=False)
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
        async_to_sync(channel_layer.group_send)(f'notify_{notification.receiver.id}', {
            'type': 'notify',
            'message': new_notifications,
        })
        
        datas = {
            'message': '알림 전송 성공'
        }
        
        return Response(datas, status=status.HTTP_200_OK)
    
    