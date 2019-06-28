#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from .models import EnvInfo
from rest_framework import serializers


class EnvInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvInfo
        fields = ('e_id', 'p_id', 'e_name', 'e_value', 'create_user', 'create_time')


class EnvInfoValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvInfo
        fields = ('e_value',)


class EnvInfoNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvInfo
        fields = ('e_name',)


class EnvListSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='e_id')
    label = serializers.CharField(source='e_name')
    e_value = serializers.CharField()
    is_default = serializers.IntegerField()

    class Meta:
        model = EnvInfo
        fields = ('value', 'label', 'e_value', 'is_default')
