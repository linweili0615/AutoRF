#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/18
from rest_framework import serializers
from .models import ApiInfo
from envs.models import EnvInfo
from envs.serializers import EnvInfoNameSerializer


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiInfo
        fields = '__all__'


class ApiEnvSerializer(serializers.ModelSerializer):
    a_id = serializers.IntegerField()
    e_id = serializers.IntegerField()
    e_name = serializers.SerializerMethodField()
    p_id = serializers.IntegerField()
    g_id = serializers.IntegerField()
    a_name = serializers.CharField()
    paths = serializers.CharField()
    methods = serializers.CharField()
    headers = serializers.CharField()
    cookies = serializers.CharField()
    param_type = serializers.CharField()
    params = serializers.CharField()
    asserts = serializers.CharField()
    # create_user = serializers.CharField()
    # update_user = serializers.CharField()
    create_time = serializers.DateTimeField()
    update_time = serializers.DateTimeField()

    class Meta:
        model = ApiInfo
        fields = ('a_id', 'e_id', 'e_name', 'p_id', 'g_id',
                  'a_name', 'paths', 'methods', 'headers',
                  'cookies', 'param_type', 'params', 'asserts', 'create_time', 'update_time')

    def get_e_name(self, obj):
        return EnvInfoNameSerializer(
            EnvInfo.objects.filter(e_id=obj.e_id).first()
        ).data['e_name']