#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-05-19
# Filename: user_manager_v1.py
# Describe:
#*******************************************

# 标准模块
import sys


# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("luofeng", "123456")


# 定义操作提示信息

op_msg = '''\033[32m
-----------------------------------------------------------------
| 1. 增 add     |   # 01 luof 28 132xx 18210085737@139.com      |
-----------------------------------------------------------------
| 2. 删 delete  |   # luof                                      |
-----------------------------------------------------------------
| 3. 改 update  |   # luof                                      |
-----------------------------------------------------------------
| 4. 查 list    |   # list                                      |
-----------------------------------------------------------------
| 5. 搜 find    |   # find                                      |
-----------------------------------------------------------------
| 6. 退出 exit  |   # exit                                      |
-----------------------------------------------------------------
\033[0m'''

#定义格式化的模版
_tab_tpl = '|{0:^6s}|{1:^10s}|{2:^6s}|{3:^17s}|{4:^22s}|{5:^12s}|'
_tab_field = ('ID', 'username', 'age', 'mobile', 'email', 'address')
title = _tab_tpl.format(_tab_field[0], _tab_field[1], _tab_field[2], _tab_field[3], _tab_field[4], _tab_field[5])
_line = len(title)
_tab_content = '|{0:^6s}|{1:^10s}|{2:^6s}|{3:^17s}|{4:^22s}|{5:^12s}|'

# 实现增、删、改、查功能
while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")

    # 判断用户名或者密码是否正确
    if username == USERINFO[0] and password == USERINFO[1]:

        # 登录成功，输出操作提示信息
        print(op_msg)

        # 如果输入无效的操作，则反复操作, 否则输入 Exit 退出
        while True:
            # 业务逻辑
            action = input("Please input your operation: ")
            if action == "add":
                # 增加用户信息
                _format = 'id username age mobile email address'
                context = input('请输入用户信息,  格式{}: '.format(_format))
                user_info = context.split()

                if len(user_info) < 6:
                    print("\033[31minput error, please try input !\033[0m")
                    break

                # 判断列表的长度，空列表无法被迭代
                if len(RESULT)  > 0:
                    checks = False
                    for user in RESULT:
                        if user_info[1] == user[1]:
                            checks = True
                            print("\033[31muser {} Already exists.\033[0m".format(user_info[1]))

                    if not checks:
                        RESULT.append(user_info)
                        print("\033[32mAdd user {} information sucesss.\033[0m".format(user_info[1]))

                else:
                    RESULT.append(user_info)
                    print("\033[32mAdd user {} information sucesss.\033[0m".format(user_info[1]))


            elif action == "delete":
                checks = False
                user = input('请输入要删除的用户: ')

                # 判断列表的长度，空列表无法被迭代
                if len(RESULT)  > 0:
                    for serial, users in enumerate(RESULT):
                        if user == users[1]:
                            checks = True
                            del RESULT[serial]
                            print("\033[32mDel user {} information sucesss.\033[0m".format(user))

                    if not checks:
                        print("\033[31muser {} does not exist.\033[0m".format(user))

                else:
                    # 如果列表为空，提示增加用户信息
                    print("\033[31mThe list of users is empty, please add user information first.\033[0m")

            elif action == "update":
                checks = False
                user = input('请输入要更新的用户: ')

                # 判断列表的长度，空列表无法被迭代
                if len(RESULT)  > 0:
                    for users in RESULT:
                        if user == users[1]:
                            _format = 'id username age mobile email address'
                            context = input('请输入用户信息,  格式{}: '.format(_format))
                            user_info = context.split()

                            if len(user_info) < 6:
                                print("\033[31minput error, please try input !\033[0m")

                            else:
                                checks = True
                                users[0] = user_info[0]
                                users[1] = user_info[1]
                                users[2] = user_info[2]
                                users[3] = user_info[3]
                                users[4] = user_info[4]
                                users[5] = user_info[5]
                                print("\033[32muser {} information update sucesss.\033[0m".format(user))

                    if not checks:
                        print("\033[31muser {} does not exist.\033[0m".format(user))

                else:
                    # 如果列表为空，提示增加用户信息
                    print("\033[31mThe list of users is empty, please add user information first.\033[0m")


            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if len(RESULT) > 0:
                    print('-' * len(title))
                    print(title)
                    for users in RESULT:
                        print(_tab_content.format(users[0], users[1], users[2], users[3], users[4], users[5]))

                    print('-' * len(title))

                else:
                    print("\033[31mThe list of users is empty, please add user information first.\033[0m")

            elif action == "find":
                search_str = input('请输入要查询的用户，支持模糊查询: ').strip()
                if len(RESULT) > 0:
                    for users in RESULT:
                        # 满足条件返回0，否则返回负数
                        resp = users[1].find(search_str)

                        if not resp:
                            print('-' * len(title))
                            print(title)
                            print(_tab_content.format(users[0], users[1], users[2], users[3], users[4], users[5]))
                            print('-' * len(title))

                        else:
                            print("\033[31mUser {} does not exist, please try !!!\033[0m".format(search_str))

                else:
                    # 如果列表为空，提示增加用户信息
                    print("\033[31mThe list of users is empty, please add user information first.\033[0m")

            elif action == "exit":
                sys.exit(0)

            else:
                print("\033[31mError: invalid action, please try !!!\033[0m")
    else:
       # 带颜色
        print("\033[31mError: username or password error, please try !!!\033[0m")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
