# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-26 10:32'

import readline
import sys


from . import recordlog
from . import myprint
from . import useroperate


def Logic():
    while True:
        # 业务逻辑
        cmd_info = input("Please input your operation: ")
        recordlog.WriteLog().info(cmd_info)
        # 如果输入为空，跳入下次循环
        if cmd_info == '':
            continue

        info_list = cmd_info.split()

        action = info_list[0]

        if action == "add":
            useroperate.add_User(info_list)


        elif action == "delete":
            useroperate.delete_User(info_list)

        elif action == "update":
            useroperate.update_User(info_list)

        elif action == "list":
            useroperate.list_User()

        elif action == "find":
            useroperate.find_User(info_list)

        elif action == 'display':
            info, ok = useroperate.display_User(info_list)
            print(info)

        elif action == 'export':
            info, ok = useroperate.export()
            print(info)

        elif action == "exit":
            sys.exit(0)
        elif action == 'help':
            print(useroperate.help())
        else:
            info = myprint.Red_print('invalid action: you can input: help ')
            print(info)
