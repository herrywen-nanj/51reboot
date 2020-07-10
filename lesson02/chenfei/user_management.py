#!/usr/bin/env python
#coding=UTF-8
# **********************************************************
# * Author        : chenfei
# * Email         : 980098396@qq.com
# * Last modified : 2019-05-23 22:38
# * Filename      : user_management.py
# * Description   : 练习条件判断和字符串
# **********************************************************


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

import os
import re


# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 3
USERINFO = ("51reboot", "123456")
TITLE= ['name', 'age', 'Tel', 'Email']

print(">>>>+++++User Login+++++<<<<")

while True:
    usrname = input("请输入用户账户： ").strip().upper().lower()
    if usrname == USERINFO[0]:
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
            password = input("请输入密码： ").strip().upper().lower()
            if password == USERINFO[1]:
                print("\033恭喜进入管理系统，大胆搞吧，没事儿！！！\033[0m")
                break
            else:
                INIT_FAIL_CNT += 1
                if INIT_FAIL_CNT < MAX_FAIL_CNT:
                    print("\033剩下{}次\033[0m".format(INIT_FAIL_CNT), "密码输入错误，请确认后再次输入：")
            if INIT_FAIL_CNT == MAX_FAIL_CNT:
                break
                print("\033密码输入超过{}次，请再次重新登录\033[0m".format(INIT_FAIL_CNT))

    else:
        INIT_FAIL_CNT += 1
        if INIT_FAIL_CNT < MAX_FAIL_CNT:
            print("\033剩下{}次\033[0m".format(INIT_FAIL_CNT),"账号输入错误，请确认后再次输入：")
    if INIT_FAIL_CNT == MAX_FAIL_CNT:
        print("\033账号输入超过{}次，请再次重新登录\033[0m".format(INIT_FAIL_CNT))
        break
#业务逻辑

    info = input("\033 Please input userinfo: \n \033[0m")
    # string -> list
    info_list = info.split()
    action = info_list[0]
    if action == "add":
            add_list = input("\033 Please input add_list: name, age, Tel, Email\033[0m")
            add_list_new = add_list.split()
            if len(add_list_new) == 4:
                RESULT.append(add_list_new)
            pass
    elif action == "delete":
        del_list = input("请输入要删除的list：")
        pattern = r'\s+'
        list1 = re.split(pattern, RESULT[0:2])
        add_list_new = RESULT.split()

        print(add_list_new)

        for item in list1:
            if del_list in item:
                add_list_new.remove(RESULT)
        pass
    elif action == "update":
        update_list = input("请输入更新人的名字：").strip()
        if pattern == update_list:
            info_list1 = input("\033 Please input info_list: \n \033[0m")
            info_list1_new = info_list1.split()
            action = info_list_new[0]
            if action == name:
               name_list = input("\033 Please input name_list: \n \033[0m")
               match = re.sub(pattern,RESULT[0] , RESULT)
            elif action == age:
               age_list = input("\033 Please input age_list: \n \033[0m")
               match = re.sub(pattern,RESULT[1] , RESULT)
            elif action == Tel:
               Tel_list = input("\033 Please input Tel_list: \n \033[0m")
               match = re.sub(pattern,RESULT[2] , RESULT)
            elif action == Email :
               Email_list = input("\033 Please input Email_list: \n \033[0m")
               match = re.sub(pattern,RESULT[3] , RESULT)
        pass
    elif action == "list":
        if len(RESULT) > 0 :
           for x in RESULT:
               print("{} {} {} {}".format(TITLE[0],TITLE[1],TITLE[2],TITLE[3]), end="\t")
               print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
               print()
               print("-" * 50)
        pass
    elif action == "find":
        find_list = input("请输入寻找人的名字：").strip()
        pattern = find_list
        match = re.search(pattern,RESULT,re.I)
        for item in RESULT:
            if item in match:
                print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                print()
                print("-" * 50)

            elif action == "exit":
                sys.exit(0)

            else:
                print("invalid action")

            else:
            print('\033[7;31musername or password error.\033[1;31;40m')
            ini_fail_times += 1

        print("\nInput {} failed, Terminal will exit.".format(Max_fail_times))


