from django.db import models

# Create your models here.


class Users(models.Model):

    username    =   models.CharField(max_length=32)
    age         =   models.IntegerField()
    phone       =   models.CharField(max_length=11)
    email       =   models.EmailField()

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['username']

