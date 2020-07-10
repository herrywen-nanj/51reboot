###############################################
#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 > File Name: urls.py
 > Author: lixuebin
 > Mail: li.xuebin@hotmail.com 
 > Created Time: 2019年08月04日 星期日 07时17分51秒
"""
################################################
from django.urls import path, re_path

from . import views, user, group, power
#from views import UserView, UserDetailView, RoleView

app_name = "users"
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('login/', views.LoginViews.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(), name = 'logout'),
    path('group/', group.RoleView.as_view(), name = "role_list"),
    path('groupUser/', group.RoleView.as_view(), name = "role_user"),
    re_path('groupdetail/(?P<pk>[0-9]+)?/$', group.RoleDetailView.as_view(), name = "role_detail"),
    path('user/', user.UserView.as_view(), name = "user_list"),
    re_path('userdetail/(?P<pk>[0-9]+)?/$', user.UserDetailView.as_view(), name= 'user_detail')

]
