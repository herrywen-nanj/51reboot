"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from api.views import helloView, SumView, CommandView, LoginShowView, LoginView, LoginAuthView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/hello/', helloView),

    # api/sum/?args1=1&args2=2
    url(r'^api/sum/', SumView),

    # api/command/?cmd=<df>
    url(r'^api/command/', CommandView),

    # login
    url(r'^api/login_auth/', LoginAuthView),

    url(r'^api/login/', LoginShowView), # 页面
    url(r'^api/auth/', LoginView),      # 登录认证

]
