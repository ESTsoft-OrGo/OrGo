from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Profile, Follower

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'is_superuser', 'liked_post')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    
    def liked_post(self, obj):
        liked_posts=obj.liked_posts.all()
        posts = []
        for post in liked_posts.all():
            posts.append(post.title)
        return posts
    liked_post.short_description = 'Liked Post'


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Follower)
