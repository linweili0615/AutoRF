#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from .models import GroupInfo
from projects.models import ProjectInfo
from rest_framework import serializers


class GroupInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInfo
        fields = ('g_id', 'p_id', 'g_name', 'create_user', 'create_time')


class GroupInfoSimSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='g_id')
    label = serializers.CharField(source='g_name')

    class Meta:
        model = GroupInfo
        fields = ('id', 'label')


class ProjectJoinGroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='p_id')
    label = serializers.CharField(source='p_name')
    children = serializers.SerializerMethodField()

    class Meta:
        model = ProjectInfo
        fields = ('id', 'label', 'children')

    def get_children(self, obj):
        return GroupInfoSimSerializer(
            GroupInfo.objects.filter(p_id=obj.p_id).order_by('-g_id'), many=True
        ).data


class GroupInfoNewSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='g_id')
    label = serializers.CharField(source='g_name')

    class Meta:
        model = GroupInfo
        fields = ('value', 'label')


class ProjectJoinGroupNewSerializer(serializers.ModelSerializer):
    value = serializers.IntegerField(source='p_id')
    label = serializers.CharField(source='p_name')
    children = serializers.SerializerMethodField()

    class Meta:
        model = ProjectInfo
        fields = ('value', 'label', 'children')

    def get_children(self, obj):
        return GroupInfoNewSerializer(
            GroupInfo.objects.filter(p_id=obj.p_id).order_by('-g_id'), many=True
        ).data





