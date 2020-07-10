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
import prettytable as pt
import datetime
import json
import xlrd, xlwt

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("xue", "123")
FILENAME = "user.txt"

# 定义字段标题
FIELDS = ['username', 'age', 'tel', 'email']

# 定义字段标题统一格式、宽度
title_head = '|{0:^10s} | {1:^5s} | {2:^15s} | {3:^20s} |'
# 定义字段文本统一格式、宽度
title_body = '|{0:^10s} | {1:^5s} | {2:^15s} | {3:^20s} |'

title = title_head.format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3])

# 随时读取最新数据到内存
def load():
    fd = open('user_info.txt', 'r')
    data = json.load(fd)
    RESULT.update(data)

# 保存数据到硬盘，实现持久化
def save():
    fd = open('user_info.txt', 'w')
    fd.write(json.dumps(RESULT))
    fd.close()

# 定义功能函数

def help():
    # 帮助信息
    print("""\033[36m
    1. add 格式：add monkey 12 132xxx monkey@51reboot.com
    2. delete 格式：delete monkey
    3. update 格式：update monkey set age = 18
    4. list  查看信息
    5. find 格式：find monkey
    6. save 保存数据到文件
    7. load 从文件读取数据到内存中
    6. exit 退出系统
    \033[0m""")


def add():
    # 判断用户是否存在, 如果用户存在，提示用户已经存在

    # if len(info_list) == 5:
    #     print("\033[31m 输入参数数量不够，请检查 或 help\033[0m")

    username = info_list[1]

    if username not in RESULT:
        user_info = {"name": info_list[1], "age": info_list[2], 'tel': info_list[3], 'email': info_list[4]}
        RESULT[username] = user_info
        print(">> \033[32m添加用户 {} 成功\033[0m".format(username))
    else:
        print("用户{}已经存在，请重新输入".format(username))

def delete():

    username = info_list[1]

    if len(RESULT) == 0:
        print("\033[32m用户信息已经空了，请添加用户\033[0m")
        return

    if username in RESULT:
        RESULT.pop(username)
        del_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\033[32m恭喜，{} 删除用户 {} 成功\033[0m".format(del_date,username))
    else:
        print("\033[32m 抱歉，用户 {} 不存在！\033[0m".format(username))


def update():

    username = info_list[1]

    # 判断用户是否存在, 如果用户存在才允许修改，否则提示告知用户不存在

    if username in RESULT:
        if info_list[2] == 'set':
            if info_list[3] == 'username':
                RESULT[info_list[-1]] = RESULT[username]
                RESULT[info_list[-1]]['name'] = info_list[-1]
                RESULT.pop(username)
            else:
            # 根据字典key取值，赋予新值
                RESULT[username][info_list[3]] = info_list[-1]
                print("用户 {} 更新成功".format(username))
    else:
        print(">> \033[32m 更新参数有误，请检查 \033[0m")


def find():
    find_status = False

    username = info_list[1]

    if username in RESULT:
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
        tb = pt.PrettyTable()
        tb.field_names = ["username", "age", "tel", "email"]
        for k, v in RESULT.items():
            tb.add_row([v['name'], v['age'], v['tel'], v['email']])

        print(tb)

def display():
    page = info_list[2]
    page_int = int(page)

    pagesize = info_list[-1]
    pagesize_int = int(pagesize)

    start = (page_int - 1) * pagesize_int
    end = page_int * pagesize_int

    for i in RESULT[start:end]:
        print(title)
        print("-" * len(title))  # 打印分隔符
        for k, v in RESULT.items():
            print(title_body.format(v['name'], v['age'], v['tel'], v['email']))
            print("-" * len(title))  # 打印分隔符


    """
    i = 0
    j = 3  # 每页显示数据量
    
    i + j    [0, 3] 0, 1, 2
    i = i + 3
    j = i + 3   [3, 6] 3, 4, 5
    
    i = 6
    j = 9 [6, 9] []
    
    """



while INIT_FAIL_CNT < MAX_FAIL_CNT:
    #username = input("Please input username: ")
    #password = input("Please input password: ")

    help()  # 调用帮助信息
    if True:
    #if username == USERINFO[0] and password == USERINFO[1]:
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
            elif action == "save":
                save()
            elif action == "load":
                load()
            elif action == "display":
                display()
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






