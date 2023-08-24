from django.urls import path
from .views import StudyList, StudyCreate, StudyEdit, StudyDelete, StudyView, TagWrite, TagEdit, TagDelete, StudySearch, StudyJoin, StudyCancel
# StudyCancel, StudyJoin

app_name = 'study'

urlpatterns = [
    path("search/", StudySearch.as_view(), name='search'),
    # 참가
    path("join/", StudyJoin.as_view(), name='join'),
    path('join/cancel/', StudyCancel.as_view(), name='cancel'),
    # 스터디
    path("", StudyList.as_view(), name='list'),
    path("create/", StudyCreate.as_view(), name='create'),
    path("edit/", StudyEdit.as_view(), name='edit'),
    path("delete/", StudyDelete.as_view(), name='delete'),
    path("detail/", StudyView.as_view(), name='detail'),
    path("tag/write/", TagWrite.as_view(), name='tag_write'),
    path("tag/edit/", TagEdit.as_view(), name='tag_edit'),
    path("tag/delete/", TagDelete.as_view(), name='tag_delete'),
    # 참가
    # path("join", StudyJoin.as_view(), name='join'),
    # path('join/cancel', StudyCancel.as_view(), name='cancel')
]