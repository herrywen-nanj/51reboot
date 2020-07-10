from django.shortcuts import render
from apps.users.models import UserProfile
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission, Group
from django.http import JsonResponse, QueryDict
# 分页
from pure_pagination import Paginator, PageNotAnInteger


# Create your views here.
class UserMangerView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        username = request.GET.get('keyword', '')
        # test = UserProfile.objects.filter(username='liyongli',)
        # filter 结果 < QuerySet[ < UserProfile: liyongli >] >
        # print(test)
        all_user_info = []
        user_group = []
        if username:
            # 搜索用户
            user_info = UserProfile.objects.all().values('username', 'name_cn', 'groups__name', 'phone', 'is_active'). \
                filter(username=username).first()
        else:
            all_user = UserProfile.objects.all().values('username')
            for user in all_user:
                # 获取全部用户信息
                user_info = UserProfile.objects.all().values('username', 'name_cn', 'groups__name', 'phone',
                                                             'is_active').filter(username=user['username'])
                # 如果长度不为1证明用户属于多个组
                if len(user_info) != 1:
                    for users in user_info:
                        # 获取用户所在的全部组
                        user_group.append(users['groups__name'])
                    # 将多用户组数据写入用户信息
                    user_info[0]['groups__name'] = user_group
                # 将用户数据加入列表
                all_user_info.append(user_info[0])
        return render(request, 'user/userlist.html', {'user_info': all_user_info})


class UserUpdateView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        user_info = UserProfile.objects.all().values('username', 'name_cn', 'phone').filter(
            username=request.user).first()
        # print(user_info)
        return render(request, 'user/center.html', {'user_info': user_info})

    def put(self, request):
        data = {
            'status': 'fail',
            'msg': '非法请求'
        }
        user = self.request.user
        put = QueryDict(request.body)
        username = put.get('username', '')
        name_cn = put.get('name_cn', '')
        phone = put.get('phone', '')

        # 判断请求是否构造非法请求
        if str(user) == username:
            try:
                UserProfile.objects.filter(username=user).update(name_cn=name_cn, phone=phone)
                data = {
                    'status': 'success',
                    'msg': '更新成功'
                }
            except Exception as e:
                data = {
                    'status': 'fail',
                    'msg': e
                }
        return JsonResponse(data)


class RoleListView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 判断传入是否为正数
        try:
            page = int(page)
        except:
            page = 1

        # 数据库查询
        role_list = Permission.objects.all().values('codename', 'name', 'content_type__model')
        # 统计总条数
        all_num = role_list.count()

        # 输入的数超过最大数量
        if page * 5 > all_num:
            if all_num % 5 == 0:
                page = all_num // 5
            else:
                page = all_num // 5 + 1

        # 设置起始页与最终页
        start_page = (page - 1) * 5 + 1
        end_page = page * 5
        # 配置分页信息
        p = Paginator(role_list, per_page=5, request=request)
        orgs = p.page(page)

        return render(request, 'user/rolelist.html', {'role_list': role_list,
                                                      'all_roles': orgs,
                                                      'all_num': all_num,
                                                      'start_page': start_page,
                                                      'end_page': end_page
                                                      })
    def put(self):
        pass

    def delete(self):
        pass


class GroupListView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        group_info = []
        try:
            all_group = Group.objects.all()
            ls = all_group
            for group in all_group:
                np = ls.values('user__username', 'permissions__name').filter(name=group)
                if len(np) >= 1:
                    user_list = []
                    permissions_list = []
                    for user_info in np:
                        if user_info['user__username'] not in user_list:
                            user_list.append(user_info['user__username'])
                        if user_info['permissions__name'] not in permissions_list:
                            permissions_list.append(user_info['permissions__name'])
                    info = {
                        'group': group,
                        'username': user_list,
                        'permissions': permissions_list
                    }
                else:
                    info = {'group': group,
                            'username': np['user__username'],
                            'permissions': np['permissions__name']
                            }
                group_info.append(info)
        except:
            pass
        return render(request, 'user/grouplist.html', {'group_info': group_info})

    def put(self):
        pass

    def delete(self):
        pass
