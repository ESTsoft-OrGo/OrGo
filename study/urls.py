from django.urls import path
from .views import StudyList, StudyCreate, StudyEdit, StudyDelete, StudyView, TagDelete, StudyJoin, StudyCancel , Tagadd

app_name = 'study'

urlpatterns = [
    # 참가
    path("", StudyList.as_view(), name='list'),
    path("join/", StudyJoin.as_view(), name='join'),
    path('join/cancel/', StudyCancel.as_view(), name='cancel'),
    path("create/", StudyCreate.as_view(), name='create'),
    path("edit/", StudyEdit.as_view(), name='edit'),
    path("delete/", StudyDelete.as_view(), name='delete'),
    path("detail/", StudyView.as_view(), name='detail'),
    path("tag/add/", Tagadd.as_view(), name='tag_add'),
    path("tag/delete/", TagDelete.as_view(), name='tag_delete'),
]