from django.contrib import admin
from .models import Study, Tag, GroupChat, GroupMessage
# Register your models here.

admin.site.register(Study)
admin.site.register(Tag)
admin.site.register(GroupChat)
admin.site.register(GroupMessage)
