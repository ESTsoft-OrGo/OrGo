from django.urls import path
from .views import StudyJoin, StudyCancel

app_name = 'study'

urlpatterns = [
    # 참가
    path("join/", StudyJoin.as_view(), name='join'),
    path('join/cancel/', StudyCancel.as_view(), name='cancel')
]