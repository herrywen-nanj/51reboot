# -*- coding: utf-8 -*-
# @Time    : 2019-06-25 22:53
# @Author  : Joe
# @Site    : 
# @File    : user_manage_v4.py
# @Software: PyCharm
# @function: xxxxx

import configparser
import csv
import json
import logging

import pymysql
from prettytable import PrettyTable

docs = '''
    输入格式example
    add joe 18 13800138000 wennjoe@163.com
    delete joe
    update joe set age = 18
    find joe
    list
    display page 1 pagesize 5
    export
    exit
    '''


def ReadConfig(filename, config_section, config_parament=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if config_section not in config.sections():
        msg = "config section not exist"
        print(msg)
    else:
        dict_config = {}
        if config_parament:
            dict_config[config_parament] = config[config_section][config_parament]
            return dict_config
        else:
            for section in config[config_section]:
                dict_config[section] = config[config_section][section]
            return dict_config


class DBControl(object):
    """
    mysql db cudr
    """

    def __init__(self, filename, config_section, config_parament=None):
        dbconfig = ReadConfig(filename, config_section, config_parament)
        if isinstance(dbconfig, dict):
            self.host = dbconfig['host']
            self.port = dbconfig['port']
            self.username = dbconfig['username']
            self.password = dbconfig['password']
            self.dbname = dbconfig['database']

    def dbconn(self):
        try:
            self.conn = pymysql.Connection(
                host=self.host,
                port=int(self.port),
                user=self.username,
                password=self.password,
                database=self.dbname
            )
            return self.conn
        except Exception as e:
            return e

    def dbinsert(self, sql_execute):
        self.dbconn()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sql_execute)
            self.conn.commit()
            return "insert data success!", True
        except Exception as e:
            self.conn.rollback()
            return e, False
        finally:
            self.cur.close()
            self.conn.close()

    def dbdelete(self, sql_execute):
        self.dbconn()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sql_execute)
            self.conn.commit()
            if self.cur.rowcount:
                return "delete data success!", True
            else:
                return "user not exist!", False
        except Exception as e:
            return e, False
        finally:
            self.cur.close()
            self.conn.close()

    def dbupdate(self, sql_execute):
        self.dbconn()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sql_execute)
            self.conn.commit()
            if self.cur.rowcount:
                return "update data success!", True
            else:
                return "infomations value, username or culume error", False
        except Exception as e:
            return e, False
        finally:
            self.cur.close()
            self.conn.close()

    def dbselect(self, sql_execute):
        self.dbconn()
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(sql_execute)
            rows = self.cur.fetchall()
            if self.cur.rowcount:
                return rows, True
            else:
                return rows, False
        except Exception as e:
            return e, False
        finally:
            self.cur.close()
            self.conn.close()


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


def user_add(*args) -> str:
    user_dict = {}
    field_key = ['name', 'age', 'tel', 'email']
    user_username = args[0]
    user_age = args[1]
    user_tel = args[2]
    user_email = args[3]
    cur = args[-1]

    rows, status = cur.dbselect('''select * from users''')
    if status:
        for i in rows:
            user_dict[i[1]] = dict(zip(field_key, i[1:]))
        if user_username in user_dict:
            result = "user {} exist!".format(user_username)
            return result
        else:
            msg, status = cur.dbinsert(
                """insert into users(username,age,tel,email) values('%s', '%s', '%s', '%s');""" % (
                    user_username, user_age, user_tel, user_email))
            result = msg
            return result


def user_delete(*args) -> str:
    user_username = args[0]
    cur = args[1]
    operater = args[2]
    msg, status = cur.dbdelete("""delete from users where username='%s';""" % user_username)
    result = msg
    user_log(" ".join([operater, msg, user_username]))
    return result


def user_update(*args) -> str:
    user_username = args[0]
    user_parament = args[1]
    user_value = args[2]
    cur = args[-1]
    msg, status = cur.dbupdate(
        """update users set %s='%s' where username='%s';""" % (user_parament, user_value, user_username))
    result = msg
    return result


def user_llists(cur):
    rows, status = cur.dbselect("""select * from users""")
    if status:
        pt = PrettyTable()
        pt.field_names = ["username", "age", "telephone", "email"]
        for i in rows:
            pt.add_row([i[1], i[2], i[3], i[4]])
        return pt
    else:
        return "userinfo empty"


def user_find(*args):
    user_username = args[0]
    cur = args[1]
    rows, status = cur.dbselect("""select * from users where username='%s';""" % user_username)
    if status:
        pt = PrettyTable()
        pt.field_names = ["username", "age", "telephone", "email"]
        for i in rows:
            pt.add_row([i[1], i[2], i[3], i[4]])
        return pt
    else:
        return "user not find"


def user_display(*args):
    cur = args[1]
    try:
        page = int(args[0][1])
        pagesize = int(args[0][3])
    except Exception as e:
        page = 1
        pagesize = 5
    start_item = (page - 1) * pagesize
    end_item = pagesize
    rows, status = cur.dbselect("""select * from users limit %s,%s;""" % (start_item, end_item))
    pt = PrettyTable()
    pt.field_names = ["username", "age", "telephone", "email"]
    for i in rows:
        pt.add_row([i[1], i[2], i[3], i[4]])
    return pt


def export_csv(cur):
    rows, status = cur.dbselect("""select * from users""")
    print(rows)
    try:
        with open('user.csv', 'w') as csffile:
            writer = csv.writer(csffile)
            writer.writerows(rows)
            return "export csv success!"
    except Exception:
        return "没有权限创建文件"


def user_login(username, password):
    logininfo = ('joe', '1')
    if username == logininfo[0] and password == logininfo[1]:
        res = [username, " login success!"]
        user_log(''.join(res))
        print(docs)
        return True, ''.join(res)
    else:
        res = [username, " username or password error!"]
        user_log(''.join(res))
        return False, ''.join(res)


def main():
    times = 0
    retry_times = 5
    cur = DBControl('config.ini', 'dbconfig')

    while times < retry_times:
        username = input('input username:')
        password = input('input password:')
        login_result, msg = user_login(username, password)
        if login_result:
            print(msg)
            while True:
                userinfo = input("input userinfo:")
                # str --> list type
                user_list = userinfo.split(' ')
                check_result = check_argument(user_list)
                if check_result:
                    if user_list[0] == 'add':
                        user_username = user_list[1]
                        user_age = user_list[2]
                        user_tel = user_list[3]
                        user_email = user_list[-1]
                        result = user_add(user_username, user_age, user_tel, user_email, cur)
                        print(result)

                    elif user_list[0] == 'delete':
                        user_username = user_list[1]
                        result = user_delete(user_username, cur, username)
                        print(result)

                    elif user_list[0] == 'update':
                        user_username = user_list[1]
                        user_parament = user_list[-3]
                        user_value = user_list[-1]
                        result = user_update(user_username, user_parament, user_value, cur)
                        print(result)

                    elif user_list[0] == 'list':
                        result = user_llists(cur)
                        print(result)

                    elif user_list[0] == 'find':
                        result = user_find(user_list[1], cur)
                        print(result)

                    elif user_list[0] == 'display':
                        result = user_display(user_list[1:], cur)
                        print(result)

                    elif user_list[0] == 'export':
                        result = export_csv(cur)
                        print(result)

                    elif user_list[0] == 'exit':
                        exit()
                    else:
                        print("active ValueError!")
        else:
            times += 1
            print(msg)


if __name__ == '__main__':
    main()
