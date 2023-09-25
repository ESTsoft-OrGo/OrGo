from django.urls import path
from .views import NotifyList, MessageNotify

app_name = 'notify'

urlpatterns = [
    path("", NotifyList.as_view(), name="events"),
    path("massage/", MessageNotify.as_view(), name="massge"),
]

