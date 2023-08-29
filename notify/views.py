from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from .models import Notification
from .serializers import NotificationSerializer
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

User = get_user_model()


# Create your views here.
class NotifyList(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
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