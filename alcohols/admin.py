from django.contrib import admin
from . import models


@admin.register(models.Alcohol)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AlcoholRecord)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AlcoholType)
class UserAdmin(admin.ModelAdmin):
    pass
