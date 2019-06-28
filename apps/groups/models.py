from django.db import models


class GroupInfo(models.Model):
    g_id = models.BigAutoField(primary_key=True, verbose_name='分组ID')
    p_id = models.BigIntegerField(null=False, verbose_name='所属项目')
    g_name = models.CharField(max_length=100, null=False, verbose_name='分组名称')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'group_info'
        verbose_name = '分组信息'
        verbose_name_plural = verbose_name