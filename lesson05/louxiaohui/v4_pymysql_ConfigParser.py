#!/usr/bin/env python
# **********************************************************
# * Author        : xoyabc
# * Email         : lxh1031138448@gmail.com
# * Last modified : 2019-06-19 08:33
# * Filename      : v3_csv_log_func.py
# * Description   : 
# **********************************************************
'''
1. 登录认证；
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
    2.6 分页显示         # display page 1 pagesize 5
3. 格式化输出
4. 数据结构：列表 -> 字典；
5. 文件持久化,数据存到文件中
6. 异常处理
7. PrettyTable 优雅的格式化输出
8. 扩展：导出csv(可写可不写)
9. 支持配置文件管理方式 
10. 存储方式 由文件 改成 数据库
'''

# 标准模块
import os
import sys
import json
import csv
from prettytable import PrettyTable
import logging, os, re
from logging.handlers import TimedRotatingFileHandler
import utils

BASEPATH = os.path.realpath(os.path.dirname(__file__))
LOGPATH = BASEPATH + os.sep + 'log'
LOGFILE = LOGPATH + os.sep + 'app.log'
os.makedirs(LOGPATH,mode=0o644,exist_ok=True)

# 定义变量
RESULT = {}
TITLE = ['name', 'age', 'tel', 'email']
USERINFO = ("admin", "123456")
csv_file = 'user_info.csv'
user_info_file = "user_info.txt"


def save_log():
    log_fmt = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        # create formatter
    formatter = logging.Formatter(log_fmt)
    formatter.datefmt = '%d/%b/%Y %H:%M:%S'
        
    # create log_file_handler
    log_file_handler = TimedRotatingFileHandler(
                       filename=LOGFILE, when="midnight", interval=1, backupCount=30)
    log_file_handler.suffix = "%Y-%m-%d.log"
    log_file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    log_file_handler.setFormatter(formatter)
    log_file_handler.setLevel(logging.DEBUG)
    # create logger named log 
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    # add log_file_handler to logger
    log.addHandler(log_file_handler)
    return log


log = save_log()


# print warning message
def print_warn(content):
    print("\n\033[1;31m {} \033[0m" .format(content))


# print info message
def print_info(content):
    print("\n\033[1;32m {} \033[0m" .format(content))


# load the previous user data from Mysql
def load():
    global RESULT
    sql = '''select username,age,tel,email from users;'''
    db_user_info, res = utils.select(sql)
    if res:
        for i in db_user_info:
            name = i[0]
            RESULT[name] = dict(zip(TITLE, i))
        return RESULT, True
    else:
        err_msg = "There is no user exist, load failed."
        return err_msg, False


def store_to_sql():
    sql = '''select username,age,tel,email from users;'''
    db_user_info, res = utils.select(sql)
    if res:
        INIT_RESULT = { i[0]:dict(zip(TITLE, i)) for i in db_user_info }
    for k, v in RESULT.items():
        if k not in INIT_RESULT:
            sql_new_user = '''insert into users(username, age, tel, email) values('{name}', {age}, '{tel}', '{email}');''' .format(**RESULT[k])
            msg, res = utils.insert(sql_new_user)
            log.info(msg) if res else log.error(msg)
            log.debug(sql_new_user)
        else:
            print ("username: {} already exist." .format(k))


# store the user info to file
def store_to_file(**DICT):
    fd = open(user_info_file, 'w')
    try:
        fd.write(json.dumps(DICT))
    except Exception as e:
        err_msg = "Write error,errmsg: {}" .format(e)
        return err_msg, False
    finally:
        fd.close()
    ok_msg = "save to {} succeed" .format(user_info_file)
    return ok_msg, True


# write to csv
def write_to_csv(fnames,user_dict):
    #print (fnames)
    #print (user_dict)
    user_dict = dict(sorted(user_dict.items(), key = lambda x: x[0])) 
    with open(csv_file, 'w') as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=fnames)  
        writer.writeheader() if len(user_dict.keys()) > 0 else None
        for k, v in user_dict.items():
            #print (k, v)
            writer.writerow(v)
    ok_msg = "save to {} succeed" .format(csv_file)
    return ok_msg, True


def check_login(username,password):
    if username == USERINFO[0] and password == USERINFO[1]:
        log.debug('login succeed')
        return True
    else:
        log.debug('login failed')
        return False


def add_user(user_info):
    # check if input field is complete
    if len(user_info) < 4:
        return "you forget input one or more field.", False
    # add user if input field is complete
    else:
        name = user_info[0]
        # check if name is already added to the system
        if name in RESULT:
            err_msg = "{} is already added" .format(" ".join(user_info))
            return err_msg, False
        else:
            RESULT[name] = dict(zip(TITLE, user_info))
            ok_msg = "add '{}' succeed" .format(" ".join(user_info))
            return ok_msg, True


