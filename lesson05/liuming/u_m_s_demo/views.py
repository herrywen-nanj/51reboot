#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         views.py
# Description:  function which user can choose
# Author:       Aaron
# Date:         2019/6/24
# -------------------------------------------------------------------------------
import sys
import csv
from settings import PASSWD_FILE_PATH, SESSION, USER_INFO_FILE_PATH
from lib.db_operation import insert, delete, select, update, get_one
from lib.utils import read_config, write_conf, msg_operation, page, log


def login():
    # create password file
    write_conf(PASSWD_FILE_PATH, "users")

    username = input("\033[36mPlease enter your username: \033[0m").strip()
    passwd = input("\033[36mPlease enter your password: \033[0m").strip()
    print(passwd, type(passwd))
    # situation that username or password is empty.
    if not username or not passwd:
        return False
    # get all of users info about username and password.
    data, is_true = read_config(PASSWD_FILE_PATH, "users")
    print(data)

    if not is_true:
        print("\033[31mreturned a error when parse configuration.\n{}\n\033[0m".format(data))
        return False

    if username not in data or data[username] != passwd:
        print("\033[31mUsername or Password entered error.\033[0m")
        return False

    SESSION["username"] = username
    SESSION["password"] = passwd
    log.info("user [{}] login success.".format(username))
    return SESSION


def logout(*args):
    username = SESSION.get("username", None)
    SESSION.clear()
    log.info("user [{}] logout.".format(username))
    print("\033[36mUser [{}] logout.\033[0m".format(username))


def output_prompt(*args):
    print("""\033[36m
        你可以进行的操作:
        1.添加, 示例: add username age phone_number email_address
        2.删除, 示例: delete user_name
        3.修改, 示例: update user_name set field_name = value
        4.列出, 示例: list
        5.查找, 示例: find user_name
        6.分页, 示例: display page 1 pagesize 5
        7.导出(存储到mysql), 示例: save
        8.导入(从mysql导入), 示例: load
        9.注销登录，示例: logout
        10.退出程序, 示例: exit
        11.打印帮助信息, 示例: help
        其他隐藏魔鬼操作，自己发现
    \033[0m""")


def add_user(*args):
    if len(args[0]) != 4:
        print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m")
        return False

    res = insert("users", args[0])
    # print(res)
    msg_operation(res)


def del_user(*args):
    if len(args[0]) != 1:
        print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m")
        return False

    res = delete("users", args[0][0])
    msg_operation(res)


def list_user(*args):
    res = select("users")
    if not res["status"] and not res["data"]:
        print("\033[34mData is empty in DB, add a user information first.\n\033[0m")
    else:
        msg_operation(res)


def update_user(*args):
    user_input = args[0]
    if len(user_input) != 5:
        print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m")
        return False

    data = {user_input[2]: user_input[4]}
    where = "username='{}'".format(user_input[0])
    res = update("users", data, where)
    msg_operation(res)


def find_user(*args):
    if len(args[0]) != 1:
        print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m")
        return False

    username = args[0][0]
    res = get_one("users", username)
    msg_operation(res)


def display_user(*args):
    data_list = args[0]
    try:
        all_users_info = select("users")["data"]
        option_1, page_number, option_2, page_size = data_list
        page_number = int(page_number)
        page_size = int(page_size)

        # 输入命令格式异常处理
        if option_1 != "page" or option_2 != "pagesize":
            raise ValueError

        # 分页
        res = page(all_users_info, page_number=page_number, page_size=page_size)

        # 格式化输出
        msg_operation(res)

        another_choice_flag = True
        while not res.get("status") and another_choice_flag:
            u_choice = input("\033[36m回车翻页, 输入数字跳转到指定页，q返回上一级菜单>>: \033[0m").strip()
            if u_choice == "q":
                return

            # 捕捉直接回车
            if u_choice == "":
                page_number += 1
                # 调用分页函数
                res = page(all_users_info, page_number=page_number, page_size=page_size)
                # 翻到最后一页退出
                if res.get("status", "") == 4:
                    another_choice_flag = False
                # 格式化输出
                msg_operation(res)
            else:
                page_number = int(u_choice)
                # 调用分页函数
                res = page(all_users_info, page_number=page_number, page_size=page_size)
                # 格式化输出
                msg_operation(res)
    # 快捷键返回上一级
    except (EOFError, KeyboardInterrupt):
        print("\n")
        return
    # 输入命令格式异常处理
    except Exception as e:
        print("\033[31m[ERROR]: the command you entered is incorrect.\n"
              "Right example: display page 1 pagesize 5\n\033[0m")
        return


def save_user(*args):
    res = select("users")
    if not res["data"]:
        print("\033[34mData is empty, need to add first.\033[0m")
        return False

    with open(USER_INFO_FILE_PATH, 'w', newline="") as f2:
        fieldnames = res["data"][0].keys()
        cw = csv.DictWriter(f2, fieldnames=fieldnames)
        # 将fieldnames 写入到第一行
        cw.writeheader()

        for u_dict in res["data"]:
            cw.writerow(u_dict)

    print("\033[36mSave success，file path:{}\033[0m".format(USER_INFO_FILE_PATH))


def load_user(*args):
    res = select("users")
    msg_operation(res)


def quit_program(*args):
    print("\033[36mBye bye\033[0m")
    sys.exit(0)


if __name__ == "__main__":
    pass

