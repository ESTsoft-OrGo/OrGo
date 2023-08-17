from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment

# Create your views here.


class CommentWrite(APIView):
    def post(self, request):
        user = request.user
        post = Post.objects.get(id=request.data['post_id'])
        comment = Comment.objects.create(writer=user,content=request.data['comment'],chat=post)
        
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
            "message": "수정되었습니다.",
        }
        return Response(datas,status=status.HTTP_200_OK)


class CommentDelete(APIView):
    def post(self, request):
        comment = Comment.objects.get(id=request.data)
        comment.is_active = False
        comment.save()
        
        datas = {
            "message": "삭제되었습니다.",
        }
        return Response(datas,status=status.HTTP_200_OK)