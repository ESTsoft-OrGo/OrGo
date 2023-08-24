from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User, Profile, Follower
from .serializers import UserSerializer, ProfileSerializer
from post.models import Post , Like
from .tokens import create_jwt_pair_for_user
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


BASE_URL = 'http://127.0.0.1:8000/'
GOOGLE_CALLBACK_URI = BASE_URL + 'user/login/google/callback/'
GITHUB_CALLBACK_URI = BASE_URL + 'user/login/github/callback/'


# Create your views here.
class Follow(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # me = User.objects.get(email='test1@gmail.com')
        me = request.user
        # 프로필 들어갔을 때나 게시글 작성자 user id
        # you = User.objects.get(email='test2@gmail.com')
        you = User.objects.get(id=request.data['you'])
        
        # 해당 프로필 user id하고 로그인한 id가 Follower에 들어가 있을 때 
        following = Follower.objects.filter(follower_id=me, target_id=you)
        
        if not following:
            follow = Follower.objects.create(follower_id=me, target_id=you, is_active=True)
            
            new_following = Follower.objects.filter(follower_id=me).values()
            
            datas = {
                "message":"follow",
                "new_following": new_following
            }
            
            return Response(datas, status=status.HTTP_200_OK)
        else:
            unfollow = following.delete()
            
            new_following = Follower.objects.filter(follower_id=me).values()
            
            datas = {
                "message":"unfollow",
                "new_following": new_following
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
            token = create_jwt_pair_for_user(user)
            serializer = UserSerializer(user)
            follower = Follower.objects.filter(follower_id=user).values()
            response = {
                "message": "로그인 성공",
                "token": token,
                "user_info": serializer.data,
                "follower": follower
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "이메일과 비밀번호를 다시 확인해 주세요."})


class MyPage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(user_profile)
        
        my_posts = Post.objects.filter(writer=request.user,is_active=True).order_by('-created_at').values()
        
        posts = []
        for post in my_posts:
            likes = Like.objects.filter(post_id=post["id"]).count()
            post_info = {
                "post": post,
                "likes": likes
            }
            posts.append(post_info)
        
        followers = Follower.objects.filter(target_id=request.user).values()
        followings = Follower.objects.filter(follower_id=request.user).values()
        
        new_followers = []
        new_followings = []
        
        for follower in followers:
            follower_pf = Profile.objects.filter(user=follower['follower_id_id']).values()
            new_followers.append(follower_pf)
            
        for following in followings:
            following_pf = Profile.objects.filter(user=following['target_id_id']).values()
            new_followings.append(following_pf)
        
        response = {"serializer": serializer.data,
            "my_posts": posts,
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

    def post(self, request):
        user = request.user
        refresh_token = RefreshToken.for_user(user)
        refresh_token.blacklist()
        user.is_active = False
        user.save()

        response = {"message": "회원탈퇴 완료"}
        return Response(data=response, status=status.HTTP_200_OK)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = GITHUB_CALLBACK_URI
    client_class = OAuth2Client