import requests, os
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User, Profile, Follower
from notify.models import Notification
from .serializers import UserSerializer, ProfileSerializer
from post.models import Post , Like
from .tokens import create_jwt_pair_for_user
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.models import SocialAccount


BASE_URL = 'http://127.0.0.1:8000/user/login/'
GOOGLE_CALLBACK_URI = BASE_URL + 'google/callback/'
GITHUB_CALLBACK_URI = BASE_URL + 'github/callback/'

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
                "message": "팔로우 추가 하셨습니다.",
                "new_following": new_following
            }
            
            return Response(datas, status=status.HTTP_200_OK)
        else:
            unfollow = following.delete()
            
            new_following = Follower.objects.filter(follower_id=me).values()
            
            datas = {
                "message":"팔로우를 해제 하셨습니다.",
                "new_following": new_following
            }
            return Response(datas, status=status.HTTP_200_OK)


class Join(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            response = {"message": "회원가입 성공", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            token = create_jwt_pair_for_user(user)
            serializer = UserSerializer(user)
            follower = Follower.objects.filter(follower_id=user).values()
            notify = Notification.objects.filter(receiver=user,is_read=False).values()
            response = {
                "message": "로그인 성공",
                "token": token,
                "user_info": serializer.data,
                "follower": follower,
                "notify": notify,
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "이메일과 비밀번호를 다시 확인해 주세요."})


class MyPage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(user_profile)
        
        my_posts = Post.objects.filter(writer=request.user,is_active=True).order_by('-created_at')
        
        posts = []
        for post in my_posts:
            likes = Like.objects.filter(post_id=post.id).count()
            images = post.image.all()  # 이미지들 가져오기
            
            post_info = {
                "post": {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "views": post.views,
                    "images": [{"image": image.image.url} for image in images],
                    "created_at": post.created_at,
                    "updated_at": post.updated_at,
                    },
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
            user_serializer = UserSerializer(request.user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
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
        user.delete()

        response = {"message": "회원탈퇴 완료"}
        return Response(data=response, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([AllowAny])
def google_login(request):
        scope = "https://www.googleapis.com/auth/userinfo.email"
        client_id = os.environ.get('GOOGLE_CLIENT_ID')
        return redirect(f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope={scope}")

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def google_callback(request):
        client_id = os.environ.get('GOOGLE_CLIENT_ID')
        client_secret = os.environ.get('GOOGLE_SECRET_KEY')
        code = request.GET.get('code')
        state = os.environ.get('STATE')

        token_req = requests.post(f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={state}")
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        if error is not None:
            raise ParseError(detail=error)

        access_token = token_req_json.get('access_token')

        email_req = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
        email_req_status = email_req.status_code
        if email_req_status != 200:
            return Response({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

        email_req_json = email_req.json()
        email = email_req_json.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            social_user = SocialAccount.objects.get(user=user)
            if social_user.provider != 'google':
                return Response({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

            data = {'access_token': access_token, 'code': code}
            accept = requests.post(f"{BASE_URL}google/success/", data=data)
            accept_status = accept.status_code
            if accept_status != 200:
                return Response({'err_msg': 'failed to signin'}, status=accept_status)
            
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
            id_token = token_req_json.get('id_token')
            data = {'access_token': access_token, 'code': code, 'id_token': id_token}
            accept = requests.post(f"{BASE_URL}google/success/", data=data)
            accept_status = accept.status_code
            accept_json = accept.json()
            accept_json.pop('user', None)

            return Response(data=accept_json, status=status.HTTP_201_CREATED)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = GOOGLE_CALLBACK_URI
    client_class = OAuth2Client


@api_view(["GET"])
@permission_classes([AllowAny])
def github_login(request):
        client_id = os.environ.get('GITHUB_CLIENT_ID')
        return redirect(f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={GITHUB_CALLBACK_URI}")

@api_view(["POST", "GET"])
@permission_classes([AllowAny])
def github_callback(request):
        client_id = os.environ.get('GITHUB_CLIENT_ID')
        client_secret = os.environ.get('GITHUB_SECRET_KEY')
        code = request.GET.get('code')

        token_req = requests.post(f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}&accept=&json&redirect_uri={GITHUB_CALLBACK_URI}&response_type=code", headers={'Accept': 'application/json'})
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        if error is not None:
            raise JSONDecodeError(error)

        access_token = token_req_json.get('access_token')

        user_req = requests.get("https://api.github.com/user", headers={"Authorization": f"Bearer {access_token}"})
        user_json = user_req.json()
        error = user_json.get("error")
        if error is not None:
            raise JSONDecodeError(error)

        email = user_json.get("email")

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            social_user = SocialAccount.objects.get(user=user)
            if social_user.provider != 'github':
                return Response({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)

            data = {'access_token': access_token, 'code': code}
            accept = requests.post(f"{BASE_URL}github/success/", data=data)
            accept_status = accept.status_code
            if accept_status != 200:
                return Response({'err_msg': 'failed to signin'}, status=accept_status)
            
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
            data = {'access_token': access_token, 'code': code}
            accept = requests.post(f"{BASE_URL}github/success/", data=data)
            accept_status = accept.status_code
            accept_json = accept.json()
            accept_json.pop('user', None)

            return JsonResponse(accept_json)

class GitHubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = GITHUB_CALLBACK_URI
    client_class = OAuth2Client