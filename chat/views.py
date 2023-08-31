from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db.models import Q
from .models import Room, Message
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from user.models import Profile, Follower

User = get_user_model()


# Create your views here.
class RoomList(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        rooms = Room.objects.filter(Q(firstuser=user) | Q(seconduser=user),is_active=True).values()
        
        room_list = []
        
        for room in rooms:
            info = {}
            message = Message.objects.filter(room=room['id']).order_by('-created_at').values()
            try:
                message[0]
            except:
                info['recent'] = {'content': '첫 메시지를 보내보세요.'}
            else:
                info['recent'] = message[0]

            if user.id == room['firstuser_id']:
                target = User.objects.get(pk=room['seconduser_id'])
            elif user.id == room['seconduser_id']:
                target = User.objects.get(pk=room['firstuser_id'])
            
            serializer = UserSerializer(target)
            info['room'] = room
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
    
        rooms = Room.objects.filter(Q(firstuser=user,seconduser=target)| Q(firstuser=target,seconduser=user),is_active=True)

        if not rooms:
            room = Room.objects.create(firstuser=user,seconduser=target)
            room.title = f'room{room.pk}'
            room.save()
            datas = {
                "message":"채팅방 생성 성공",
            }
            return Response(datas, status=status.HTTP_200_OK)
        else:
            datas = {
                "message":"채팅방이 이미 존재합니다.",
            }
            return Response(datas, status=status.HTTP_200_OK)


class RoomDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            room = Room.objects.get(pk=request.data['target'],is_active=True)
        except:
            datas = {
                "message":"이미 삭제된 채팅방 입니다.",
            }
            return Response(datas, status=status.HTTP_200_OK)
        
        room.is_active = False
        room.save()
        datas = {
            "message":"채팅방이 삭제 되었습니다..",
        }
        return Response(datas, status=status.HTTP_200_OK)


class Following(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        followings = Follower.objects.filter(follower_id=request.user)
        newFollowings = []
        for following in followings:
            following_pf = UserSerializer(following.target_id).data
            newFollowings.append(following_pf)
        
        response = {"following": newFollowings}

        return Response(data=response, status=status.HTTP_200_OK)
