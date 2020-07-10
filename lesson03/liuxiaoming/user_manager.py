import sys
import re
from prettytable import PrettyTable
import csv

re_email = re.compile(r'^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
RESULT = {"lxm0": {"age": "12", "tel": 13968775214, "email": "lxm0@qq.com"}}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "admin")
F_CSV = "manager.csv"

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("请输入登录用户名: ")
    password = input("请输入密码: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        while True:
            info = input("请输入你的操作:")
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                username = info_list[1]
                names = []
                for i in RESULT:
                    name = i[0]
                    names.append(name)
                if username not in names:
                    RESULT[username] = {"age": info_list[2], "tel": info_list[3], "email": info_list[4]}
                    print("\033[32m{}添加成功！\033[0m".format(username))
                else:
                    print("\033[31m{}已经存在！\033[0m".format(username))
            elif action == "delete":
                username = info_list[1]
                if username in RESULT:
                    del RESULT[username]
                    print("\033[32m{}删除成功！\033[0m".format(username))
                else:
                    print("\033[31m{}不存在！\033[0m".format(username))
            elif action == "update":
                username = info_list[1]
                i_value = info_list[5]
                i_key = info_list[3]
                if username in RESULT:
                    RESULT[username][i_key] = i_value
                    print("\033[32m{}修改成功！\033[0m".format(username))
                    print(RESULT)
                else:
                    print("\033[31m{}不存在！\033[0m".format(username))
            elif action == "find":
                username = info_list[1]
                if username in RESULT:
                    table = PrettyTable()
                    table.field_names = ["用户名", "年龄", "电话", "邮箱"]
                    table.add_row([username, RESULT[username]["age"], RESULT[username]["tel"], RESULT[username]["email"]])
                    print(table)
                else:
                    print("\033[31m{}不存在！\033[0m".format(username))
            elif action == "list":
                if len(RESULT) == 0:
                    print("没有用户数据.")
                else:
                    table = PrettyTable()
                    for u in RESULT.keys():
                        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
                        table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
                    print(table)
            elif action == "save":
                with open(F_CSV, 'w', newline='') as datacsv:
                    csvwriter = csv.writer(datacsv, dialect="excel")
                    csvwriter.writerow(["用户名", "年龄", "电话", "邮件"])
                    for u in RESULT.keys():
                        csvwriter.writerow([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
                print("\033[32m数据保存在{}中！\033[0m".format(F_CSV))
            elif action == "load":
                try:
                    csv_file = csv.reader(open(F_CSV, 'r'))
                    for u in csv_file:
                        if u[0] == "用户名":
                            continue
                        else:
                            RESULT[u[0]] = {"age": u[1], "tel": u[2], "email": u[3]}
                    print("\033[32m成功从{}获取到数据！\033[0m".format(F_CSV))
                except IOError:
                    print("\033[31m{}不存在！\033[0m".format(F_CSV))
            elif action == "display":
                page = int(info_list[2])
                pagesize = int(info_list[4])
                data = list(RESULT.keys())
                table = PrettyTable()
                if (page-1)*pagesize <= len(data):
                    for u in data[(page-1)*pagesize:page*pagesize]:
                        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
                        table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
                else:
                    #如果现有数据只能生成一页分页
                    for u in data[0:pagesize]:
                        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
                        table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
                print(table)
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        print("用户名或者密码错误")
        INIT_FAIL_CNT += 1
print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")




