# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-26 10:32'

import readline
import sys


from . import recordlog
from . import myprint
from . import useroperate
from . import  auth
from . import  help





def Logic():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 3
    while INIT_FAIL_CNT < MAX_FAIL_CNT:

        username = input("Please input your username: ").strip()
        password = input("Please input your password: ").strip()
        Auth = auth.Auth(username,password)
        if Auth.login():

            print(myprint.Green_Print('登录成功!'))
            print(help.help())
            while True:
                # 业务逻辑
                cmd_info = input("Please input your operation: ")
                recordlog.WriteLog().info(cmd_info)
                # 如果输入为空，跳入下次循环
                if cmd_info == '':
                    continue

                info_list = cmd_info.split()
                User = useroperate.User(info_list)
                action = info_list[0]

                if action == "add":
                    User.add_User()


                elif action == "delete":
                    User.delete_User()

                elif action == "update":
                    User.update_User()

                elif action == "list":
                    User.list_User()

                elif action == "find":
                    User.find_User()

                elif action == 'display':
                    info, ok = User.display_User()
                    print(info)

                elif action == 'export':
                    info, ok = User.export()
                    print(info)

                elif action == "exit":
                    Auth.logout()


                elif action == 'help':
                    print(help.help())
                else:
                    info = myprint.Red_print('invalid action: you can input: help ')
                    print(info)


        else:

            print(myprint.Red_print("username or password valid failed."))
            INIT_FAIL_CNT += 1

    print(myprint.Red_print("Game Over."))

