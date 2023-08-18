from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.


class CommentWrite(APIView):
    def post(self, request):
        # user = request.user
        print("Postman Test")

        user = User.objects.get(email='test1@gmail.com')
        post = Post.objects.get(id=request.data['post_id'])
        
        comment = Comment.objects.create(writer=user,content=request.data['content'],post=post)
        
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
        comment = Comment.objects.get(id=request.data)
        comment.is_active = False
        comment.save()
        
        datas = {
            "message": "댓글 삭제 완료",
        }
        return Response(datas,status=status.HTTP_200_OK)