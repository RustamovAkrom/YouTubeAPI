from django.contrib import admin

from apps.videos.models.playlists import PlayList, PlayListVideo


@admin.register(PlayList)
class PlayListAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_public', 'channel', 'user']
    search_fields = ['name', 'description']


@admin.register(PlayListVideo)
class PlayListVideoAdmin(admin.ModelAdmin):...
