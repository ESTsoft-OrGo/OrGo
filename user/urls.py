from django.urls import path
from .views import JoinView, LoginView, ProfileView, Follow
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
app_name = 'user'

urlpatterns = [
    # path("join/", Join.as_view(), name='join'),
    # path("login/", Login.as_view(), name="login"),
    # path("profile/", Profile.as_view(), name="profile"),
    path("follow/", Follow.as_view(), name="follow"),
    path("join/", JoinView.as_view(), name='join'),
    path("login/", LoginView.as_view(), name="login"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("profile/", ProfileView.as_view(), name="profile"),
    # path("follow/", Follow.as_view(), name="follow"),
    # path("unfollow/", Unfollow.as_view(), name="unfollow"),
]

