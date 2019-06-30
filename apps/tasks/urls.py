#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from django.urls import path
from .views import TaskListView, DelTaskView, DealTaskView, GetTaskView, \
    TaskExtendInfoListView, TaskExtendStatusView, DelTaskExtendView, AddTaskExtendView, \
    EditTaskView, ChangeTaskExtendInfoRankView, TaskTestView, TaskResultListView, \
    AddTaskView, DelTaskResultView, TaskResultView

urlpatterns = [
    # path('add', AddApiView.as_view()),
    path('status', DealTaskView.as_view()),
    path('del', DelTaskView.as_view()),
    path('add', AddTaskView.as_view()),
    path('edit', EditTaskView.as_view()),
    path('info', GetTaskView.as_view()),
    path('extend/list', TaskExtendInfoListView.as_view()),
    path('extend/status', TaskExtendStatusView.as_view()),
    path('extend/del', DelTaskExtendView.as_view()),
    path('extend/add', AddTaskExtendView.as_view()),
    path('extend/change', ChangeTaskExtendInfoRankView.as_view()),
    path('list', TaskListView.as_view()),
    path('test', TaskTestView.as_view()),
    path('result/list', TaskResultListView.as_view()),
    path('result/del', DelTaskResultView.as_view()),
    path('result/get', TaskResultView.as_view()),
]