# Generated by Django 2.2 on 2019-08-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0006_deploy_build_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deploy',
            name='build_serial',
            field=models.IntegerField(default=0, null=True, verbose_name='构建序号'),
        ),
    ]
