import requests, os
from json.decoder import JSONDecodeError
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .models import User, Profile, Follower
from notify.models import Notification
from .serializers import UserSerializer, ProfileSerializer, VerifySerializer
from post.models import Post , Like
from .tokens import create_jwt_pair_for_user
from .utils import send_otp_via_email, generate_otp, generate_random_nickname
from post.uploads import S3ImgUploader


GOOGLE_CALLBACK_URI = 'http://127.0.0.1:5500/src/view/login.html'
GITHUB_CALLBACK_URI = 'http://127.0.0.1:5500/src/view/login.html'
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_SECRET_KEY = os.environ.get('GOOGLE_SECRET_KEY')
GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
GITHUB_SECRET_KEY = os.environ.get('GITHUB_SECRET_KEY')
STATE = os.environ.get('STATE')


class Follow(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        me = request.user
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

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            user.profile.nickname = generate_random_nickname()
            user.profile.save()
            response = {"message": "회원 가입 성공", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateOTP(APIView):

    def post(self, request):
        email = request.data.get('email')
        if email:
            otp = generate_otp()
            send_otp_via_email(email, otp=otp)
            response = {"message": "인증 번호 생성", "otp": otp}
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response({"message": "이메일 주소를 입력하세요."}, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):

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
        if int(request.data['user_profile']) == request.user.id:
            user = request.user.id
        else:
            user = int(request.data['user_profile'])
        user_profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile)
        userprofile = User.objects.get(id = user)
        userserializer = UserSerializer(userprofile)
        my_posts = Post.objects.filter(writer=request.data['user_profile'],is_active=True).order_by('-created_at')
        followers = Follower.objects.filter(target_id=user)
        followings = Follower.objects.filter(follower_id=user)
        
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
        
        
        
        new_followers = []
        new_followings = []
        
        for follower in followers:
            follower_pf = UserSerializer(follower.follower_id).data
            new_followers.append(follower_pf)
            
        for following in followings:
            following_pf = UserSerializer(following.target_id).data
            new_followings.append(following_pf)
        
        response = {
            "user_id" : request.user.id,
            "serializer": serializer.data,
            "user" : userserializer.data,
            "my_posts": posts,
            "follower": new_followers,
            "following": new_followings
        }

        return Response(data=response, status=status.HTTP_200_OK)


class ProfileSave(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_profile = get_object_or_404(Profile, user=request.user)
        serializer = ProfileSerializer(user_profile, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            try:
                image = request.FILES['profileImage']
            except:
                is_image = False
            else:
                is_image = True
                
            if is_image:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload()
                user_profile.profileImage = uploaded_url
                user_profile.save()
            
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


class GoogleLogin(APIView):
    def post(self, request):
        data = {
            'url': f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&response_type=code&redirect_uri={GOOGLE_CALLBACK_URI}&scope=https://www.googleapis.com/auth/userinfo.email"
        }
        return Response(data)


class GoogleCallback(APIView):
    def post(self, request):
        code = request.data['code']

        token_req = requests.post(f"https://oauth2.googleapis.com/token?client_id={GOOGLE_CLIENT_ID}&client_secret={GOOGLE_SECRET_KEY}&code={code}&grant_type=authorization_code&redirect_uri={GOOGLE_CALLBACK_URI}&state={STATE}")
        token_req_json = token_req.json()
        error = token_req_json.get("error")
        if error is not None:
            raise JSONDecodeError(error)

        access_token = token_req_json.get('access_token')

        email_req = requests.get(f"https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={access_token}")
        email_req_status = email_req.status_code
        if email_req_status != 200:
            return Response({'err_msg': 'failed to get email'}, status=status.HTTP_400_BAD_REQUEST)

        email_req_json = email_req.json()
        email = email_req_json.get('email')

        try:
            user = User.objects.get(email=email)
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

        except User.DoesNotExist:
            user = User.objects.create(email=email, login_method='google')
            user.set_unusable_password()
            user.save()

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
            return Response(data=response, status=status.HTTP_201_CREATED)


class GithubLogin(APIView):
    def post(self, request):
        data = {
            'url': f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={GITHUB_CALLBACK_URI}"
        }
        return Response(data)


class GithubCallback(APIView):
    def post(self, request):
        code = request.data['code']

        token_req = requests.post(f"https://github.com/login/oauth/access_token?client_id={GITHUB_CLIENT_ID}&client_secret={GITHUB_SECRET_KEY}&code={code}&accept=&json&redirect_uri={GITHUB_CALLBACK_URI}&response_type=code", headers={'Accept': 'application/json'})
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

        try:
            user = User.objects.get(email=email)
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

        except User.DoesNotExist:
            user = User.objects.create(email=email, login_method='github')
            user.set_unusable_password()
            user.save()

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
            return Response(data=response, status=status.HTTP_201_CREATED)