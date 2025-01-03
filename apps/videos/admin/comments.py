from django.contrib import admin

from apps.videos.models.comments import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'message', 'created_at', 'updated_at')
    search_fields = ('user', 'video', 'message')
