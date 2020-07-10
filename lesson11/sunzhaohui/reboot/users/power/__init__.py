# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-08-05 17:21'

from django.shortcuts import render

from django.http import HttpResponse,QueryDict,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.conf import settings
from users.models import UserProfile
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



from django.contrib.auth.hashers import make_password

from django.views.generic import View,ListView,DetailView
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# 用户认证及权限管理模块导入
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from pure_pagination.mixins import PaginationMixin

from django.db.models import Q
from  users.forms import PowerForm


# class PowerListView(LoginRequiredMixin,View):
#     login_url = '/login/'  # 用户没有通过或者权限不够时跳转的地址，默认是 settings.LOGIN_URL.
#     # 把没通过检查的用户重定向到没有 "next page" 的非登录页面时，把它设置为 None ，这样它会在 URL 中移除。
#     redirect_field_name = 'redirect_to'
#     #@method_decorator(login_required(login_url='/login/'))
#     def get(self,request):
#         #permissionlist = []
#         Permissionlist = Permission.objects.values()
#         Permissionlist=list(Permissionlist)
#         for i in Permissionlist:
#             i['content_type'] = ContentType.objects.get(id=i['content_type_id'])
#
#         paginator = Paginator(Permissionlist,10)
#         page = request.GET.get('page')
#         try:
#             permissionlist = paginator.page(page)
#             # todo: 注意捕获异常
#         except PageNotAnInteger:
#             # 如果请求的页数不是整数, 返回第一页。
#             permissionlist = paginator.page(1)
#         except InvalidPage:
#             # 如果请求的页数不存在, 重定向页面
#             return HttpResponse('找不到页面的内容')
#         except EmptyPage:
#             # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
#             permissionlist = paginator.page(paginator.num_pages)
#         #permissionlist = list(permissionlist)
#
#         #print(len(permissionlist))
#         print(paginator.num_pages)
#         print(permissionlist)
#         print('----')
#         print(len(permissionlist))
#         page_number_list= [{'page':i} for i in range(1,paginator.num_pages+1)]
#         return render(request, 'users/powerlist.html', {'permissionlist': permissionlist,'page_number_list':page_number_list})

