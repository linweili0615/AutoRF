#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from django.urls import path
from .views import ApiListView, DelApiView, ApiView, AddApiView, TestApiView, EditApiView

urlpatterns = [
    path('add', AddApiView.as_view()),
    path('test', TestApiView.as_view()),
    path('del', DelApiView.as_view()),
    path('edit', EditApiView.as_view()),
    path('info', ApiView.as_view()),
    path('all', ApiListView.as_view()),
]