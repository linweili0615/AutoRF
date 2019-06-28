from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from common.requestUtil import do_api
from .models import ApiInfo
from .serializers import ApiEnvSerializer
from common.PageUtil import NewPageNumberPagination
from rest_framework import permissions
from rest_framework_jwt import authentication


class EditApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            a_id = request.data['a_id']
            e_id = request.data['e_id']
            p_id = request.data['p_id']
            g_id = request.data['g_id']
            a_name = request.data['a_name']
            methods = request.data['methods']
            paths = request.data['paths']
            headers = request.data['headers']
            params = request.data['params']
            param_type = request.data['param_type']
            if a_id and e_id and p_id and g_id and a_name and methods and paths:
                _api = ApiInfo.objects.get(a_id=a_id)
                if _api:
                    _api.e_id = e_id
                    _api.p_id = p_id
                    _api.g_id = g_id
                    _api.a_name = a_name
                    _api.methods = methods
                    _api.paths = paths
                    _api.headers = headers
                    _api.params = params
                    _api.param_type = param_type
                    _api.update_user = request.user.username
                    _api.save()
                    return Response({'code': 'success', 'msg': '已更新'})
                else:
                    return Response({'code': 'error', 'msg': '接口信息不存在'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '更新接口异常'})


class AddApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            e_id = request.data['e_id']
            p_id = request.data['p_id']
            g_id = request.data['g_id']
            a_name = request.data['a_name']
            methods = request.data['methods']
            paths = request.data['paths']
            headers = request.data['headers']
            params = request.data['params']
            param_type = request.data['param_type']
            if e_id and p_id and a_name and methods and paths:
                if not g_id:
                    g_id = None
                _api = ApiInfo(e_id=e_id, p_id=p_id, g_id=g_id, a_name=a_name, methods=methods, paths=paths,
                               headers=headers, params=params, param_type=param_type, create_user=request.user.username, update_user=request.user.username)
                _api.save()
                return Response({'code': 'success', 'msg': '已添加'})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '添加接口异常'})


class TestApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            if request.data['e_id'] and request.data['a_name'] and request.data['methods'] and request.data['paths']:
                result = do_api(**request.data)
                return Response({'code': 'test', 'msg': '请求成功', 'result': result, 'a_name': request.data['a_name']})
            else:
                return Response({'code': 'error', 'msg': '参数错误，请检查!'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '测试接口异常'})


class DelApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            a_id = request.data['a_id']
            if a_id:
                ApiInfo.objects.filter(a_id=a_id).delete()
                return Response({'code': 'success', 'msg': '已删除'})
            else:
                return Response({'code': 'error', 'msg': '接口ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '删除接口异常'})


class ApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request):
        try:
            a_id = request.data['a_id']
            if a_id:
                data = ApiEnvSerializer(ApiInfo.objects.filter(a_id=a_id).first()).data
                return Response({'code': 'success', 'data': data})
            else:
                return Response({'code': 'error', 'msg': '接口ID不能为空'})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取接口信息异常'})


class ApiListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def get(self, request):
        try:
            a_name = request.GET.get('a_name', None)
            g_id = request.GET.get('g_id', None)
            p_id = request.GET.get('p_id', None)
            q1 = Q()
            if a_name:
                q1.add(Q(a_name__contains=a_name), Q.AND)
            if g_id:
                q1.add(Q(g_id=g_id), Q.AND)
            if p_id:
                q1.add(Q(p_id=p_id), Q.AND)
            if q1:
                apilist = ApiInfo.objects.filter(q1).order_by('-a_id')
            else:
                apilist = ApiInfo.objects.order_by('-a_id')
            pg = NewPageNumberPagination()
            api = pg.paginate_queryset(queryset=apilist, request=request)
            data = ApiEnvSerializer(instance=api, many=True).data
            return Response({'code': 'success', 'total': apilist.count(), 'list': data})
        except Exception as e:
            print(e)
            return Response({'code': 'error', 'msg': '获取api列表异常'})
