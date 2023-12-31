from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from study.models import Study, Tag
from study.serializers import StudySerializer
from .models import Post, Like as Like_Model, Comment, PostImage
from user.models import Profile
from .serializers import PostSerializer, CommentSerializer
from user.serializers import UserSerializer
from rest_framework.views import APIView
from django.db.models import Q, Count
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .uploads import S3ImgUploader
import json

User = get_user_model()
# Create your views here.


class CommentWrite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        post = Post.objects.get(id=request.data['post_id'])
        comment = Comment.objects.create(
            writer=user, content=request.data['content'], post=post, parent_comment=None)

        datas = {
            "message": "댓글 생성 완료",
        }
        return Response(datas, status=status.HTTP_201_CREATED)


class CommentDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        comment = Comment.objects.get(id=request.data['comment_id'])
        comment.is_active = False
        comment.save()

        datas = {
            "message": "댓글 삭제 완료",
        }
        return Response(datas, status=status.HTTP_200_OK)


class ReCommentWrite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            post = Post.objects.get(id=request.data['post_id'])
        except:
            datas = {
                "message": "해당 게시물을 찾을 수 없습니다.",
            }
            return Response(datas, status=status.HTTP_400_BAD_REQUEST)
        else:
            parent_comment = Comment.objects.get(id=request.data['comment_id'])
            comment = Comment.objects.create(
                writer=user, content=request.data['content'], post=post, parent_comment=parent_comment)
            datas = {
                "message": "대댓글 생성 완료",
            }
            return Response(datas, status=status.HTTP_201_CREATED)


class Unlike(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
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


class List(APIView):

    def get(self, request):
        posts = Post.objects.filter(is_active=True).order_by('-created_at')

        data = []
        for post in posts:
            writer = post.writer
            profile = UserSerializer(writer)
            likes = Like_Model.objects.filter(post_id=post.id).count()
            comments = Comment.objects.filter(
                post=post.id, is_active=True).count()
            images = post.image.all()  # 이미지들 가져오기

            post_info = {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "views": post.views,
                "commnet_count": comments,
                "images": [{"image": image.image.url} for image in images],
                "created_at": post.created_at,
                "updated_at": post.updated_at,
            }

            add_new = {
                "post": post_info,
                "likes": likes,
                "writer": profile.data
            }

            data.append(add_new)

        response_data = {
            "posts": data
        }

        return Response(response_data, status=status.HTTP_200_OK)


class RecommendedPost(APIView):
    def get(self, request):
        # 게시물을 좋아요 수와 작성일자(created_at)를 기준으로 정렬하고 가장 높은 5개를 가져옵니다.
        recommended_posts = Post.objects.filter(is_active=True).annotate(
            like_count=Count('likes')
        ).order_by('-like_count', '-created_at')[:5]

        response_data = {
            "recommended_posts": PostSerializer(recommended_posts, many=True).data
        }

        return Response(response_data, status=status.HTTP_200_OK)


class Write(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        post_data = {
            'title': request.data['title'],
            'content': request.data['content'],
            'writer': user
        }
        images = request.FILES.getlist('images')
        post = Post.objects.create(**post_data)

        for image in images:
            img_uploader = S3ImgUploader(image)
            uploaded_url = img_uploader.upload()
            PostImage.objects.create(post=post, image=uploaded_url)

        data = {
            "message": "글 생성 완료"
        }
        return Response(data, status=status.HTTP_201_CREATED)


class Edit(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        post = Post.objects.get(id=pk)

        post.title = request.data.get('title', post.title)
        post.content = request.data.get('content', post.content)
        post.save()

        img_edit = request.data.get('img_edit')
        delete_img_str = request.data.get('deleted_images')
        delete_img_list = json.loads(delete_img_str)
        if delete_img_list != '[]':
            for img in delete_img_list:
                img_delete = S3ImgUploader(img[1:])
                img_delete.delete()
                prev_imgs = PostImage.objects.get(image=img[1:])
                prev_imgs.delete()
        if img_edit == "true":
            prev_imgs = PostImage.objects.filter(post=post)

            images = request.FILES.getlist('images')

            for image in images:
                img_uploader = S3ImgUploader(image)
                uploaded_url = img_uploader.upload()
                PostImage.objects.create(post=post, image=uploaded_url)

        data = {
            "message": "글 수정 완료"
        }
        return Response(data, status=status.HTTP_200_OK)


class Delete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):

        try:
            post = Post.objects.get(id=pk)
        except ObjectDoesNotExist:
            raise Http404

        images = post.image.all()

        for image in images:
            img_delete = S3ImgUploader(image.image)
            img_delete.delete()
            image.image.delete()
            image.delete()

        post.is_active = False
        post.save()

        data = {
            "message": "글 삭제 완료"
        }
        return Response(data, status=status.HTTP_200_OK)


class View(APIView):
    # 좋아요, 글 정보, 댓글과 대댓글 구분
    def get(self, request, pk):
        raw_post = Post.objects.get(id=pk)
        raw_post.views = raw_post.views + 1
        raw_post.save()

        comments = Comment.objects.filter(post=raw_post, is_active=True)
        likes = Like_Model.objects.filter(post=raw_post).values()
        writer_info = UserSerializer(raw_post.writer).data
        images = raw_post.image.all()
        comment_count = comments.count()

        comments_infos = []

        for comment in comments:
            comments_info = {}
            comments_info['comment'] = CommentSerializer(comment).data
            comments_info['writer'] = UserSerializer(comment.writer).data
            comments_infos.append(comments_info)

        post_data = PostSerializer(raw_post).data
        post_data["images"] = [{"image": image.image.url} for image in images]
        post_data["likes"] = likes.count()
        post_data["comment_count"] = comment_count

        data = {
            "post": post_data,
            "comments": comments_infos,
            "writer": writer_info,
            "likes": likes
        }

        return Response(data, status=status.HTTP_200_OK)


class PostSearch(APIView):
    def get(self, request, query):
        # query = request.data.get('query')

        if query is None:
            return Response({"error": "Missing 'query' parameter"}, status=400)

        profiles = Profile.objects.filter(
            Q(nickname__icontains=query) | Q(about__icontains=query), is_active=True)

        new_profiles = []

        for pf in profiles:
            pf_serializer = UserSerializer(pf.user).data
            new_profiles.append(pf_serializer)

        posts = Post.objects.filter(Q(title__icontains=query) | Q(
            content__icontains=query), is_active=True).order_by('-created_at')
        post_serializers = PostSerializer(posts, many=True).data

        studies = Study.objects.filter(Q(title__icontains=query) | Q(
            description__icontains=query), is_active=True).order_by('-created_at')
        study_serializer = StudySerializer(studies, many=True).data

        new_postlist = []

        for p_s in post_serializers:

            writer = User.objects.get(id=p_s['writer'])
            writer_info = UserSerializer(writer).data

            post_imgs = Post.objects.get(id=p_s['id'])
            images = post_imgs.image.all()  # 이미지들 가져오기
            p_s["images"] = [{"image": image.image.url} for image in images]

            info = {
                'post': p_s,
                'writer': writer_info
            }
            new_postlist.append(info)

        new_studies = []

        for s_s in study_serializer:
            leader = User.objects.get(id=s_s['leader'])
            leader_info = UserSerializer(leader).data
            tags = Tag.objects.filter(study=s_s['id']).values()
            info = {
                'study': s_s,
                'leader': leader_info,
                'tags': tags
            }
            new_studies.append(info)

        response_data = {
            "profiles": new_profiles,
            "posts": new_postlist,
            "studies": new_studies
        }

        return Response(response_data)
