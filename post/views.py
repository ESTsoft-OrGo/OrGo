from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from .models import Post, Like
from django.views import View
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()


class PostListView(View):
    template_name = 'post_list.html'

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        context = {
            'posts': posts,
        }

        return render(request, self.template_name, context)

class PostDetailView(View):
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')  # URL에서 post_id 가져오기
        post = Post.objects.get(id=post_id)
        user = User.objects.get(email='test123@example.com')

        # 해당 사용자가 해당 게시글을 좋아요한 경우인지 확인
        liked = Like.objects.filter(user=user, post=post).exists()

        context = {
            'post': post,
            'liked': liked,
        }

        return render(request, self.template_name, context)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        post_id = request.data.get('post_id')
        user = request.user

        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=user)

        if created:
            return Response({"detail": "Post liked successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You've already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    def unlike(self, request):
        post_id = request.data.get('post_id')
        user = request.user

        post = get_object_or_404(Post, pk=post_id)
        like = Like.objects.filter(post=post, user=user).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You haven't liked this post before."}, status=status.HTTP_400_BAD_REQUEST)
