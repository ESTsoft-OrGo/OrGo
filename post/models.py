from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='Like')
    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post'


# 이미지 업로드 경로
def image_upload_path(instance, filename):
    return f'{instance.post.id}/{filename}'


class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post_image'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)