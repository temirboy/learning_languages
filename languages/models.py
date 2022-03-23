from django.db import models
from users.models import User



class Languages(models.Model):
    """

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Полное название языка', max_length=50)
    reduction = models.CharField('Сокращенное название языка', max_length=6)

    class Meta:
        db_table = 'languages'
