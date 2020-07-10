#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         u_m_s_demo_v2.py
# Description:  
# Author:       Aaron
# Date:         2019/5/27
# -------------------------------------------------------------------------------

import sys
from utils import DataOperate, query_all_user_info, page, save_csv, load_csv, format_print, create_logs,\
    drop_data


# Default variable
# 数据字段列表，做异常判定
FIELDS = ["username", "age", "phone", "email"]
# 全局session，做状态判定
SESSION = {}
# 选项功能字典
# 每多增加一个提供用户操作的功能(函数)，都需要添加到该字典中
OPREATTION_FUNC_DICT = {
    "help": "friendly_prompt",
    "add": "add_user",
    "delete": "del_user",
    "update": "update_user",
    "list": "list_user",
    "find": "find_user",
    "display": "display",
    "save": "export_user",
    "load": "import_user",
    "clean": "drop_all",
    "logout": "user_logout",
    "exit": "program_exit",
}

# 实例化增删改查类
data_operate = DataOperate()

# 调用写日志模块
log = create_logs()


# 用户登录模块
def login(user_name: str, password: str) -> dict:
    """

    :param user_name:
    :param password:
    :return:
    """
    # 取得登录所需用户名密码，[{"username": str, "password": str, "role": str}, ...]
    all_user_info_list = query_all_user_info()

    # 密码为空处理
    if not password:
        print("\033[31m[ERROR]: u must to enter password!\033[0m")
        return

    # 验证用户名密码是否正确
    for user_info in all_user_info_list:
        if user_info["username"] == user_name and user_info["password"] == password:
            log.info("user [{}] login success.".format(user_name))
            SESSION.update(user_info)
            SESSION["is_login"] = True
            return SESSION
    else:
        print("\033[31m[ERROR]: username or password error.\033[0m")


# 判断登录状态和执行权限的装饰器
def check_login_status(role: str):
    def decorate(func):
        def wrapper(*func_args, **func_kwargs):
            if not SESSION:
                # 用户没有进行登录执行入口函数
                # 本程序逻辑中，默认不会走到该判断
                return main()

            # 根据传入的role参数是否是admin 和 是否和session中的一致判定是否有执行权限
            # 也可换一种思路实现，维护一个全局字典，id数字对应角色名，根据id大小判定调用权限
            elif SESSION["role"] != "admin" and role != SESSION["role"]:
                print("\033[31mu don't have permission to do it!\n\033[0m")
                return None

            func(*func_args, **func_kwargs)
        return wrapper
    return decorate


# 根据角色信息打印提示
def friendly_prompt(*args):
    role = SESSION.get("role", None)
    if role == "admin":
        print("""\033[36m
            你可以进行的操作:
            1.添加, 示例: add username age phone_number email_address
            2.删除, 示例: delete user_name
            3.修改, 示例: update user_name set field_name = value
            4.列出, 示例: list
            5.查找, 示例: find user_name
            6.分页, 示例: display page 1 pagesize 5
            7.导出(csv格式文件), 示例: save
            8.导入(指定的csv格式), 示例: load
            9.注销登录，示例: logout
            10.退出, 示例: exit
            11.打印帮助信息, 示例: help
            其他隐藏魔鬼操作，自己发现
        \033[0m""")
    elif role == "guest":
        print("""\033[36m
            你可以进行的操作:
            1.列出, 示例: list
            2.查找, 示例: find user_name
            3.分页, 示例: display page 1 pagesize 5
            4.导出(csv格式文件), 示例: save
            5.导入(指定的csv格式), 示例: load
            6.注销登录，示例: logout
            7.退出, 示例: exit
            8.打印帮助信息, 示例: help
        \033[0m""")
    else:
        print("role -->", role)


# 给最终需要输出的结果上色；根据status_dict["code"] 输出指定颜色
# 日志统一在该函数中记录
def msg_operation(status_dict: dict):
    msg, data = status_dict.get("msg", None), status_dict.get("data", None)

    # 格式化输出
    if status_dict["code"] == 0:
        # 记录日志
        log.info(msg)

        print("\033[32m{}\033[0m".format(msg))
        if data:
            res = format_print(rows=data)
            print("\033[32m{}\n\033[0m".format(res))
    elif status_dict["code"] == 4:
        print("\033[34m{}\033[0m\n".format(msg))
        if data:
            res = format_print(rows=data)
            print("\033[32m{}\n\033[0m".format(res))
    else:
        print("\033[31m{}\033[0m\n".format(msg))


# 删库跑路功能
@check_login_status("admin")
def drop_all(info_list: list):
    print("\033[31m[WARNING]: 骚操作警告! 骚操作警告! 骚操作警告!\033[0m")
    res = drop_data()
    if res:
        print("\033[31m[CRITICAL]: user [{}] already deleted the database and gone.\n\033[0m".format(
            SESSION.get("username", None)
        ))
        log.info("[CRITICAL]: user [{}] already deleted the database and gone.\n".format(
            SESSION.get("username", None)
        ))


# 增加功能
@check_login_status("admin")
def add_user(info_list: list):
    data_list = info_list[1:]
    # 输入不合法粗暴处理法
    if len(data_list) < len(FIELDS):
        print("\033[31m[ERROR]: the user information you entered is incomplete.\n"
              "Right example: add  小李  18  113114  xiaoli@gmail.com\033[0m")
        return

    # 调用添加方法
    res = data_operate.add(data_list)

    # 格式化输出
    msg_operation(res)


