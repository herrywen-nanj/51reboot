# Generated by Django 2.2 on 2019-08-26 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0002_auto_20190826_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='deploy',
            name='deploy_time',
            field=models.DateTimeField(null=True, verbose_name='上线时间'),
        ),
        migrations.AlterField(
            model_name='deploy',
            name='review_time',
            field=models.DateTimeField(null=True, verbose_name='审核时间'),
        ),
    ]
