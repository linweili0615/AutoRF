
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_jwt import authentication
from rest_framework_jwt.utils import jwt_decode_handler


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (authentication.JSONWebTokenAuthentication,)

    def post(self, request,):

        toke_user = jwt_decode_handler(request.auth)
        username = toke_user["username"]
        return Response({'code': 'success', 'username': username})
