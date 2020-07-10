#!/usr/bin/python

import csv,os
import json
import datetime
from prettytable import PrettyTable   # 将输出内容如表格方式整齐地输出
from dbutils import select,insert,delete,update

# 定义变量
FIELDS = ['id', 'username', 'age', 'tel', 'email']

def add_user(userinfo):
    while len(userinfo) == 4:
        sql = '''insert into users(username,age,tel,email)  values('{}','{}','{}','{}');'''.format(userinfo[0],userinfo[1],userinfo[2],userinfo[3])
        insertMsg, ok = insert(sql)
        if not ok:
            print(insertMsg)
        else:
            cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return ("\033[5;31m[INFO] {}\033[0m Add {} succ.\n".format(cur_time, userinfo[0]))
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: add [{}] [{}] [{}] [{}]\033[0m\n").format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3])

def del_user(userinfo):
    while len(userinfo) == 1:
        sql = '''delete from users where username = '{}';'''.format(userinfo[0])
        deleteMsg, ok = delete(sql)
        if not ok:
            print(deleteMsg)
        else:
            cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return ("\033[5;31m[INFO] {} \033[0m {} has been deleted.\n".format(cur_time,userinfo[0]))
        # else:
        #     return "\033[5;31m{} does not exist.\033[0m\n".format(info_list[1])
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: delete|del [ {} ]\033[0m\n").format(FIELDS[1])

def update_info(userinfo):
    while len(userinfo) == 5:
        username = userinfo[0]
        alter_key = userinfo[2]
        alter_value = userinfo[4]
        sql = '''update users set {} = '{}' where username = '{}';'''.format(alter_key,alter_value,username)
        msg,ok = update(sql)
        if not ok:
            print(msg)
        else:
            cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return "\033[5;31m[INFO] {} \033[0m {} {} was changed to {}.\n".format(cur_time,username,alter_key,alter_value)
    # else:
    #     return "\033[1;31;43m{} does not exist!\033[0m\n".format(userinfo[1])
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: update [ {} ] set [ {}|{}|{}|{} ] = [ Target field ]\033[0m\n").format(FIELDS[1],FIELDS[1],FIELDS[2],FIELDS[3],FIELDS[4])

def find_info(userinfo):
    while len(userinfo) == 1:
        sql = '''select * from users where username='{}';'''.format(userinfo[0])
        findMsg, ok = select(sql)
        if not ok:
            return (findMsg)
        else:
            ltab = PrettyTable()
            ltab.field_names = FIELDS
            for i in findMsg:
                ltab.add_row(i)
            return (ltab)
    # else:
    #     return ("\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1]))
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: find [ {} ]\033[0m\n".format(FIELDS[1]))

def get_list():
    sql = '''select * from users;'''
    result, ok = select(sql)
    if not ok:
        print(result)
    else:
        ltab = PrettyTable()
        ltab.field_names = FIELDS
        for i in result:
            ltab.add_row(i)
        print(ltab)

def get_pageinfo(userinfo):
    '''
    display page 2 pagesize 5
    :param args: page 2 pagesize 5 ;default pagesize = 5
    page 1 -> 0-4
    切片
    slice
    '''
    if len(userinfo) == 2:
        if userinfo[0] != 'page':
            return "syntax error."
        pagesize = 5

    elif len(userinfo) == 4:
        if userinfo[0] != 'page' or userinfo[-2] != 'pagesize':
            return "syntax error."
        pagesize = int(userinfo[-1])
    else:
        return "syntax error."

    sql = '''select * from users;'''
    result, ok = select(sql)
    if not ok:
        print(result)
    else:
        page_value = int(userinfo[1]) - 1  # 1
        # 总数据长度
        data_length = len(result)
        # 计算出最大可以输入的页码
        max_page_number = data_length // pagesize + 1 if data_length % pagesize else data_length // pagesize
        start = page_value * pagesize
        end = start + pagesize
        # 0:5
        # 5:10

        # 输入的页码过大时打印提示，输出最后一页内容
        if page_value < max_page_number:
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for index in result[start:end]:
                xtb.add_row(index)
            return (xtb)
        else:
            return "\033[5;31mQuery data does not exist.\n"

# def csv_export():
#     userid_sort = sorted(RESULT['userid'].items(), key=lambda x: x[1])
#
#     with open('export.csv', 'w', newline="") as csvfile:
#         fieldnames = FIELDS
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for i in userid_sort:
#             get_id = str(i[1])
#             RESULT['userinfo'][get_id].update({'id': str(i[1])})
#             writer.writerow(RESULT['userinfo'].get(get_id))
#         return "\033[5;32mExport Succeed.\033[0m\n"