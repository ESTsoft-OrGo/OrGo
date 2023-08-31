from django.db import models
from django.contrib.auth import get_user_model

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


class Tag(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

