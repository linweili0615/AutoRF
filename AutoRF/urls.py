"""AutoRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from users.views import UserView

urlpatterns = [
    re_path('login', obtain_jwt_token),
    re_path('getinfo', UserView.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('group/', include('groups.urls')),
    path('project/', include('projects.urls')),
    path('envs/', include('envs.urls')),
    path('api/', include('apis.urls')),
    path('task/', include('tasks.urls')),
    path('func/', include('funcs.urls')),
]
