#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/10
from django.urls import path
from .views import AddProjectView, DelProjectView, EditProjectStatusView, \
    EditProjectView, ProjectView, ProjectListView

urlpatterns = [
    path('add', AddProjectView.as_view()),
    path('del', DelProjectView.as_view()),
    path('edit', EditProjectView.as_view()),
    path('status', EditProjectStatusView.as_view()),
    path('get', ProjectView.as_view()),
    path('get/all', ProjectListView.as_view()),
]
