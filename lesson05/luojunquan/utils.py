#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : utils
# @Software: PyCharm
from db import db_qurey
from prettytable import PrettyTable

#优雅的格式化输出
def list_table():
    results = db_qurey()
    tb = PrettyTable()
    for x in results:
        tb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
        tb.add_row([x[0],x[1],x[2],x[3],x[4]])
    print(tb)
