from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, DetailView,TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpRequest, HttpResponse, JsonResponse, QueryDict, Http404

from reboot import settings
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .forms import UserProfileForm, UserUpdateForm
from django.contrib.auth.models import Group, Permission




class IndexView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:login"))
        return render(request, 'index.html')

class LoginViews(View):
    def get(self, request):
        return render(request, "login.html")
#
    def post(self, request):
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
                # return HttpResponseRedirect(reverse("users：index"))   # 命名空间的写法
            else:
                return render(request, "login.html", {"msg": "用户未激活！"})
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误！"})

class LogoutView(View):
    """
    登出功能
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("users:login"))











