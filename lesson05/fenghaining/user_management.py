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
import pymysql
import configmgt
import dbutils

RESULT = {}
FIELDS = ['username', 'age', 'tel', 'email']
FLAG = True
FILENAME = '51reboot.ini'


def connect():
    cfg, ok = configmgt.ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        return cfg, False
    print(cfg)
    try:
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except:
        return None
    return conn


def logger(data):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='agent.log',
                        filemode='a'
                        )
    logging.debug(data)
    msg = '日志写入成功'
    return msg


def load():
    # v2数据存储于数据库
    fields = [ 'username', 'age', 'tel', 'email']
    sql = ''' select * from users'''
    result, ok = dbutils.select(sql)
    if not ok:
        msg = 'result:%s' % result
    else:
        data_dic = {}
        # print(result, type(result))
        for i in result:
            data_dic[i[1]] = dict(zip(fields, i[1:]))
    return data_dic

    # v1，数据存储于文件
    # try:
    #     with open('userinfo.txt', 'r') as f:
    #         RESULT = json.loads(f.read())
    #
    # except FileNotFoundError as e:
    #     os.system('touch userinfo.txt')


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
    if len(info_list) != 5:
        msg = '数据长度不等于5，请重新输入'
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
        # users[username] = {'username': username, "age": age, "tel": tel, "email": email}
        users[username] = dict(zip(FIELDS, info_list[1:]))
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
    if len(info_list) != 2:
        msg = '数据长度不等于2，请重新输入'
        return msg, flag
    username = info_list[1]
    result = users.pop(username, None)
    if result != None:
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
    if len(info_list) != 6:
        msg = '数据长度不等于6，请重新输入'
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
            msg = '用户%s,%s已更新为%s' % (username, field, val)
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
    # 如果没有一条记录， 那么提示为空
    if len(users) < 1:
        msg = '列表为空'
        flag = False
        return msg, flag
    tmp = []
    for k, v in users.items():
        tmp.append(list(v.values()))
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
    if len(info_list) != 2:
        msg = '数据长度不等于2，请重新输入'
        flag = False
        return msg, flag

    username = info_list[1]

    tmp = []
    if username in users.keys():
        # tmp.append([username, users.get(username)['age'], users.get(username)['tel'],
        #             users.get(username)['email']])
        msg = serialize_data([list(users.get(username).values())])
    else:
        msg = '%s不存在' % username
        flag = False
    # result = serialize_data(tmp)
    return msg, flag


def user_save(users):
    """
    数据保存到本地文件功能
    :param users: 存储于文件中的用户信息字典
    :return:
    """
    msg = ''
    flag = True

    # v2数据存储于数据库
    sql_data = load()
    # 判断内存中的数据是否在sql中，
    # 如果在判断是否一致，数据不一致，执行sql更新
    # 如果不在将该数据插入sql中，执行sql新增
    for k,v in RESULT.items():
        # print('='*50)
        if k in sql_data:
            if v != sql_data[k]:
                sql = ''' update users set age = {},tel='{}',email='{}' where username='{}';
                '''.format(RESULT[k]['age'],RESULT[k]['tel'],RESULT[k]['email'],RESULT[k]['username'])
                print(sql)
                updateMsg, ok = dbutils.update(sql)
                print('updateMsg:%s'%updateMsg)

        else:
            # sql新增
            print('新增数据：%s'%k)
            sql = ''' insert into users(username,age,tel,email) \
            values('{}',{},'{}','{}');
            '''.format(RESULT[k]['username'],RESULT[k]['age'],RESULT[k]['tel'],RESULT[k]['email'])
            print(sql)
            insertMsg,ok = dbutils.insert(sql)
            print('insertMsg:%s'%insertMsg)

    # 判断数据库中的数据与内存中的数据,不存在则删除该数据
    for i in sql_data:
        if i not in RESULT:
            # sql='''  '''
            sql = ''' delete from users where username = '{}'; '''.format(i)
            print(sql)
            deleteMsg, ok = dbutils.delete(sql)
            print(deleteMsg)
    return msg, flag

    # v1 数据保存到文件
    # with open('userinfo.txt', 'w') as f:
    #     f.write(json.dumps(users))
    # msg = '数据保存成功'
    # return msg, flag


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
    pagesize = 0
    if len(info_list) >= 3 and len(info_list) <= 5:
        # pagesize = 5
        if len(info_list) == 3:
            if info_list[1] == 'page':
                pagesize = 5
            else:
                msg = 'Display info invalid. Please input again.'
                flag = False
                return msg, flag
        else:
            if info_list[1] == "page" and info_list[3] == "pagesize":
                pagesize = int(info_list[-1])
            else:
                msg = "Display method error."
                flag = False
                return msg, flag

    page = int(info_list[2])
    # pagesize = int(info_list[-1])

    result = []
    for k, v in users.items():
        result.append(list(v.values()))

    start = (page - 1) * pagesize
    end = start + pagesize
    msg = serialize_data(result[start:end])
    return msg, flag


