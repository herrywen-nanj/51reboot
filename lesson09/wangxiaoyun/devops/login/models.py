from django.db import models

# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# Create your models here.
#ORM
class Users(models.Model):   #创建mysql数据库表字段信息
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    roles = models.CharField(max_length=10)

    class Meta:   #指定mysql 数据库的表名
        db_table = 'users'
        verbose_name = 'users'   #解决Django administration 页面显示userss的问题
        verbose_name_plural = verbose_name    #同上