#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auth : xuegqcto@aliyun.com

'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''

# 标准模块
import sys


# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("xue", "123")

# 定义字段标题
FIELDS = ['username', 'age', 'tel', 'email']

# 定义字段标题统一格式、宽度
title_head = '|{0:^10s} | {1:^5s} | {2:^15s} | {3:^20s} |'
# 定义字段文本统一格式、宽度
title_body = '|{0:^10s} | {1:^5s} | {2:^15s} | {3:^20s} |'

title = title_head.format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3])

# 定义功能函数

def help():
    # 帮助信息
    print("""
    1. add 格式：add monkey 12 132xxx monkey@51reboot.com
    2. delete 格式：delete monkey
    3. update 格式：update monkey set age = 18
    4. list  查看信息
    5. find 格式：find monkey
    6. exit 退出系统
    """)


def add():
    # 判断用户是否存在, 如果用户存在，提示用户已经存在
    for user in RESULT:
        if user[0] == info_list[1]:
            print("用户{}已经存在，请重新输入".format(user[0]))
            break
    else:# 添加用户，并给予用户提示信息
        RESULT.append(info_list[1:])
        print(">> \033[32m添加用户 {} 成功\033[0m".format(info_list[1]))

def delete():
    del_status = False

    for user in RESULT:
        if user[0] == info_list[1]:
            del_user = user[0]
            del_status = True

    if del_status:
        # 删除用户，并给予用户提示信息
        print("\033[32m恭喜，删除用户 {} 成功\033[0m".format(user[0]))
        RESULT.remove(user)
    else:
        print("\033[32m 抱歉，用户 {} 不存在！\033[0m".format(info_list[1]))


def update():
    # 判断用户是否存在, 如果用户存在才允许修改，否则提示告知用户不存在
    for user in RESULT:
        if user[0] == info_list[1]:
            if info_list[2] == 'set':
                if info_list[3] == 'name':
                    user[0] = info_list[5]
                elif info_list[3] == 'age':
                    user[1] = info_list[5]
                elif info_list[3] == 'tel':
                    user[2] = info_list[5]
                elif info_list[3] == 'email':
                    user[3] = info_list[5]
            print("用户 {} 更新成功".format(user[0]))
            list()
        else:
            print(">> \033[32m更新参数有误，请检查\033[0m")


def find():
    find_status = False

    for user in RESULT:
        if user[0] == info_list[1]:
            find_user = user[0]
            find_status = True

    if find_status:
        print("\033[32m 恭喜，用户 {} 找到了！\033[0m".format(info_list[1]))
    else:
        print("\033[32m 抱歉，用户 {} 不存在！\033[0m".format(info_list[1]))

def list():
    # 1. 先判断是否有用户信息
    # 2. 如果用户信息为空，提示用户添加用户
    # 3. 如果用户信息存在，则按要求列出

    if len(RESULT) == 0:
        print("\033[32m用户信息已经空了，请添加用户\033[0m")
    else:
        # print(RESULT)
        print(title)
        print("-" * len(title))  # 打印分隔符
        for user in RESULT:
            print(title_body.format(user[0], user[1], user[2], user[3]))
            print("-" * len(title))  # 打印分隔符



while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input username: ")
    password = input("Please input password: ")

    help()  # 调用帮助信息
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input your operation\033[32m[add/delete/update/list/exit]:\033[0m ")
            # string -> list

            info_list = info.split()
            #print(info)
            #print(info_list)

            action = info_list[0]
            if action == "add":
                add()
            elif action == "delete":
                delete()
            elif action == "update":
                update()
            elif action == "list":
                list()
            elif action == "find":
                find()
            elif action == "exit":
                sys.exit(0)
            elif action == "help":
                help()
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("\033[31m username or password error.\033[0m")
        INIT_FAIL_CNT += 1






