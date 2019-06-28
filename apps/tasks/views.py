from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskListSerializer, TaskInfoSerializer, \
    TaskExtendSerializer, TaskExtendInfoSerializer, TaskResultSerializer
from .models import TaskInfo, TaskExtendInfo, TaskResult
from apis.models import ApiInfo
from apis.serializers import ApiSerializer
from common.PageUtil import NewPageNumberPagination
from django.db.models import Q
from rest_framework import permissions
from rest_framework_jwt import authentication
from common.redisUtil import getRedis
from common.rediskey import RKeys
from common.requestUtil import do_api


class DealTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            t_id = request.data['t_id']
            status = request.data['status']
            if t_id and status:
                TaskInfo.objects.filter(t_id=t_id).update(status=status, update_user=request.user.username)
            return Response({'code': 'success', 'msg': '已处理'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '任务id或状态不能为空'})


class EditTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            un = request.user.username
            t_id = request.data['t_id']
            e_id = request.data['e_id']
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            cron = request.data['cron']
            status = request.data['status']
            if t_id and start_time and end_time and cron and status:
                if not e_id:
                    e_id = None
                TaskInfo.objects.filter(t_id=t_id).update(e_id=e_id,  start_time=start_time,
                                                          end_time=end_time, cron=cron, status=status, update_user=un)
                return Response({'code': 'success', 'msg': '已更新'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查！'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '任务id或状态不能为空'})


class AddTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            un = request.user.username
            e_id = request.data['e_id']
            t_name = request.data['t_name']
            start_time = request.data['start_time']
            end_time = request.data['end_time']
            cron = request.data['cron']
            status = request.data['status']
            if e_id and start_time and end_time and cron and status and t_name:
                info = TaskInfo(e_id=e_id,  t_name=t_name, start_time=start_time,end_time=end_time, cron=cron, status=status, update_user=un)
                info.save()
                return Response({'code': 'success', 'msg': '已更新', 't_id': info.t_id})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查！'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '添加任务异常'})


class DelTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            t_id = request.data['t_id']
            if t_id:
                TaskInfo.objects.filter(t_id=t_id).delete()
            return Response({'code': 'success', 'msg': '已删除'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '任务id不能为空'})


class GetTaskView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            t_id = request.GET.get('t_id', None)
            if t_id:
                info = TaskInfo.objects.filter(t_id=t_id).first()
                if not info:
                    return Response({'code': '404', 'msg': '未找到相关信息'})
                data = TaskInfoSerializer(info).data
                return Response({'code': 'success', 'data': data})
            else:
                return Response({'code': 'error', 'msg': '任务ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取定时任务信息异常'})


class TaskListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            q1 = Q()
            t_id = request.GET.get('t_id', None)
            t_name = request.GET.get('t_name', None)
            if t_name:
                q1.add(Q(t_name__contains=t_name), Q.AND)
            if t_id:
                q1.add(Q(t_id=t_id), Q.AND)
            if q1:
                info = TaskInfo.objects.filter(q1).order_by('-t_id')
            else:
                info = TaskInfo.objects.order_by('-t_id')
            pg = NewPageNumberPagination()
            pg_info = pg.paginate_queryset(queryset=info, request=request)
            data = TaskListSerializer(instance=pg_info, many=True).data
            return Response({'code': 'success', 'list': data, 'total': info.count()})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取任务列表异常'})


class TaskExtendInfoListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            t_id = request.GET.get('t_id', None)
            if t_id:
                data = TaskExtendInfoSerializer(TaskExtendInfo.objects.filter(t_id=t_id).order_by('rank'), many=True).data
                return Response({'code': 'success', 'data': data})
            else:
                return Response({'code': 'error', 'msg': '任务ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取任务详情异常'})


class ChangeTaskExtendInfoRankView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            old_id = request.data['old_id']
            old_rank = request.data['old_rank']
            new_id = request.data['new_id']
            new_rank = request.data['new_rank']

            if old_id and old_rank and new_id and new_rank:
                TaskExtendInfo.objects.filter(te_id=old_id).update(rank=new_rank)
                TaskExtendInfo.objects.filter(te_id=new_id).update(rank=old_rank)
                return Response({'code': 'success', 'msg': '任务详情顺序已更改'})
            else:
                return Response({'code': 'error', 'msg': '更改任务详情顺序失败'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '更改任务详情顺序异常'})


class TaskExtendStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            te_id = request.data['te_id']
            status = request.data['status']
            if te_id and status:
                TaskExtendInfo.objects.filter(te_id=te_id).update(status=status)
                return Response({'code': 'success', 'msg': '状态已更改'})
            else:
                return Response({'code': 'error', 'msg': '任务详情ID或状态不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '更改任务详情状态异常'})


class DelTaskExtendView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            te_id = request.data['te_id']
            if te_id:
                TaskExtendInfo.objects.filter(te_id=te_id).delete()
                return Response({'code': 'success', 'msg': '已删除'})
            else:
                return Response({'code': 'error', 'msg': '任务详情ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '删除任务详情异常'})


class AddTaskExtendView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            un = request.user.username
            t_id = request.data['t_id']
            api_list = request.data['api_list']
            if t_id and api_list:
                taskinfo_list = []
                for api in api_list:
                    api_info = ApiSerializer(ApiInfo.objects.filter(a_id=api['a_id']).first()).data

                    info = TaskExtendInfo.objects.order_by('-rank').first()
                    if info:
                        rank = TaskExtendSerializer(info).data['rank'] + 1
                    else:
                        rank = 1
                    task_extend_info = TaskExtendInfo(t_id=t_id, e_id=api_info['e_id'], te_name=api_info['a_name'],
                                                      paths=api_info['paths'],
                                                      methods=api_info['methods'], headers=api_info['headers'],
                                                      cookies=api_info['cookies'],
                                                      param_type=api_info['param_type'], params=api_info['params'],
                                                      asserts=api_info['asserts'],
                                                      status='-1', rank=rank, create_user=un,
                                                      update_user=un)
                    taskinfo_list.append(task_extend_info)
                TaskExtendInfo.objects.bulk_create(taskinfo_list)
                return Response({'code': 'success', 'msg': '已添加'})
            else:
                return Response({'code': 'error', 'msg': '任务ID或添加api列表不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '添加  任务详情异常'})


class TaskTestView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            t_id = request.data['t_id']
            uname = request.user.username
            if not uname:
                uname = '定时执行'
            if t_id:
                task_extend_list = TaskExtendInfoSerializer(TaskExtendInfo.objects.filter(t_id=t_id).all(), many=True).data
                redis = getRedis()
                import uuid
                uid = str(uuid.uuid1())
                for info in task_extend_list:
                    if info['status'] == '1':
                        t_result = TaskResult(batch_id=uid, e_id=info['e_id'], t_id=info['t_id'], te_id=info['te_id'], t_status=1, execute_user=uname)
                        t_result.save()
                        result = do_api(**info)
                        status_code = result['res']['status_code']
                        _taskresult = TaskResult.objects.get(r_id=t_result.r_id)
                        if status_code == '200':
                            _taskresult.t_status = 3
                        else:
                            _taskresult.t_status = 4
                        _taskresult.save()
                        redis.hset(name=RKeys.TASK_EXTEND_RESULT + uid, key=info['te_id'], value=result)
                    else:
                        TaskResult(batch_id=uid, e_id=info['e_id'], t_id=info['t_id'], te_id=info['te_id'], t_status=-1, execute_user=uname).save()
                return Response({'code': 'success', 'msg': '任务已执行', 'batch_id': uid})
            else:
                return Response({'code': 'error', 'msg': '任务ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '执行任务异常'})


class TaskResultListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            t_id = request.GET.get('t_id', None)
            if t_id:
                taskResult = TaskResult.objects.filter(t_id=t_id).values('batch_id', 'execute_user').distinct()
                data = TaskResultSerializer(taskResult, many=True).data
                return Response({'code': 'success', 'list': data})
            else:
                return Response({'code': 'error', 'msg': '任务ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取历史结果列表异常'})


class DelTaskResultView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            batch_id = request.GET.get('batch_id', None)
            if batch_id:
                TaskResult.objects.filter(batch_id=batch_id).delete()
                redis = getRedis()
                redis.delete(RKeys.TASK_EXTEND_RESULT + batch_id)
                return Response({'code': 'success', 'msg': '记录已删除'})
            else:
                return Response({'code': 'error', 'msg': '批次ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '删除记录失败'})
