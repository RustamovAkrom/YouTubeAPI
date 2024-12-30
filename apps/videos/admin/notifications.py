from django.contrib import admin

from apps.videos.models.notifications import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):...
