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
from users.forms import RoleProfileForm, UserUpdateForm
from django.contrib.auth.models import Group, Permission


class RoleView(LoginRequiredMixin, PaginationMixin, ListView):

    model = Group
    template_name = 'user/group_list.html'
    context_object_name = 'grouplist'
    keyword = ''
    login_url = 'login.html'
    redirect_field_name = 'redirect_to'
    permission_required = ('users.view_group', 'users.delete_group', 'users.add_group', 'users.change_group')


    def get_queryset(self):
        queryset = super(RoleView, self).get_queryset()
        self.keyword = self.request.GET.get("keyword", "").strip()
        if self.keyword:
            queryset &= queryset.filter(Q(name=self.keyword))
        return queryset
    def get_context_data(self,  **kwargs):
        context = super(RoleView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context

    def post(self,request):
        roleForm = RoleProfileForm(request.POST)
        if roleForm.is_valid():
            try:
                data = roleForm.cleaned_data
                print(data)
                self.model.objects.create(**data)
                res = {'code':0,'result':'添加成功'}
            except:
                res = {'code':1,'result':'添加失败'}
        else:
            print(roleForm.errors)
            print(roleForm.errors.as_json())
            print(roleForm.errors['name'][0])
            res = {'code':1,'errmsg':roleForm.errors.as_json()}



class RoleDetailView(LoginRequiredMixin, DetailView):
    '''
    组详情
    '''
    model = Group
    template_name = 'user/group_edit.html'
    context_object_name = 'role_detail'
