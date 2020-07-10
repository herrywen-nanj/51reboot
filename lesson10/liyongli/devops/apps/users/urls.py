# -*- coding:utf-8 -*-
# author: lyl
from django.conf.urls import url
from apps.users.views import UserMangerView, UserUpdateView, RoleListView, GroupListView

urlpatterns = [
    url(r'^user_list/$', UserMangerView.as_view(), name='user_list'),
    url(r'^update_center/$', UserUpdateView.as_view(), name='update_center'),
    url(r'^role_list/$', RoleListView.as_view(), name='role_list'),
url(r'^group_list/$', GroupListView.as_view(), name='group_list'),
]
