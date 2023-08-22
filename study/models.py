from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Study(models.Model):
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_leader')
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    ON_OFF_CHOICES = [
        ('ON', 'online'), 
        ('OFF', 'offline'),
        ]
    online_offline = models.CharField(max_length=5, choices=ON_OFF_CHOICES)

    location = models.CharField()
    max_participants = models.IntegerField(default=0)
    
    STATUS_CHOICES = [
        ('종료', '종료')
        ('모집중', '모집중')
        ('진행중','진행중')
    ]
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)
    
    participants = models.ForeignKey(User, on_delete=models.CASCADE, related_name='study_participants')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    Study = models.ForeignKey(Study, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
