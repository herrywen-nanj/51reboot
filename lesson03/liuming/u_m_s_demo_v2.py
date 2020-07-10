#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         u_m_s_demo_v2.py
# Description:  
# Author:       Aaron
# Date:         2019/5/27
# -------------------------------------------------------------------------------

"""
需求
1. 登录认证，用户名密码序列化到文件及从文件反序列化；
2. 提示可选操作，以及示例.
3. 增删改查和搜索
    3.1 增 add           # add monkey 18 132xxx monkey@51reboot.com
    3.2 删 delete        # delete user_name
    3.3 改 update        # update user_name set field_name = value
    3.4 查 list          # list
    3.5 搜 find          # find user_name
4. 格式化输出
5. 分页输出功能
6. csv导入导出
"""

import sys
import getpass
from prettytable import PrettyTable
from utils import DataOperate, query_all_user_info, page, save_csv, load_csv, format_print

# 定义变量
FIELDS = ["username", "age", "phone", "email"]  # 做格式化定义的列表
INIT_FAIL_CNT = 0   # 初始化尝试次数
MAX_FAIL_CNT = 6    # 用户名密码每次最大尝试次数

# 友情提示
friendly_prompt = """\033[36m
        你可以进行的操作:
        1.添加, 示例: add username age phone_number email_address
        2.删除, 示例: delete user_name
        3.修改, 示例: update user_name set field_name = value
        4.列出, 示例: list
        5.查找, 示例: find user_name
        6.分页, 示例: display page 1 pagesize 5
        7.导出(csv格式文件), 示例: save
        8.导入(指定的csv格式), 示例: load
        9.退出, 示例: exit
        其他隐藏魔鬼操作，自己发现
\033[0m"""

# 实例化增删查改类
data_operate = DataOperate()


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    # 取得登录所需用户名密码，{"username": "pwd", ...}
    all_user_pwd_dict = query_all_user_info()
    print(all_user_pwd_dict)
    username = input("\033[36mPlease input your username: \033[0m").strip()
    password = input("\033[36mPlease input your password: \033[0m").strip()

    # 验证用户名是否正确
    if username not in all_user_pwd_dict:
        print("\033[31m[ERROR]: username error.\033[0m")
        INIT_FAIL_CNT += 1
        continue

    # 验证密码不为空且是否正确
    if not password or password != all_user_pwd_dict.get(username, None):
        print("\033[31m[ERROR]: assword error.\033[0m")
        INIT_FAIL_CNT += 1
        continue

    print(friendly_prompt)

    while True:
        info = input("\033[36mPlease input what do u wanna do: \033[0m").strip()
        # 处理用户直接回车情况
        try:
            # string -> list
            info_list = info.split()

            # print(info_list)
            action = info_list[0]
        except IndexError:
            continue

        # 业务逻辑
        if action == "add":
            data_list = info_list[1:]
            # 输入不合法粗暴处理法
            if len(data_list) < len(FIELDS):
                print("""\033[31m
                [ERROR]: the user information you entered is incomplete.
                Right example: add  小李  18  113114  xiaoli@gmail.com
                \033[0m""")
                continue

            # 添加
            res = getattr(data_operate, action)(data_list)

            # 格式化输出
            if res["code"] == 0:
                print("\033[32m{}\033[0m".format(res["msg"]))
                format_print(res["data"])
            else:
                print("\033[31m{}\033[0m\n".format(res["msg"]))

        elif action == "delete":
            try:
                username = info_list[1]
            except IndexError:
                print("""\033[31m
                [ERROR]: the command you entered is incorrect.
                Right example: delete username
                \033[0m""")
                continue

            # 删除
            res = getattr(data_operate, action)(username)

            if res["code"] == 0:
                print("\033[32m{}\033[0m".format(res["msg"]))
            elif res["code"] == 4:
                print("\033[34m{}\033[0m".format(res["msg"]))
            else:
                print("\033[31m{}\033[0m".format(res["msg"]))

        elif action == "update":
            try:
                where_update = info_list[1:6]
                where_action = where_update[1]
                symbol = where_update[3]
                if len(where_update) < 5 or where_action != "set" or symbol != "=":
                    print("""\033[31m
                    [ERROR]: the command format is invalid..
                    Right example: update  小李  set age  =  22
                    \033[0m""")
                    continue
            except IndexError:
                print("""\033[31m
                [ERROR]: the command you entered is incorrect.
                Right example: update  小李  set age  =  22
                \033[0m""")
                continue

            # 更新
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
                format_print(rows=res["data"])
            elif res["code"] == 4:
                print("\033[34m{}\033[0m\n".format(res["msg"]))
            else:
                print("\033[31m{}\033[0m\n".format(res["msg"]))

        elif action == "find":
            try:
                username = info_list[1]
            except IndexError:
                print("""\033[31m
                [ERROR]: the command you entered is incorrect.
                Right example: find 小黑
                \033[0m""")
                continue

            # 查找
            res = getattr(data_operate, action)(username)

            # 格式化输出
            if res["code"] == 0:
                format_print(rows=res["data"])
            elif res["code"] == 4:
                print("\033[34m{}\033[0m\n".format(res["msg"]))
            else:
                print("\033[31m{}\033[0m\n".format(res["msg"]))

        elif action == "save":
            res = save_csv()

            if res["code"] == 0:
                print("\033[32m{}\n\033[0m".format(res["msg"]))
            else:
                print("\033[34m{}\n\033[0m".format(res["msg"]))

        elif action == "load":
            res = load_csv()

            if res["code"] == 0:
                # 先合并现有的RESULT字典
                # 再格式化输出
                print(res["data"])
            else:
                print("\033[31m{}\n\033[0m".format(res["msg"]))

        elif action == "display":
            data_list = info_list[1:5]
            try:
                option_1, page_number, option_2, page_size = data_list
                page_number = int(page_number)
                page_size = int(page_size)

                if option_1 != "page" or option_2 != "pagesize":
                    raise ValueError("the command you entered is incorrect.")

            except Exception as e:
                print("""\033[31m
                [ERROR]: the command you entered is incorrect.
                Right example: display page 1 pagesize 5
                \033[0m""")
                continue

            # 分页
            res = page(page_number=page_number, page_size=page_size)

            # 格式化输出
            if res["code"] == 0:
                format_print(rows=res["data"])
            elif res["code"] == 4:
                print("\033[34m{}\033[0m\n".format(res["msg"]))
            else:
                print("\033[31m{}\033[0m\n".format(res["msg"]))

        elif action == "clear":
            # 删库跑路
            print("\033[31m已拨打110，删库跑路操作玩的六呀，小老弟\033[0m")

        elif action == "exit":
            sys.exit(0)
        else:
            print("\033[34minvalid action.\033[0m")


print("\033[31mYou tried more than {} times， terminal exit\033[0m".format(MAX_FAIL_CNT))