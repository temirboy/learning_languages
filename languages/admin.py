from django.contrib import admin
from . import models


@admin.register(models.Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']


