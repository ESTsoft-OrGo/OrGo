from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
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


class FollowList(APIView):
    def get(self, request):
        # 내가 팔로우한 사람들
        me = User.objects.get(email='test1@gmail.com')
        follow = Follower.objects.filter(follower_id=me)
        datas = {
            "message":"followlist"
            }
            
        return Response(datas, status=status.HTTP_200_OK)


class FollowerList(APIView):
    def get(self, request):
        # 나를 팔로우 한 사람들
        me = User.objects.get(email='test1@gmail.com')
        target = Follower.objects.filter(target_id가=me)
        
        datas = {
            "message":"followlist"
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
        
        my_posts = Post.objects.filter(writer=request.user)
        follower_count = Follower.objects.filter(follower_id=request.user)
        following_count = Follower.objects.filter(target_id=request.user)
        
        response = {"serializer": serializer.data,
            "my_posts": my_posts,
            "follower_count": follower_count,
            "following_count": following_count}
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


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get("current_password")
        new_password = request.data.get("new_password")

        if not user.check_password(current_password):
            return Response(
                data={"message": "현재 비밀번호가 일치하지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.set_password(new_password)
        user.save()

        response = {"message": "비밀번호 변경이 완료되었습니다."}
        return Response(data=response, status=status.HTTP_200_OK)


class Delete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        user.delete()

        response = {"message": "회원탈퇴 완료"}
        return Response(data=response, status=status.HTTP_200_OK)