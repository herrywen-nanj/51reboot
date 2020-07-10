# -*- coding: utf-8 -*-
# @Time    : 2019-06-18 14:05
# @Author  : Joe
# @Site    : 
# @File    : user_manage_v3.py
# @Software: PyCharm
# @function: xxxxx


import csv
import json
import logging

from prettytable import PrettyTable

user_lists = []
times = 0
retry_times = 6
logininfo = ('joe', '1')
# username_all变量装载user_lists中的用户名，方便各个方法定位
username_all = []
user_dict = {}
docs = '''
输入格式example
add joe 18 13800138000 wennjoe@163.com
delete joe
update joe set age = 18
find joe
list
display page 1 pagesize 5
exit
'''


def user_log(message):
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
        filemode='a',
        filename='userlog.log'
    )
    logging.debug(message)


def check_argument(user_list: list) -> bool:
    argument_count = len(user_list)
    if user_list[0] == 'update' and argument_count != 6:
        print("takes at 6 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
        return False
    elif user_list[0] == 'add' and argument_count != 5:
        print("takes at 5 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
        return False
    elif user_list[0] == 'delete' and argument_count != 2:
        print("takes at 2 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
        return False
    elif user_list[0] == 'find' and argument_count != 2:
        print("takes at 2 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
        return False
    elif user_list[0] == 'display' and argument_count != 1 and argument_count != 5:
        print("takes at 5 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
        return False
    elif user_list[0] == 'list' and argument_count != 1:
        print("takes at 1 argument (%s give)" % len(user_list))
        print("input error\n %s" % docs)
    else:
        return True


def record_data_to_file(user_dict: dict) -> str:
    '''
    write data to file
    :return: None
    '''
    data = json.dumps(user_dict)
    try:
        with open('userinfos.txt', 'w') as fp:
            fp.write(data)
    except Exception:
        print("读取用户文件不存在或权限问题")

    return "saved to file success!"


def user_add(user_dict: dict) -> str:
    if user_list[1] not in user_dict:
        field_key = ['name', 'age', 'telephone', 'email']
        user_dict[user_list[1]] = {}
        zipped = dict(zip(field_key, user_list[1:]))
        user_dict[user_list[1]] = zipped
        result = record_data_to_file(user_dict)
        return result
    else:
        return "user: %s exist" % user_list[1]


def user_delete(user_dict: dict) -> str:
    if user_list[1] in user_dict:
        user_dict.pop(user_list[1])
        result = record_data_to_file(user_dict)
        logres = [username, ' ', user_list[0], ' ', user_list[1]]
        user_log(''.join(logres))
        return result
    else:
        return "user: %s not exist!" % user_list[1]


def user_update(user_dict: dict) -> str:
    if user_list[1] in user_dict:
        if user_list[3] != "name":
            user_dict[user_list[1]][user_list[3]] = user_list[-1]
            result = record_data_to_file(user_dict)
            return result
        else:
            return "username can't change"
    else:
        return "%s use not in userinfo" % user_list[1]


def user_llists(user_dict):
    if user_dict:
        pt = PrettyTable()
        pt.field_names = ["username", "age", "telephone", "email"]
        for vs in user_dict.values():
            pt.add_row([vs['name'], vs['age'], vs['telephone'], vs['email']])
        return pt
    else:
        return "userinfo empty"


def user_find(user_dict):
    if user_list[1] in user_dict:
        find_result = user_dict[user_list[1]]
        pt = PrettyTable()
        pt.field_names = ["username", "age", "telephone", "email"]
        pt.add_row(
            [find_result['name'], find_result['age'], find_result['telephone'], find_result['email']])
        return pt
    else:
        return "%s use not find" % user_list[1]


def user_display(user_dict):
    pt = PrettyTable()
    pt.field_names = ["username", "age", "telephone", "email"]
    for k, v in user_dict.items():
        user_lists.append([v['name'], v['age'], v['telephone'], v['email']])
    # user_lists[start_page:end_page]
    try:
        pagesize = int(user_list[-1])
    except Exception:
        pagesize = 5

    try:
        page = int(user_list[2])
    except Exception as e:
        page = 1

    start_item = (page - 1) * pagesize
    end_item = page * pagesize
    for i in user_lists[start_item:end_item]:
        pt.add_row([i[0], i[1], i[2], i[3]])
    user_lists.clear()
    return pt


def export_csv(user_dict):
    for k, v in user_dict.items():
        user_lists.append([v['name'], v['age'], v['telephone'], v['email']])
    try:
        with open('user.csv', 'w') as csffile:
            writer = csv.writer(csffile)
            writer.writerows(user_lists)
            return "导出csv成功"
    except Exception:
        return "没有权限创建文件"


def user_login(username, password):
    if username == logininfo[0] and password == logininfo[1]:
        res = [username, " login success!"]
        user_log(''.join(res))
        print(docs)
        return True, ''.join(res)
    else:
        global times
        times += 1
        res = [username, " username or password error!"]
        user_log(''.join(res))
        return False, ''.join(res)


while times < retry_times:
    username = input('input username:')
    password = input('input password:')
    login_result, msg = user_login(username, password)
    if login_result:
        print(msg)
        try:
            with open('userinfos.txt', 'r') as fp:
                user_dict = json.load(fp)
        except Exception:
            print("读取用户文件不存在或权限问题")
        while True:
            userinfo = input("input userinfo:")
            # str --> list type
            user_list = userinfo.split(' ')
            check_result = check_argument(user_list)
            if check_result:
                if user_list[0] == 'add':
                    result = user_add(user_dict)
                    print(result)

                elif user_list[0] == 'delete':
                    result = user_delete(user_dict)
                    print(result)

                elif user_list[0] == 'update':
                    result = user_update(user_dict)
                    print(result)

                elif user_list[0] == 'list':
                    result = user_llists(user_dict)
                    print(result)

                elif user_list[0] == 'find':
                    result = user_find(user_dict)
                    print(result)

                elif user_list[0] == 'display':
                    result = user_display(user_dict)
                    print(result)

                elif user_list[0] == 'export':
                    result = export_csv(user_dict)
                    print(result)
                elif user_list[0] == 'exit':
                    exit()
                else:
                    print("active ValueError!")
    else:
        print(msg)
