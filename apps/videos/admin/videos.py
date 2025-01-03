from django.contrib import admin

from apps.videos.models.videos import Video, VideoDislike, VideoLike


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
    

@admin.register(VideoDislike)
class VideoDislikeAdmin(admin.ModelAdmin):
    pass


@admin.register(VideoLike)
class VideoLikeAdmin(admin.ModelAdmin):
    pass
