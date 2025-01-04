from django.contrib import admin

from apps.videos.models import LiveStream


@admin.register(LiveStream)
class LiveStreamAdmin(admin.ModelAdmin):
    pass
