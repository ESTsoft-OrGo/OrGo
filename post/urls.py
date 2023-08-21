from django.urls import path
<<<<<<< HEAD
from .views import CommentWrite, CommentDelete, CommentEdit, ReCommentWrite #, Like, Unlike, List, Write ,Edit, Delete, View, Search, 
=======
from .views import LikeView #,PostListView, PostDetailView #List, Write ,Edit, Delete, View, Search, CommentWrite, CommentDelete, CommentEdit, 
>>>>>>> origin/sarang

app_name = 'post'

urlpatterns = [
<<<<<<< HEAD
    # # 게시글
=======
    # 게시글
>>>>>>> origin/sarang
    # path("", List.as_view(), name='list'),
    # path("write/", Write.as_view(), name='write'),
    # path("edit/", Edit.as_view(), name="edit"),
    # path("delete/", Delete.as_view(), name="delete"),
    # path("view/", View.as_view(), name="view"),
<<<<<<< HEAD
    # # 검색
=======
    # 검색
>>>>>>> origin/sarang
    # path("search/", Search.as_view(), name="search"),
    # 댓글
    path("comment/write/", CommentWrite.as_view(), name="cm-write"),
    path("comment/delete/", CommentDelete.as_view(), name="cm-delete"),
    path("comment/edit/", CommentEdit.as_view(), name="cm-edit"),
<<<<<<< HEAD
    # 대댓글
    path("re-comment/write/", ReCommentWrite.as_view(), name="r-cm-write"),
    # # 좋아요
    # path("like/", Like.as_view(), name="like"),
    # path("unlike/", Unlike.as_view(), name="unlike"),
    
=======
    # 좋아요
    path("like/", LikeView.as_view(), name="like"),    
    # 좋아요 기능 확인용
    # path("", PostListView.as_view(), name='post-list'),
    # path("<int:post_id>/", PostDetailView.as_view(), name="post-details"),
>>>>>>> origin/sarang
]
