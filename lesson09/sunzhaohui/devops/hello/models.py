from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=30)
    age = models.IntegerField()
    phone = models.CharField(max_length=11)
    email = models.EmailField()

    class Meta:
        db_table = 'users'
        verbose_name = 'users'
        verbose_name_plural = verbose_name