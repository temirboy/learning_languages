from django.db import models
from users.models import User
from languages.models import Languages


class VideoUrl(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    name = models.CharField('Название видео:', max_length=100)
    url = models.URLField('Ссылка на youtube видео:')

    def __str__(self):
        return self.name

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

