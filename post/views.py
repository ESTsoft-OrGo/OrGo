from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, Post_editSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated  

User = get_user_model()
# Create your views here.
## Post

class List(APIView):
    def post(self, request):
        posts = Post.objects.all().values()
        
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
        likes = LikeModel.objects.filter(post=raw_post).count()
        
        post = raw_post.__dict__
        post['_state'] = ""
        
        data = {
            "post": post,
            "comments": comments,
            "likes": likes
        }
        
        return Response(data,status=status.HTTP_200_OK)