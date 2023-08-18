from django.urls import path
from .views import CommentWrite, CommentDelete, CommentEdit #, Like, Unlike, List, Write ,Edit, Delete, View, Search, 

app_name = 'post'

urlpatterns = [
    # # 게시글
    # path("", List.as_view(), name='list'),
    # path("write/", Write.as_view(), name='write'),
    # path("edit/", Edit.as_view(), name="edit"),
    # path("delete/", Delete.as_view(), name="delete"),
    # path("view/", View.as_view(), name="view"),
    # # 검색
    # path("search/", Search.as_view(), name="search"),
    # 댓글
    path("comment/write/", CommentWrite.as_view(), name="cm-write"),
    path("comment/delete/", CommentDelete.as_view(), name="cm-delete"),
    path("comment/edit/", CommentEdit.as_view(), name="cm-edit"),
    # # 좋아요
    # path("like/", Like.as_view(), name="like"),
    # path("unlike/", Unlike.as_view(), name="unlike"),
    
]
