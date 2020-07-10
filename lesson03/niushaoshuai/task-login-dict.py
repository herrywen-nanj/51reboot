# task02模拟登陆-列表实现方式
"""
Created on May 29th 20:20:52 2019
@author: Owen.Niu
"""

# 标准模块
import os
import json
import getpass
from prettytable import PrettyTable

# 定义变量
RESULT = dict()
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
                       '6. 分页显示所有学生信息: display 2 pagesize 5\n'
                       '7. 保存所有学生信息: save\n'
                       '8. 加载所有学生信息: load\n'
                       '9. 退出: exit\n')
            try:
                # 业务逻辑
                info = input("\033[36mPlease input oper userinfo: \033[0m")
                info_list = info.split()
                ## 输入过滤器
                if len(info_list) == 5:
                    action = info_list[0]
                elif len(info_list) == 4:
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
                if action == "add" and len(info_list) == 5:
                    username = info_list[1]
                    if username in RESULT.keys():
                        print('\033[31mAdd {} fail,user exist.\033[0m'.format(username))
                    else:
                        RESULT[username] = dict()
                        RESULT[username]["age"] = info_list[2]
                        RESULT[username]["tel"] = info_list[3]
                        RESULT[username]["email"] = info_list[4]
                        print("\033[32mAdd {} succ.\033[0m".format(username))
                elif action == "delete" and len(info_list) == 2:
                    username = info_list[1]
                    if RESULT.pop(username, False):
                        print("\033[32mDel {} succ.\033[0m".format(username))
                    else:
                        print('\033[31mDel {} fail,no such user.\033[0m'.format(username))
                elif action == "update" and len(info_list) == 6:
                    username = info_list[1]
                    operfiled = info_list[3]
                    datafiled = info_list[5]
                    if username in RESULT.keys():
                        try:
                            Nothing = RESULT[username][operfiled]
                            RESULT[username][operfiled] = datafiled
                            print("\033[32mUpdate {} succ.\033[0m".format(username))
                        except Exception as e:
                            print('\033[31mUpdate {} fail,no such filed {}.\033[0m'.format(username, operfiled))
                    else:
                        print('\033[31mUpdate {} fail,no such user.\033[0m'.format(username))
                elif action == "list" and len(info_list) == 1:
                    x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])
                    for k, v in RESULT.items():
                        try:
                            i = [k, v["age"], v["tel"], v["email"]]
                        except:
                            i = []
                        x.add_row(i)
                    print(x)
                elif action == "display" and (len(info_list) == 4 or len(info_list) == 2):
                    x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])
                    num = int(info_list[1])
                    if len(info_list) == 2:
                        info_list.extend(['pagesize', 5])
                    size = int(info_list[3])
                    length = len(RESULT)
                    pages = int(length / size) + 1
                    if num > pages:
                        RESULT1 = RESULT
                        print('\033[31mDisplay fail,no such page.\033[0m')
                    else:
                        if num == 1:
                            # 字典切片
                            RESULT1 = {k: RESULT[k] for k in list(RESULT.keys())[:num * size]}
                        elif num > 1:
                            RESULT1 = {k: RESULT[k] for k in list(RESULT.keys())[(num - 1) * size:num * size]}
                        else:
                            RESULT1 = {}
                    for k, v in RESULT1.items():
                        try:
                            i = [k, v["age"], v["tel"], v["email"]]
                        except:
                            i = []
                        x.add_row(i)
                    print(x)
                elif action == "find" and len(info_list) == 2:
                    x = PrettyTable(["姓名", "年龄", "电话", "邮箱"])
                    username = info_list[1]
                    try:
                        i = []
                        i.append(username)
                        i.extend(RESULT[username].values())
                    except:
                        i = []
                    x.add_row(i)
                    print(x)
                elif action == "save" and len(info_list) == 1:
                    fd = open("51reboot.txt", 'w')
                    try:
                        fd.write(json.dumps(RESULT))
                    except Exception as e:
                        print('\033[31mWrite file fail,errmsg: {}.\033[0m'.format(e))
                    finally:
                        fd.close()
                elif action == "load" and len(info_list) == 1:
                    fd = open("51reboot.txt", 'r')
                    try:
                        RESULT = json.loads(fd.read())
                    except Exception as e:
                        print('\033[31mRead file fail,errmsg: {}.\033[0m'.format(e))
                    finally:
                        fd.close()
                elif action == "exit":
                    os._exit(0)
                else:
                    print("\033[31minvalid action \033[0m")
            except KeyboardInterrupt as e:
                print("\033[1;31m兄弟按Ctrl + C是不对的,真想退出请用exit\033[0m")
    else:
        print('\033[31musername or password error,剩余{}次 \033[0m'.format(6-INIT_FAIL_CNT))
        #print("username or password error")
        INIT_FAIL_CNT += 1
print("\033[31m Input {} failed,Game Over.\033[0m".format(MAX_FAIL_CNT))