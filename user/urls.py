from django.urls import path
from .views import Join, Login, MyPage, ProfileSave, Follow, Delete, ChangePassword, GitHubLogin, GoogleLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)
app_name = 'user'

urlpatterns = [
    path("follow/", Follow.as_view(), name="follow"),
    path("join/", Join.as_view(), name='join'),
    path("login/", Login.as_view(), name="login"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('jwt/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path("profile/", MyPage.as_view(), name="profile"),
    path("profile/update/", ProfileSave.as_view(), name="update"),
    path("profile/change-password/", ChangePassword.as_view(), name="change-password"),
    path("profile/delete/", Delete.as_view(), name="delete"),

    # path('login/google/', google_login.as_view(), name='google_login'),
    # path('login/google/callback/', google_callback.as_view(), name='google_callback'),
    path('login/google/finish/', GoogleLogin.as_view(), name='google_login_finish'),

    # path('login/github/', github_login.as_view(), name='github_login'),
    # path('login/github/callback/', github_callback.as_view(), name='github_callback'),
    path('login/github/finish/', GitHubLogin.as_view(), name='github_login_finish'),
]

