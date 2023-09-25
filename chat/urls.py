from django.urls import path
from .views import GroupChatJoin, GroupChatCreate, GroupChatList, GroupChatInvite, GroupChatLeave, RoomList , RoomJoin , Following , RoomDelete

urlpatterns = [
    path('', RoomList.as_view(), name='room'),
    path('join/', RoomJoin.as_view(), name='join'),
    path('delete/', RoomDelete.as_view(), name='delete'),
    path('following/', Following.as_view(), name='follow'),
    path('groupchat/', GroupChatList.as_view(), name='group_chat_list'),
    path('groupchat/create/', GroupChatCreate.as_view(), name='group_chat_create'),
    path('groupchat/join/', GroupChatJoin.as_view(), name='group_chat_join'),
    path('groupchat/invite/', GroupChatInvite.as_view(), name='group_chat_invite'),
    path('groupchat/leave/', GroupChatLeave.as_view(), name='group_chat_leave'),
]