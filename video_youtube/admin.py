from django.contrib import admin
from . import models


@admin.register(models.VideoUrl)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['language', 'url', 'name']


@admin.register(models.VideoTime)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['video_url', 'start_time', 'stop_time', 'text_en', 'text_ru_original', 'text_ru_youtube']


