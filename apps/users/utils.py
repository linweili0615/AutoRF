#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/12
import re

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


def jwt_response_payload_handler(token, user=None, request=None):
    """为返回的结果添加用户相关信息"""

    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


def get_user_by_account(account):
    """
    添加通过手机号查询用户的方法
    """
    try:
        if re.match(r'^1[356789]\d{9}$', account):  # account 是手机号
            user = User.objects.get(mobile=account)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


class UsernameMobileAuthBackend(ModelBackend):
    """添加支持手机号登录"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)  # username 可能是用户名也可能是手机号
        return user