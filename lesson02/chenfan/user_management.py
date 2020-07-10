# !/bin/env python3
# -*- coding:utf-8 -*-
# 没有调试
"""
用户管理系统
登录验证
登录成功后增删改查和搜索
格式化输出
"""

import sys

name_info = {"chenfan": "1234", "min": "1234"}
user_info = []
count = 0


def choice(c):
    # 根据判断做选择
    if c == "add":
        radd()
    elif c == "delete":
        rdelete()
    elif c == "update":
        rupdate()
    elif c == "list":
        rlist()
    elif c == "find":
        rfind()
    elif c == "exit":
        sys.exit(0)
    else:
        print("Your input must be <add|delete|update|list|find|exit> ")


def menu():
    # 帮助信息
    print(
        """
        1. add 追加信息
        2. delete 删除信息
        3. update 修改信息
        4. list 查信息
        5. find 搜索信息
        6. exit 退出用户管理系统
        """
    )


def radd():
    # 添加用户信息
    info = input("Pls enter <name> <age> <sex> <email>: ")
    # string -> list
    info_list = info.split()

    if info_list[0] in user_info:
        print("user {} is exist".format(info_list[0]))
    else:
        user_info.append(info_list)
        print("add user {} success".format(info_list[0]))


def rdelete():
    # 删除用户信息
    name = input("Pls enter <name> which you want to delete: ")
    print(user_info)

    for name_all in user_info:
        if name == name_all[0]:
            user_info.remove(name_all)
            print("Delete user {} success".format(name))
        else:
            print("用户不存在,所以兄嘚你GG了")


def rupdate():
    # 修改用户信息
    name = input("Pls enter name for modify: ")

    for x in user_info:
        if name == x[0]:
            # 判断修改的信息
            nus = int(input("Pls enter which info you want to modify <0: name> <1: age> <2: sex> <3: email>: "))
            x[nus] = input("Pls enter your modify message: ")
            print(user_info)
        else:
            print("用户更新失败，不存在")


def rlist():
    # 列出用户信息
    for x in user_info:
        print("{name} {sex} {age} {address}".format(name=x[0], sex=x[1], age=x[2], address=x[3]))
    print()


def rfind():
    # 查找用户信息
    name = input("Pls enter which name you want to find: ")

    for x in user_info:
        if name == x[0]:
            print("{name} {sex} {age} {address}".format(name=x[0], sex=x[1], age=x[2], address=x[3]))
        else:
            print("{} not exist".format(name))


while count <= 3:
    # 登录验证
    if count == 3: sys.exit()
    name = input("Pls enter your name: ")
    passwd = input("Pls enter your passwd:")
    if name in name_info and passwd == name_info.get(name):
        print("Login ok")
        while True:
            menu()
            cho = input("Pls enter your choice,it must be <add> <delete> <update> <find> <list>: ")
            choice(cho)
    else:
        print("Login faild!")
        count += 1
