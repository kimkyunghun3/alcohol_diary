from django.contrib import admin

from users.models import User
from config import settings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'img_profile',

    )
