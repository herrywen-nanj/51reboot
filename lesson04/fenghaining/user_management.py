'''
1. 登录认证；
2. 增删改查和搜索
    1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2 删 delete        # delete monkey
    3 改 update        # update monkey set age = 18
    4 查 list          # list
    5 搜 find          # find monkey
    6 分页显示         # display page 1 pagesize 2
    7 保存             # save
    8 导出为cvs格式    # export
3. 格式化输出
'''

import sys
import os
import json
import csv
import logging
from prettytable import PrettyTable

def logger(data):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='agent.log',
                        filemode='a'
                        )
    logging.debug(data)
    msg = '日志写入成功'
    return msg


def serialize_data(data):
    """
    格式化数据
    :param data: 要格式化的数据
    :return:
    """
    xtb = PrettyTable()
    xtb.field_names = ['username', 'age', 'tel', 'email']
    for i in data:
        xtb.add_row(i)
    return xtb


def user_add(users, info_list):
    """
    用户添加功能
    :param users: 存储于文件中的用户信息字典
    :param info_list: 用户输入信息列表
    :return:
    """
    msg = ''
    flag = False
    if len(info_list) < 5:
        msg = '数据长度不够，请重新输入'
        return msg, flag
    username = info_list[1]
    age = info_list[2]
    tel = info_list[3]
    email = info_list[4]

    # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
    if username in users.keys():
        msg = '用户已存在，请重新输入'
        flag = False
    else:
        users[username] = {"age": age, "tel": tel, "email": email}
        # 打印结果信息
        msg = "Add {} succ.".format(username)
        logger(msg)
        flag = True
    return msg, flag


def user_del(users, info_list):
    """
    用户删除功能
    :param users: 存储于文件中的用户信息字典
    :param info_list: 要删除的用户列表
    :return:
    """
    msg = ''
    flag = False
    if len(info_list) < 2:
        msg = '数据长度不够，请重新输入'
        return msg, flag
    username = info_list[1]
    if username in users.keys():
        users.pop(username)
        msg = '%s已删除' % username
        logger(msg)
        flag = True
    else:
        msg = '%s不存在' % username
        flag = False
    return msg, flag


def user_update(users, info_list):
    """
    用户更新功能
    :param users: 存储于文件中的用户信息字典
    :param info_list: 要删除的用户列表
    :return:
    """
    msg = ''
    flag = False
    if len(info_list) < 6:
        msg = '数据长度不够，请重新输入'
        return msg, flag
    # update monkey1 set age = 20
    username = info_list[1]
    where = info_list[2]
    field = info_list[3]
    fuhao = info_list[-2]
    val = info_list[-1]

    if where != "set" or fuhao != "=":
        msg = "Update method error."
        flag = False
        return msg, flag

    if username not in users.keys():
        msg = '用户%s不存在' % username
        flag = False
    else:
        if users[username].get(field, None) == None:
            msg = '%s字段不存在' % field
            flag = False
        else:
            users[username][field] = val
            msg = '用户%s,%s已更新为%s' % (username, field,val)
            logger(msg)
            flag = True
    return msg, flag


def user_list(users):
    """
    用户展示功能
    :param users: 存储于文件中的用户信息字典
    :return:
    """
    msg = ''
    flag = True
    # xtb = PrettyTable()
    # xtb.field_names = ['username', 'age', 'tel', 'email']
    # 如果没有一条记录， 那么提示为空
    if len(users) < 1:
        msg = '列表为空'
        flag = False
        return msg, flag

    # for k, v in users.items():
    #     xtb.add_row([k, v['age'], v['tel'], v['email']])
    tmp = []
    for k, v in users.items():
        tmp.append([k, v['age'], v['tel'], v['email']])
    result = serialize_data(tmp)

    return result, flag


def user_find(users, info_list):
    """
    用户查找功能
    :param users: 存储于文件中的用户信息字典
    :param info_list:  输入的用户信息列表
    :return:
    """
    msg = ''
    flag = True
    if len(info_list) < 2:
        msg = '数据长度不够，请重新输入'
        flag = False
        return msg, flag

    username = info_list[1]
    # xtb = PrettyTable()
    # xtb.field_names = ['username', 'age', 'tel', 'email']
    tmp = []
    if username in users.keys():
        # xtb.add_row([username, users.get(username)['age'], users.get(username)['tel'],
        #              users.get(username)['email']])
        # msg = xtb
        tmp.append([username, users.get(username)['age'], users.get(username)['tel'],
                    users.get(username)['email']])
    else:
        msg = '%s不存在' % username
        flag = False
    result = serialize_data(tmp)
    return result, flag


