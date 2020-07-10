from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, ListView, DetailView,TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpRequest, HttpResponse, JsonResponse, QueryDict, Http404

from django.conf import settings
from users.models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from pure_pagination.mixins import PaginationMixin
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from users.forms import UserProfileForm, UserUpdateForm
from django.contrib.auth.models import Group, Permission

class UserView(LoginRequiredMixin, PaginationMixin, ListView):
    """
    组功能
    """
    model = UserProfile
    template_name = 'user/user_list.html'
    context_object_name = 'userlist'
    paginate_by = 2
    keyword = ''
    login_url = '/login'

    def get_queryset(self):
        queryset = super(UserView, self).get_queryset()
        self.keyword = self.request.GET.get("keyword", "").strip()
        if self.keyword:
            queryset = queryset.filter(Q(name_cn__icontains=self.keyword)|
                                       Q(username__icontains=self.keyword))
        return queryset

    def get_context_data(self,  **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context
    def post(self, request):
        _userForm = UserProfileForm(request.POST)
        if _userForm.is_valid():
            try:
                _userForm.cleaned_data['password'] = make_password("12345678")
                _userForm.cleaned_data['is_active'] = True
                data = _userForm.cleaned_data
                self.model.objects.create(**data)
                res = {'code': 0, 'result': '添加用户成功'}
            except:
                res = {'code': 1, 'errmsg': '添加用户失败'}
        else:
            # 获取自定义的表单错误的两种常用方式
            # print(_userForm.errors)
            print(_userForm.errors.as_json())
            # print(_userForm.errors['phone'][0])  # 手机号码非法
            # print(_userForm.errors['username'][0])  # 已存在一位使用该名字的用户
            res = {'code': 1, 'errmsg': _userForm.errors.as_json()}

        return JsonResponse(res, safe=True)
    def delete(self, request):
        data = QueryDict(request.body).dict()
        print(data)
        pk = data.get('id')
        try:
            if pk == 1:
                res = {'code': 1, 'result': '不能删除管理员'}
            else:
                user = self.model.objects.filter(pk=pk)
                user.delete()
                res = {'code':0,'result':'删除用户成功'}
        except:
                res = {'code':1, 'result':'删除用户失败'}
        return JsonResponse(res,safe=True)




class UserDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'user/user_edit.html'
    context_object_name = 'user'

    def post(self, request, **kwargs):
        print(
            request.POST)  # <QueryDict: {'id': ['7'], 'username': ['aa'], 'name_cn': ['bb'], 'phone': ['13305779168']}>
        print(kwargs)  # {'pk': '7'}
        print(request.body)  # b'id=7&username=aa&name_cn=bb&phone=13305779168'
        pk = kwargs.get("pk")
        data = QueryDict(request.body).dict()
        print(data)  # {'id': '7', 'username': 'aa', 'name_cn': 'bb', 'phone': '13305779168'}
        _userForm = UserUpdateForm(request.POST)
        if _userForm.is_valid():
            try:
                self.model.objects.filter(pk=pk).update(**data)
                res = {'code': 0, "next_url": reverse("users:user_list"), 'result': '更新用户成功'}
            except:
                res = {'code': 1, "next_url": reverse("users:user_list"), 'errmsg': '更新用户失败'}

        else:
            # 获取所有的表单错误
            print(_userForm.errors)
            res = {'code': 1, "next_url": reverse("users:user_list"), 'errmsg': _userForm.errors}
        return render(request, settings.JUMP_PAGE, res)


