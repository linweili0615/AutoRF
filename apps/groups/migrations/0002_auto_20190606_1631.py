# Generated by Django 2.2.1 on 2019-06-06 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupinfo',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 6, 16, 31, 4, 838225), verbose_name='创建时间'),
        ),
    ]