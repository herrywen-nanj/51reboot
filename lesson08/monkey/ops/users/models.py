from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Users(models.Model):

    username    =   models.CharField(max_length=32)
    age         =   models.IntegerField()
    phone       =   models.CharField(max_length=11)
    email       =   models.EmailField()
    address     =   models.CharField(max_length=100)

    class Meta:
        db_table = 'users'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['username']


class Manufacturer(models.Model):
    name        =   models.CharField(max_length=32, unique=True, verbose_name="制造商")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "manufacturer"
        verbose_name = "制造商"
        verbose_name_plural = verbose_name

class Car(models.Model):
    name        =   models.CharField(max_length=32, unique=True, verbose_name="车")
    manufacturers   = models.ForeignKey(Manufacturer)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "car"
        verbose_name = "车"
        verbose_name_plural = verbose_name


class UserProfile(models.Model):
    username_cn      = models.CharField(max_length=32, verbose_name="中文名")
    users           =   models.OneToOneField(User)

    def __str__(self):
        return self.username_cn

    class Meta:
        db_table = "user_profile"
        verbose_name = "扩展用户表"
        verbose_name_plural = verbose_name
