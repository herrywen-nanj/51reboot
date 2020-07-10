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
import json
import datetime
from prettytable import PrettyTable

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FILENAME = "51reboot.txt"
# FIELDS = ["username", "age", "tel", "email"]
# RESULT.append(FIELDS)


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

            # print(info)
            # print(info_list)
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                username = info_list[1]

                NAMES = []

                for i in RESULT:
                    name = i[0]
                    NAMES.append(name)

                if username in NAMES:
                    print("User {} already exists.".format(username))
                else:
                    RESULT.append(info_list[1:])

                    # RESULT.append(info_list[1:])
                    # 打印结果信息
                    print("Add {} succ.".format(info_list[1]))

            elif action == "delete":
                # .remove
                # delete
                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                username = info_list[1]
                delete_flag = False

                for i in RESULT:
                    name = i[0]
                    if name == username:
                        RESULT.remove(i)
                        print("[DEBUG] {} {}".format(cur_time, info))
                        delete_flag = True

                if not delete_flag:
                    print("User {} not found.".format(username))

            elif action == "update":
                # update monkey1 set age = 20

                username = info_list[1]
                where = info_list[2]
                fuhao = info_list[-2]

                if where != "set" or fuhao != "=":
                    print("Update method error.")
                    break

                NAMES = []

                for i in RESULT:
                    name = i[0]
                    NAMES.append(name)

                if username in NAMES:
                    idx = NAMES.index(username)
                    if info_list[3] == "age":
                        RESULT[idx][1] = info_list[-1]
                    elif info_list[3] == "tel":
                        RESULT[idx][2] = info_list[-1]
                    elif info_list[3] == "email":
                        RESULT[idx][3] = info_list[-1]
                else:
                    print("User {} not found.".format(username))

            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]

                # print(RESULT)
                for x in RESULT:
                    xtb.add_row(x)
                    # print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    # print()
                    # print("-" * 50)
                print(xtb)

            elif action == "find":
                # 查找
                username = info_list[1]
                find_flag = False

                for i in RESULT:
                    name = i[0]
                    if name == username:
                        print("{} {} {} {}".format(i[0], i[1], i[2], i[3]))
                        print()
                        find_flag = True

                if not find_flag:
                    print("User {} not found.".format(username))

            elif action == "save":
                pass
                # save
                # 1. 打开文件 file describe
                fd = open(FILENAME, 'w')

                # 2. 操作文件 read / write
                fd.write(json.dumps(RESULT))

                # 3. 关闭文件
                fd.close()

                print("Save file:{} succ.".format(FILENAME))

            elif action == "load":
                pass
                # load

                # 1. 打开文件 file describe
                fd = open(FILENAME, 'r')

                # 2. 操作文件 read / write
                data = fd.read()
                RESULT = json.loads(data)

                # 3. 关闭文件
                fd.close()


            elif action == "display":
                pass
                # dispaly page 2 pagesize 5
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
