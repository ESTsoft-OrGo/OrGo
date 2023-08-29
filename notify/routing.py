from django.urls import path, re_path
from .consumers import NotifyConsumer

websocket_urlpatterns = [
    path('notify/<str:user_id>', NotifyConsumer.as_asgi()),
]