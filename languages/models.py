from django.db import models
from users.models import User
from django.conf.global_settings import LANGUAGES
from django.utils.translation import gettext_lazy as _


class Languages(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_("lang"), max_length=50, choices=LANGUAGES)
    #name = models.CharField('Полное название языка', max_length=50)
    #reduction = models.CharField('Сокращенное название языка', max_length=6)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'languages'


#class LanguagesName(models.Model):
#    """

#   """
    #name = models.CharField(_("lang"), max_length=50, choices=LANGUAGES)

    #class Meta:
    #    db_table = 'languages_name'
