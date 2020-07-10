# -*- coding:utf-8 -*-
# author: lyl

import check
from prettytable import PrettyTable


def list_user():
        # 检测用户文件是否为空，如非空将结果转换为字典并返回
        tag, user_dict = check.user_dict()
        if tag:
            # 格式化输出
            xtb = PrettyTable()
            xtb.field_names = ["id", "username", "age", "tel", "email"]
            for x in user_dict.keys():
                xtb.add_row([user_dict[x]['id'], user_dict[x]['name'], user_dict[x]['age'], user_dict[x]['tel'],
                             user_dict[x]['email']])
            print(xtb)
        else:
            print(user_dict)


def find_user(info_list):
    # 检查用户输入是否合规
    if len(info_list) != 2:
        print("\033[1;31m输入有误，请重新输入. eg: find username|id \033[0m")
        return
    # 检查用户是否存在，并返回用户名
    tag, user_name, _ = check.user(info_list[1])
    if tag:
        # 获取用户信息转换为字典形式
        _, user_dict = check.user_dict()
        # 格式化输出
        xtb = PrettyTable()
        xtb.field_names = ["id", "username", "age", "tel", "email"]
        xtb.add_row([user_dict[user_name]['id'], user_dict[user_name]['name'], user_dict[user_name]['age'],
                     user_dict[user_name]['tel'], user_dict[user_name]['email']])
        print(xtb)


def pagesize(info_list):
    # display page 2 pagesize 5
    if len(info_list) != 5:
        print("\033[1;31m输入格式有误，请重新输入. eg: display page 2 pagesize 5 \033[0m")
        return
    if info_list[1] != 'page' or not info_list[2].isdigit() or info_list[3] != 'pagesize' or not info_list[4].isdigit():
        print("\033[1;31m输入参数有误，请重新输入. eg: display page 2 pagesize 5 \033[0m")
        return
    tag, user_dict = check.user_dict()
    if tag:
        # 设置表头
        xtb = PrettyTable()
        xtb.field_names = ["id", "username", "age", "tel", "email"]
        # 判断单页显示数据
        if int(info_list[4]) >= len(user_dict.keys()):
            print("\033[1;31m 单页显示内容过多，默认全部输出\033[0m")
            list_user()
            return
        # 判断页数是否超过最大值
        if int(info_list[2]) * int(info_list[4]) >= len(user_dict.keys()):
            print("\033[1;31m 页数超出范围，已为您显示最后一页\033[0m")
            user_list = list(user_dict.keys())[-int(info_list[4]):]
        else:
            # 容量小于最大值
            user_list = list(user_dict.keys())[(int(info_list[2])-1) * int(info_list[4]):
                                               (int(info_list[2])) * int(info_list[4])]
        for x in user_list:
            xtb.add_row([user_dict[x]['id'], user_dict[x]['name'], user_dict[x]['age'], user_dict[x]['tel'],
                         user_dict[x]['email']])
        print(xtb)
    else:
        print(user_dict)
