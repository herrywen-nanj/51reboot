# -*- coding:utf-8 -*-
# author: lyl
import user_expand
import logs
import getpass

def main():
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        try:
            username = input("Please input your login username: ")
            password = input("Please input your login password: ")
            # password = getpass.getpass("Please input your login password: ")
            check_user = user_expand.Auth(username, password)

            if check_user.auth():
                _, roles = check_user.auth()
                logs.save_log("{} 登录成功".format(username))
                user_expand.user_help(username=username, roles=roles)
                user_expand.logic(roles)
            else:
                logs.save_log("{} 登录失败".format(username), tag='error')
                user_expand.format_print(False, "username or password valid failed.")
                print()
                init_fail_count += 1
        except Exception as e:
            print(e)
            user_expand.format_print(False, "操作异常，程序退出!!!")
            exit(1)
    user_expand.format_print(False,"Game Over.")
    logs.save_log("密码错误次数过多，退出登录", tag='error')



if __name__ == '__main__':
    main()
