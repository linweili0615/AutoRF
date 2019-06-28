#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/18
from rest_framework import serializers
from .models import TaskInfo, TaskExtendInfo, TaskResult
from envs.serializers import EnvInfoValueSerializer
from envs.models import EnvInfo
from envs.serializers import EnvInfoNameSerializer


class TaskInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskInfo
        fields = '__all__'


class TaskExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskExtendInfo
        fields = '__all__'


class TaskResultSerializer(serializers.ModelSerializer):
    # batch_id = serializers.CharField()
    # execute_user = serializers.CharField()
    class Meta:
        model = TaskResult
        # fields = '__all__'
        fields = ('batch_id', 'execute_user')


class TaskListSerializer(serializers.ModelSerializer):
    t_id = serializers.IntegerField()
    t_name = serializers.CharField()
    e_value = serializers.SerializerMethodField()
    cron = serializers.CharField()
    start_time = serializers.CharField()
    end_time = serializers.CharField()
    status = serializers.CharField()
    update_user = serializers.CharField()
    update_time = serializers.DateTimeField()

    class Meta:
        model = TaskInfo
        fields = ('t_id', 't_name', 'e_value', 'cron', 'start_time', 'end_time', 'status', 'update_user', 'update_time')

    def get_e_value(self, obj):
        return EnvInfoValueSerializer(
            EnvInfo.objects.filter(e_id=obj.e_id).first()
        ).data['e_value']


class TaskExtendInfoSerializer(serializers.ModelSerializer):
    te_id = serializers.IntegerField()
    t_id = serializers.IntegerField()
    e_id = serializers.IntegerField()
    e_name = serializers.SerializerMethodField()
    te_name = serializers.CharField()
    paths = serializers.CharField()
    methods = serializers.CharField()
    status = serializers.CharField()
    rank = serializers.IntegerField()
    headers = serializers.CharField()
    cookies = serializers.CharField()
    param_type = serializers.CharField()
    params = serializers.CharField()
    asserts = serializers.CharField()
    extracts = serializers.CharField()

    # create_user = serializers.CharField()
    # update_user = serializers.CharField()
    # create_time = serializers.DateTimeField()
    # update_time = serializers.DateTimeField()

    class Meta:
        model = TaskExtendInfo
        fields = ('te_id', 't_id', 'e_id', 'e_name', 'te_name', 'paths',
                  'methods', 'status', 'rank', 'headers', 'cookies',
                  'param_type', 'params', 'asserts',  'extracts')

    def get_e_name(self, obj):
        return EnvInfoNameSerializer(
            EnvInfo.objects.filter(e_id=obj.e_id).first()
        ).data['e_name']
