"""
@user:Do丶
@time:2019/2/20 11:23
"""
from django.urls import path
from . import views

urlpatterns = [
    path('publish/', views.publish,name="发布页面"),
]
