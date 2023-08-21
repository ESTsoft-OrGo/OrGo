from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from .models import Post, Like
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class CommentWrite(APIView):
    def post(self, request):
        # user = request.user
        print("Postman Test")

        user = User.objects.get(email='test1@gmail.com')
        post = Post.objects.get(id=request.data['post_id'])
        
        comment = Comment.objects.create(writer=user,content=request.data['content'],post=post,parent_comment=None)
        
        datas = {
            "message": "댓글 생성 완료",
        }
        return Response(datas,status=status.HTTP_201_CREATED)


class CommentEdit(APIView):
    def post(self, request):
        comment = Comment.objects.get(id=request.data['comment_id'])
        comment.content = request.data['comment']
        comment.save()
        
        datas = {
            "message": "댓글 수정 완료",
        }
        return Response(datas,status=status.HTTP_200_OK)


class CommentDelete(APIView):
    def post(self, request):
        comment = Comment.objects.get(id=request.data['comment_id'])
        comment.is_active = False
        comment.save()
        
        datas = {
            "message": "댓글 삭제 완료",
        }
        return Response(datas,status=status.HTTP_200_OK)
    

class ReCommentWrite(APIView):
    def post(self, request):

        user = User.objects.get(email='test1@gmail.com')
        post = Post.objects.get(id=request.data['post_id'])
        parent_comment = Comment.objects.get(id=request.data['comment_id'])
        
        comment = Comment.objects.create(writer=user,content=request.data['content'],post=post,parent_comment=parent_comment)
        
        datas = {
            "message": "대댓글 생성 완료",
        }
        return Response(datas,status=status.HTTP_201_CREATED)


class Unlike(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        post_id = request.data.get('post_id')
        user = request.user

        post = get_object_or_404(Post, pk=post_id)
        like = Like.objects.filter(post=post, user=user).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You haven't liked this post before."}, status=status.HTTP_400_BAD_REQUEST)


class Like(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        user = request.user

        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=user)

        if created:
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You've already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
