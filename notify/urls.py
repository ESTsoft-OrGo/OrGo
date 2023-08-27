from django.urls import path
from .views import NotifyList

app_name = 'notify'

urlpatterns = [
    path("", NotifyList.as_view(), name="events"),
]

