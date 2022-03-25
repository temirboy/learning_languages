from django.db import models
from users.models import User
from languages.models import Languages


class VideoUrl(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    url = models.URLField('Ссылка на youtube видео')
    name = models.TextField('Название видео')

    class Meta:
        db_table = 'video_url'


class VideoTime(models.Model):
    """

    """
    video_url = models.ForeignKey(VideoUrl, on_delete=models.CASCADE)
    start_time = models.FloatField()
    stop_time = models.FloatField()
    text_en = models.TextField('Субтитры на en')
    text_ru_original = models.TextField('Субтитры оригинальные, если есть')
    text_ru_youtube = models.TextField('Субтитры сгенерированные youtube')

    class Meta:
        db_table = 'video_time'


class NewWorlds(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    video_time = models.ForeignKey(VideoTime, on_delete=models.CASCADE)
    text_en = models.TextField()
    text_ru = models.TextField()

    class Meta:
        db_table = 'new_worlds'


class LearnedWords(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    video_time = models.ForeignKey(VideoTime, on_delete=models.CASCADE)
    text_en = models.TextField()
    text_ru = models.TextField()
    phrase = models.BooleanField('false-слово, true-фраза')
    video = models.BooleanField('false-изучал через текст, true-изучал через видео')

    class Meta:
        db_table = 'learned_words'
