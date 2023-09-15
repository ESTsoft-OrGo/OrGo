from django.db import models
from django.contrib.auth import get_user_model
from notify.models import Notification
from django.db.models.signals import post_save

User = get_user_model()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.CharField(max_length=200,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', through='Like')
    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post'


class PostImage(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='image')
    image = models.FileField()

    def __int__(self):
        return self.id

    class Meta:
        db_table = 'post_image'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    content = models.CharField(max_length=50)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def comment_action(sender, **kwargs):
    if kwargs['created']:
        comment = kwargs['instance']
        post = comment.post
        content = f'{post.title}에 댓글을 남겼습니다.'
        
        # noti = Notification.objects.create(sender=comment.writer,receiver=post.writer,content=content)
        if comment.parent_comment is None:
            noti = Notification.objects.create(sender=comment.writer, receiver=post.writer, content=content)
        else:
            parent_comment = comment.parent_comment
            noti_content = f'{parent_comment.content}에 대댓글을 달았습니다.'
            noti = Notification.objects.create(sender=comment.writer, receiver=parent_comment.writer, content=noti_content)

post_save.connect(comment_action, sender=Comment)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
def like_action(sender, **kwargs):
    if kwargs['created']:
        like = kwargs['instance']
        post = like.post
        content = f'{post.title}에 좋아요를 남겼습니다.'
        
        noti = Notification.objects.create(sender=like.user,receiver=post.writer,content=content)

post_save.connect(like_action, sender=Like)
