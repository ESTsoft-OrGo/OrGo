from django.urls import path
from .views import Join, Login, MyPage, ProfileSave, Follow
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
    path("join/", Join.as_view(), name='join'),
    path("login/", Login.as_view(), name="login"),
    path('jwt/create/', TokenObtainPairView.as_view(), name='token_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("profile/", MyPage.as_view(), name="profile"),
    path("profile/update/", ProfileSave.as_view(), name="profile"),
    # path("follow/", Follow.as_view(), name="follow"),
    # path("unfollow/", Unfollow.as_view(), name="unfollow"),
]

