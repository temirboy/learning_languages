from django.db import models
from users.models import User
from django.conf.global_settings import LANGUAGES


class Languages(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название языка', max_length=10, choices=LANGUAGES, default='en')
    default = models.BooleanField(default=True)

    class Meta:
        db_table = 'languages'
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_languages')
        ]
