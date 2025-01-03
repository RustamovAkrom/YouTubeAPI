from django.contrib import admin
from apps.videos.models import SearchHistory


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    pass