def user_save(users):
    """
    数据保存到本地文件功能
    :param users: 存储于文件中的用户信息字典
    :return:
    """
    msg = ''
    flag = True
    with open('userinfo.txt', 'w') as f:
        f.write(json.dumps(users))
    msg = '数据保存成功'
    return msg, flag


def user_display(users, info_list):
    """
    数据分页功能
    :param users: 存储于文件中的用户信息字典
    :param info_list: 输入的用户信息列表
    :return:
    """
    # 分页 display page 1 pagesize 5
    msg = ''
    flag = True
    if len(info_list) < 5:
        msg = '数据长度不够，请重新输入'
        flag = False
        return msg, flag
    if info_list[1] != "page" or info_list[3] != "pagesize":
        msg = "Display method error."
        flag = False
        return msg, flag

    page = int(info_list[2])
    pagesize = int(info_list[-1])

    # xtb = PrettyTable()
    # xtb.field_names = ['username', 'age', 'tel', 'email']

    tmp = []
    result = []
    for k, v in users.items():
        tmp.append([k, v['age'], v['tel'], v['email']])

    for i in tmp[(page - 1) * pagesize:(page - 1) * pagesize + pagesize]:
        # xtb.add_row(i)
        result.append(i)
    msg = serialize_data(result)
    return msg, flag


def data_export(users, filename):
    """
    数据导出到csv文件
    :param users: 存储于文件中的用户信息字典
    :return:
    """
    msg = ''
    flag = True
    with open('%s.csv'%filename, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect=('excel'))
        csvwriter.writerow(['姓名', '年龄', '电话', '邮箱'])
        for k, v in users.items():
            csvwriter.writerow([k, v['age'], v['tel'], v['email']])
    msg = '文件导出成功，文件名为%s.csv' % filename
    return msg, flag


if __name__ == '__main__':
    """
    主函数
    """
    # 定义变量
    RESULT = {}
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    # USERINFO = ("1", "1")
    USERINFO = ("51reboot", "123456")
    FIELDS = ['username', 'age', 'tel', 'email']
    FLAG = True
    try:
        with open('userinfo.txt', 'r') as f:
            RESULT = json.loads(f.read())
    except FileNotFoundError as e:
        os.system('touch userinfo.txt')

    while INIT_FAIL_CNT < MAX_FAIL_CNT and FLAG:
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            # 如果输入无效的操作，则反复操作, 否则输入exit退出
            msg = '%s用户已登录'%username
            logger(msg)
            while True:
                info = """
                1 增 add           # add monkey 12 132xxx monkey@51reboot.com
                2 删 delete        # delete monkey
                3 改 update        # update monkey set age = 18
                4 查 list          # list
                5 搜 find          # find monkey
                6 分页显示         # display page 1 pagesize 2
                7 保存             # save   
                8 导出为cvs格式    # export filename
                """

                print(info)
                print('=' * 80)
                # 业务逻辑
                info = input("Please input your operation: ")
                info_list = info.split()
                action = info_list[0]
                if action == "add":
                    # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                    result, ok = user_add(RESULT, info_list)
                    print(result)

                elif action == "delete":
                    result, ok = user_del(RESULT, info_list)
                    print(result)

                elif action == "update":
                    result, ok = user_update(RESULT, info_list)
                    print(result)

                elif action == "list":
                    result, flag = user_list(RESULT)
                    print(result)

                elif action == "find":
                    result, flag = user_find(RESULT, info_list)
                    print(result)

                elif action == "save":
                    result, flag = user_save(RESULT)
                    print(result)

                elif action == "display":
                    result, flag = user_display(RESULT, info_list)
                    print(result)

                elif action == "export":
                    filename = info_list[1]
                    result, flag = data_export(RESULT,filename)
                    print(result)

                elif action == "exit":
                    msg = '%s用户退出'%username
                    logger(msg)
                    sys.exit(0)
                else:
                    print("invalid action.")
        else:
            # 带颜色
            print("username or password error.")
            INIT_FAIL_CNT += 1

    print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
