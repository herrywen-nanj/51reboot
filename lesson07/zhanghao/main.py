import sys
import configparser
import pymysql
from prettytable import PrettyTable

RESULT = {}
FIELDS = ['username', 'age', 'phone', 'email']


class User(object):

    def add(self, username, age, tel, email):
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {'username': username, 'age': age, 'phone': tel, 'email': email}
            print("add user {} succ.".format(username))

    def delete(self, username):
        if username in RESULT:
            RESULT.pop(username, None)
            print("delete user {} succ.".format(username))
            sql = "delete from users where username = '{}';".format(username)
            dbconn.delete(sql)
        else:
            print("Username: {} not found.".format(username))

    def update(self, username, keyword, field, mark, update_value):
        try:
            if keyword != 'set' or mark != '=':
                return 'syntax error.'
            else:
                RESULT[username][field] = update_value
                sql = "update users set {} = '{}' where username = '{}';".format(field, update_value, username)
                dbconn.update(sql)
        except Exception as e:
            return e

    def find(self, username):
        if username in RESULT:
            user_info = RESULT[username]
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(list(user_info.values()))
            print(xtb)
        else:
            print("Username: {} not found.".format(username))

    def list(self):
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(list(v.values()))
        print(xtb)

    def display(self, page, pagesize=5):
        print("page: {}, pagesize: {}".format(page, pagesize))
        values = [list(v.values()) for k, v in RESULT.items()]
        page_value = int(page) - 1
        start = page_value * pagesize
        end = start + pagesize
        print("start: {}, end: {}".format(start, end))
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for t_user_info in values[start:end]:
            xtb.add_row(t_user_info)
        print(xtb)


class Auth(object):

    def login(self, username, password):
        user_password = ('51reboot', '123456')
        if username == user_password[0] and password == user_password[1]:
            return True
        else:
            return False

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
            sql = "SELECT {} FROM users WHERE username = '{}';".format(','.join(FIELDS), username)
            # print(sql)
            resp, ok = dbconn.select(sql)  # select需要一个单独的判断是否为空的情况
            if not ok:
                fields_string = ','.join(FIELDS)
                values_string = "'{}', {}, '{}', '{}'".format(info['username'], info['age'], info['phone'],
                                                              info['email'])
                sql = '''INSERT INTO users({}) VALUES({});'''.format(fields_string, values_string)
                # print(sql)
                resp, ok = dbconn.insert(sql)
                if ok:
                    print('username: {} save succ.'.format(username))
                else:
                    print('username: {} save fail, err: {}.'.format(username, resp))
            else:
                print('username: {} already exists.'.format(username))

    def load(self):
        sql = "SELECT {} FROM users;".format(','.join(FIELDS))
        # print(sql)
        resp, ok = dbconn.select(sql)
        if ok:
            global RESULT
            RESULT = {x[0]: dict(zip(FIELDS, x)) for x in resp}
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
            self.conn = pymysql.connect(
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
        self.connect()
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            # print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Update fail.', False
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
            # print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Delete fail', False
            self.conn.commit()
            return 'Delete succ.', True
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
        user_info = input("Please input user info: ")  # add monkey 12 132xx monkey@qq.com
        if len(user_info) == 0:
            print("invalid input.")
        else:
            user_info_list = user_info.split()
            action = user_info_list[0]
            user_list = user_info_list[1:]
            user = User()
            if action == 'add':
                user.add(user_list[0], user_list[1], user_list[2], user_list[3])
            elif action == 'list':
                user.list()
            elif action == 'delete':
                user.delete(user_list[0])
            elif action == 'update':
                user.update(user_list[0], user_list[1], user_list[2], user_list[3], user_list[4])
            elif action == 'find':
                user.find(user_list[0])
            elif action == 'display':
                if len(user_list) == 2:
                    user.display(user_list[1])
                elif len(user_list) == 4:
                    user.display(user_list[1], int(user_list[-1]))
            elif action == 'save':
                Persistence().save()
            elif action == 'load':
                Persistence().load()
            elif action == 'logout':
                Auth().logout()


def init():
    FILENAME = '51reboot.ini'
    resp, ok = ReadConfig(FILENAME, 'db')
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
