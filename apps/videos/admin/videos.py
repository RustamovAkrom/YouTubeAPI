from django.contrib import admin

from apps.videos.models.videos import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'description', 
        'thumbnail', 
        'channel', 
        'category', 
        'visibility', 
        'views_count', 
        'duration',
    ]
    search_fields = [
        'title',
        'description',
        'thumbnail',
        'channel',
        'category',
        'tag',
        'visibility',
    ]
    