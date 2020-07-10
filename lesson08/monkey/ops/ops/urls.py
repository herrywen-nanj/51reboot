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
from assets.views import CollectHostInfo, AssetsView, CmdbView, CmdbDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/hello/', helloView, name="hello"),

    # api/sum/?args1=1&args2=2
    url(r'^api/sum/', SumView),

    # api/command/?cmd=<df>
    url(r'^api/command/', CommandView),

    # login
    url(r'^api/login_auth/', LoginAuthView),

    url(r'^api/login/', LoginShowView), # 页面
    url(r'^api/auth/', LoginView),      # 登录认证

    url(r'^api/v1/cmdb$', CmdbView.as_view(), name='cmdb_list'),
    url(r'^api/v1/cmdb/delete/(?P<pk>[0-9]+)/$', CmdbDeleteView),
    url(r'^api/v1/cmdb/collect', CollectHostInfo.as_view()),

    # url(r'^assets/2019/', AssetsView),
    # url(r'^assets/([0-9]{4})/', AssetsView),
    # url(r'^assets/([0-9]{4})/([0-9]{2})/([0-9]+)/', AssetsView),
    url(r'^assets/(?P<year>[0-9]{4})/$', AssetsView, name='book_year')

]
