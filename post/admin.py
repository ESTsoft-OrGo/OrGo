from django.contrib import admin
from .models import User, Post, Like, Comment

#좋아요 기능 확인용

class PostAdmin(admin.ModelAdmin):
    list_display = ('writer', 'title', 'created_at', 'updated_at', 'liked_by_count')
    list_filter = ('writer', 'created_at')
    search_fields = ('title', 'content')
    
    def liked_by_count(self, obj):
        return obj.likes.count()
    liked_by_count.short_description = 'Liked By Count'
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)