def del_user(user_info):
    name = user_info[0]
    # remove from RESULT if name exist
    if name in RESULT:
        try:
            del RESULT[name]
            ok_msg = "user '{}' has been deleted" .format(name)
            log.debug(ok_msg)
            store_to_file(**RESULT)
            return ok_msg, True
        except KeyError:
            err_msg = "user '{}' does not exist" .format(name)
            log.debug(err_msg)
            return err_msg, False


def update_user(user_info):
    name = user_info[0]
    if len(user_info) != 5:
        err_msg = "invalid update info"
        return err_msg ,False
    ele_key = user_info[2]
    ele_value = user_info[4]
    # check if name is already added to the system
    if name in RESULT:
        if ele_key in RESULT[name]:
            RESULT[name][ele_key] = ele_value
            ok_msg = "update {} of {} succeed" .format(ele_key, name)
            store_to_file(**RESULT)
            print (RESULT)
            return ok_msg, True
        else:
            err_msg = "invalid update field: {}" .format(ele_key)
            return err_msg, False
    else:
        err_msg = "user '{}' does not exist" .format(name)
        return err_msg, False


def list_user():
     #print (RESULT)
     xoy = PrettyTable()
     xoy.field_names = TITLE
     if len(RESULT.keys()) > 0:    
         for k, v in RESULT.items(): 
             xoy.add_row(v.values())
     else:
         err_msg = "There is no user in system"
         return err_msg, False
     return xoy, True


def find_user(user_info):
    if len(user_info) < 1:
        err_msg = "invalid input info, pls input again"
        return err_msg, False
    name = user_info[0]
    xoy = PrettyTable()
    xoy.field_names = TITLE
    if len(RESULT.keys()) > 0:    
        if name in RESULT.keys():
            info = RESULT.get(name).values()
            xoy.add_row(info)
        else:
            err_msg = "user not found in system"
            return err_msg, False
    else:
        err_msg = "There is no user in system"
        return err_msg, False
    return xoy, True


def display_user(user_info):
    xoy = PrettyTable()
    xoy.field_names = TITLE
    try:
        page_num = int(user_info[1])
        page_size = int(user_info[3])
    except Exception as e:
        err_msg = "you forget input one or more field"
        return err_msg, False
    else:
        RESULT_LIST = list(RESULT.values()) 
        RESULT_LIST_LEN = len(RESULT_LIST)
        TOTAL_NUM = page_num * page_size
        if RESULT_LIST_LEN < TOTAL_NUM:    
            err_msg = "pagesize is out of range"
            return err_msg, False
        else:
            start_index = (page_num -1) * page_size
            end_index = page_num * page_size
            for x in RESULT_LIST[start_index:end_index]:
                xoy.add_row([x['name'], x['age'], x['tel'], x['email']])
            return xoy, True


def operation():
    while True:
        # 业务逻辑
        info = input("Please input the action and info: ")
        # string -> list
        info_list = info.split()
        # handle abnormal input,do not exit until input exit
        try:
            action = info_list[0]
        except IndexError:
            print("invalid input info,pls input again")
            continue
        # get the name and userinfo
        if len(info_list) > 1:
            user_info = info_list[1:]
        if action == "add":
           msg, res = add_user(user_info)
           print ("{}, status: {}" .format(msg, res))
        elif action == "save":
            store_to_sql()
            store_to_file(**RESULT)
            msg, res = write_to_csv(TITLE, RESULT)
            print ("{}, status: {}" .format(msg, res))
        elif action == "delete":
            msg, res = del_user(user_info)
            print ("{}, status: {}" .format(msg, res))
        elif action == "update":
            msg, res = update_user(user_info)
            print ("{}, status: {}" .format(msg, res))
        elif action == "list":
            msg, res = list_user()
            print (msg) if res else print ("{}, status: {}" .format(msg, res))
        elif action == "load":
            msg, res = load()
            print ("load succeed.") if res else print ("{}, status: {}" .format(msg, res))
        elif action == "find":
            msg, res = find_user(user_info)
            print (msg) if res else print ("{}, status: {}" .format(msg, res))
        elif action == "display":
            msg, res = display_user(user_info)
            print (msg) if res else print ("{}, status: {}" .format(msg, res))
        elif action == "exit":
            sys.exit(0)
        else:
            print_warn ("invalid action.")


def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    CHANCE_TIMES = 5
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        res = check_login(username,password)
        if res:
            # 如果输入无效的操作，则反复操作, 直到输入exit退出
            #RESULT = load()
            operation()
        else:
            # 带颜色
            print("\033[1;31m username or password error,you have {} times to input \033[0m" .format(CHANCE_TIMES))
            CHANCE_TIMES -= 1
            INIT_FAIL_CNT += 1
    print("\n\033[1;31m Input {} times, all failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))


if __name__ == '__main__':
    main()
