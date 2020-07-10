#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         u_m_s_demo.py
# Description:  Simple version of user management system
# Author:       Aaron
# Date:         2019/5/19
# -------------------------------------------------------------------------------
"""
需求
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 18 132xxx monkey@51reboot.com
    3.2 删 delete        # delete user_name
    3.3 改 update        # update user_name set field_name = value
    3.4 查 list          # list
    3.5 搜 find          # find user_name
3. 格式化输出
"""

from utils import DataOperate, get_one

# 定义变量
FIELDS = ["username", "age", "phone", "email"]  # 做格式化定义的列表
MAX_FAIL_CNT = 6    # 用户名密码每次最大尝试次数
USERINFO = ("lm", "1")      # 用户名，密码

data_operate = DataOperate()    # 实例化增删查改类

while MAX_FAIL_CNT:
    print(USERINFO)
    username = input("\033[36mPlease input your username: \033[0m")
    password = input("\033[36mPlease input your password: \033[0m")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("\033[36mPlease input what do u wanna do: \033[0m").strip()
            # 处理用户直接回车情况
            try:
                # string -> list
                info_list = info.split()

                # print(info)
                # print(info_list)
                action = info_list[0]
            except IndexError:
                continue

            if action == "add":
                data_list = info_list[1:]
                if len(data_list) < 4:
                    print("""\033[31m
                    Error: the user information you entered is incomplete.
                    Right example: add  小李  18  113114  xiaoli@gmail.com  
                    \033[0m""")
                    continue

                res = getattr(data_operate, action)(data_list)

                # 格式化输出
                if res["code"] == 0:
                    table_head = "".join(["|" + "{:^20}".format(i) for i in FIELDS]) + "|"
                    table_body = "".join(["|" + "{:^20}".format(i) for i in data_list]) + "|"
                    msg = """
                    \033[32m{}\033[0m\n
                    \033[32m{}\033[0m
                    \033[32m{}\033[0m
                    \033[32m{}\033[0m
                    \033[32m{}\033[0m
                    \033[32m{}\033[0m\n
                    """.format(res["msg"], "-"*85, table_head, "-"*85, table_body, "-"*85)
                else:
                    msg = """
                        \033[31m{}\033[0m\n
                    """.format(res["msg"],)
                print(msg)

            elif action == "delete":
                username = info_list[1]
                res = getattr(data_operate, action)(username)

                if res["code"] == 0:
                    print("\033[32m{}\033[0m".format(res["msg"]))
                elif res["code"] == 4:
                    print("\033[34m{}\033[0m".format(res["msg"]))
                else:
                    print("\033[31m{}\033[0m".format(res["msg"]))

            elif action == "update":
                where_update = info_list[1:]
                if len(where_update) < 5:
                    print("""\033[31m
                    Error: the user information you entered is incomplete.
                    Right example: update  小李  set age  =  22  
                    \033[0m""")
                    continue
                res = getattr(data_operate, action)(where_update)

                # 格式化输出
                if res["code"] == 0:
                    print("\033[32m{}\033[0m".format(res["msg"]))
                elif res["code"] == 4:
                    print("\033[34m{}\033[0m".format(res["msg"]))
                else:
                    print("\033[31m{}\033[0m".format(res["msg"]))

            elif action == "list":
                res = getattr(data_operate, action)()

                # 格式化输出
                if res["code"] == 0:
                    user_lists = res["msg"]

                    table_body = ""
                    print("\033[32m{}\033[0m".format("-"*90))
                    table_head = "|{:^4}".format("id") + "".join(["|" + "{:^20}".format(i) for i in FIELDS]) + "|"
                    print("\033[32m{}\033[0m".format(table_head))
                    for k, u in enumerate(user_lists):
                        table_body = "|{:^4}".format(k) + "".join(["|" + "{:^20}".format(i) for i in u]) + "|"
                        print("\033[32m{}\033[0m".format("-"*90))
                        print("\033[32m{}\033[0m".format(table_body))
                    print("\033[32m{}\033[0m".format("-"*90))
                elif res["code"] == 4:
                    print("\033[34m{}\033[0m\n".format(res["msg"]))
                else:
                    print("\033[31m{}\033[0m\n".format(res["msg"]))

            elif action == "find":
                index_list = info_list[1:]
                res = getattr(data_operate, action)(*index_list)

                # 格式化输出
                if res["code"] == 0:
                    user_lists = res["msg"]

                    table_body = ""
                    print("\033[32m{}\033[0m".format("-"*90))
                    table_head = "|{:^4}".format("id") + "".join(["|" + "{:^20}".format(i) for i in FIELDS]) + "|"
                    print("\033[32m{}\033[0m".format(table_head))
                    for k, u in enumerate(user_lists):
                        table_body = "|{:^4}".format(k) + "".join(["|" + "{:^20}".format(i) for i in u]) + "|"
                        print("\033[32m{}\033[0m".format("-"*90))
                        print("\033[32m{}\033[0m".format(table_body))
                    print("\033[32m{}\033[0m".format("-"*90))

                elif res["code"] == 4:
                    print("\033[34m{}\033[0m\n".format(res["msg"]))
                else:
                    print("\033[31m{}\033[0m\n".format(res["msg"]))

            elif action == "exit":
                break
            else:
                print("invalid action.")
    else:
        print("\033[31musername or password error.\033[0m")
        MAX_FAIL_CNT -= 1


print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")
