#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from django.urls import path
from .views import EnvListView, AddEnvView, DelEnvView, EditEnvView, EnvView

urlpatterns = [
    path('add', AddEnvView.as_view()),
    path('del', DelEnvView.as_view()),
    path('edit', EditEnvView.as_view()),
    path('get', EnvView.as_view()),
    path('list', EnvListView.as_view())
]