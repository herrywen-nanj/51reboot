from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, QueryDict
from django.urls import reverse
from django.views.generic import View, ListView, DetailView
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from pure_pagination.mixins import PaginationMixin
from apps.work_order.form import WorkOrderApplyForm
from apps.work_order.models import WorkOrder, WorkOrder_Contents
from apps.base import script


# logger = logging.getLogger("reboot")

class WorkOrderApplyView(LoginRequiredMixin, View):

    def get(self, request):
        forms = WorkOrderApplyForm()
        return render(request, 'order/workorder_apply.html', {'forms': forms})

    def post(self, request):
        forms = WorkOrderApplyForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            try:
                title = forms.cleaned_data["title"]
                order_contents = forms.cleaned_data["order_contents"]
                assign = forms.cleaned_data["assign"]
                orderfiles = forms.cleaned_data["orderfiles"]

                work_order = WorkOrder()
                work_order.title = title
                work_order.assign_id = assign
                work_order.orderfiles = orderfiles
                work_order.applicant = request.user
                work_order.status = 0
                tag = script.return_str()
                work_order.tag = tag
                work_order.save()

                contents = WorkOrder_Contents()
                contents.order_contents = order_contents
                contents.order_id = WorkOrder.objects.get(tag=tag)
                contents.write_user = request.user
                contents.save()

                # 给指派的人发邮件
                # send_mail(work_order.title,
                #           work_order.order_contents,
                #           settings.EMAIL_FROM,
                #           ['787696331@qq.com'],
                #           fail_silently=False,)
                # sendmail.delay(work_order.title,
                #             work_order.order_contents,
                #             settings.EMAIL_FROM,
                #             ['787696331@qq.com'],
                # )
                return HttpResponseRedirect(reverse('work_order:list'))
            except Exception as e:
                # logger.error("commit  workorder  error: %s" % traceback.format_exc())
                print(e)
                return render(request, 'order/workorder_apply.html', {'forms': forms, 'errmsg': '工单提交出错！'})

        else:
            return render(request, 'order/workorder_apply.html', {'forms': forms, 'errmsg': '工单填写格式出错！'})


class WorkOrderDetailView(LoginRequiredMixin, DetailView):
    """
    工单详情页，包括处理结果表单的填写
    """
    model = WorkOrder
    template_name = "order/workorder_detail.html"
    context_object_name = "workorder"

    def post(self, request, **kwargs):
        pk = kwargs.get("pk")
        work_order = self.model.objects.get(pk=pk)
        action = request.POST.get('action', '')
        text = request.POST.get('text', '')

        data = {}
        try:
            if action == 'accept':
                if work_order.status == 0:
                    work_order.status = 1
                    work_order.handler = request.user
                    work_order.save()

                    data = {
                        'code': 0,
                    }

            elif action == 'finish':
                if work_order.status == 1:
                    work_order.status = 2
                    work_order.handler = request.user
                    work_order.save()
                    data = {
                        'code': 0,
                    }
            elif action == 'replay':
                contents = WorkOrder_Contents()
                contents.order_contents = text
                contents.order_id = WorkOrder.objects.get(id=pk)
                contents.write_user = request.user
                contents.save()

                data = {
                    'code': 0,
                }
        except Exception as e:
            data = {
                'code': 1,
                'errmsg': str(e)
            }

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super(WorkOrderDetailView, self).get_context_data(**kwargs)
        context['contents'] = WorkOrder_Contents.objects.all()
        return context


class WorkOrderListView(LoginRequiredMixin, PaginationMixin, ListView):
    """
    待处理工单列表展示
    """

    model = WorkOrder
    # print(model)
    template_name = 'order/workorder_list.html'
    context_object_name = "orderlist"
    paginate_by = 10
    keyword = ''

    def get_queryset(self):
        queryset = super(WorkOrderListView, self).get_queryset()
        # 只显示状态小于2，即申请和处理中的工单
        queryset = queryset.filter(status__lt=2)
        # 如果不是sa组的用户只显示自己申请的工单，别人看不到你申请的工单，管理员可以看到所有工单
        if 'sa' not in [group.name for group in self.request.user.groups.all()]:
            queryset = queryset.filter(applicant=self.request.user)

        self.keyword = self.request.GET.get('keyword', '')
        if self.keyword:
            queryset = queryset.filter(Q(title__icontains=self.keyword) |
                                       Q(order_contents__icontains=self.keyword) |
                                       Q(result_desc__icontains=self.keyword))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(WorkOrderListView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        context['contents'] = WorkOrder_Contents.objects.all()
        return context

    def delete(self, request):

        delete_info = QueryDict(request.body)

        try:
            id = delete_info.get('id', '')
            if id:
                work_order = self.model.objects.get(pk=id)
                if work_order.status == 0:
                    work_order.status = 3
                    work_order.save()
                    data = {
                        'code': 0
                    }
                else:
                    data = {
                        'code': 1,
                        'errmsg': '工单状态异常，取消失败'
                    }
            else:
                data = {
                    'code': 1,
                    'errmsg': '参数异常，取消失败'
                }
        except Exception as e:
            data = {
                'code': 1,
                'errmsg': '数据库异常'
            }

        return JsonResponse(data)


class WorkOrderHistoryView(LoginRequiredMixin, PaginationMixin, ListView):
    """
    待处理工单列表展示
    """

    model = WorkOrder
    template_name = 'order/workorder_history.html'
    context_object_name = "orderlist"
    paginate_by = 10
    keyword = ''

    def get_queryset(self):
        queryset = super(WorkOrderHistoryView, self).get_queryset()
        # 只显示状态大于1，即申请和处理中的工单
        queryset = queryset.filter(status__gt=1)
        # 如果不是sa组的用户只显示自己申请的工单，别人看不到你申请的工单，管理员可以看到所有工单
        if 'sa' not in [group.name for group in self.request.user.groups.all()]:
            queryset = queryset.filter(applicant=self.request.user)

        self.keyword = self.request.GET.get('keyword', '')
        if self.keyword:
            queryset = queryset.filter(Q(title__icontains=self.keyword) |
                                       Q(order_contents__icontains=self.keyword) |
                                       Q(result_desc__icontains=self.keyword))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(WorkOrderHistoryView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context
