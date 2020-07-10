#!/usr/bin/python
import sys
from .utils import Action

FILENAME = "dic.txt"
help_info = '''---------------------------------------------
命令：
> 增: add monkey 12 132xxx monkey@51reboot.com
> 删: delete monkey
> 改: update monkey set age = 18
> 搜: find monkey
> 查: list
>分页: display page 1 pagesize 5
>导出：export
---------------------------------------------
'''
def logic():
    # 读取文件
    # 如果输入无效的操作，则反复操作, 否则输入exit退出
    while True:
        try:
            # 业务逻辑
            info = input("\033[1;35mPlease input your operation: \033[0m")
            # string -> list
            input_list = info.split()
            user_action = input_list[0]
            userinfo_string = ' '.join(input_list[1:])
            action = Action(userinfo_string)

            if user_action == "add":
                action.add_user()
            elif user_action == "delete" or user_action == "del":
                # .remove
                action.del_user()
            elif user_action == "find":
                action.find_info()
            elif user_action == "update":
                action.update_info()
            elif user_action == "list":
                action.get_list()
            elif user_action == "display":
                action.get_pageinfo()
            # elif action == "export":
            #     res = csv_export()
            #     print(res)
            elif user_action == "help" or user_action == "h":
                print(help_info)
            elif user_action == "exit":
                sys.exit(0)
            else:
                print("\033[1;36m输入错误，请输入 help 查看帮助！\033[0m\n")
        # except IndexError:
        #     print('\033[1;36m[Errno] list index out of range.\033[0m\n')
        # except FileNotFoundError:
        #     print('\033[1;36m[Errno] No such file or directory.\033[0m\n')
        # except TypeError:
        #     print('\033[1;36m[Errno] Type Error.\033[0m\n')
        # except KeyError:
        #     print('\033[1;36m[Errno] Key Error.\033[0m\n')
        except Exception as e:
            print(e)
