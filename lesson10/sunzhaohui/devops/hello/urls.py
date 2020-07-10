# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-21 10:38'

from django.urls import path,re_path

from . import views

app_name='hello'
urlpatterns = [
    path('login/',views.login,name='login'),
    path('hello/',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('hello/list', views.list, name='list'),

    re_path('hello/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/',views.index,name='index'),
]