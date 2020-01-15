from django.contrib import admin
from . import models

@admin.register(models.Alcohol)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'Alcohol_name',
        'volume',
    )