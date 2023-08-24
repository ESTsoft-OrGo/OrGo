from django.urls import path
from .views import StudyList, StudyCreate, StudyEdit, StudyDelete, StudyView
# StudyCancel, StudyJoin

app_name = 'study'

urlpatterns = [
    # 스터디
    path("", StudyList.as_view(), name='list'),
    path("create/", StudyCreate.as_view(), name='create'),
    path("edit/", StudyEdit.as_view(), name='edit'),
    path("delete/", StudyDelete.as_view(), name='delete'),
    path("detail/", StudyView.as_view(), name='detail'),
    # 참가
    # path("join", StudyJoin.as_view(), name='join'),
    # path('join/cancel', StudyCancel.as_view(), name='cancel')
]