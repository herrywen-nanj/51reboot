from django.urls import path, re_path

from . import views

app_name = 'hello'

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('login/', views.login, name='login'),
    re_path('hello/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index')
]