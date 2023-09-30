from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

User = get_user_model()

class Study(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_leader')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    
    ON_OFF_CHOICES = [
        ('ON', 'Online'), 
        ('OFF', 'Offline'),
    ]
    online_offline = models.CharField(max_length=5, choices=ON_OFF_CHOICES)

    
    STATUS_CHOICES = [
        ('종료', '종료'),
        ('모집중', '모집중'),
        ('진행중','진행중')
    ]
    
    location = models.CharField(max_length=200,null=True)
    max_participants = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    is_active = models.BooleanField(default=True)
    participants = models.ManyToManyField(User, related_name='study_participants', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def on_post_save_for_study(sender, **kwargs):
    if kwargs['created']:
        study = kwargs['instance']
        groupChat = GroupChat.objects.create(study=study)
        groupChat.title = f'studyroom{groupChat.pk}'
        groupChat.save()

post_save.connect(on_post_save_for_study, sender=Study)

class GroupChat(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leader',null=True)
    study = models.OneToOneField(Study,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # members = models.ManyToManyField(User, related_name="group_chats")

# def group_chat_action(sender, **kwargs):
#     if kwargs['created']:
#         group_chat = kwargs['instance']
#         content = f'단체 채팅방을 생성하였습니다.'
        
#         for member in group_chat.members.all():
#             Notification.objects.create(sender=group_chat.leader, receiver=member, content=content)

# post_save.connect(group_chat_action, sender=GroupChat)


class GroupMessage(models.Model):
    chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

