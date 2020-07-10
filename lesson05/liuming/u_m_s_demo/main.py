#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         main.py
# Description:  程序主逻辑
# Author:       Aaron
# Date:         2019/6/24
# -------------------------------------------------------------------------------
import sys
from settings import OPERATION_FUNC_DICT 
from settings import PASSWD_FILE_PATH, SESSION
from u_m_s_demo.views import login, logout, quit_program, save_user, load_user, display_user, find_user, \
    list_user, update_user, del_user, add_user, output_prompt


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

    func = eval(OPERATION_FUNC_DICT[action_choice])
    return func(user_enter_data)


def main():
    print("\033[34musername: aaron\tpassword: 1\033[0m")
    init_fail_count = 0
    max_fail_count = 3
    try:
        while init_fail_count < max_fail_count:
            if not login():
                init_fail_count += 1
                continue

            output_prompt()
            while SESSION:
                logic()
        else:
            # log.info("尝试登录[{}]次失败.".format(max_fail_count))
            print("\033[31mYou tried more than {} times， terminal exit\033[0m".format(max_fail_count))

    # 支持快捷键退出
    except (EOFError, KeyboardInterrupt):
        print("\033[36m\nBye bye.\n\033[0m")
        sys.exit(0)

    # 捕捉可能出现的未知异常
    except Exception as e:
        print("\033[31m\ncontact developer that found an unknown BUG, Bye bye.\n\033[0m")
        sys.exit(0)


if __name__ == "__main__":
    import os
    import sys
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 把项目目录加入环境变量
    sys.path.append(BASE_DIR)
    main()



