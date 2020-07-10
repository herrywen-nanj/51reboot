#!/bin/env python3
#

"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    3.6 分页             # display
    3.7 存储 save        # save
    3.8 加载 load        # load
    3.9 退出 exit        # exit
3. 格式化输出
4. 日志记录
"""

import sys
from prettytable import PrettyTable
import json
import logging

user_info = {"chenfan":"1234"}
user_rdict = {}
FILEDS=["name","age","phone","email"]
FLAG=True
S_DB = "chenfan.db"

def login(name,passwd):

    if name in user_info and passwd == user_info.get(name,None):
        return "Login in", True
    else:
        return "Failed", False

def add_info(message):
    name=message[0]

    if len(message) != len(FILEDS):
        print("[ERROR]: the user information you entered is incomplete.")
    if name in user_rdict:
        return "user {} is exist".format(name), False
    else:
        user_rdict[name] = dict(zip(FILEDS,message))
        return "add user {} success".format(name), True

    print(user_rdict)

def delete_info(message):
    name = message[0]

    try:
        user_rdict.pop(name)
    except Exception as e:
        print(e)
        print("User {} is not exist in user_rdict".format(name))
        return "User is not exist in user_rdict".format(name), False
    else:
        print("Congratulations on your success to delete user {} from user_rdict".format(name))
        return "delete user {} success".format(name), True
    finally:
        print("Please note that backup operations are performed before deletion")

def update_info(message):
    name = message[0]

    if name not in user_rdict: print("user {} is not exist".format(name))

    if message[1] != "set" and message[-2] != "=":
        print("grammatical mistake")
    else:
        try:
            user_rdict[name][message[2]] = message[-1]
        except Exception as e:
            print(e)
            return "modify user {} Failed".format(name), False
        else:
            print("modify success")
            return "modify user {} success".format(name), True

def list_info():

    if len(user_rdict) == 0:
        print("No data")
    tb = PrettyTable()
    tb.field_names = FILEDS

    for k,v in user_rdict.items():
        tb.add_row(v.values())

    print(tb)

def find_info(message):

    name = message[0]
    if name in user_rdict:
        print(user_rdict.get(name,None))
        return "find user {} success".format(name), True
    else:
        print("User not exist in it, pls enter <list> to see it first.")
        return "find user {} Failed".format(name),False

def save_info():

    with open(S_DB,"w") as f:
        f.write(json.dumps(user_rdict))
    print("Save file: {} scuess".format(user_rdict))

def load_info():

    try:
        f = open(S_DB)
    except Exception as e:
        print(e)
        print("Read file failed, filename {} is not exist\n".format(S_DB))
    else:
        data = f.read()
        user_rdict = json.loads(data)
    finally:
        f.close()
        return  user_rdict

def doc_info():
    print("""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    3.6 分页             # display
    3.7 存储 save        # save
    3.8 加载 load        # load
    3.9 退出 exit        # exit
3. 格式化输出
    """)

def display_info(message):
    # if len(message) != 4:
    #    print("Your input error")

    total_count = len(user_rdict)
    per_page_count = 5
    if total_count > per_page_count:
        max_per_num, a = divmod(total_count, per_page_count)
    else:
        try:
            per_page_count = int(input("Pls enter your page_count: "))
        except Exception as e:
            print(e)
        else:
            max_per_num, a = divmod(total_count,per_page_count)

    if a > 0:
        max_per_num += 1

    while FLAG:
        pager = int(input("Pls enter the page you want to look: "))

        data = user_rdict.values()
        info = []
        for i in data: info.append(i.values())

        if pager < 1 or pager > max_per_num:
            print("error, it must be 1-{}".format(max_per_num))
        else:
            start = (pager - 1) * per_page_count
            end = pager * per_page_count

            data = info[start:end]

            tb = PrettyTable()
            tb.field_names = FILEDS

            for item in data: tb.add_row(item)
            print(tb)
            choice = input("Pls enter <y/n> to exit: ")
            if choice == "y" or choice == "Y": break

def exit_info():
    return "sys exit", True
    sys.exit()

# 业务逻辑
def yewu(info):
    action= info[0]
    message = info[1:]
    if action == "add":
       info,ok =  add_info(message)
       logging.info(info)
    elif action == "delete":
        info,ok = delete_info(message)
        logging.info(info)
    elif action == "update":
        info,ok = update_info(message)
        logging.info(info)
    elif action == "list":
        list_info()
    elif action == "find":
        if len(info) != 2:
            print("grammatical mistake,you should input <find name>")
        info,ok = find_info(message)
        logging.info(info)
    elif action == "save":
        save_info()
    elif action == "load":
        global user_rdict
        user_rdict=load_info()
    elif action == "doc":
        doc_info()
    elif action == "exit":
        exit_info()
    elif action == "display":
        display_info(message)
    else:
        print("Your input error")



def main():
    COUNT = 0

    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='access.log',
                        filemode='a'
                        )
    while COUNT<=3:
        if COUNT == 3: sys.exit()

        name = input("Pls enter your name: ")
        passwd = input("Pls enter your passwd: ")

        info, ok = login(name, passwd)
        logging.info(info)
        COUNT += 1

        while ok:
            message = input("Pls enter your choice: ")
            # print(user_rdict)
            action = message.strip()
            message2 = action.split()
            yewu(message2)

if __name__ == '__main__':
    main()