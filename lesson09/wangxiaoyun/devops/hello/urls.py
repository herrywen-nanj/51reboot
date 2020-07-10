from django.urls import path, re_path

from . import views

app_name = 'hello'
urlpatterns = [
    # get 不带参数, get 通过? 加参数， post请求的格式如下
    path('hello/', views.index2, name='index2'),
    path('hello2/', views.index3, name='index3'),

    # 关键字传参, (?<参数名>参数类型) -- 试图中通过参数名获取值(最常用)
    re_path ('^hello/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/',views.index2,name='index2'),
]
