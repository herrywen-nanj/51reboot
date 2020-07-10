#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 21:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : People_Manage_System_v5
# @Software: PyCharm

from luojunquan.moudules.db import Sql_Util
from luojunquan.utils.check_utils import Check
from luojunquan.utils import list_table_util
from luojunquan.utils.log_utils import Logs

sql_util = Sql_Util()
log = Logs()
check = Check()

class PeopleManageSystem(object):
    #添加用户
    def add(self):
        username = input('请输入用户名：')
        age = input('请输入年龄：')
        sex = input('请输入性别：')
        phone = input('请输入手机号：')
        email = input('请输入邮箱地址：')
        email_tag = check.check_email(email)
        phone_tag = check.check_phone(phone)
        sex_tag = check.check_sex(sex)
        username_tag = check.check_user(username)
        age_tag = check.check_age(age)
        try:
            if email_tag is not True or phone_tag is not True or age_tag is not True or sex_tag is not True or username_tag is not True:
                log.info('请检查输入的格式')
            else:
                sql_insert = "insert into users(username,age,sex,phone,email) values (%s,%s,%s,%s,%s);"
                data = (username,age,sex,phone,email)
                sql_util.db_insert(sql_insert,data)
        except Exception as e:
            raise e

    #删除用户
    def delete(self):
        username = input('请输入需要删除的用户名：')
        sql_util.db_delete(username)

    #更新用户
    def update(self):
        username = input('请输入需要更新的用户名：')
        new_username = input('请输入新用户名：')
        new_age = input('请输入新年龄：')
        new_sex = input('请输入新性别：')
        new_phone = input('请输入新手机号：')
        new_email = input('请输入新邮箱地址：')
        sql_util.db_update(username,new_username,new_age,new_sex,new_phone,new_email)

    #显示所有用户
    def list_all(self):
        list_table_util.list_table()
