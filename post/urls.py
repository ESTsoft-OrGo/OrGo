from django.urls import path, include
from rest_framework import routers
from .views import List, Write, Edit, Delete,  View
# Search, CommentWrite, CommentDelete, CommentEdit, Like, Unlike



app_name = 'post'

urlpatterns = [
    path("", List.as_view(), name='list'),
    path("write/", Write.as_view(), name='write'),
    path('edit/<int:pk>/', Edit.as_view(), name='edit'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('view/<int:pk>/', View.as_view(), name='view'),
]

