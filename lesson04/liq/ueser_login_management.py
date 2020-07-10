import csv
import logging
import time
from prettytable import PrettyTable

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

user_info = ("user","123456")
init_fail_cnt = 0
max_fail_cnt = 6
file_name = "51reboot.csv"
RESULT = {}
header = ['name','age','phone','email']


def info_log(message):
    today = time.strftime("%Y%m%d%H%M")
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='info' + today + '.log',
                        )
    logging.info(message)
def error_log(message):
    today = time.strftime("%Y%m%d%H%M")
    logging.basicConfig(level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='error' + today + '.log',
                        )
    logging.error(message)

def add_user(info_list):
    if len(info_list) == 5:
        if info_list[1] not in RESULT:
            content = {"age": info_list[2], "phone": info_list[3], "email": info_list[4]}
            RESULT[info_list[1]] = content
            info_log("Added {} user successfully".format(info_list[1]))
        else:
            error_log("Added {} user successfully".format(info_list[1]))


def delete():
    if len(info_list) == 2:
        user_name = info_list[1]
        if user_name in RESULT:
            del RESULT[user_name]
            info_log('Delete {} user successfully'.format(user_name))
        else:
            error_log('Delete {} failed，user is not exists'.format(user_name))

def update():
    username = info_list[1]
    i_value = info_list[5]
    i_key = info_list[3]
    if username in RESULT:
        RESULT[username][i_key] = i_value
        info_log('Update {} user successfully!'.format(username))
    else:
        error_log('Update {} user successfully!'.format(username))

def find():
    if len(info_list) == 2:
        user_name = info_list[1]
        if user_name in RESULT:
            table = PrettyTable()
            table.field_names = ['name','age','phone','email']
            table.add_row([user_name, RESULT[user_name]["age"], RESULT[user_name]["phone"], RESULT[user_name]["email"]])
            info_log(table)
        else:
            error_log('{} user is not exists！'.format(user_name))

def save():
    with open(file_name, 'w',newline='') as f:
        csv_writer = csv.writer(f,dialect='excel')
        csv_writer.writerow(header)
        for x in RESULT.keys():
            csv_writer.writerow([x, RESULT[x]['age'], RESULT[x]['phone'], RESULT[x]['email']])
        info_log('datas is saved in {} ！'.format(file_name))

def load():
    try:
        csv_file = csv.reader(open(file_name,'r'))
        for x in csv_file:
            if x[0] == 'name':
                continue
            else:
                RESULT[x[0]] = {'age':x[1],'phone':x[2],'email':x[3]}
        info_log('load datas from {} successfully！'.format(file_name))
    except Exception as e:
        error_log(e)

def lists():
    if len(RESULT) == 0:
        info_log('List data shows exceptions')
    else:
        table = PrettyTable()
        for u in RESULT.keys():
            table.field_names = ['name','age','phone','email']
            table.add_row([u, RESULT[u]["age"], RESULT[u]["phone"], RESULT[u]["email"]])
        print(table)

def display():
    page = int(info_list[2])
    pagesize = int(info_list[4])
    data = list(RESULT.keys())
    table = PrettyTable()
    if (page - 1) * pagesize <= len(data):
        for x in data[(page - 1) * pagesize:page * pagesize]:
            table.field_names = ['name','age','phone','email']
            table.add_row([x, RESULT[x]['age'], RESULT[x]['phone'],RESULT[x]['email']])
    else:
        # 如果现有数据只能生成一页分页
        for x in data[0:pagesize]:
            table.field_names = ['name','age','phone','email']
            table.add_row([x, RESULT[x]['age'], RESULT[x]['phone'],RESULT[x]['email']])
    print(table)

if __name__ == '__main__':

    while init_fail_cnt < max_fail_cnt:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == user_info[0] and password == user_info[1]:
            while True:
                info = input("Please input your operation:")
                info_list = info.split()
                action = info_list[0]
                if action == "add":
                    add_user(info_list)
                elif action == "delete":
                    delete()
                elif action == "update":
                    update()
                elif action == "find":
                    find()
                elif action == "load":
                    load()
                elif action == "list":
                    lists()
                elif action == "save":
                    save()
                elif action == "display":
                    display()
                elif action == "exit":
                    print("exit system")
                    exit(0)

        else:
            print("username or password error.")
            init_fail_cnt += 1

    print("\nInput {} failed, Terminal will exit.".format(max_fail_cnt))