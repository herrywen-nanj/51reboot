# -*- coding:utf-8 -*-
# author: lyl
import user_expand
import logs

def main():
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        if user_expand.auth(username, password):
            logs.save_log("{} 登录成功".format(username))
            #user_expand.format_print(True, "\n\tWelcome to user magage system.\n")
            user_expand.user_help(username=username)
            user_expand.logic()
        else:
            logs.save_log("{} 登录失败".format(username), tag='error')
            user_expand.format_print(False, "username or password valid failed.")
            print()
            init_fail_count += 1
    user_expand.format_print(False,"Game Over.")
    logs.save_log("密码错误次数过多，退出登录", tag='error')



if __name__ == '__main__':
    main()
