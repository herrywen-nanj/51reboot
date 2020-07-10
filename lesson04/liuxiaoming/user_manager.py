import sys
import re
from prettytable import PrettyTable
import csv
import logging

re_email = re.compile(r'^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
RESULT = {"lxm0": {"age": "12", "tel": 13968775214, "email": "lxm0@qq.com"}}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "password")
F_CSV = "manager.csv"
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt = DATE_FORMAT ,filename="user_logs.log")


def check_user(username):
    names = []
    for i in RESULT:
        names.append(i)
    if username in names:
        return True
    return False

def check_type(age, tel, mail):
    if not age.isdigit():
        return False 
    if len(tel) != 11:
        return False
    if re_email.match(mail) is None:
        return False
    return True

def login(username, password):
    if username == USERINFO[0] and password == USERINFO[1]:
        logging.info('{}登入了系统'.format(username))
        return True
    else:
        return False

def find_user(username):
    if check_user(username):
        table = PrettyTable()
        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
        table.add_row([username, RESULT[username]["age"], RESULT[username]["tel"], RESULT[username]["email"]])
        print(table)
    else:
        print("\033[31m{}不存在！\033[0m".format(username))

def list_user():
    table = PrettyTable()
    for u in RESULT.keys():
        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
        table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
    print(table)

def add_user(info_list):
    if check_type(age=info_list[2], tel=info_list[3], mail=info_list[4]):
        if not check_user(info_list[1]):
            RESULT[info_list[1]] = {"age": info_list[2], "tel": info_list[3], "email": info_list[4]}
            print("\033[32m{}添加成功！\033[0m".format(info_list[1]))
        else:
            print("\033[31m{}已存在！\033[0m".format(info_list[1]))
    else:
        print("\033[31m请确定输入的格式！\033[0m")

def update_user(info_list):
    if check_user(info_list[1]):
        RESULT[info_list[1]][info_list[3]] = info_list[5]
        print("\033[32m{}修改成功！\033[0m".format(info_list[1]))
    else:
        print("\033[31m{}不存在！\033[0m".format(username)) 

def delete_user(username):
    if check_user(username):
        del RESULT[username]
        print("\033[32m{}删除成功！\033[0m".format(username))
        logging.debug('删除了用户{}'.format(username))
    else:
        print("\033[31m{}不存在！\033[0m".format(username))
        
def save_csv():
    with open(F_CSV, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect="excel")
        csvwriter.writerow(["用户名", "年龄", "电话", "邮件"])
        for u in RESULT.keys():
            csvwriter.writerow([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
    print("\033[32m数据保存在{}中！\033[0m".format(F_CSV))

def load():
    csv_file = csv.reader(open(F_CSV, 'r'))
    for u in csv_file:
        if u[0] == "用户名":
            continue
        else:
            RESULT[u[0]] = {"age": u[1], "tel": u[2], "email": u[3]}
    print("\033[32m成功从{}获取到数据！\033[0m".format(F_CSV))

def display():
    page = int(info_list[2])
    pagesize = int(info_list[4])
    data = list(RESULT.keys())
    table = PrettyTable()
    if (page-1)*pagesize <= len(data):
        for u in data[(page-1)*pagesize:page*pagesize]:
            table.field_names = ["用户名", "年龄", "电话", "邮箱"]
            table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
    else:
        for u in data[0:pagesize]:
            table.field_names = ["用户名", "年龄", "电话", "邮箱"]
            table.add_row([u, RESULT[u]["age"], RESULT[u]["tel"], RESULT[u]["email"]])
    print(table)

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("请输入登录用户名: ")
    password = input("请输入密码: ")
    if login(username, password):
        while True:
            info = input("请输入你的操作:")
            info_list = info.split()
            action = info_list[0]
            if action == "find":
                try:
                    find_user(info_list[1])
                except Exception as e:
                    print(e)
            elif action == "add":
                try:
                    add_user(info_list)
                except Exception as e:
                    print(e)
            elif action == "update":
                try:
                    update_user(info_list)
                except Exception as e:
                    print(e)
            elif action == "delete":
                try:
                    delete_user(info_list[1])
                except Exception as e:
                    print(e)
            elif action == "list":
                if len(RESULT) == 0:
                    print("\033[31m没有用户数据.\033[0m")
                else:
                    list_user()
            elif action == "save":
                try:
                    save_csv()
                except:
                    print("\033[31m未知错误,没有保存成功！\033[0m")
            elif action == "load":
                try:
                    load()
                except IOError:
                    print("\033[31m{}不存在！\033[0m".format(F_CSV))
            elif action == "display":
                display()
            elif action == "exit":
                sys.exit(0)
    else:
        print("\033[1;31m用户名或者密码错误.\033[0m")
        INIT_FAIL_CNT += 1
print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")