"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 dict          # dict
    3.5 搜 find          # find monkey
    3.6 保存 save
    3.7 加载 load
    3.8 分页 display    # display page 1 pagesize 5
3. 格式化输出
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
USERINFO = ("dingsc", "123456")
FILENAME = "51reboot.txt"

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
                field = {}
                field["name"] = info_list[1]
                field["age"] = info_list[2]
                field["tel"] = info_list[3]
                field["email"] = info_list[4]
                print(field)
                if username in RESULT:
                    print("User {} already exists.".format(username))
                else:
                    RESULT[username] = field
                    # print(RESULT)
                    # 打印结果信息
                    print("Add {} succ.".format(RESULT[username]))

            elif action == "delete":

                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                username = info_list[1]
                delete_flag = False
                if username in RESULT:
                    RESULT.pop(username)
                    print("\033[0;31;1m[Debug] {} {}.\033[0m".format(cur_time, info))
                    delete_flag = True
                if not delete_flag:
                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))

            elif action == "update":

                # update dingsc set age = 20

                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                username = info_list[1]

                where = info_list[2]

                field = info_list[3]

                field_value = info_list[-1]

                fuhao = info_list[-2]

                if where != "set" or fuhao != "=":
                    print("\033[0;31;1m[Debug] {} update method error.\033[0m".format(cur_time))

                if username in RESULT:

                    if field == "age":

                        RESULT[username]["age"] = field_value

                        print("\033[0;31;1m[Debug] {} update {} success.\033[0m".format(cur_time, username))

                    elif field == "tel":

                        RESULT[username]["tel"] = field_value

                        print("\033[0;31;1m[Debug] {} update {} success.\033[0m".format(cur_time, username))

                    elif field == "email":

                        RESULT[username]["email"] = field_value

                        print("\033[0;31;1m[Debug] {} update {} success.\033[0m".format(cur_time, username))

                    else:

                        print("\033[0;31;1m[Debug] {} update field {} not exists.\033[0m".format(cur_time, field))

                else:

                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))

            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]

                # print(RESULT)
                # for k, v in RESULT.items():
                #     xtb.add_row([k, v.get("age"), v.get("tel"), v.get("email")])
                # print(xtb)
                for k, v in RESULT.items():
                    xtb.add_row([k, v.get("age"), v.get("tel"), v.get("email")])
                print(xtb)

            elif action == "find":
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                username = info_list[1]
                find_flag = False
                if username in RESULT:
                    xtb.add_row([RESULT[username].get("name"), RESULT[username].get("age"), RESULT[username].get("tel"),
                                 RESULT[username].get("email")])
                    print(xtb)
                    find_flag = True
                if not find_flag:
                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))

            elif action == "save":
                fd = open(FILENAME, 'w')
                fd.write(json.dumps(RESULT))
                fd.close()
                print("\033[0;31;1m[Debug] save file:{} success.\033[0m".format(FILENAME))
            elif action == "load":
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                fd = open(FILENAME, 'r')
                data = fd.read()
                RESULT = json.loads(data)
                fd.close()
                #print(RESULT)
                for k, v in RESULT.items():
                    xtb.add_row([k, v.get("age"), v.get("tel"), v.get("email")])
                print(xtb)
            # dispaly page 2 pagesize 5
            # default = 5

            elif action == "display":
                # display page 1 pagesize 5
                # default = 5
                try:
                    result = []
                    xtb = PrettyTable()
                    xtb.field_names = ["username", "age", "tel", "email"]
                    page = int(info_list[2])
                    pagesize = int(info_list[-1])
                    start = (page - 1) * pagesize
                    end = page * pagesize

                    for k, v in RESULT.items():
                        result.append([k, v.get("age"), v.get("tel"), v.get("email")])
                    if start < len(result):
                        n = 0
                        for i in result[start:end]:
                            xtb.add_row(i)
                            n += 1
                        print(xtb)
                        print("\033[0;31;1mdispaly page {} pagesize {}\033[0m".format(page, n))
                    else:
                        print("\033[0;31;1m[Debug] {} too many.\033[0m".format(start))
                except IndexError:
                    print("你的分页输入有错误examp:display page 1 pagesize 5")
                except Exception as e:
                    print(e)
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        print("username or password error.")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
