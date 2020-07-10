from django.shortcuts import render, HttpResponseRedirect, reverse, render_to_response
from django.http import HttpResponseServerError, response
from django.views.generic import View
from apps.users.models import UserProfile
from django.contrib.auth import authenticate, login, logout
# 权限认证
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.template import RequestContext
from django.http import JsonResponse
import traceback


# Create your views here.


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username_info = ''
        password_info = ''
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username is '':
            username_info = '用户名不能为空'
        if password is '':
            password_info = '密码不能为空'
        if username is '' or password is '':
            return render(request, 'login.html', {'username_info': username_info,
                                                  'password_info': password_info})
        # authenticate
        tag = authenticate(username=username, password=password)

        if tag:
            login(request, tag)
            return HttpResponseRedirect(reverse('index'))
        msg = '用户名密码错误'
        return render(request, 'login.html', {'msg': msg})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("login"))


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'index.html')


class page_not_found(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    # 异常信息捕获
    # tb = traceback.format_exc()
    # print(tb)
    def get(request, *args, **kwargs):
        return render(request, '404.html', {'request': request.request}, status=404)
