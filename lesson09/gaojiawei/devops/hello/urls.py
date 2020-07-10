from django.urls import path, re_path

from . import views

app_name = 'hello'
urlpatterns = [
    # get不带参数 get通过？加参数   post请求的url格式如下
    path('hello/', views.index, name='index'),
    path('login/', views.login, name='login'),

    # 关键字传参数  (?<参数名>参数类型)??视图中直接通过参数名获取值（最常用）
    re_path('hello/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index')
]