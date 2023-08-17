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