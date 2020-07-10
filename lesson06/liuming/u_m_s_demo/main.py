#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         main.py
# Description:  程序主逻辑
# Author:       Aaron
# Date:         2019/7/4
# -------------------------------------------------------------------------------
import sys
from settings import OPERATION_FUNC_DICT 
from settings import PASSWD_FILE_PATH, SESSION
from u_m_s_demo.views import UserAction


def logic():
    user_enter = input("\033[36mEnter what do u wanna do: \033[0m").strip()
    if not user_enter:
        print("\033[34mInvalid input, please try again.\033[0m")
        return False

    user_enter_list = user_enter.split()
    action_choice = user_enter_list[0]
    user_enter_data = []
    if len(user_enter_list) > 1:
        user_enter_data.extend(user_enter_list[1:])

    if action_choice not in OPERATION_FUNC_DICT:
        print("\033[34mInvalid input, please try again.\033[0m")
        return False

    user_action = UserAction(user_enter_data)
    method_name = OPERATION_FUNC_DICT[action_choice]
    getattr(user_action, method_name)()


def main():
    print("\033[34m{'username': 'aaron', 'password': '2', 'role': 'admin'}\n"
          "{'username': 'monkey', 'password': '1', 'role': 'guest'}\033[0m")
    init_fail_count = 0
    max_fail_count = 3
    try:
        user_action = UserAction()
        while init_fail_count < max_fail_count:
            # execute login function.
            is_login = user_action.login()
            if not is_login:
                init_fail_count += 1
                continue

            # user_action.greet_msg()
            user_action.output_prompt()
            while SESSION:
                logic()
        else:
            # log.debug("尝试登录[{}]次失败.".format(max_fail_count))
            print("\033[31mYou tried more than {} times， terminal exit\033[0m".format(max_fail_count))

    # 支持快捷键退出
    except (EOFError, KeyboardInterrupt):
        print("\033[36m\nBye bye.\n\033[0m")
        sys.exit(0)

    # 捕捉可能出现的未知异常
    except Exception as e:
        print("\033[31m\ncontact developer that found an unknown BUG, Bye bye.\n\033[0m")
        print(e)
        sys.exit(0)


if __name__ == "__main__":
    import os
    import sys
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 把项目目录加入环境变量
    sys.path.append(BASE_DIR)
    main()
    pass



