"""
用户管理系统
=================V1===================
1、登录认证；
2、增删改查和搜索
    3.1 增 add      # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete   # delete mobkey
    3.3 改 update   # update monkey set age = 18
    3.4 查 list     # list
    3.5 搜 find     # find monkey
3、格式化输出
===================V2=================
1. 数据结构：列表 -> 字典；
2. 分页 display page 1 pagesize 5
3. 文件持久化
4. 异常处理
5. PrettyTable 优雅的格式化输出
6. 扩展：导出csv(可写可不写)
"""

# 标准模块
import sys
import json
import datetime
from prettytable import PrettyTable


# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ('username', 'age', 'tel', 'email')
FILENAME = "51reboot.txt"
cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

helpinfo = '''{}
add         : add monkey 12 132xxx monkey@51reboot.com
update      : udpate monkey set age = 20
list        : list
find        : find monkey
display     : display page 2 page_size 3
doc         : show help
exit        : quit
save        : save as 51reboot.txt
load        : load 51reboot.txt
{}
'''.format('=' * 70, '=' * 70)

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    name = input("Please input your name:")
    password = input("Please input your password:")
    if name == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作，否则输入exit退出
        while True:
            # 业务逻辑
            # print(helpinfo)
            info = input("Please input your operation:").strip()  # 去前后空格
            # string -> list
            info_list = info.split()
            if len(info) == 0: # 如果为空， 则提示
                print("Input info invalid, Please input again.")
                continue
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在，如果用户存在，提示用户已经存在，不再添加
                username = info_list[1]
                if username in RESULT:
                    # print("User {} already exists.".format(username))
                    print("[DEBUG] {} User {} already exists..".format(cur_time, username))
                    continue
                else:
                    RESULT[username] = dict(zip(FIELDS, info_list[1:]))
                    # print("Add {} succ.".format(username))
                    print("[INFO] {} Add User {} succ.".format(cur_time, username))

                # NAMES = []
                # for i in RESULT:
                #     name = i[0]
                #     NAMES.append(name)
                #
                # if username in NAMES:
                #     print("User {} already exists".format(username))
                # else:
                #     RESULT.append(info_list[1:])
                #     print("Add{} success".format(username))

            elif action == "delete":
                # delete monkey
                username = info_list[1]

                delete_flag = RESULT.pop(username, None)
                if delete_flag == None:
                    # print("User {} not found.".format(username))
                    print("[DEBUG] {} User {} not found".format(cur_time, username))
                else:
                    # print("User {} Delete succ.".format(username))
                    print("[INFO] {} {}.".format(cur_time, info))

                # delete_flag = False
                # for x in RESULT:
                #     name = x[0]
                #     if name == username:
                #         RESULT.remove(x)
                #         print("[DEBUG] {} {}.".format(cur_time, info))
                #         delete_flag = True
                # if not delete_flag:
                #     print("USER {} not found".format(username))


            elif action == "update":
                # update monkey set age = 20
                username = info_list[1]
                where = info_list[2]
                fuhao = info_list[-2]
                if where != "set" or fuhao != "=":
                    print("[DEBUG] {} Update method error!".format(cur_time))
                    break

                update_field = info_list[-3]
                update_value = info_list[-1]

                if username in RESULT:
                    if update_field in RESULT[username]:
                        RESULT[username][update_field] = update_value
                        print("[INFO] {} Username {} update succ.".format(cur_time, username))
                    else:
                        print("[DEBUG] {} field: {} invalid.".format(cur_time, update_field))
                        continue
                else:
                    print("[DEBUG] {} username: {} not found.".format(cur_time, username))

                # NAMES = []
                #
                # for i in RESULT:
                #     name = i[0]
                #     NAMES.append(name)
                # if username in NAMES:
                #     idx = NAMES.index(username)
                #     if info_list[3] == "age":
                #         RESULT[idx][1] = info_list[-1]
                #     elif info_list[3] == "tel":
                #         RESULT[idx][2] = info_list[-1]
                #     elif info_list[3] == "email":
                #         RESULT[idx][3] == info_list[-1]
                # else:
                #     print("User {} not found.".format(username))

            elif action == "list":
                xtb = PrettyTable()
                xtb.field_names = FIELDS
                for k, v in RESULT.items():
                    xtb.add_row(v.values())
                print(xtb)

                # xtb = PrettyTable()
                # FIELDS = ['username', 'age', 'tel', 'email']
                # xtb.field_names = ['username', 'age', 'tel', 'email']
                # for x in RESULT:
                #     xtb.add_row([x[0], x[1], x[2], x[3]])
                # print(xtb)

                # for x in RESULT:
                #     print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                #     print()
                #     print("-" * 50)

            elif action == "find":
                username = info_list[1]
                userinfo = RESULT.get(username, None)
                if userinfo == None:
                    print("[DEBUG] {} User {} not found.".format(cur_time, username))
                else:
                    xtb = PrettyTable()
                    xtb.field_names = FIELDS
                    xtb.add_row(userinfo.values())
                    print(xtb)

                # find_flag = False
                # for x in RESULT:
                #     if x[0] == username:
                #         print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                #         print()
                #         print("-" * 50)
                #         find_flag = True
                # if not find_flag:
                #     print("USER {} not found".format(username))

            elif action == "save":
                # 1. 打开文件
                fd = open(FILENAME, 'w')

                # 2. 操作文件  write
                fd.write(json.dumps(RESULT))

                # 3. 关闭文件
                fd.close()

                print("Save file:{} succ.".format(FILENAME))

            elif action == "load":
                try:
                    # 1、打开文件
                    fd = open(FILENAME, 'r')
                except Exception as e:
                    print("Read file fail, filename: {} not found.\n".format(FILENAME))
                    continue
                # 2. 操作文件 read
                data = fd.read()
                RESULT = json.loads(data)
                # 3. 关闭文件
                fd.close()
                print("Load file:{} succ.".format(FILENAME))

            elif action == "display":
                # display page 2 pagesize 5
                # default = 5
                pagesize = 5
                # display page 2
                if len(info_list[1:]) == 2:
                    if info_list[1] == "page":
                        pagesize = 5
                    else:
                        print("Display info invalid. Please input again.")
                        continue
                # display page 2 pagesize 5
                else:
                    if info_list[1] == "page" and info_list[3] == "pagesize":
                        pagesize = int(info_list[-1])
                    else:
                        print("Display info invalid. Please input again.")
                        continue

                page = int(info_list[2]) - 1
                data = []
                for k, v in RESULT.items():
                    data.append(v.values())

                # start, end sep
                start = page * pagesize
                end = start + pagesize
                print("Start: {}, End:{}".format(start, end))

                xtb = PrettyTable()
                xtb.field_names = FIELDS
                for userinfo in data[start:end]:
                    xtb.add_row(userinfo)
                print(xtb)

            elif action == "doc":
                print(helpinfo)
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[31m invalid action\033[0m")
    else:
        # 带颜色
        print("\033[31m username or password error.\033[0m")
        INIT_FAIL_CNT += 1

print("\033[31m \nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
