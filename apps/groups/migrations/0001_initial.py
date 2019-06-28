# Generated by Django 2.2.1 on 2019-06-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupInfo',
            fields=[
                ('g_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='分组ID')),
                ('p_id', models.BigIntegerField(verbose_name='所属项目')),
                ('g_name', models.CharField(max_length=100, unique=True, verbose_name='分组名称')),
                ('create_user', models.CharField(max_length=50, verbose_name='创建者')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '分组信息',
                'verbose_name_plural': '分组信息',
                'db_table': 'group_info',
            },
        ),
    ]
