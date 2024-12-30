from django.contrib import admin

from apps.users.models.users import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):...
