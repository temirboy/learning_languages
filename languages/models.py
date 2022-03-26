from django.db import models
from users.models import User
from django.conf.global_settings import LANGUAGES
from django.utils.translation import gettext_lazy as _


class Languages(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=LANGUAGES, default='en')

    class Meta:
        db_table = 'languages'
        constraints = [
            models.UniqueConstraint(fields=['user', 'name'], name='unique_languages')
        ]
