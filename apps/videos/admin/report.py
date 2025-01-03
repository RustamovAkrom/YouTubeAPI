from django.contrib import admin
from apps.videos.models import VideoReport


@admin.register(VideoReport)
class VideoReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'report_type', 'status', 'created_at', 'updated_at', )
    list_filter = ('report_type', 'status', )
    search_fields = ('user__username', 'video__title', 'description', )

    actions = ['mark_resolved']

    def mark_resolved(self, request, queryset):
        queryset.update(status=VideoReport.StatusChoices.RESOLVED)
        self.message_user(request, "Выбранные жалобы помечены как решенные.")
