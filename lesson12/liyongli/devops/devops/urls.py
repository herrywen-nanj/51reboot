"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url, include
from apps.base.views import LoginView, IndexView, LogoutView, page_not_found

from django.views import static ##新增
from django.conf import settings ##新增
from devops.settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    url('^user/', include(('apps.users.urls', 'users'), namespace='user')),
    path("workorder/", include(('apps.work_order.urls', 'work_order'), namespace='work_order')),
    re_path("media/(?P<path>.*)",  serve, {"document_root": MEDIA_ROOT}),
    # url('^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
]

handler404 = page_not_found.as_view()
