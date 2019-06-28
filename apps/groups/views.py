from django.db import IntegrityError
from rest_framework.response import Response
from .models import GroupInfo
from projects.models import ProjectInfo
from .serializers import ProjectJoinGroupSerializer, ProjectJoinGroupNewSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt import authentication


class AddGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            g_name = request.data['g_name']
            p_id = request.data['p_id']
            if p_id and g_name:
                try:
                    g = GroupInfo(p_id=p_id, g_name=g_name, create_user=request.user.username)
                    g.save()
                    return Response({'code': 'success', 'msg': '已添加'})
                except IntegrityError:
                    return Response({'code': 'error', 'msg': '该分组名称已存在'})
            else:
                return Response({'code': 'error', 'msg': '项目ID或分组名称不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '添加分组信息异常'})


class DelGoupView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['g_id']:
                GroupInfo.objects.filter(g_id=res_data['g_id']).delete()
                return Response({'code': 'success', 'msg': '已删除'})
            else:
                return Response({'code': 'error', 'msg': '分组ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '删除分组信息异常'})


class EditGoupView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['g_id'] and res_data['g_name']:
                count = GroupInfo.objects.filter(g_id=res_data['g_id']).update(g_name=res_data['g_name'])
                if count > 0:
                    return Response({'code': 'success', 'msg': '已修改'})
                else:
                    return Response({'code': 'error', 'msg': '该分组不存在'})
            else:
                return Response({'code': 'error', 'msg': '分组ID或分组名称不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '编辑分组信息异常'})


class GroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            g_id = request.GET.get('g_id', None)
            if g_id:
                info = ProjectJoinGroupSerializer(ProjectInfo.objects.filter(g_id=g_id).first())
                return Response({'code': 'success', 'data': info.data})
            else:
                return Response({'code': 'error', 'msg': '分组ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取分组信息异常'})


class GroupListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            p_id = request.GET.get('p_id', None)
            if p_id:
                info = ProjectJoinGroupSerializer(ProjectInfo.objects.filter(p_id=p_id).all(), many=True)
            else:
                info = ProjectJoinGroupSerializer(ProjectInfo.objects.all(), many=True)
            return Response({'code': 'success', 'data': info.data})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取分组列表异常'})


class GroupListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            info = ProjectJoinGroupNewSerializer(ProjectInfo.objects.all(), many=True)
            return Response({'code': 'success', 'data': info.data})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取分组关联项目列表异常'})
