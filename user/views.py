from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import User, Profile, Follower
from .serializers import UserSerializer, ProfileSerializer
from post.models import Post
from .tokens import create_jwt_pair_for_user

# Create your views here.
class Follow(APIView):
    def post(self, request):
        # me = User.objects.get(email='test1@gmail.com')
        me1 = request.data['me']
        me = User.objects.get(email=me1)
        # 프로필 들어갔을 때나 게시글 작성자 user id
        # you = User.objects.get(email='test2@gmail.com')
        you1 = request.data['you']
        you = User.objects.get(email=you1)
        # 해당 프로필 user id하고 로그인한 id가 Follower에 들어가 있을 때 
        following =  Follower.objects.filter(follower_id=me, target_id=you)
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


class Join(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            response = {"message": "회원가입 성공", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)
            serializer = UserSerializer(user)
            response = {
                "message": "로그인 성공",
                "token": tokens,
                "user_info": serializer.data,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "이메일과 비밀번호를 다시 확인해 주세요."})


class MyPage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(user_profile)
        
        my_posts = Post.objects.filter(writer=request.user).values()
        followers = Follower.objects.filter(follower_id=request.user).values()
        followings = Follower.objects.filter(target_id=request.user).values()
        
        new_followers = []
        new_followings = []
        
        for follower in followers:
            print(follower)
            follower_pf = Profile.objects.filter(user=follower['target_id_id']).values()
            new_followers.append(follower_pf)
            
        for following in followings:
            following_pf = Profile.objects.filter(user=following['follower_id_id']).values()
            new_followings.append(following_pf)
        
        response = {"serializer": serializer.data,
            "my_posts": my_posts,
            "follower": new_followers,
            "following": new_followings}

        return Response(data=response, status=status.HTTP_200_OK)


class ProfileSave(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(user_profile, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)