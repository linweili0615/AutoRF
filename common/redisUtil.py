#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/28
import redis


def getRedis():
    return redis.Redis(host='localhost', port=6379, password='linweili123', db=0)

