from django.contrib import admin
from apps.videos.models import VideoReport


@admin.register(VideoReport)
class VideoReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'report_type', 'created_at', 'updated_at')
    list_filter = ('report_type')
    search_fields = ('user__username', 'video__title', 'description')
