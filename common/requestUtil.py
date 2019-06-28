#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/11
from json import JSONDecodeError

import requests
from envs.models import EnvInfo
from envs.serializers import EnvInfoSerializer


def do_case():
    do_api(**{'k1': 'v2'})


def do_api(**kwargs):
    # cookie处理
    # jar = requests.cookies.RequestsCookieJar()
    # jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    paths = kwargs['paths']
    headers = kwargs['headers']
    if headers:
        headers = eval(headers)
    # cookies = kwargs['cookies']
    params = kwargs['params']
    param_type = kwargs['param_type']
    if param_type == 'FORM':
        if params:
            params = eval(params)
    env = EnvInfoSerializer(EnvInfo.objects.get(e_id=kwargs['e_id'])).data['e_value']

    if kwargs['methods'].upper() == 'GET':
        return get(env, paths, params, headers)
        pass
    elif kwargs['methods'].upper() == 'POST':
        return post(env, paths, params, headers)


def get(env, paths, params, headers=None):
    url = env + paths
    try:
        response = requests.get(url=url, params=params, headers=headers, timeout=4)
        return get_normal_result(response)
    except JSONDecodeError:
        return get_error_result(response)
    except Exception as e:
        print(e)
        return get_error_result(response)


def get_normal_result(response):
    return {
        'req': {
            'method': response.request.method,
            'url': response.request.url,
            'body': response.request.body,
            'headers': response.request.headers,
            'cookies': response.request._cookies,
        },
        'res': {
            'status_code': response.status_code,
            'body': response.json(),
            'headers': response.headers,
            'cookies': response.cookies,
        }
    }


def get_error_result(response):
    return {
        'req': {
            'method': response.request.method,
            'url': response.request.url,
            'body': response.request.body,
            'headers': response.request.headers,
            'cookies': response.request._cookies,
        },
        'res': {
            'status_code': response.status_code,
            'body': response.content,
            'headers': response.headers,
            'cookies': response.cookies,
        }
    }


def post(env, paths, params, headers=None):
    try:
        url = env + paths
        import json
        response = requests.post(url=url, data=params, headers=headers, timeout=4)
        return get_normal_result(response)
    except JSONDecodeError:
        return get_error_result(response)
    except Exception as e:
        print(e)
        return get_error_result(response)

    # #请求历史
    # # response.history