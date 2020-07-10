# 标准模块
import os
import sys
import json
import datetime
from prettytable import PrettyTable

RESULT = {}

FIELDS = ("name", "age", "tel", "email")

# -----------------------------------------------------------------登录操作

def loginAuto(username,password):
    USERINFO = ("1", "1")
    if username == USERINFO[0] and password == USERINFO[1]:
        return True
    else:
        return False

def add_user(info_list):
    username = info_list[1]
    USER_NAME = info_list[0]
    if username in RESULT:
        print('\033[1;31m"用户{}已存在"\033[0m'.format(username))
        return False
    else:
        RESULT[username] = dict(zip(FIELDS, info_list[1:]))
        print('\033[1;32m"用户 {} 添加成功"\033[0m'.format(username))
        return True

def update_user(info_list):
    if len(info_list) != 6:
        print('\033[1;31m"错误的操作请重新输入"\033[0m')
        return False
    # update monkey set age = 18
    username = info_list[1]
    update_1 = info_list[-1]
    update_2 = info_list[-3]
    if info_list[2] != "set" and info_list[-2] != "=":
        print('\033[1;31m"输入错误"\033[0m')
        return False
    if username in RESULT:
        if update_2 in RESULT[username]:
            RESULT[username][update_2] = update_1
            print('\033[1;32m"{}用户修改成功"\033[0m'.format(username))
            return True
        else:
            print('\033[1;31m"用户{}修改不成功"\033[0m'.format(username))
            return False
    else:
        print("用户{}不存在".format(username))
        return False

def delete_user(info_list):
    username = info_list[1]
    DEL = RESULT.pop(username, None)
    if DEL == None:
        print('\033[1;31m"用户{}不存在"\033[0m'.format(username))
        return False
    else:
        print('\033[1;32m"用户{}删除成功"\033[0m'.format(username))
        return True

def list_user(info_list):
    if len(RESULT) == 0:
        print("数据为空，请添加数据")
        return False
    #                C = PrettyTable()
    #                C.field_names = FIELDS
    C = PrettyTable(FIELDS)
    for i, j in RESULT.items():
        C.add_row(j.values())
    print(C)
    return True

def find_user(info_list):
    # find monkey
    try:
        username = info_list[1]
        x = RESULT.get(username, None)
        if x == None:
            print("用户{}未找到".format(username))
            return False
        else:
            C = PrettyTable(FIELDS)
            C.add_row(x.values())
            print(C)
            return True
    except Exception as e:
        pass

def save_user(info_list):
    try:
        fd = open("save3.txt", 'w')
        fd.write(json.dumps(RESULT))
    finally:
        fd.close()
        print('\033[1;31m"保存成功"\033[0m')
        return True

def load_user(info_list):
    fd = open("save3.txt", 'r')
    data = fd.read()
    global RESULT
    RESULT = json.loads(data)
    fd.close()
    return True

def dispaly_user(info_list):
    if len(info_list[1:]) >= 2 and len(info_list[1:]) <= 4:
        pagesize = 5
        if len(info_list[1:]) == 2:
            if info_list[1] == "page":
                pagesize = 5
            else:
                print('\033[1;31m"输入错误，请重新输入"\033[0m')
                return False
        else:
            if info_list[1] == "page" and info_list[3] == "page_size":
                pagesize = int(info_list[-1])
            else:
                print('\033[1;31m"输入错误，请重新输入"\033[0m')
                return False
                

        page = int(info_list[2]) - 1
        data = []
        for k, v in RESULT.items():
            data.append(v.values())
        # start, end sep
        start = page * pagesize
        end = start + pagesize
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for userinfo in data[start:end]:
            xtb.add_row(userinfo)
        print(xtb)
        return True
    else:
        print("格式错误")
        return False

def loginto():
    while True:
        info = input("请输入你的操作：").strip()
        info_list = info.split()
        action = info_list[0]
        if len(info) == 0 :
            print("操作错误，请重新输入操作信息")
            continue
        if action == "add":
            add_user(info_list)
        elif action == "delete":
            delete_user(info_list)
        elif action == "update":
            update_user(info_list)
        elif action == "list":
            list_user(info_list)
        elif action == "find":
            find_user(info_list)
        elif action == "save":
            save_user(info_list)
        elif action == "load":
            load_user(info_list)
        elif action == "display":
            dispaly_user(info_list)
            # dispaly page 2 pagesize 5
        elif action == "exit":
            sys.exit()
        else:
            print('\033[1;31m"无效的操作"\033[0m')

def print_user():
    C = PrettyTable(['执行动作', '输入方式'])
    D = {
        '增': "add monkey 12 123XXX  mokey@51reboot.com",
        '改': "update monkey set age = 18",
        '删': "delete monkey",
        '查': "list",
        '查找用户': "find monkey",
        "保存数据": "save",
        "读取数据": "load",
        "分页显示": "display page 2 page_size 3",
        '退出': "exit"
    }
    for i, j in D.items():
        C.add_row([i, j])
    print(C)


def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("请输入账号：")
        password = input("请输入密码：")

        if loginAuto(username,password):
            print("登陆成功")
        else:
            print("登陆失败")
            INIT_FAIL_CNT += 1
            continue

        print_user()

        loginto()

    print('\033[1;31m"输入{}次错误系统退出"\033[0m'.format(MAX_FAIL_CNT))
if __name__ == '__main__':
    main()
