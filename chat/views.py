from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from .models import Room, Message
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer

User = get_user_model()


# Create your views here.
class RoomList(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        rooms = Room.objects.filter(Q(firstuser=user) | Q(seconduser=user)).values()
        
        room_list = []
        
        for room in rooms:
            info = {}

            message = Message.objects.filter(room=room['id']).order_by('-created_at').values()[0]
            
            if user.id == room['firstuser_id']:
                target = User.objects.get(pk=room['seconduser_id'])
            elif user.id == room['seconduser_id']:
                target = User.objects.get(pk=room['firstuser_id'])
            
            serializer = UserSerializer(target)
            info['room'] = room
            info['recent'] = message
            info['target'] = serializer.data
            
            room_list.append(info)
        
        datas = {
            "rooms": room_list
        }
        return Response(datas, status=status.HTTP_200_OK)
    

class RoomJoin(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        target = User.objects.get(pk=request.data['target'])
    
        rooms = Room.objects.filter(Q(firstuser=user,seconduser=target)| Q(firstuser=target,seconduser=user))

        if not rooms:
            room = Room.objects.create(firstuser=user,seconduser=target)
            room.title = f'room{room.pk}'
            room.save()
            datas = {
                "message":"Create Success",
            }
            return Response(datas, status=status.HTTP_200_OK)
        else:
            datas = {
                "message":"Room is already exists ",
            }
            return Response(datas, status=status.HTTP_200_OK)
