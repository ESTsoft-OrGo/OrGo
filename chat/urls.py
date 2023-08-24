from django.urls import path
from .views import RoomList , RoomJoin

urlpatterns = [
    path('', RoomList.as_view(), name='room'),
    path('join/', RoomJoin.as_view(), name='join'),
]