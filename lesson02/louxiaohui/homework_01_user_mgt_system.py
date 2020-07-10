#!/usr/bin/env python
# **********************************************************
# * Author        : xoyabc
# * Email         : lxh1031138448@gmail.com
# * Last modified : 2019-05-19 22:38
# * Filename      : homework_01_user_mgt_system.py
# * Description   : 
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

# 标准模块
import os
import sys


# 定义变量
RESULT = []
TITLE= ['name', 'age', 'Tel', 'Email']
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "123456")
CHANCE_TIMES = 5


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 直到输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input the action and info: ")
            # string -> list
            info_list = info.split()
            # print(info)
            # print(info_list)
            # print (len(info_list))
            # check if input format is legal or not
            if len(info_list) > 0:
                action = info_list[0]
                if len(info_list) > 1:
                    name = info_list[1]
            else:
                # input nothing
                print("invalid input info")
                sys.exit(2)
            if action == "add":
                # check if name is already added to the system
                flag = 0
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                if flag > 0:
                    print ("'{}' is already added" .format(" ".join(info_list[1:])))
                else:
                    RESULT.append(info_list[1:])
                    print ("add '{}' succeed" .format(" ".join(info_list[1:])))
            elif action == "delete":
                # remove from RESULT if name exist
                flag = 0
                delete_list = []
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        delete_list = x
                if flag > 0:
                    RESULT.remove(delete_list)
                else:
                    print ("user '{}' does not exist" .format(info_list[1]))
            elif action == "update":
                update_list = info.replace("="," ").split()
                ele = update_list[3]
                ele_value = update_list[4]
                # check if name is already added to the system
                flag = 0
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        if ele == "age":
                            x[1] = ele_value
                        elif ele == "Tel":
                            x[2] = ele_value
                        elif ele == "Email":
                            x[3] = ele_value
                        else:
                            print ("invalid update field")
                if flag == 0:
                    print ("user '{}' does not exist" .format(info_list[1]))
            elif action == "list":
                if len(RESULT) > 0:
                    print ("--------------------------------------------------------")
                    print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(TITLE[0],TITLE[1],TITLE[2],TITLE[3]))
                    for x in RESULT:
                        print ("--------------------------------------------------------")
                        print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(x[0],x[1],x[2],x[3]))
                else:
                    print ("There is no user in system")
            elif action == "find":
                pass
                # check if name is already added to the system
                flag = 0
                ele_list = []
                for x in RESULT:
                    if name in x[0]:
                        flag += 1
                        ele_list = x
                if flag > 0:
                    print ("--------------------------------------------------------")
                    print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(TITLE[0],TITLE[1],TITLE[2],TITLE[3]))
                    print ("--------------------------------------------------------")
                    print ("|{:<10} |{:<3} |{:<13} |{:<20}" .format(ele_list[0],ele_list[1],
                                                 ele_list[2],ele_list[3]))
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("\033[1;31m username or password error,you have {} times to input \033[0m" .format(CHANCE_TIMES))
        CHANCE_TIMES -= 1
        INIT_FAIL_CNT += 1

print("\n\033[1;31m Input {} times, all failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

