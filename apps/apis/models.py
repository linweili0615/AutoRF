from django.db import models


class ApiInfo(models.Model):
    a_id = models.BigAutoField(primary_key=True)
    e_id = models.BigIntegerField(null=False, verbose_name='环境')
    p_id = models.BigIntegerField(null=False, verbose_name='所属项目')
    g_id = models.BigIntegerField(null=True, verbose_name='所属分组')
    a_name = models.CharField(max_length=100, null=False, unique=True, verbose_name='接口名称')
    paths = models.TextField(null=False, verbose_name='请求路径')
    methods = models.CharField(max_length=20, verbose_name='请求方法')
    headers = models.TextField(null=True, verbose_name='请求头部')
    cookies = models.TextField(null=True, verbose_name='请求cookie')
    param_type = models.CharField(null=True, max_length=20, verbose_name='参数类型')
    params = models.TextField(null=True, verbose_name='请求参数')
    asserts = models.TextField(null=True, verbose_name='断言')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建')
    update_user = models.CharField(max_length=50, null=False, verbose_name='修改')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'api_info'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name
