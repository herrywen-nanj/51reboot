'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add
    3.2 删 delete
    3.3 改 update
    3.4 查 list
    3.5 搜 find
3. 格式化输出
'''

# 标准模块
import sys
import json
import datetime
from prettytable import PrettyTable

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot","123456")
FILENAME = "51reboot.txt"
LOGFILE = "51reboot.log"

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username：")
    password = input("Please input your password：")
    if username == USERINFO[0] and password == USERINFO[1]:
        login_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fd = open(LOGFILE,'a+')
        fd.write(login_time + " " + username + " login success.\n")
        fd.close()
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input your operation：")
            # add monkey 12 188*** monkey@51reboot.com
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在, 如果用户存在，提示用户已经存在，不存在添加
                add_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                username = info_list[1]
                field = {}
                field["name"] = info_list[1]
                field["age"] = info_list[2]
                field["tel"] = info_list[3]
                field["email"] = info_list[4]
                if username in RESULT:
                    print("\033[0;31;1m[Debug] user {} already exists.\033[0m".format(username))
                else:
                    RESULT[username] = field
                    fd = open(LOGFILE, 'a+')
                    fd.write(add_time + " add " +  username + " success.\n")
                    fd.close()
                    print("\033[0;31;1m[Debug] {} add {} success.\033[0m".format(add_time,username))
            elif action == "delete":
                del_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                username = info_list[1]
                delete_flag = False
                if username in RESULT:
                    RESULT.pop(username)
                    fd = open(LOGFILE, 'a+')
                    fd.write(del_time + " delete " + username + " success.\n")
                    fd.close()
                    print("\033[0;31;1m[Debug] {} {} success.\033[0m".format(del_time,info))
                    delete_flag = True
                if not delete_flag:
                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))
            elif action == "update":
                # update monkey set age = 20
                up_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                username = info_list[1]
                where = info_list[2]
                field = info_list[3]
                field_value = info_list[-1]
                mark = info_list[-2]
                if where != "set" or mark != "=":
                    print("\033[0;31;1m[Debug] {} update method error.\033[0m".format(up_time))
                if username in RESULT:
                    if field == "age":
                        RESULT[username]["age"] = field_value
                        fd = open(LOGFILE, 'a+')
                        fd.write(up_time + " update " + username + " age success.\n")
                        fd.close()
                        print("\033[0;31;1m[Debug] {} update {} age success.\033[0m".format(up_time, username))
                    elif field == "tel":
                        RESULT[username]["tel"] = field_value
                        fd = open(LOGFILE, 'a+')
                        fd.write(up_time + " update " + username + " tel success.\n")
                        fd.close()
                        print("\033[0;31;1m[Debug] {} update {} tel success.\033[0m".format(up_time, username))
                    elif field == "email":
                        RESULT[username]["email"] = field_value
                        fd = open(LOGFILE, 'a+')
                        fd.write(up_time + " update " + username + " email success.\n")
                        fd.close()
                        print("\033[0;31;1m[Debug] {} update {} email success.\033[0m".format(up_time, username))
                    else:
                        print("\033[0;31;1m[Debug] {} update field {} not exists.\033[0m".format(up_time,field))
                else:
                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))
            elif action == "list":
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                for k, v in RESULT.items():
                    xtb.add_row([k,v.get("age"),v.get("tel"),v.get("email")])
                print(xtb)
            elif action == "find":
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                username = info_list[1]
                find_flag = False
                if username in RESULT:
                    xtb.add_row([RESULT[username].get("name"),RESULT[username].get("age"),RESULT[username].get("tel"),RESULT[username].get("email")])
                    print(xtb)
                    find_flag = True
                if not find_flag:
                    print("\033[0;31;1m[Debug] user {} not found.\033[0m".format(username))
            elif action == "save":
                fd = open(FILENAME,'w')
                fd.write(json.dumps(RESULT))
                fd.close()
                print("\033[0;31;1m[Debug] save file:{} success.\033[0m".format(FILENAME))
            elif action == "load":
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                fd = open(FILENAME,'r')
                data = fd.read()
                RESULT = json.loads(data)
                fd.close()
                for k, v in RESULT.items():
                    xtb.add_row([k,v.get("age"),v.get("tel"),v.get("email")])
                print(xtb)
            elif action == "display":
                # display page 1 pagesize 5
                # default = 5
                result = []
                xtb = PrettyTable()
                xtb.field_names = ["username", "age", "tel", "email"]
                page = int(info_list[2])
                pagesize = 5
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
                    print("\033[0;31;1mdispaly page {} pagesize {}\033[0m".format(page,n))
                else:
                    print("\033[0;31;1m[Debug] {} too many.\033[0m".format(start))
            elif action == "exit":
                exit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                fd = open(LOGFILE, 'a+')
                fd.write(exit_time + " " + username + " exit success.\n")
                fd.close()
                sys.exit(0)
            else:
                print("\033[0;31;1minvalid action.\033[0m")
    else:
        print("\033[0;31;1musername or password error.\033[0m")
        INIT_FAIL_CNT += 1

print("\n\033[0;31;1mInput {} times failed,Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
