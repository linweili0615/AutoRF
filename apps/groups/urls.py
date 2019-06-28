#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from django.urls import path
from .views import GroupListView, AddGroupView, EditGoupView, DelGoupView, GroupView, GroupListApiView


urlpatterns = [
    path('add', AddGroupView.as_view()),
    path('del', DelGoupView.as_view()),
    path('edit', EditGoupView.as_view()),
    path('get', GroupView.as_view()),
    path('api', GroupListApiView.as_view()),
    path('all', GroupListView.as_view()),
]