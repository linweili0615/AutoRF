from rest_framework.response import Response
from .models import EnvInfo
from .serializers import EnvInfoSerializer, EnvListSerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt import authentication


class AddEnvView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['e_name'] and res_data['e_value']:
                e_info = EnvInfo(e_name=res_data['e_name'], e_value=res_data['e_value'], create_user=request.user)
                e_info.save()
                return Response({'code': 'success', 'msg': '已添加', 'e_id': e_info.e_id})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查！'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '添加异常'})


class DelEnvView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['e_id']:
                count = EnvInfo.objects.filter(e_id=res_data['e_id']).delete()
                if count.index(0) > 0:
                    return Response({'code': 'success', 'msg': '记录已删除'})
                else:
                    return Response({'code': 'error', 'msg': '记录不存在'})
            else:
                return Response({'code': 'erorr', 'msg': '参数不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'erorr', 'msg': '删除记录异常'})


class EditEnvView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['e_id'] and res_data['e_name']:
                EnvInfo.objects.filter(e_id=res_data['e_id']).update(e_name=res_data['e_name'])
                return Response({'code': 'success', 'msg': '已更新'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '更新异常'})


class EnvView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            res_data = request.data
            if res_data['e_id']:
                e_info = EnvInfo.objects.filter(e_id=res_data['e_id']).all()
                data = EnvInfoSerializer(instance=e_info, many=True).data
                return Response({'code': 'success', 'data': data})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取环境信息异常'})


class EnvListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            # p_id = request.data.get('p_id')
            # if p_id:
            #     data = EnvListSerializer(instance=EnvInfo.objects.filter(p_id=p_id).all(), many=True).data
            # else:
            data = EnvListSerializer(instance=EnvInfo.objects.all(), many=True).data
            return Response({'code': 'success', 'data': data})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取环境列表异常'})
