from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProjectInfo
from .serializers import ProjectInfoSerializer
from django.db.models import Q
from rest_framework.views import APIView
from common.PageUtil import NewPageNumberPagination
from rest_framework import permissions
from rest_framework_jwt import authentication


class AddProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['p_name'] and res_data['p_type'] and ['p_status']:
                p_info = ProjectInfo(p_name=res_data['p_name'], p_type=res_data['p_type'], p_status=res_data['p_status'], create_user=request.user.username)
                p_info.save()
                return Response({'code': 'success', 'msg': '项目已添加'})
            else:
                Response({'code': 'error', 'msg': '参数错误，请检查'})
        except IntegrityError:
            return Response({'code': 'error', 'msg': '该项目名称已存在'})


class DelProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['p_id']:
                ProjectInfo.objects.filter(p_id=res_data['p_id']).delete()
                return Response({'code': 'success', 'msg': '记录已删除'})
            else:
                return Response({'code': 'error', 'msg': '项目ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '删除项目异常'})


class EditProjectStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['p_id'] and res_data['p_status']:
                ProjectInfo.objects.filter(p_id=res_data['p_id']).update(p_status=res_data['p_status'])
                return Response({'code': 'success', 'msg': '状态已更改'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查！'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '编辑项目状态异常'})


class EditProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['p_id'] and res_data['p_status'] and res_data['p_type'] and res_data['p_name']:
                ProjectInfo.objects.filter(p_id=res_data['p_id']).update(p_status=res_data['p_status'],
                                                                         p_type=res_data['p_type'], p_name=res_data['p_name'])
                return Response({'code': 'success', 'msg': '已更新'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查'})
        except IntegrityError:
            return Response({'code': 'error', 'msg': '该项目名称已存在'})
        except Exception as e:
            return Response({'code': 'error', 'msg': '更新项目异常'})


class ProjectView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['p_id']:
                p_info = ProjectInfo.objects.filter(p_id=res_data['p_id']).first()
                Seria = ProjectInfoSerializer(instance=p_info)
                return Response({'code': 'success', 'data': Seria.data})
            else:
                return Response({'code': 'error', 'msg': '项目ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取项目信息失败'})


class ProjectListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            q1 = Q()
            p_name = request.GET.get('p_name', None)
            p_id = request.GET.get('p_id', None)

            if p_name is not None:
                q1.add(Q(p_name__contains=p_name), Q.AND)
            if p_id is not None:
                q1.add(Q(p_id=p_id), Q.AND)
            if q1:
                projectinfo = ProjectInfo.objects.filter(q1).order_by('-p_id')
            else:
                projectinfo = ProjectInfo.objects.all().order_by('-p_id')
            pg = NewPageNumberPagination()
            pg_projectinfo = pg.paginate_queryset(queryset=projectinfo, request=request)
            Seria = ProjectInfoSerializer(instance=pg_projectinfo, many=True)

            return Response({'total': projectinfo.count(), 'list': Seria.data})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取项目列表失败'})