def data_export(users, info_list):
    """
    数据导出到csv文件
    :param users: 存储于文件中的用户信息字典
    :return:
    """

    msg = ''
    flag = True
    if len(info_list) < 2:
        msg = '数据长度不等于2，请重新输入'
        flag = False
        return msg, flag
    filename = info_list[1]
    with open('%s.csv' % filename, 'w', newline='') as datacsv:
        csvwriter = csv.writer(datacsv, dialect=('excel'))
        csvwriter.writerow(['姓名', '年龄', '电话', '邮箱'])
        for k, v in users.items():
            csvwriter.writerow(list(v.values()))
    msg = '文件导出成功，文件名为%s.csv' % filename
    return msg, flag


def opLogic():
    """
    业务逻辑
    :return:
    """
    global RESULT
    while True:
        info = """
            1 增 add           # add monkey 12 132xxx monkey@51reboot.com
            2 删 delete        # delete monkey
            3 改 update        # update monkey set age = 18
            4 查 list          # list
            5 搜 find          # find monkey
            6 分页显示         # display page 1 pagesize 2
            7 保存             # save   
            8 数据导入         # load
            9 导出为cvs格式    # export filename
            10 退出登录        # exit
            """
        print('*' * 80)
        print(info)
        print('=' * 80)
        # 业务逻辑
        info = input("Please input your operation: ").strip()
        if len(info) == 0:
            print("Input info invalid, Please input again.")
            continue
        info_list = info.split()
        action = info_list[0]
        # RESULT = {}
        if action == "add":
            # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
            result, ok = user_add(RESULT, info_list)
            print("\n{}, State: {}, Result: {} \n".format(action, ok, result))

        elif action == "delete":
            result, ok = user_del(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "update":
            result, ok = user_update(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "list":
            result, ok = user_list(RESULT)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "find":
            result, ok = user_find(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "save":
            result, ok = user_save(RESULT)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "display":
            result, ok = user_display(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "export":
            result, ok = data_export(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))
        elif action == 'load':
            # global RESULT
            RESULT = load()
        elif action == "exit":
            msg = '%s用户退出' % username
            logger(msg)
            sys.exit(0)
        else:
            print("invalid action.")


def login(username, password):
    """
    用户登录
    :param username:
    :param password:
    :return:
    """
    msg = ''
    flag = True
    # USERINFO = ("1", "1")
    USERINFO = ("51reboot", "123456")
    if username == USERINFO[0] and password == USERINFO[1]:
        msg = '%s用户已登录' % username
        logger(msg)
    else:
        msg = '%s用户登录失败' % username
        flag = False
    return msg, flag


def logout():
    """
    用户退出
    :return:
    """
    sys.exit()


if __name__ == '__main__':
    """
    主函数
    """
    # 定义变量
    # RESULT = {}
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    # FIELDS = ['username', 'age', 'tel', 'email']
    # FLAG = True

    while INIT_FAIL_CNT < MAX_FAIL_CNT and FLAG:
        username = input("Please input your username: ")
        password = input("Please input your password: ")

        result, flag = login(username, password)
        if not flag:
            print(result)
            INIT_FAIL_CNT += 1
            continue
        else:
            print(result)
            opLogic()

    print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
