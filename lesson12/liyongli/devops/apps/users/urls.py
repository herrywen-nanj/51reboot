# -*- coding:utf-8 -*-
# author: lyl
from django.conf.urls import url, re_path
from apps.users.views import UserMangerView, UserUpdateView, RoleListView, GroupListView, RebootView, UserDetailView

urlpatterns = [
    url(r'^user_list/$', UserMangerView.as_view(), name='user_list'),
    url(r'^update_center/$', UserUpdateView.as_view(), name='update_center'),
    url(r'^role_list/$', RoleListView.as_view(), name='role_list'),
    url(r'^group_list/$', GroupListView.as_view(), name='group_list'),
    url(r'^51list/$', RebootView.as_view(), name='51list'),
    re_path('userdetail/(?P<pk>[0-9]+)?/$', UserDetailView.as_view(), name='user_detail'),
]
