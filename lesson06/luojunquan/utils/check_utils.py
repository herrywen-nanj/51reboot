#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 21:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : check_utils
# @Software: PyCharm

import re
from luojunquan.moudules.db import Sql_Util

sql_util = Sql_Util()
class Check(object):
    #检查用户email地址是否符合邮件格式
    def check_email(selef,mail):
        email_pattern = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')
        email = email_pattern.match(mail)
        if email is None:
            return "\033[1;31m邮件格式有误 eg: xxx@xxx.com\033[0m"
        return True

    #检查用户手机号是否符合格式
    def check_phone(selef,phone):
        phone_pat = re.compile(r'^(13\d|14[5|7]|15\d|166|17[3|6|7]|18\d)\d{8}$')
        res = phone_pat.match(phone)
        if res is None:
            return "\033[1;31m手机号格式有误\033[0m"
        return True

    #检查年龄
    def check_age(selef,age):
        age_pat = re.compile(r'^((1[0-5])|[1-9])?\d$')
        res = age_pat.match(age)
        if res is None:
            return "\033[1;31年龄有误\033[0m"
        return True

    #检查用户性别是否符合
    def check_sex(selef,sex):
        if sex == '男' or sex == '女':
            return True
        else:
            print("\033[1;31m输入的性别有问题\033[0m")

    #检查用户是否存在
    def check_user(selef,username):
        qurey_all = sql_util.db_qurey()
        for x in qurey_all:
            if x[0] == username:
                return "\033[1;31m用户已存在\033[0m"
        return True