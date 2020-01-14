from django.contrib import admin

from account.models import User
from config import settings


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass