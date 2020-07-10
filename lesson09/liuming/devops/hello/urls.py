from django.urls import path, re_path
from . import views

app_name = "hello"

urlpatterns = [
    # path('hello/(?<year>[0-9]{4})/(?<month>[0-9]{2})/)', views.hello, name="hello"),
    re_path('login/$', views.Login.as_view(), name="login"),
    re_path('logout/$', views.Logout.as_view(), name="logout"),
    # path('', views.Home.as_view(), name="home"),
    re_path('home/$', views.Home.as_view(), name="home"),
]
