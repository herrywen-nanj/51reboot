import sys
import logging

import csv
from prettytable import PrettyTable

from operate import db_add, db_find, db_delete, db_update, db_list

F_CSV = "manager.csv"
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "password")
LOG_FORMAT = "%(asctime)s %(name)s %(levelname)s %(pathname)s %(message)s "
DATE_FORMAT = '%Y-%m-%d  %H:%M:%S %a '
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt = DATE_FORMAT ,filename="user_logs.log")

def login(username, password):
    if username == USERINFO[0] and password == USERINFO[1]:
        logging.info('{}登入了系统'.format(username))
        return True
    else:
        return False

def add_user(info_list):
    if db_find(info_list):
        print("\033[31m{}已存在！\033[0m".format(info_list[1]))
    else:
        db_add(info_list)
        print("\033[32m{}添加成功！\033[0m".format(info_list[1]))
        logging.debug('添加了用户{}'.format(info_list[1]))

def update_user(info_list):
    if not db_find(info_list):
        print("\033[31m{}不存在！\033[0m".format(info_list[1]))
    else:
        db_update(info_list)
        logging.debug('修改了用户{}'.format(info_list[1]))
        print("\033[32m{}修改成功！\033[0m".format(info_list[1]))

def delete_user(info_list):
    if not db_find(info_list):
        print("\033[31m{}不存在！\033[0m".format(info_list[1]))
    else:
        db_delete(info_list)
        logging.debug('删除了用户{}'.format(info_list[1]))
        print("\033[32m{}删除成功！\033[0m".format(info_list[1]))

def find_user(info_list):
    results = db_find(info_list)
    if db_find(info_list):
        table = PrettyTable()
        table.field_names = ["用户名", "年龄", "电话", "邮箱"]
        table.add_row([results[0][0], results[0][1], results[0][2], results[0][3]])
        print(table)
    else:
        print('查找的用户不存在')

def list_user():
    results = db_list()
    table = PrettyTable()
    if db_list():
        for u in results:
            table.field_names = ["用户名", "年龄", "电话", "邮箱"]
            table.add_row([u[0], u[1], u[2], u[3]])
        print(table)
    else:
        print("暂时没有用户存在")

def save_csv():
    results = db_list()
    with open(F_CSV, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect="excel")
        csvwriter.writerow(["用户名", "年龄", "电话", "邮件"])
        for u in results:
            csvwriter.writerow([results[0][0], results[0][1], results[0][2], results[0][3]])
    print("\033[32m数据保存在{}中！\033[0m".format(F_CSV))

def display(info_list):
    page = int(info_list[2])
    pagesize = int(info_list[4])
    data = db_list()
    table = PrettyTable()
    if (page-1)*pagesize <= len(data):
        for u in data[(page-1)*pagesize:page*pagesize]:
            table.field_names = ["用户名", "年龄", "电话", "邮箱"]
            table.add_row([u[0], u[1], u[2], u[3]])
    else:
        for u in data[0:pagesize]:
            table.field_names = ["用户名", "年龄", "电话", "邮箱"]
            table.add_row([u[0], u[1], u[2], u[3]])

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("请输入登录用户名: ")
    password = input("请输入密码: ")
    if login(username, password):
        while True:
            info = input("请输入你的操作:")
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                add_user(info_list)
            elif action == "find":
                find_user(info_list)
            elif action == "list":
                list_user()
            elif action == "delete":
                delete_user(info_list)
            elif action == "update":
                update_user(info_list)
            elif action == "save":
                save_csv()
            elif action == "display":
                display(info_list)
            elif action == "exit":
                sys.exit(0)
            else:
                print("未知操作.")
    else:
        print("\033[1;31m用户名或者密码错误.\033[0m")
        INIT_FAIL_CNT += 1
print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")