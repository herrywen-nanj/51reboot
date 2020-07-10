# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 14:33
# @Author  : cf
# @Site    :
# @File    : user_manger.py
# @Software: PyCharm
# @function: 字典



import csv
import json
import sys

from prettytable import PrettyTable

user_lists = []
times = 0
retry_times = 3
logininfo = ('cf', '1')
username_all = []

user_dict = {}


def record_data_to_file():
    '''
    write data to file
    :return: None
    '''
    data = json.dumps(user_dict)
    with open('userinfos.txt', 'w') as fp:
        fp.write(data)

    return print("saved to file success!")


while times < retry_times:
    username = input('input username:')
    password = input('input password:')

    if username == logininfo[0] and password == logininfo[1]:
        print("%s login success!" % username)
        try:
            with open('userinfos.txt', 'r') as fp:
                user_dict = json.load(fp)
        except Exception as e:
            pass

        while True:
            userinfo = input("input userinfo:")
            # str --> list type
            user_list = userinfo.split(' ')

                user_dict = json.load(fp)
        except Exception as e:
            pass

        while True:
            userinfo = input("input userinfo:")
            # str --> list type
            user_list = userinfo.split(' ')

            if user_list[0] == 'add':
                if user_list[1] not in user_dict:
                    add_dict[user_list[1]] = {}
                    add_dict[user_list[1]]['name'] = user_list[1]
                    add_dict[user_list[1]]['age'] = user_list[2]
                    add_dict[user_list[1]]['telephone'] = user_list[3]
                    add_dict[user_list[1]]['email'] = user_list[4]
                    record_data_to_file()
                else:
                    print("user: %s exist" % user_list[1])

            elif user_list[0] == 'delete':
                if user_list[1] in user_dict:
                    user_dict.pop(user_list[1])
                    record_data_to_file()
                else:
                    print("user: %s not exist!" % user_list[1])

            elif user_list[0] == 'update':
                # update joe set age = 20
                if user_list[1] in user_dict:
                    if user_list[3] != "name":
                        user_dict[user_list[1]][user_list[3]] = user_list[-1]
                        record_data_to_file()
                    else:
                        print("username can't change")
                else:
                    print("%s use not in userinfo" % user_list[1])

            elif user_list[0] == 'list':
                if user_dict:
                    pt = PrettyTable()
                    pt.field_names = ["username", "age", "telephone", "email"]
                    for vs in user_dict.values():
                        pt.add_row([vs['name'], vs['age'], vs['telephone'], vs['email']])
                    print(pt)
                else:
                    print("userinfo empty")

            elif user_list[0] == 'find':
                if user_list[1] in user_dict:
                    find_result = user_dict[user_list[1]]
                    pt = PrettyTable()
                    pt.field_names = ["username", "age", "telephone", "email"]
                    pt.add_row(
                        [find_result['name'], find_result['age'], find_result['telephone'], find_result['email']])
                    print(pt)
                else:
                    print("%s use not find" % user_list[1])

            elif user_list[0] == 'display':
                # display page 1 pagesize 5
                pt = PrettyTable()
                pt.field_names = ["username", "age", "telephone", "email"]
                for k, v in user_dict.items():
                    user_lists.append([v['name'], v['age'], v['telephone'], v['email']])
                # user_lists[start_page:end_page]
                pagesize = int(user_list[-1])

                try:
                    page = int(user_list[2])
                except Exception as e:
                    page = 1

                start_item = (page - 1) * pagesize
                end_item = page * pagesize
                for i in user_lists[start_item:end_item]:
                    pt.add_row([i[0], i[1], i[2], i[3]])
                print(pt)
                user_lists.clear()

            elif user_list[0] == 'export':
                for k, v in user_dict.items():
                    user_lists.append([v['name'], v['age'], v['telephone'], v['email']])
                with open('user.csv', 'w') as csffile:
                    writer = csv.writer(csffile)
                    writer.writerows(user_lists)
                    print("导出csv成功")

            elif user_list[0] == 'save':
                record_data_to_file()

            else:
                print("active ValueError")
                sys.exit()

    else:
        times += 1
        print("username or password error!")
