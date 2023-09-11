from django.urls import path
from .views import CommentWrite, CommentDelete, ReCommentWrite, Like, Unlike, List, Write, Edit, Delete,  View, PostSearch, RecentPost, RecommendedPost

app_name = 'post'

urlpatterns = [
    # 게시글
    path("", List.as_view(), name='list'),
    path("recent/", RecentPost.as_view(), name='recent'),
    path("recommended/", RecommendedPost.as_view(), name='recommended_post'),
    path("write/", Write.as_view(), name='write'),
    path('edit/<int:pk>/', Edit.as_view(), name='edit'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('view/<int:pk>/', View.as_view(), name='view'),
    path('search/', PostSearch.as_view(), name='post-search'),
    # 댓글
    path("comment/write/", CommentWrite.as_view(), name="cm-write"),
    path("comment/delete/", CommentDelete.as_view(), name="cm-delete"),
    # 대댓글
    path("re-comment/write/", ReCommentWrite.as_view(), name="r-cm-write"),
    # 좋아요
    path("like/", Like.as_view(), name="like"),    
    path("unlike/", Unlike.as_view(), name="unlike"),  
]

