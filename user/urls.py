from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)
app_name = "user"

urlpatterns = [
    path("follow/", Follow.as_view(), name="follow"),
    path("join/", Join.as_view(), name="join"),
    path("otp/", GenerateOTP.as_view(), name="otp"),
    path("login/email/", Login.as_view(), name="login"),
    path("login/google/", GoogleLogin.as_view(), name="google_login"),
    path("login/google/callback/", GoogleCallback.as_view(), name="google_callback"),
    path("login/github/", GithubLogin.as_view(), name="github_login"),
    path("login/github/callback/", GithubCallback.as_view(), name="github_callback"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="token_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("jwt/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path("profile/", MyPage.as_view(), name="profile"),
    path("profile/update/", ProfileSave.as_view(), name="update"),
    path("profile/change-password/", ChangePassword.as_view(), name="change-password"),
    path("profile/delete/", Delete.as_view(), name="delete"),
]
