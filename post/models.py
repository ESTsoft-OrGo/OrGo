from django.db import models
from django.contrib.auth import get_user_model
from notify.models import Notification
from django.db.models.signals import post_save

User = get_user_model()


class Post(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.CharField(max_length=200,null=True,blank=True)
    postImage = models.ImageField(upload_to='post/media',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='Like')


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
    
def Like_action(sender, **kwargs):
    if kwargs['created']:
        like = kwargs['instance']
        post = like.post
        content = f'{post.title}에 좋아요를 남겼습니다.'
        
        noti = Notification.objects.create(sender=like.user,receiver=post.writer,content=content)

post_save.connect(Like_action, sender=Like)