# task02模拟登陆-列表实现方式
"""
Created on May 21th 20:20:52 2019
Modify1 on May 22th 16:49:30 2019
@author: Owen.Niu
"""

# 标准模块
import os
import getpass
from prettytable import PrettyTable
#x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])

# 定义变量
RESULT = []
INIT_FAIL_CNT = 1
MAX_FAIL_CNT = 6
USERINFO = ("51reboot","123456")

while INIT_FAIL_CNT <= MAX_FAIL_CNT:
    username = input("\033[36mPlease input your username: \033[0m")
    password = getpass.getpass("\033[36mPlease input your password: \033[0m")
    if username == USERINFO[0] and password == USERINFO[1]:
        print("\033[32mLogin {} succ.\033[0m".format(username))
        while True:
            print ('\n帮助信息: \n'
                       '1. 添加学生信息: add monkey1 12 13910988765 monkey@51reboot\n'
                       '2. 删除学生信息: delete monkey1\n'
                       '3. 更新学生信息: update monkey1 set age = 20\n'
                       '4. 搜索学生信息: find monkey1\n'
                       '5. 显示所有学生信息: list\n'
                       '6. 退出: exit\n')
            # 业务逻辑
            info = input("\033[36mPlease input oper userinfo: \033[0m")
            info_list = info.split()
            ## 输入过滤器
            if len(info_list) == 5:
                action = info_list[0]
            elif len(info_list) == 6:
                action = info_list[0]
            elif len(info_list) == 2:
                action = info_list[0]
            elif len(info_list) == 1:
                action = info_list[0]
            else:
                print("\033[31m filed not enough\033[0m")
                continue

            if action == "add" and len(info_list) ==5:
                username=info_list[1]
                if len(RESULT) > 0:
                    for i in RESULT:
                        if i[0] == username:
                            print('\033[31mAdd {} fail,user exist.\033[0m'.format(username))
                            break
                    else:
                        RESULT.append(info_list[1:])
                        print("\033[32mAdd {} succ.\033[0m".format(info_list[1]))
                else:
                    RESULT.append(info_list[1:])
                    print("\033[32mAdd {} succ.\033[0m".format(info_list[1]))  
            elif action == "delete" and len(info_list) ==2:
                username=info_list[1]
                for i in RESULT:
                    if i[0] == username:
                        j=RESULT.index(i)
                        del(RESULT[j])
                        print("\033[32mDel {} succ.\033[0m".format(username))
                        break
                else:
                    print('\033[31mDel {} fail,no such user.\033[0m'.format(username))
            elif action == "update" and len(info_list) == 6:
                username=info_list[1]
                age=info_list[5]
                for i in RESULT:
                    if i[0] == username:
                        i[1] = age
                        print("\033[32mUpdate {} succ.\033[0m".format(username))
                        break
                else:
                    print('\033[31mUpdate {} fail,no such user.\033[0m'.format(username))
            elif action == "list" and len(info_list) == 1:
                x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])
                for i in RESULT:
                    x.add_row(i)
                print(x)
            elif action == "find" and len(info_list) == 2:
                x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])
                if RESULT:
                    for i in RESULT:
                        if i[0] == username:
                            x.add_row(i)
                            print(x)
                        #else:
                        #   print(x)
                else:
                    print(x)
            elif action == "exit":
                os._exit(0)
            else:
                print("\033[31minvalid action \033[0m")
    else:
        # 带颜色ex
        print('\033[31musername or password error,剩余{}次 \033[0m'.format(6-INIT_FAIL_CNT))
        #print("username or password error")
        INIT_FAIL_CNT += 1
print("\033[31m Input {} failed,Game Over.\033[0m".format(MAX_FAIL_CNT))
