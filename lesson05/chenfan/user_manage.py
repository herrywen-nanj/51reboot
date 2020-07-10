#!/bin/env python
# -*- coding:utf-8

"""
用户登陆认证
"""

import json
import sys
from prettytable import PrettyTable

from help_doc import doc_info
from my_log import log_info

from cnmysql import user_check,add_info,del_info,update_info,search


ned_filed=["name","age","phone","email"]


def yewu(message):
    action = message[0]
    data = message[1:]
    if action == "add":
        if len(data) != 4:
            print("语法错误")

        sql='''insert into users(username,age,tel,email) values("{}","{}","{}","{}"); '''.format(data[0],data[1],data[2],data[3])
        infoMessg, ok = add_info(sql)
        if not ok:
            print(infoMessg)
        else:
            print(infoMessg)
    elif action == "delete":
        sql = '''delete from users where username="{}";'''.format(data[0])
        infoMessg, ok = del_info(sql)
        if not ok:
            print(infoMessg)
        else:
            print(infoMessg)
    elif action == "update":
        if len(data) != 5:
            print("语法错误")

        if data[1] != set and data[-2] != "=":
            print("your input must be <update monkey set age = 18>")

        sql = '''update users set age="{}" where username="{}";'''.format(data[-1],data[0])
        # print(sql)
        infoMessg, ok = update_info(sql)
        log_info(infoMessg)
        if not ok:
            print(infoMessg)
        else:
            print(infoMessg)
    elif action == "find":
        sql = '''select * from users where username="{}";'''.format(data[0])
        # print(sql)
        infoMessg, ok = search(sql)
        log_info(infoMessg)
        if not ok:
            print(infoMessg)
        else:
            tb = PrettyTable()
            tb.field_names= ned_filed
            for i in infoMessg:
                data = list(i[1:])
                tb.add_row(data)
                print(tb)

    elif action == "list":
        sql = '''select * from users;'''
        # print(sql)
        infoMessg, ok = search(sql)
        log_info(infoMessg)
        if not ok:
            print(infoMessg)
        else:
            tb = PrettyTable()
            tb.field_names= ned_filed

            for i in infoMessg:
                data = list(i[1:])
                tb.add_row(data)
            print(tb)
    elif action == "doc":
        doc_info()
    elif action == "display":
        sql = '''select * from users;'''
        # print(sql)
        infoMessg, ok = search(sql)
        log_info(infoMessg)
        if not ok:
            print(infoMessg)
        else:
            # print(infoMessg)
            ifo_list = []
            for i in infoMessg: ifo_list.append(list(i[1:]))
            per_page = 10
            total_count = len(ifo_list)
            print(total_count)
            if total_count > per_page:
                max_per_num, a = divmod(total_count,per_page)
                print(max_per_num, a)
            else:
                try:
                    per_page = int(input("Pls enter your page_count: "))
                except Exception as e:
                    return e, False
                else:
                    max_per_num, a = divmod(total_count,per_page)

            if a > 0:
                max_per_num += 1

            while True:
                page = int(input("Pls enter the page you want to look: "))
                if page < 1 and page> max_per_num:
                    print("Your input error")
                else:
                    start = (page-1)*per_page
                    end = page * per_page
                    data = ifo_list[start:end]

                    tb = PrettyTable()
                    tb.field_names=ned_filed
                    for i in data:
                        tb.add_row(i)
                    print(tb)
                    choice = input("Pls enter <Y/N> to exit this loop: ")
                    if choice == "y" or choice == "Y": break

    elif action == "exit":
        sys.exit(0)
    else:
        print("Your input action is error! pls try again.")

# 用户登陆验证
def user_login():
    sql='''select * from user_info;'''
    info, ok = user_check(sql)
    log_info(info)
    if not ok:
        print(info)
    else:
        count = 0
        data = json.loads(info)
        name = input("Pls enter your name: ")
        password = input("Pls enter your password: ")
        while count < 3:
            count += 1
            for i in data:
                if i["name"] == name and i["password"] == password:
                    print("User {} Login Succ".format(name))
                    log_info("User {} Login Succ".format(name))
                    while True:
                        message = input("Pls enter your choice: ")
                        action = message.strip()
                        message2 = action.split()
                        yewu(message2)
                else:
                    log_info("User {} Login Faild".format(name))
            if count == 3: sys.exit(0)
user_login()