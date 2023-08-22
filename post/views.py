from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post, Like as Like_Model, Comment
from .serializers import PostSerializer, Post_editSerializer
from user.models import Profile


User = get_user_model()
# Create your views here.

class CommentWrite(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        post = Post.objects.get(id=request.data['post_id'])
        
        comment = Comment.objects.create(writer=user,content=request.data['content'],post=post,parent_comment=None)
        
        datas = {
            "message": "댓글 생성 완료",
        }
        return Response(datas,status=status.HTTP_201_CREATED)


class CommentEdit(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        comment = Comment.objects.get(id=request.data['comment_id'])
        comment.content = request.data['comment']
        comment.save()
        
        datas = {
            "message": "댓글 수정 완료",
        }
        
        return Response(datas,status=status.HTTP_200_OK)


class CommentDelete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        comment = Comment.objects.get(id=request.data['comment_id'])
        comment.is_active = False
        comment.save()
        
        datas = {
            "message": "댓글 삭제 완료",
        }
        return Response(datas,status=status.HTTP_200_OK)
    

class ReCommentWrite(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
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
        like = Like_Model.objects.filter(post=post, user=user).first()

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
        like, created = Like_Model.objects.get_or_create(post=post, user=user)

        if created:
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You've already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

## Post
class List(APIView):
    def post(self, request):
        posts = Post.objects.filter(is_active=True).order_by('-created_at').values()
        
        new_posts = []
        for post in posts:
            writer = User.objects.get(id=post["writer_id"])
            profile = writer.profile
            
            pf_info = profile.__dict__
            pf_info['_state'] = ""
            
            post_info = {
                "post": post,
                "writer": pf_info
            }
            new_posts.append(post_info)
        
        data = {
            "posts": new_posts
        }
        
        return Response(data,status=status.HTTP_200_OK)
    

class Write(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        user = request.user
        post = Post.objects.create(title=request.data['title'],content=request.data['content'],writer=user)
        
        try:
            postImage = request.FILES['postImage']
        except:
            post.postImage = None
        else:
            post.postImage = postImage
            
        post.save()
        
        data = {
            "message": "글 생성 완료"
        }
        return Response(data,status=status.HTTP_201_CREATED)


class Edit(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,pk):
        post = Post.objects.get(id=pk)
        
        try:
            postImage = request.FILES['postImage']
        except:
            post.title = request.data["title"]
            post.content = request.data["content"]
            post.postImage = None
        else:
            post.title = request.data["title"]
            post.content = request.data["content"]
            post.postImage = postImage
            
        post.save()
        
        data = {
            "message": "글 수정 완료"
        }
        return Response(data,status=status.HTTP_200_OK)


class Delete(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request,pk):
        post = Post.objects.get(id=pk)
        post.is_active = False
        post.save()
        
        data = {
            "message": "글 삭제 완료"
        }
        return Response(data,status=status.HTTP_200_OK)


class View(APIView):
    # 좋아요, 글 정보, 댓글과 대댓글 구분
    def post(self,request,pk):

        raw_post = Post.objects.get(id=pk)
        comments = Comment.objects.filter(post=raw_post).values()
        likes = Like_Model.objects.filter(post=raw_post).count()
        writer = Profile.objects.filter(user=raw_post.writer_id).values()
        
        post = raw_post.__dict__
        post['_state'] = ""
        
        data = {
            "post": post,
            "comments": comments,
            "likes": likes,
            "writer": writer[0]
        }
        
        return Response(data,status=status.HTTP_200_OK)
