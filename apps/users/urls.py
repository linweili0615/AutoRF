#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/6
from rest_framework import routers
from django.urls import path, include
from . import views as user_views


router = routers.DefaultRouter()
router.register(r'do_users', user_views.UserViewSet)
router.register(r'do_groups', user_views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
]