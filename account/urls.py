"""
@user:Do丶
@time:2019/2/19 15:02
"""
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup,name='注册页面'),
    path('login/', views.login, name='登录页面'),
    path('logout/', views.logout, name='退出页面'),
]
