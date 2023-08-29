from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Notification(models.Model):
    content = models.CharField(max_length=30)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE , related_name='receiver')
    sender = models.ForeignKey(User, on_delete=models.CASCADE , related_name='sender')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    