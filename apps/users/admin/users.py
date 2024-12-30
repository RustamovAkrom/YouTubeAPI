from django.contrib import admin

from apps.users.models.users import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'avatar']
    search_fields = ['email', 'username']
    