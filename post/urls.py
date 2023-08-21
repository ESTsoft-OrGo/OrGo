from django.urls import path
from .views import LikeView #,PostListView, PostDetailView #List, Write ,Edit, Delete, View, Search, CommentWrite, CommentDelete, CommentEdit, 

app_name = 'post'

urlpatterns = [
    # 게시글
    # path("", List.as_view(), name='list'),
    # path("write/", Write.as_view(), name='write'),
    # path("edit/", Edit.as_view(), name="edit"),
    # path("delete/", Delete.as_view(), name="delete"),
    # path("view/", View.as_view(), name="view"),
    # 검색
    # path("search/", Search.as_view(), name="search"),
    # 댓글
    # path("comment/write/", CommentWrite.as_view(), name="cm-write"),
    # path("comment/delete/", CommentDelete.as_view(), name="cm-delete"),
    # path("comment/edit/", CommentEdit.as_view(), name="cm-edit"),
    # 좋아요
    path("like/", LikeView.as_view(), name="like"),    
    # 좋아요 기능 확인용
    # path("", PostListView.as_view(), name='post-list'),
    # path("<int:post_id>/", PostDetailView.as_view(), name="post-details"),
]
