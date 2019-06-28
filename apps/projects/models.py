from django.db import models


class ProjectInfo(models.Model):
    p_id = models.BigAutoField(primary_key=True)
    p_name = models.CharField(max_length=100, null=False, unique=True, verbose_name='项目名称')
    p_type = models.CharField(max_length=50, null=False, verbose_name='类型')
    p_status = models.CharField(max_length=50, null=False, default=1, verbose_name='状态')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'project_info'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name