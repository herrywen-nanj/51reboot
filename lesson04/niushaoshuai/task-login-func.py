# task02模拟登陆-列表实现方式
"""
Created on May 29th 20:20:52 2019
@author: Owen.Niu
"""

# 标准模块
import sys
import os
import json
import getpass
from prettytable import PrettyTable

# 定义变量
RESULT = dict()
FILENAME = "51reboot.db"
FIELDS = ("name","age","tel","email")

'''帮助 '''
def help_info():

    info = {
        '增': 'add monkey1 12 13910988765 monkey@51reboot',
        '删': 'delete monkey',
        '改': 'update monkey set age = 18',
        '查': 'list',
        '搜': 'find monkey',
        '存': 'save',
        '读': 'load',
        '分': 'display page 1 pagesize 5',
        '退': 'exit',
        '帮': 'doc'
    }
    for k, v in info.items():
        print(k, v)

'''验证账号和密码是否正确，如果正确返回True，否则返回False
'''
def loginAuth(username,password):
    user_passwd_t = ("1","1")
    if username == user_passwd_t[0] and password == user_passwd_t[1]:
        return "Login succ",True
    else:
        return "Login,fail",False

'''添加用户
'''
def addUser(info_list:list):
    if len(info_list) != 4:
        errMsg = "\033[31m filed not enough\033[0m"
        return errMsg,False
    # 判断用户是否存在，如果存在，提示用户已存在，不添加
    username = info_list[0]
    if username in RESULT:
        errMsg='\033[31mAdd {} fail,user exist.\033[0m'.format(username)
        return errMsg,False
    else:
        RESULT[username] = dict(zip(FIELDS,info_list))
        succMsg = "\033[32mAdd {} succ.\033[0m".format(username)
        return succMsg,True

'''删除用户
'''
def deleteUser(info_list:list):
    username = info_list[0]
    isSucc = RESULT.pop(username, False)
    if isSucc:
        succMsg="\033[32mDel {} succ.\033[0m".format(username)
        return succMsg,True
    else:
        errMsg='\033[31mDel {} fail,no such user.\033[0m'.format(username)
        return errMsg,False

'''修改用户
'''
def updateUser(info_list:list):
    if len(info_list) != 5:
        errMsg = "\033[31m filed not enough\033[0m"
        return errMsg, False
    username = info_list[0]
    operfiled = info_list[2]
    datafiled = info_list[-1]
    if info_list[1] != "set" or info_list[-2] != "=":
        errMsg = "Update format invalid error."
        return errMsg, False
    if username in RESULT:
        try:
            RESULT[username][operfiled] = datafiled
            succMsg = "\033[32mUpdate {} succ.\033[0m".format(username)
            return succMsg,True
        except Exception as e:
            errMsg = '\033[31mUpdate {} fail,no such filed {}.\033[0m'.format(username, operfiled)
            return errMsg,False
    else:
        errMsg = '\033[31mUpdate {} fail,no such user.\033[0m'.format(username)
        return errMsg,False
'''列出所有用户
'''
def listUser():
    if len(RESULT) == 0:
        errMsg = "data is null"
        return errMsg,False

    x = PrettyTable(FIELDS)
    for k, v in RESULT.items():
        x.add_row(v.values())
    return x,True

'''分页显示用户信息
'''
def displayUser(info_list:list):
    # 对每页的大小pagesize进行语法解释
    print(len(info_list))
    if len(info_list)>=2 and len(info_list)<=4:
        pagesize = 5
        if len(info_list) == 2:
            if info_list[0] == "page":
                pagesize = 5
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        else:
            if  info_list[2] == "pagesize":
                pagesize = int(info_list[-1])
            else:
                errMsg = "Display info invalid,Please input again"
                return errMsg,False

        data = []
        for k,v in RESULT.items():
            data.append(v.values())
        # 根据页数和每页大小推导出在所有数据中的区间
        page = int(info_list[1]) - 1
        start = page * pagesize
        end = start + pagesize

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for userinfo in data[start:end]:
            xtb.add_row(userinfo)
        return xtb,True
    else:
        errMsg = "Input info invalid,Please input again"
        return errMsg,False

'''搜索用户信息
'''
def findUser(info_list):
    username = info_list[0]
    userinfo = RESULT.get(username, None)
    if userinfo == None:
        errMsg = "Username {} not found.".format(username)
        return errMsg, False
    else:
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(userinfo.values())
        return xtb, True

'''loads,读取文件内容到内存
'''
def readFile():
    try:
        with open(FILENAME,'r') as fd:
            data = json.loads(fd.read())
            return data,True
    except Exception as e:
        return {},False

'''save,写内存数据到文件
'''
def writeFile():
    try:
        with open(FILENAME,'w') as fd:
            fd.write(json.dumps(RESULT))
        return "Save succ",True
    except Exception as e:
        print('\033[31mWrite file fail,errmsg: {}.\033[0m'.format(e))

''' 登出
'''
def logout():
    sys.exit()


'''业务逻辑
'''
def opLogic():
    while True:
        try:
            info = input("\033[36mPlease input oper userinfo: \033[0m")
            info_list = info.split()
            # 不输入，则提示重新输入
            if len(info) == 0:
                print("Input info invalid,Please input again")
                continue
            action = info_list[0]
            input_user_manage_info = info_list[1:]

            if action == "add":
                addMsg, ok = addUser(input_user_manage_info)
                print("{}, State: {}, Result: {}".format(action, ok, addMsg))
            elif action == "delete":
                delMsg, ok = deleteUser(input_user_manage_info)
                print("{}, State: {}, Result: {}".format(action, ok, delMsg))
            elif action == "update":
                updateMsg, ok = updateUser(input_user_manage_info)
                print("{}, State: {}, Result: {}".format(action, ok, updateMsg))
            elif action == "list":
                listMsg, ok = listUser()
                if not ok:
                    print("{}, State: {}, Result: {}".format(action, ok, listMsg))
                else:
                    print(listMsg)
            elif action == "find":
                findMsg, ok = findUser(input_user_manage_info)
                if not ok:
                    print("{}, State: {}, Result: {}".format(action, ok, findMsg))
                else:
                    print(findMsg)
            elif action == "save":
                writeMsg, ok = writeFile()
                print("{}, State: {}, Result: {}".format(action, ok, writeMsg))
            elif action == "load":
                readMsg, ok = readFile()
                if ok:
                    global RESULT
                    RESULT = readMsg
                    #print(RESULT)
                    print("{}, State: {}".format(action, ok))
                else:
                    print("{}, State: {}, Result: {}".format(action, ok, readMsg))
            elif action == "display":
                disMsg, ok = displayUser(input_user_manage_info)
                if not ok:
                    print("{}, State: {}, Result: {}".format(action, ok, disMsg))
                else:
                    print(disMsg)
            elif action == "doc":
                help_info()
            elif action == "exit":
                logout()
            else:
                print("invalid action.")
        except KeyboardInterrupt as e:
                print("\033[1;31m兄弟按Ctrl + C是不对的,真想退出请用exit\033[0m")
'''
入口函数
'''
def main():


    # 变量
    init_fail_cnt = 0
    max_fail_cnt = 6

    while init_fail_cnt < max_fail_cnt:
        username = input("Please input your username: ")
        password = input("Please input your password: ")

        loginMsg, ok = loginAuth(username, password)
        if not ok:
            print(loginMsg)

            init_fail_cnt += 1
            continue

        print("Login succ\n\n")
        help_info()
        opLogic()

    print("\nInput {} failed, Terminal will exit.".format(max_fail_cnt))





if __name__ == '__main__':
    main()