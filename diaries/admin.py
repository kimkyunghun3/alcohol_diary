from django.contrib import admin
from . import models


@admin.register(models.Diary)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'date',
        'review',
        'drunken_level',
        'hangover_level',
        'action_type',
        'action_type_img',

    )
