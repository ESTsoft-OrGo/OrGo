from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile, Follower

User = get_user_model()

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Follower)