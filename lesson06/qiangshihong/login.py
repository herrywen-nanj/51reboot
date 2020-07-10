#!/usr/bin/python
# author: qiangsh
# V5.0 面向对象

import getpass   #用于隐藏用户输入的字符串，常用来接收密码
from user_auth.login_check import Login_Check
from user_manage.act_logic import logic


def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = getpass.getpass("Please input your password: ")   #输入密码不可见
        login_action = Login_Check(username,password)
        if login_action.checkuser():
            print("\033[1;36mLogin Suceesfully.\033[0m")
            logic()
        else:
            INIT_FAIL_CNT += 1
            if INIT_FAIL_CNT < MAX_FAIL_CNT:
                print("\033[5;35musername or password error！\033[0m\n还剩 {} 次机会.".format(MAX_FAIL_CNT - INIT_FAIL_CNT))
    else:
        print("\n\033[1;31mBye-bye, Input {} failed.\033[0m".format(MAX_FAIL_CNT))


if __name__ == "__main__":
    main()
