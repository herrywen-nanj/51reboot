# -*- coding:utf-8 -*-
# author: lyl

from django.views.generic import ListView
from pure_pagination.mixins import PaginationMixin
from apps.users.models import UserProfile

class MyModelListView(PaginationMixin, ListView):
    # Important, this tells the ListView class we are paginating
    paginate_by = 10

    # Replace it for your model or use the queryset attribute instead
    object = UserProfile