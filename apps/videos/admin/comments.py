from django.contrib import admin

from apps.videos.models.comments import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['message']
