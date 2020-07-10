from django.urls import path, re_path

from . import views

app_name = 'adminlte'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
]
