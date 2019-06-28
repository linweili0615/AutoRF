# Generated by Django 2.2.1 on 2019-06-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInfo',
            fields=[
                ('p_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100, unique=True, verbose_name='项目名称')),
                ('create_user', models.CharField(max_length=50, verbose_name='创建者')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'project_info',
            },
        ),
    ]