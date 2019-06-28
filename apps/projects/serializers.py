#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/10
from rest_framework import serializers
from .models import ProjectInfo


class ProjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInfo
        fields = ('p_id', 'p_name', 'p_type', 'p_status',  'create_user', 'update_time')