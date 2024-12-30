from django.contrib import admin

from apps.videos.models.tags import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):...