# 删除功能
@check_login_status("admin")
def del_user(info_list: list):
    try:
        username = info_list[1]

    # 输入命令格式异常处理
    except IndexError:
        print("\033[31m[ERROR]: the command you entered is incorrect.\n"
              "Right example: delete username\033[0m")
        return

    # 删除
    res = data_operate.delete(username)

    # 格式化输出
    msg_operation(res)


# 更新功能
@check_login_status("admin")
def update_user(info_list: list):
    try:
        where_update = info_list[1:6]
        where_action = where_update[1]
        symbol = where_update[3]

        # 输入命令格式异常处理
        if len(where_update) < 5 or where_action != "set" or symbol != "=":
            print("\033[31m[ERROR]: the command format is invalid.\n"
                  "Right example: update  小李  set age  =  22\033[0m")
            return

    # 输入命令格式异常处理
    except IndexError:
        print("\033[31m[ERROR]: the command format is invalid.\n"
              "Right example: update  小李  set age  =  22\033[0m")
        return

    # 更新
    res = data_operate.update(where_update)

    # 格式化输出
    msg_operation(res)


# 查询所有功能
def list_user(info_list: list):
    # print("info_list", info_list)
    res = data_operate.list()

    # 格式化输出
    msg_operation(res)


# 精确查找功能
def find_user(info_list: list):
    try:
        username = info_list[1]

    # 输入命令格式异常处理
    except IndexError:
        print("\033[31m[ERROR]: the command you entered is incorrect.\n"
              "Right example: find 小黑\033[0m")
        return

    # 查找
    res = data_operate.find(username)

    # 格式化输出
    msg_operation(res)


# 分页显示功能
def display(info_list: list):
    data_list = info_list[1:5]
    try:
        option_1, page_number, option_2, page_size = data_list
        page_number = int(page_number)
        page_size = int(page_size)

        # 输入命令格式异常处理
        if option_1 != "page" or option_2 != "pagesize":
            raise ValueError

        # 分页
        res = page(page_number=page_number, page_size=page_size)

        # 格式化输出
        msg_operation(res)

        another_choice_flag = True
        while not res.get("code") and another_choice_flag:
            u_choice = input("\033[36m回车翻页, 输入数字跳转到指定页，q返回上一级菜单>>: \033[0m")
            if u_choice == "q":
                return

            # 捕捉直接回车
            if u_choice == "":
                page_number += 1
                # 调用分页函数
                res = page(page_number=page_number, page_size=page_size)
                # 翻到最后一页退出
                if res.get("code", "") == 4:
                    another_choice_flag = False
                # 格式化输出
                msg_operation(res)
            else:
                page_number = int(u_choice)
                # 调用分页函数
                res = page(page_number=page_number, page_size=page_size)
                # 格式化输出
                msg_operation(res)
    # 快捷键返回上一级
    except (EOFError, KeyboardInterrupt):
        print("\n")
        return
    # 输入命令格式异常处理
    except Exception as e:
        print("\033[31m[ERROR]: the command you entered is incorrect.\n"
              "Right example: display page 1 pagesize 5\033[0m")
        return


# 导出csv功能
def export_user(info_list: list):
    res = save_csv()
    # 格式化输出
    msg_operation(res)


# 导入csv功能
def import_user(info_list: list):
    res = load_csv()
    # 格式化输出
    msg_operation(res)


# 退出登录功能 (切换登录用户)
def user_logout(*args):
    log.info("user [{}] logout.".format(SESSION.get("username", None)))
    SESSION.clear()
    return


# 退出功能
def program_exit(*args):
    log.info("user [{}] logout.".format(SESSION.get("username", None)))
    print("\033[36m\n\nBye bye.\033[0m")
    sys.exit(0)


# 主逻辑
def main():
    init_fail_cnt = 0   # 初始化尝试次数
    max_fail_cnt = 6    # 用户名密码每次最大尝试次数

    # 验证用户输入的命令合法性
    try:
        while init_fail_cnt < max_fail_cnt:
            # 取得登录所需用户名密码，[{"username": str, "password": str, "role": str}, ...]
            all_user_info_list = query_all_user_info()
            print("你可以使用的用户名密码字典: \n", all_user_info_list)

            user_name = input("\033[36mPlease input your username: \033[0m").strip()
            password = input("\033[36mPlease input your password: \033[0m").strip()
            # 用户名密码验证
            res = login(user_name, password)
            if not res:
                init_fail_cnt += 1
                continue

            # 登录成功打印操作选项
            friendly_prompt()

            while SESSION.get("is_login", None):
                info = input("\033[36mPlease input what do u wanna do: \033[0m").strip()
                # string -> list
                info_list = info.split()
                # print(info_list)

                # 处理直接回车
                if not info_list:
                    continue
                action = info_list[0]

                # 业务逻辑
                if action in OPREATTION_FUNC_DICT:
                    # 使用内置函数 eval 执行每一个功能函数
                    eval(OPREATTION_FUNC_DICT[action])(info_list)
                else:
                    print("\033[34mInvalid action.\033[0m")
        else:
                log.info("用户[{}]尝试登录[{}]次失败.".format(user_name, max_fail_cnt))
                print("\033[31mYou tried more than {} times， terminal exit\033[0m".format(max_fail_cnt))

    # 支持快捷键退出
    except (EOFError, KeyboardInterrupt):
        print("\033[36m\nBye bye.\033[0m")
        sys.exit(0)

    # 捕捉可能出现的未知异常
    except Exception as e:
        print("\033[34m\n程序遇到bug, byebye.\033[0m")
        log.error(e)
        sys.exit(0)


if __name__ == '__main__':
    main()
