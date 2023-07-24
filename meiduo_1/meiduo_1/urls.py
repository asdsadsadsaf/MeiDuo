"""
URL configuration for meiduo_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path

# 日志
from django.http import HttpResponse
def log(request):
    # 方便分析问题
#     日志级别：
    #     DEBUG：排查故障时使用的低级别系统信息
    #     INFO：一般的系统信息
    #     WARNING：描述系统发生了一些小问题的信息
    #     ERROR：描述系统发生了大问题的信息
    #     CRITICAL：描述系统发生严重问题的信息
    import logging
    logger=logging.getLogger('django')
    logger.info('info~~~~~')
    logger.warning('waring~~~')

    return HttpResponse('log')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('log/', log),
]