class PowerListView(LoginRequiredMixin,PermissionRequiredMixin,PaginationMixin,ListView):

    login_url = '/login/'  # 用户没有通过或者权限不够时跳转的地址，默认是 settings.LOGIN_URL.
    # 把没通过检查的用户重定向到没有 "next page" 的非登录页面时，把它设置为 None ，这样它会在 URL 中移除。
    redirect_field_name = 'redirect_to'

    permission_required = ('users.add_permission','users.change_permission','users.delete_permission','users.view_permission')

    model = Permission
    template_name = "users/power_list.html"
    context_object_name = "powerlist"

    paginate_by = 10
    keyword = ''


    #搜索
    def get_queryset(self):
        queryset = super(PowerListView, self).get_queryset()
        self.keyword = self.request.GET.get('keyword','').strip()
        print(self.keyword)
        if self.keyword:
            queryset = queryset.filter(Q(codename__icontains=self.keyword)| Q(name__icontains=self.keyword))
        return queryset
    #显示搜索关键字
    def get_context_data(self, **kwargs):
        context = super(PowerListView,self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        context['user'] = self.request.user.username
        ContentType_object_list = ContentType.objects.all()

        context['ContentType_object_list'] = ContentType_object_list
        #print(context)
        return context


    """
        创建权限
    """

    def post(self, request):
        data = QueryDict(self.request.body).dict()
        print(data)
        try:
                # _userForm.cleaned_data['password'] = make_password("12345678")
                # _userForm.cleaned_data['is_active'] = True
                #data = _userForm.cleaned_data

            self.model.objects.create(**data)
            res = {'code': 0, 'result': '添加权限成功'}
        except Exception as e:
                #logger.error("create user  error: %s" % traceback.format_exc())
            print(e)

            res = {'code': 1, 'errmsg': '添加权限失败'}
        #else:
            # 获取自定义的表单错误的两种常用方式
            #print(_userForm.errors)
            # <ul class="errorlist">
            #   <li>phone<ul class="errorlist"><li>手机号码非法</li></ul></li>
            #   <li>username<ul class="errorlist"><li>已存在一位使用该名字的用户。</li></ul></li>
            # </ul>
            #print(_userForm.errors.as_json())
            # {"phone": [{"message": "\u624b\u673a\u53f7\u7801\u975e\u6cd5", "code": "invalid"}],
            # "username": [{"message": "\u5df2\u5b4f7f\u7528\u8be5\u540d\u5b57\u7684\u7528\u6237\u3002",
            # "code": "unique"}]}
            # print(_userForm.errors['phone'][0])  # 手机号码非法
            # print(_userForm.errors['username'][0])  # 已存在一位使用该名字的用户
            #res = {'code': 1, 'errmsg': _userForm.errors.as_json()}
        print(JsonResponse(res))
        return JsonResponse(res, safe=True)

    def delete(self,request,**kwargs):
        print(kwargs)
        data = QueryDict(request.body).dict()
        id = data['id']

        try:
            self.model.objects.get(id=id).delete()
            res = {'code': 0, 'result': '删除成功'}
        except:
        # print(id)
            res = {'code': 1, 'errmsg': '删除失败'}

        return JsonResponse(res, safe=True)

class PowerView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url = '/login/'  # 用户没有通过或者权限不够时跳转的地址，默认是 settings.LOGIN_URL.
    # 把没通过检查的用户重定向到没有 "next page" 的非登录页面时，把它设置为 None ，这样它会在 URL 中移除。
    redirect_field_name = 'redirect_to'

    permission_required = (
    'users.add_permission', 'users.change_permission', 'users.delete_permission', 'users.view_permission')
    """
        更新权限
    """
    template_name = 'users/modify_power.html'
    model = Permission
    context_object_name = 'power'

    def get_context_data(self, **kwargs):
        context = super(PowerView,self).get_context_data(**kwargs)
        # context['keyword'] = self.keyword
        # context['user'] = self.request.user.username
        ContentType_object_list = ContentType.objects.all()

        # for ContentType_object in ContentType_object_list:
        #     print(ContentType_object)
        #     print(ContentType_object.id,ContentType_object.app_label,ContentType_object.model)
        context['ContentType_object_list'] = ContentType_object_list
        #print(context)
        return context


    def post(self, request, **kwargs):
        print(request.POST)  # <QueryDict: {'id': ['7'], 'username': ['aa'], 'name_cn': ['bb'], 'phone': ['13305779168']}>
        print(kwargs)  # {'pk': '7'}
        print(request.body)  # b'id=7&username=aa&name_cn=bb&phone=13305779168'
        pk = kwargs.get("pk")
        data = QueryDict(request.body).dict()
        print(data)  # {'id': '7', 'username': 'aa', 'name_cn': 'bb', 'phone': '13305779168'}
        #_userForm = UserUpdateForm(request.POST)
        #if _userForm.is_valid():
        try:
            self.model.objects.filter(pk=pk).update(**data)
            res = {'code': 0, "next_url": reverse("users:power_list"), 'result': '更新权限成功'}
        except Exception as e:
            print(e)
            res = {'code': 1, "next_url": reverse("users:power_list"), 'errmsg': '更新权限失败'}

    # else:
    #     # 获取所有的表单错误
    #     print(_userForm.errors)
    #     res = {'code': 1, "next_url": reverse("users:user_list"), 'errmsg': _userForm.errors}
        return render(request, settings.JUMP_PAGE, res)

    # # 返回所有组、权限，并将当前用户所拥有的组、权限显示
    # def get_context_data(self, **kwargs):
    #     context = super(RolePowerView, self).get_context_data(**kwargs)
    #     context['role_has_users'], context['role_has_permissions'] = self._get_role_power()
    #     context['role_not_users'], context['role_not_permissions'] = self._get_role_not_power()
    #     return context
    #
    # # 获取当前角色所有用户，权限以列表形式返回
    # def _get_role_power(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     try:
    #         role = self.model.objects.get(pk=pk)
    #         users = role.user_set.all()
    #         return users, role.permissions.all()
    #     except self.model.DoesNotExist:
    #         raise Http404
    #
    # # 获取当前角色没有的用户，权限，以列表形式返回
    # def _get_role_not_power(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     try:
    #         role = self.model.objects.get(pk=pk)
    #         all_user = UserProfile.objects.all()
    #         users = [user for user in all_user if user not in role.user_set.all()]
    #         all_perms = Permission.objects.all()
    #         perms = [perm for perm in all_perms if perm not in role.permissions.all()]
    #         return users, perms
    #     except:
    #         return JsonResponse([], safe=False)
    #
    # # 修改角色
    # def post(self, request, **kwargs):
    #     # ops.user_set.set([2])
    #     print(request.POST)
    #     print(request.POST.getlist('users', []))
    #     user_id_list = request.POST.getlist('users_selected', [])
    #     permission_id_list = request.POST.getlist('perms_selected', [])
    #     pk = kwargs.get("pk")
    #     try:
    #         role = self.model.objects.get(pk=pk)
    #         # user.groups.set(group_id_list)
    #         print(user_id_list)
    #         role.user_set.set(user_id_list)
    #         role.permissions.set(permission_id_list)
    #         res = {'code': 0, 'next_url': reverse("users:role_list"), 'result': '角色权限更新成功'}
    #     except:
    #         res = {'code': 1, 'next_url': reverse("users:role_list"), 'errmsg': '角色权限更新失败'}
    #         # logger.error("edit  user group pwoer error: %s" % traceback.format_exc())
    #     return render(request, settings.JUMP_PAGE, res)