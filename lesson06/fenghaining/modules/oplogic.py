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
from . import configmgt
from . import dbutils
from . import auth
from . import user
from . import logger
from . import data_export
# from . import persistence

RESULT = {}
FIELDS = ['username', 'age', 'tel', 'email']
FLAG = True
FILENAME = '51reboot.ini'
sqlop = dbutils.DB()
auth = auth.Auth()
user = user.User()
username =''

class Persistence(object):
    def load(self):
        # v2数据存储于数据库
        fields = ['username', 'age', 'tel', 'email']
        sql = ''' select * from users'''
        result, ok = sqlop.select(sql)
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

    def user_save(self,users):
        """
        数据保存到本地文件功能
        :param users: 存储于文件中的用户信息字典
        :return:
        """
        msg = ''
        flag = True

        # v2数据存储于数据库
        # sql_data = load()
        sql_data = self.load()
        # 判断内存中的数据是否在sql中，
        # 如果在判断是否一致，数据不一致，执行sql更新
        # 如果不在将该数据插入sql中，执行sql新增
        for k, v in RESULT.items():
            # print('='*50)
            if k in sql_data:
                if v != sql_data[k]:
                    sql = ''' update users set age = {},tel='{}',email='{}' where username='{}';
                    '''.format(RESULT[k]['age'], RESULT[k]['tel'], RESULT[k]['email'], RESULT[k]['username'])
                    print(sql)
                    updateMsg, ok = sqlop.update(sql)
                    print('updateMsg:%s' % updateMsg)

            else:
                # sql新增
                print('新增数据：%s' % k)
                sql = ''' insert into users(username,age,tel,email) \
                values('{}',{},'{}','{}');
                '''.format(RESULT[k]['username'], RESULT[k]['age'], RESULT[k]['tel'], RESULT[k]['email'])
                print(sql)
                insertMsg, ok = sqlop.insert(sql)
                print('insertMsg:%s' % insertMsg)

        # 判断数据库中的数据与内存中的数据,不存在则删除该数据
        for i in sql_data:
            if i not in RESULT:
                # sql='''  '''
                sql = ''' delete from users where username = '{}'; '''.format(i)
                print(sql)
                deleteMsg, ok = sqlop.delete(sql)
                print(deleteMsg)
        return msg, flag

        # v1 数据保存到文件
        # with open('userinfo.txt', 'w') as f:
        #     f.write(json.dumps(users))
        # msg = '数据保存成功'
        # return msg, flag


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
        persistence = Persistence()

        if action == "add":
            # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
            result, ok = user.user_add(RESULT, info_list)
            print("\n{}, State: {}, Result: {} \n".format(action, ok, result))

        elif action == "delete":
            result, ok = user.user_del(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "update":
            result, ok = user.user_update(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "list":
            result, ok = user.user_list(RESULT)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "find":
            result, ok = user.user_find(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "save":
            result, ok = persistence.user_save(RESULT)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "display":
            result, ok = user.user_display(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))

        elif action == "export":
            result, ok = data_export.data_export(RESULT, info_list)
            print("\n{}, State: {}, Result: {}\n".format(action, ok, result))
        elif action == 'load':
            # global RESULT
            RESULT = persistence.load()
        elif action == "exit":
            msg = '%s用户退出' % username
            logger.logger(msg)
            auth.logout()

        else:
            print("invalid action.")


def main():
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

        result, flag = auth.login(username, password)
        if not flag:
            print(result)
            INIT_FAIL_CNT += 1
            continue
        else:
            print(result)
            opLogic()

    print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))



if __name__ == '__main__':
    main()

