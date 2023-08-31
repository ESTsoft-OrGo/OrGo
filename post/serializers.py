from rest_framework import serializers
from .models import Post, Like, PostImage, Comment


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    def get_images(self, obj):
        image = obj.image_set.all() 
        return PostImageSerializer(instance=image, many=True, context=self.context).data

    class Meta:
        model = Post
        fields = ['id', 'writer', 'title', 'content', 'images', 'is_active', 'created_at', 'updated_at', 'likes','views']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images') 
        instance = Post.objects.create(**validated_data)

        for image_data in images_data:
            PostImage.objects.create(post=instance, image=image_data)

        return instance


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class Post_editSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'postImage']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'