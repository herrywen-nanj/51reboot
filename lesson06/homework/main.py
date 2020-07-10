import sys
import configparser

import pymysql
from prettytable import PrettyTable



RESULT = {}
FIELDS = ['name', 'age', 'tel', 'email']
DBCONN = None


class User(object):

    def add(self, username, age, tel, email):
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {
                'name': username,
                'age': age,
                'tel': tel,
                'email': email,
            }
            print("add user {} secc.".format(username))

    def delete(self, username):
        if username in RESULT:
            RESULT.pop(username, None)
            print("delete user {} secc.".format(username))
        else:
            print("Username: {} not found.".format(username))

    def update(self, username, where_field, wherefuhao, update_value):

        if where_field != 'set' or wherefuhao != '=':
            return 'syntax error.'
        else:
            RESULT[username][where_field] = update_value

    def find(self, username):
        if username in RESULT:
            userinfo = RESULT[username]  # userinfo是字典
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(list(userinfo.values()))
            print(xtb)
        else:
            print("Username: {} not found.".format(username))

    def list(self):
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(v.values())
        print(xtb)

    def display(self, page, pagesize=5):
        print("page: {}, pagesize:{}".format(page, pagesize))

        values = [list(v.values()) for k, v in RESULT.items()]
        # print(values)

        page_value = int(page) - 1  # 1
        start = page_value * pagesize
        end = start + pagesize
        print(start)
        print(end)
        # 0:5
        # 5:10

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for t_user_info in values[start:end]:
            xtb.add_row(t_user_info)
        print(xtb)


class Auth(object):

    def login(self, username, password):
        userpassinfo = ('1', '1')
        if username == userpassinfo[0] and password == userpassinfo[1]:
            return True
        else:
            return False

    def session(self):
        pass

    def logout(self):
        sys.exit(0)


def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "config init is empty", False

    if key:
        if section in config.sections():
            return dict(config[section])[key], True
        else:
            return '', False
    else:
        return dict(config[section]), True

class Persistence(object):

    def save(self):

        for username, info in RESULT.items():
            sql = "SELECT {} FROM 51reboot_users WHERE name = '{}';".format(','.join(FIELDS), username)
            print(sql)
            resp, ok = dbconn.select(sql)  # select需要一个单独的判断是否为空的情况
            if not ok:
                fields_string = ','.join(FIELDS)
                values_string = "'{}', {}, '{}', '{}'".format(info['name'], info['age'], info['tel'], info['email'])
                sql = '''INSERT INTO 51reboot_users({}) VALUES({})'''.format(fields_string, values_string)
                print(sql)
                resp, ok = dbconn.insert(sql)
                if ok:
                    print('username: {} save succ.'.format(username))
                else:
                    print('username: {} save fail, err: {}.'.format(username, resp))
            else:
                print('username: {} already exists.'.format(username))

    def load(self):

        sql = "SELECT {} FROM 51reboot_users;".format(','.join(FIELDS))
        print(sql)
        resp, ok = dbconn.select(sql)
        if ok:
            global RESULT
            RESULT = { x[0] : dict(zip(FIELDS, x)) for x in resp}
        else:
            print('Load from db fail.')


class DB(object):

    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database
        self.conn = None

    def connect(self):
        if self.conn:
            return
        try:
            self.conn =  pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port=int(self.port),
                )
        except Exception as e:
            msg = "Conn database {} fail, err: {}".format(self.database, e)
            print(msg)
            # raise ConnectDatabaseExcept(msg)
            return None

    def insert(self, sql):
        self.connect()
        print(self.conn)
        cur = self.conn.cursor()

        try:
            cur.execute(sql)
            self.conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False
        # finally:
        #     cur.close()
        #     self.conn.close()

    def select(self, sql):
        self.connect()
        cur = self.conn.cursor()

        try:
            cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = cur.fetchall()
            # 增加一行如果查询为空的情况， 如果为空，则返回查询失败
            if len(rows) == 0:
                return '', False
            else:
                return rows, True
        # finally:
        #     cur.close()
        #     self.conn.close()

    def update(self, sql):
        self.conn()
        cur = self.conn.cursor()

        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Update fail', False

            self.conn.commit()
            return 'Update succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False
        # finally:
        #     cur.close()
        #     self.conn.close()

    def delete(self, sql):
        self.connect()
        cur = self.conn.cursor()

        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Delete fail', False

            self.conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False
        # finally:
        #     cur.close()
        #     self.conn.close()

    def close(self):
        self.conn.cursor().close()
        self.conn.close()


def logic():
    while True:
        userinfo = input("Please input user info: ") # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            # userinfo_string = ' '.join(userinfo_list[1:])
            userlist = userinfo_list[1:]

            user = User()
            if action == 'add':
                user.add(userlist[0], userlist[1], userlist[2], userlist[3])
            elif action == 'list':
                user.list()
            elif action == 'delete':
                user.delete(userlist[0])
            elif action == 'find':
                user.delete(userlist[0])
            elif action == 'display':
                # display page 1 pagesize 5
                user.display(userlist[1], userlist[-1])
            elif action == 'save':
                Persistence().save()
            elif action == 'load':
                Persistence().load()
            elif action == 'exit':
                sys.exit()


def init():
    FILENAME = '51reboot.ini'
    resp, ok = ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        msg = 'Read config fail, err: {}.'.format(resp)
        print(msg)
        return

    global dbconn
    dbconn = DB(resp['host'], resp['username'], resp['password'], resp['database'])


def main():
    init_fail_count = 0
    max_fail_count = 3

    while init_fail_count < max_fail_count:
        username = input('Please input username: ')
        password = input('Please input password: ')
        auth = Auth()
        if auth.login(username, password):
            print("Username {} login succ\n".format(username))
            init()
            logic()
        else:
            print("Username {} login fail\n".format(username))
            init_fail_count += 1


if __name__ == '__main__':
    main()