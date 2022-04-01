from django.contrib import admin
from . import models

@admin.register(models.LearnedWords)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['user', 'language', 'video_time', 'text_en', 'text_ru', 'phrase', 'video']

