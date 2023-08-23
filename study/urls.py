from django.urls import path
from .views import StudyList, StudyCreate, StudyJoin, StudyEdit, StudyDelete, StudyCancel

app_name = 'study'

urlpatterns = [
    # 스터디
    path("", StudyList.as_view(), name='list'),
    path("create", StudyCreate.as_view(), name='create'),
    path("edit", StudyEdit.as_view(), name='edit'),
    path("delete", StudyDelete.as_view(), name='delete'),
    # 참가
    path("join", StudyJoin.as_view(), name='join'),
    path('join/cancel', StudyCancel.as_view(), name='cancel')
]