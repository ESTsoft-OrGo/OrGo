from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from user.models import User, Follower


# Create your views here.
class Follow(APIView):
    
    def post(self, request):
        me = User.objects.get(email='test1@gmail.com')
        
        # 프로필 들어갔을 때나 게시글 작성자 user id
        you = User.objects.get(email='test2@gmail.com')
        
        # 해당 프로필 user id하고 로그인한 id가 Follower에 들어가 있을 때 
        following =  Follower.objects.filter(follower_id = me, target_id = you)

        if not following:
            follow = Follower.objects.create(follower_id= me, target_id=you, is_active=True)
            
            datas = {
            "message":"follow"
            }
            
            return Response(datas, status=status.HTTP_200_OK)
        else:
            unfollow = following.delete()
            datas = {
                "message":"unfollow"
            }
            return Response(datas, status=status.HTTP_200_OK)
