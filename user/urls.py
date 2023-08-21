from django.urls import path
from .views import Follow

app_name = 'user'

urlpatterns = [
    # path("join/", Join.as_view(), name='join'),
    # path("login/", Login.as_view(), name="login"),
    # path("profile/", Profile.as_view(), name="profile"),
    path("follow/", Follow.as_view(), name="follow"),
    # path("unfollow/", Unfollow.as_view(), name="unfollow"),
]

