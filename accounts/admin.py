from django.contrib import admin

from accounts.models import User
from config import settings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
