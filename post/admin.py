from django.contrib import admin
from .models import User, Post, Like

# 좋아요 기능 확인용

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

class PostAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'created_at', 'updated_at', 'liked_by_count')
    list_filter = ('writer', 'created_at')
    search_fields = ('title', 'content')

    def liked_by_count(self, obj):
        return obj.likes.count()
    liked_by_count.short_description = 'Liked By Count'


admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)