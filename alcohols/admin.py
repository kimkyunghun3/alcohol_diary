from django.contrib import admin
from . import models


@admin.register(models.Alcohol)
class AlcoholAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AlcoholRecord)
class AlcoholRecordAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AlcoholType)
class AlcoholTypeAdmin(admin.ModelAdmin):
    pass
