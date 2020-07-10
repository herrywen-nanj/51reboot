#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         views.py
# Description:  function which user can choose
# Author:       Aaron
# Date:         2019/7/4
# -------------------------------------------------------------------------------
import sys
from lib.utils import DB, MemoryData, ConfigOperator, page, create_logs, auth, print_table
from settings import PASSWD_FILE_PATH, SESSION, FIELDS, RESULT


# 按用户可操作的功能维度进行抽象
class UserAction(object):
    db = DB()
    mem = MemoryData()
    logger = create_logs()

    def __init__(self, *args):
        self.args = args

    def login(self):
        username = input("\033[36mPlease enter your username: \033[0m").strip()
        passwd = input("\033[36mPlease enter your password: \033[0m").strip()
        # situation that username or password is empty.
        if not username or not passwd:
            return False

        # create password file
        cnf_opt = ConfigOperator(PASSWD_FILE_PATH, "users", username)
        cnf_opt.write_conf()
        # get all of users info about username and password.
        data, is_true = cnf_opt.read_config()

        if not is_true:
            print("\033[31mReturned a error when parse configuration.\n{}\n\033[0m".format(data))
            return False

        if passwd != data["password"]:
            print("\033[31mUsername or Password entered error.\033[0m")
            return False

        SESSION["username"] = username
        SESSION["password"] = passwd
        SESSION["role"] = data["role"]
        self.logger.info("user [{}] login success.".format(username))
        self._greet_msg()
        return SESSION

    def logout(self):
        username = SESSION.get("username", None)
        SESSION.clear()
        self.logger.info("user [{}] logout.".format(username))
        print("\033[36mUser [{}] logout.\033[0m".format(username))

    def _greet_msg(self):
        msg = "Welcome user [{}] to User Management System".format(SESSION["username"])
        whole_msg = """\t{}\n\t{}\n\t{}\n\t{}{:^100}{}\n\t{}\n\t{}\n\t{}""".format(
            "+" + "-"*100 + "+",
            "|" + " "*100 + "|",
            "|" + " "*100 + "|",
            "|",
            msg,
            "|",
            "|" + " "*100 + "|",
            "|" + " "*100 + "|",
            "+" + "-"*100 + "+",
        )
        print("\033[36m{}\033[0m".format(whole_msg))

    def output_prompt(self):
        guest_help = """
            你可以进行的操作:
            1.添加, 示例: add username age phone_number email_address
            2.列出, 示例: list
            3.查找, 示例: find user_name
            4.分页, 示例: display page 1 pagesize 5
            5.导出(存储到mysql), 示例: save
            6.导入(从mysql导入), 示例: load
            7.注销登录，示例: logout
            8.退出程序, 示例: exit
            9.打印帮助信息, 示例: help
        """
        admin_help = """
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
        """
        current_help = admin_help if SESSION["role"] == "admin" else guest_help
        print("\033[36m{}\033[0m".format(current_help))

    def add_user(self):
        if len(self.args[0]) != len(FIELDS):
            print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m"
                  "\033[31mRight example: add  小李  18  113114  xiaoli@gmail.com\n\033[0m")
            return False

        res = self.mem.add(self.args[0])
        # print(res)
        self._msg_operation(res)

    @auth("admin")
    def del_user(self):
        if len(self.args[0]) != 1:
            print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m"
                  "\033[31mRight example: delete username\n\033[0m")
            return False

        res = self.mem.delete(self.args[0][0])
        self._msg_operation(res)

    def list_user(self):
        # self.load_db()
        res = self.mem.list()
        # print("list_user -> res: ", res)
        self._msg_operation(res)

    @auth("admin")
    def update_user(self):
        user_input = self.args[0]
        if len(user_input) != 5:
            print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m"
                  "\033[31mRight example: update  小李  set age  =  22\033[0m")
            return False

        if self.args[0][1] != "set" or self.args[0][3] != "=":
            print("\033[31m[ERROR]: the command format is invalid.\n"
                  "\033[31mRight example: update  小李  set age  =  22\033[0m")
            return False

        # 更新内存数据
        res = self.mem.update(self.args[0])
        self._msg_operation(res)

    def find_user(self):
        if len(self.args[0]) != 1:
            print("\033[31m[ERROR]: the user information you entered is incomplete.\n\033[0m"
                  "\033[31mRight example: find 小黑\n\033[0m")
            return False

        username = self.args[0][0]
        res = self.mem.get_one(username)
        self._msg_operation(res)

    def display_user(self):
        data_list = self.args[0]
        try:
            option_1, page_number, option_2, page_size = data_list
            page_number = int(page_number)
            page_size = int(page_size)

            # 输入命令格式异常处理
            if option_1 != "page" or option_2 != "pagesize":
                raise ValueError

            # 分页
            res = page(page_number=page_number, page_size=page_size)
            # print("page res: ", res)

            # 格式化输出
            self._msg_operation(res)

            another_choice_flag = True
            while not res.get("status") and another_choice_flag:
                u_choice = input("\033[36m回车翻页, 输入数字跳转到指定页，q返回上一级菜单>>: \033[0m").strip()
                if u_choice == "q":
                    return

                # 捕捉直接回车
                if u_choice == "":
                    page_number += 1
                    # 调用分页函数
                    res = page(page_number=page_number, page_size=page_size)
                    # 翻到最后一页退出
                    if res.get("status", "") == 4:
                        another_choice_flag = False
                    # 格式化输出
                    self._msg_operation(res)
                else:
                    page_number = int(u_choice)
                    # 调用分页函数
                    res = page(page_number=page_number, page_size=page_size)
                    # 格式化输出
                    self._msg_operation(res)
        # 快捷键返回上一级
        except (EOFError, KeyboardInterrupt):
            print("\n")
            return
        # 输入命令格式异常处理
        except Exception as e:
            print("\033[31m[ERROR]: the command you entered is incorrect.\n"
                  "\033[31mRight example: display page 1 pagesize 5\n\033[0m")
            # print(e)
            return

    def save_db(self):
        if not RESULT:
            print("\033[34mData is empty, need to add first.\033[0m")
            return False

        # 是否已存在db中，通过username判断记录在db中是否存在，不存在则插入
        for username in RESULT:
            res = self.db.get_one("users", username)
            if res["status"] != 0:
                self.db.insert("users", [RESULT[username][k] for k in FIELDS])
        print("\033[36mAll of user already insert completed.\n\033[0m")

    def load_db(self):
        res = self.db.select("users", fields=FIELDS)
        if res["status"] == 0:
            for d_user_info in res["data"]:
                RESULT[d_user_info["username"]] = d_user_info
        print("\033[36mAll of user already insert completed.\n\033[0m")

    def quit_program(self):
        print("\033[36mBye bye\033[0m")
        self.logger.info("user [{}] logout.".format(SESSION["username"]))
        sys.exit(0)

    # Color and record logs based on status codes
    def _msg_operation(self, status_dict):
        msg, data = status_dict.get("msg", None), status_dict.get("data", None)
    
        # 格式化输出
        if status_dict["status"] == 0:
            # 记录日志
            self.logger.info(msg)
    
            print("\033[32m{}\033[0m".format(msg))
            if data:
                res = print_table(rows=data)
                print("\033[32m{}\n\033[0m".format(res))
        elif status_dict["status"] == 4:
            print("\033[34m{}\033[0m\n".format(msg))
        else:
            print("\033[31m{}\033[0m\n".format(msg))


if __name__ == "__main__":
    pass

