"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys
import os
import json
import datetime
from prettytable import PrettyTable

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("liq", "liq")
FILENAME = "51reboot.txt"
# FIELDS = ["username", "age", "tel", "email"]
# RESULT.append(FIELDS)

def load():
    # load
    if os.path.exists(FILENAME):
        try:
            # 1. 打开文件 file describe
            fd = open(FILENAME, 'r')

            # 2. 操作文件 read / write
            data = fd.read()
            RESULT = json.loads(data)
        except Exception as f:
            print(f)
        else:
            # 3. 关闭文件
            fd.close()
    return RESULT

if __name__ in  '__main__':
    if os.path.exists(FILENAME):
        RESULT_LOAD = load()
    else:
        RESULT_LOAD = {}
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            # 如果输入无效的操作，则反复操作, 否则输入exit退出
            while True:
                # 业务逻辑
                info = input("Please input your operation: ")
                # add monkey1 12 13987654321 monkey@51reboot.com
                # string -> list
                info_list = info.split()
                action = info_list[0]
                if action == "add":
                    # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                    username = info_list[1]

                    if username not in RESULT_LOAD.keys():
                        RESULT_LOAD[username] = {'age':info_list[2],'tel':info_list[3],'email':info_list[4]}
                    else:
                        print("User {} already exists.".format(username))

                    # 打印结果信息
                    print("Add {} succ.".format(info_list[1]))
                    try:
                        # 1. 打开文件 file describe
                        fd = open(FILENAME, 'w')
                        # 2. 操作文件 read / write
                        fd.write(json.dumps(RESULT_LOAD))
                    except Exception as p:
                        print(p)
                    finally:
                        # 3. 关闭文件
                        fd.close()

                elif action == "delete":
                    # load
                    try:
                        # 1. 打开文件 file describe
                        fd = open(FILENAME, 'r')

                        # 2. 操作文件 read / write
                        data = fd.read()
                        RESULT_LOAD = json.loads(data)
                    except Exception as f:
                        print(f)
                    finally:
                        # 3. 关闭文件
                        fd.close()

                    # .remove
                    # delete
                    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    username = info_list[1]
                    delete_flag = False

                    if username in RESULT_LOAD.keys():
                        RESULT_LOAD.pop(username)
                        delete_flag = True

                    if not delete_flag:
                        print("User {} not found.".format(username))

                    try:
                        # 1. 打开文件 file describe
                        fd = open(FILENAME, 'w')
                        # 2. 操作文件 read / write
                        fd.write(json.dumps(RESULT_LOAD))
                    except Exception as p:
                        print(p)
                    finally:
                        # 3. 关闭文件
                        fd.close()

                elif action == "update":
                    # update monkey1 set age = 20

                    username = info_list[1]
                    where = info_list[2]
                    fuhao = info_list[-2]

                    if where != "set" or fuhao != "=":
                        print("Update method error.")
                        break

                    if username in RESULT_LOAD.keys():
                        if info_list[3] == "age":
                            RESULT_LOAD[username]["age"] = info_list[-1]
                        elif info_list[3] == "tel":
                            RESULT_LOAD[username]["tel"] = info_list[-1]
                        elif info_list[3] == "email":
                            RESULT_LOAD[username]["email"] = info_list[-1]
                    else:
                        print("User {} not found.".format(username))

                    try:
                        # 1. 打开文件 file describe
                        fd = open(FILENAME, 'w')
                        # 2. 操作文件 read / write
                        fd.write(json.dumps(RESULT_LOAD))
                    except Exception as p:
                        print(p)
                    finally:
                        # 3. 关闭文件
                        fd.close()

                elif action == "list":
                    # 如果没有一条记录， 那么提示为空
                    xtb = PrettyTable()
                    xtb.field_names = ["username", "age", "tel", "email"]

                    # print(RESULT)
                    for x in RESULT_LOAD:
                        xtb.add_row([x,RESULT_LOAD[x]['age'],RESULT_LOAD[x]['tel'],RESULT_LOAD[x]['email']])
                    print(xtb)

                elif action == "find":
                    # 查找
                    username = info_list[1]
                    find_flag = False

                    xtb = PrettyTable()
                    for i in RESULT_LOAD.keys():
                        name = i
                        if name == username:
                            xtb.field_names = ["username", "age", "tel", "email"]
                            xtb.add_row([i, RESULT_LOAD[i]['age'], RESULT_LOAD[i]['tel'], RESULT_LOAD[i]['email']])
                            find_flag = True
                            print(xtb)

                    if not find_flag:
                        print("User {} not found.".format(username))

                elif action == "load":
                    # load
                    if os.path.exists(FILENAME):
                        try:
                            # 1. 打开文件 file describe
                            fd = open(FILENAME, 'r')

                            # 2. 操作文件 read / write
                            data = fd.read()
                            RESULT_LOAD = json.loads(data)
                        except Exception as f:
                            print(f)
                        finally:
                            # 3. 关闭文件
                            fd.close()
                    else:
                        print('File does not exist')

                elif action == "display":
                    pass
                    # paging = []
                    # star_paging = 0
                    # end_paging = 5
                    # xtb = PrettyTable()
                    # xtb.field_names = ["username", "age", "tel", "email"]
                    # for x in range(0,len(RESULT_LOAD.keys())):
                    #     print(list(RESULT_LOAD.keys())[x])
                    #     xtb.add_row([x, RESULT_LOAD[x]['age'], RESULT_LOAD[x]['tel'], RESULT_LOAD[x]['email']])
                    # dispaly page 1 pagesize 5
                    # default = 5
                elif action == "exit":
                    sys.exit(0)
                else:
                    print("invalid action.")
        else:
            # 带颜色
            print("username or password error.")
            INIT_FAIL_CNT += 1

    print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
