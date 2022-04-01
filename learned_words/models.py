from django.db import models
from users.models import User
from languages.models import Languages
from video_youtube.models import VideoTime


class LearnedWords(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    video_time = models.ForeignKey(VideoTime, on_delete=models.CASCADE)
    text_en = models.CharField('Новое слово:', max_length=200)
    text_ru = models.CharField('Перевод:', max_length=200)
    phrase = models.BooleanField('false-слово, true-фраза')
    video = models.BooleanField('false-изучал через текст, true-изучал через видео')

    class Meta:
        db_table = 'learned_words'
