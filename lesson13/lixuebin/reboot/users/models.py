from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, User, Group, Permission

class UserProfile(AbstractUser):
    name_cn = models.CharField('中文名', max_length=30)
    phone = models.CharField('手机号', max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.username