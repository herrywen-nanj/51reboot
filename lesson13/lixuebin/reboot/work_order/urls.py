from django.urls import path, re_path
from .views import *
from . import workorder

app_name = 'workorder'

urlpatterns = [
    path("apply/", workorder.WorkOrderApplyView.as_view(),name = "apply"),
    path("list/", workorder.WorkOrderListView.as_view(), name = 'list'),
    path("history", workorder.WorkOrderHistView.as_view(), name = 'history'),
    re_path("detail/(?P<pk>[0-9]+)?/", workorder.WorkOrderDetailView.as_view(), name = 'detail'),
]
2