from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from users.models import User
from config import settings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'img_profile',

    )
