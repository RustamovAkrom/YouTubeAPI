from django.contrib import admin

from apps.videos.models.histories import WatchHistory


@admin.register(WatchHistory)
class WatchHistoryAdmin(admin.ModelAdmin):...
