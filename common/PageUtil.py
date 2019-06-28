#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created by lwl at 2019/6/26
from rest_framework.pagination import PageNumberPagination


class NewPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'size'
    max_page_size = 30
    page_query_param = 'page'