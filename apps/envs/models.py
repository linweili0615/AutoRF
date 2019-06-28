from django.db import models


class EnvInfo(models.Model):
    e_id = models.BigAutoField(primary_key=True)
    p_id = models.BigIntegerField(null=False, verbose_name='所属项目')
    e_name = models.CharField(max_length=50, null=True, unique=True, verbose_name='环境名称')
    e_value = models.CharField(max_length=150, null=True, verbose_name='环境变量')
    is_default = models.IntegerField(null=True, verbose_name='是否默认')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'env_info'
        verbose_name = '环境信息'
        verbose_name_plural = verbose_name