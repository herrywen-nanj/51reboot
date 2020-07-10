#!/usr/bin/env python
# **********************************************************
# * Author        : xoyabc
# * Email         : lxh1031138448@gmail.com
# * Last modified : 2019-05-27 22:46
# * Filename      : user_mgt_system_dict_and_file.py
# * Description   : 
# **********************************************************
'''
1. 登录认证；
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
    2.6 分页显示         # display page 1 pagesize 5
3. 格式化输出
4. 数据结构：列表 -> 字典；
5. 文件持久化,数据存到文件中
6. 异常处理
7. PrettyTable 优雅的格式化输出
8. 扩展：导出csv(可写可不写)
'''

# 标准模块
import os
import sys
import json
from prettytable import PrettyTable


# 定义变量
RESULT = {}
TITLE= ['name', 'age', 'Tel', 'Email']
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "123456")
CHANCE_TIMES = 5

# print warning message
def print_warn(content):
    print("\n\033[1;31m {} \033[0m" .format(content))

# print info message
def print_info(content):
    print("\n\033[1;32m {} \033[0m" .format(content))

# put the previous user data to RESULT dict
def get_data():
    global RESULT
    try:
        fd = open('user_info.txt', 'rU')
        data = fd.read()
        RESULT_DICT = json.loads(data, strict=False)
    except Exception as e:
        pass
    else:
        if not RESULT:
            RESULT = RESULT_DICT
        for k, v in RESULT_DICT.items():
            # you cannot iterate while modifying the dict
            # 1, use list(RESULT) to force a copy of keys to be made
            # 2, use deep copy, RESULT.copy()
            #for m in list(RESULT):
            for m in RESULT.copy():
                if k not in m:
                    RESULT[k] = v
        fd.close()
    return RESULT

# store the user info to file
def store_to_file(**DICT):
    fd = open('user_info.txt', 'w')
    try:
        fd.write(json.dumps(DICT))
    except Exception as e:
        print ("Write error,errmsg: {}" .format(e))
    finally:
        fd.close()

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
            # define a dictionary named dict_info to store use info
            dict_info = {}
            # handle abnormal input,do not exit until input exit
            try:
                action = info_list[0]
            except IndexError:
                print("invalid input info,pls input again")
                continue
            # get the name
            if len(info_list) > 1:
                name = info_list[1]
            if action == "add":
                # check if input field is complete
                try:
                    dict_info['name'] = info_list[1]
                    dict_info['age'] = info_list[2]
                    dict_info['tel'] = info_list[3]
                    dict_info['email'] = info_list[4]
                except Exception as e:
                    print ("you forget input one or more field.")
                # add user if input field is complete
                else:
                    # check if name is already added to the system
                    flag = 0
                    for x in RESULT.keys():
                        if name == x:
                            flag += 1
                    if flag > 0:
                        print ("'{}' is already added" .format(" ".join(info_list[1:])))
                    else:
                        RESULT[info_list[1]] = dict_info
                        print_info ("add '{}' succeed" .format(" ".join(info_list[1:])))
                        #print (RESULT)
            elif action == "save":
                RESULT = get_data()
                store_to_file(**RESULT)
            elif action == "delete":
                RESULT = get_data()
                # remove from RESULT if name exist
                flag = 0
                for x in RESULT.copy():
                    if name == x:
                        flag += 1
                        del RESULT[name]
                if flag == 0:
                    print ("user '{}' does not exist" .format(info_list[1]))
                else:
                    print ("user '{}' has been deleted" .format(info_list[1]))
                #print (RESULT)
                store_to_file(**RESULT)
            elif action == "update":
                update_list = info.replace("="," ").split()
                ele = update_list[3]
                ele_value = update_list[4]
                # check if name is already added to the system
                flag = 0
                for x in RESULT.copy():
                    if name == x:
                        flag += 1
                        if ele == "age":
                            RESULT[x]['age'] = ele_value
                        elif ele == "tel":
                            RESULT[x]['tel'] = ele_value
                        elif ele == "email":
                            RESULT[x]['email'] = ele_value
                        else:
                            print_warn ("invalid update field")
                if flag == 0:
                    print_warn ("user '{}' does not exist" .format(info_list[1]))
                store_to_file(**RESULT)
            elif action == "list":
                RESULT = get_data()
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                if len(RESULT.keys()) > 0:    
                    for k, v in RESULT.items(): 
                        xoy.add_row([v['name'], v['age'], v['tel'], v['email']])
                    print(xoy)
                else:
                    print_warn ("There is no user in system")
            elif action == "load":
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                fd = open('user_info.txt', 'rU')
                data = fd.read()
                try:
                    RESULT_DICT = json.loads(data, strict=False)
                    for k, v in RESULT_DICT.items(): 
                        row_list = [v['name'], v['age'], v['tel'], v['email']]
                        xoy.add_row(row_list)
                    print(xoy)
                except Exception as e:
                    print_warn ("There is no user in system")
                finally:
                    fd.close()
            elif action == "find":
                RESULT = get_data()
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                flag = 0
                if len(RESULT.keys()) > 0:    
                    for k, v in RESULT.items(): 
                        if name in k:
                            flag += 1
                            xoy.add_row([v['name'], v['age'], v['tel'], v['email']])
                    if flag > 0:
                        print(xoy)
                    else:
                        print_warn ("There is no such user in system")
                else:
                    print_warn ("There is no user in system")
            elif action == "display":
                RESULT = get_data()
                xoy = PrettyTable()
                xoy.field_names = ['name', 'age', 'Tel', 'Email']
                try:
                    page_num = int(info_list[2])
                    page_size = int(info_list[4])
                except Exception as e:
                    print ("you forget input one or more field.")
                else:
                    RESULT_LIST = list(RESULT.values()) 
                    RESULT_LIST_LEN = len(RESULT_LIST)
                    TOTAL_NUM = page_num * page_size
                    if RESULT_LIST_LEN < TOTAL_NUM:    
                        print_warn ("pagesize is out of range")
                    else:
                        start_index = (page_num -1) * page_size
                        end_index = page_num * page_size
                        for x in RESULT_LIST[start_index:end_index]:
                            xoy.add_row([x['name'], x['age'], x['tel'], x['email']])
                        print(xoy)
            elif action == "exit":
                sys.exit(0)
            else:
                print_warn ("invalid action.")
    else:
        # 带颜色
        print("\033[1;31m username or password error,you have {} times to input \033[0m" .format(CHANCE_TIMES))
        CHANCE_TIMES -= 1
        INIT_FAIL_CNT += 1

print("\n\033[1;31m Input {} times, all failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

