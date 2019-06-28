from django.db import models


class TaskInfo(models.Model):
    t_id = models.BigAutoField(primary_key=True)
    t_name = models.CharField(max_length=100, null=False, unique=True, verbose_name='任务名称')
    e_id = models.BigIntegerField(null=True, verbose_name='环境')
    cron = models.CharField(null=True, max_length=20, verbose_name='定时策略')
    status = models.CharField(max_length=2, verbose_name='是否启用')
    start_time = models.DateTimeField(max_length=50, verbose_name='开始时间')
    end_time = models.DateTimeField(max_length=50, verbose_name='结束时间')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建')
    update_user = models.CharField(max_length=50, null=False, verbose_name='修改')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'task_info'
        verbose_name = '任务信息'
        verbose_name_plural = verbose_name


class TaskExtendInfo(models.Model):
    te_id = models.BigAutoField(primary_key=True)
    t_id = models.BigIntegerField(null=False, verbose_name='所属任务')
    e_id = models.BigIntegerField(null=False, verbose_name='环境')
    te_name = models.CharField(max_length=100, null=False, verbose_name='接口名称')
    paths = models.TextField(null=False, verbose_name='请求路径')
    methods = models.CharField(max_length=20, verbose_name='请求方法')
    headers = models.TextField(null=True, verbose_name='请求头部')
    cookies = models.TextField(null=True, verbose_name='请求cookie')
    param_type = models.CharField(null=True, max_length=20, verbose_name='参数类型')
    params = models.TextField(null=True, verbose_name='请求参数')
    asserts = models.TextField(null=True, verbose_name='断言')
    extracts = models.TextField(null=True, verbose_name='断言')
    status = models.CharField(max_length=2, verbose_name='是否启用')
    rank = models.IntegerField(verbose_name='序号')
    create_user = models.CharField(max_length=50, null=False, verbose_name='创建')
    update_user = models.CharField(max_length=50, null=False, verbose_name='修改')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'task_extend_info'
        verbose_name = '任务扩展信息'
        verbose_name_plural = verbose_name


class TaskResult(models.Model):
    r_id = models.BigAutoField(primary_key=True)
    batch_id = models.CharField(max_length=50, null=False, verbose_name='批次ID')
    e_id = models.BigIntegerField(null=False, verbose_name='环境')
    t_id = models.BigIntegerField(null=False, verbose_name='所属任务')
    te_id = models.BigIntegerField(null=False, verbose_name='任务详情')
    # -1 未启用 1 执行中 3 通过 4 失败
    t_status = models.IntegerField(null=False, verbose_name='执行状态')
    execute_user = models.CharField(max_length=50, null=False, verbose_name='执行')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='开始时间')
    end_time = models.DateTimeField(auto_now=True, verbose_name='结束时间')

    class Meta:
        db_table = 'task_result'
        verbose_name = '任务执行结果'
        verbose_name_plural = verbose_name
