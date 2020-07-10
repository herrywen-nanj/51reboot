
import configparser

import pymysql
from prettytable import PrettyTable


# 全局变量
DBCONN = None
FIELDS = ['username', 'age', 'tel', 'email']
RESULT = {}

class User(object):

    def add(self, username, age, tel, email):
        # userinfolist = args.split(" ")
        # if len(userinfolist) != 4:
        #     return "addUser failed, args length != 4"

        # username = userinfolist[0]
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {'name': username, 'age': age, 'tel': tel,'email': email}
            print("add user {} secc.".format(username))

    def delete(self, name):
        pass

    def update(self, name, field, value):
        pass

    def find(self, name):
        pass

    def list(self):
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(v.values())
        print(xtb)

    def display(self, page, pagesize=5):
        pass


class Auth(object):

    def login(self, username, password):
        userpassinfo = ('51reboot', '123456')
        if username == userpassinfo[0] and password == userpassinfo[1]:
            return True
        else:
            return False

    def session(self):
        pass

    def logout(self):
        pass


class Persistence(object):

    def save(self):
        TABLE = 'users'

        for username, info in RESULT.items():
            sql = "SELECT {} FROM {} WHERE username = '{}';".format(','.join(FIELDS), TABLE, username)
            print(sql)
            # break
            resp, ok = DBCONN.select(sql)  # select需要一个单独的判断是否为空的情况
            if not ok:
                fields_string = ','.join(FIELDS)  # "name,age,tel,email"
                values_string = "'{}', {}, '{}', '{}'".format(info['name'], info['age'], info['tel'], info['email'])
                # "'monkey2', 12, '132xxx', 'monkey@qq.com'"
                sql = '''INSERT INTO {}({}) VALUES({})'''.format(TABLE, fields_string, values_string)
                # INSERT INTO users(name,age,tel,email) VALUES('monkey2', 12, '132xxx', 'monkey@qq.com')
                print(sql)
                resp, ok = DBCONN.insert(sql)
                if ok:
                    print('username: {} save succ.\n'.format(username))
                else:
                    print('username: {} save fail.\n'.format(username))
            else:
                print('username: {} already exists.\n'.format(username))


    def load(self):
        sql = "SELECT {} FROM users;".format(','.join(FIELDS))
        print(sql)
        resp, ok = DBCONN.select(sql)
        print("---> resp：{}".format(resp))
        if ok:
            global RESULT
            # RESULT = [ dict(zip(FIELDS, x)) for x in resp]
            # RESULT = [ {FIELDS[0] : x[0], FIELDS[1] :x[1], FIELDS[2] :x[2], FIELDS[3] :x[3]} for x in resp ]
            RESULT = {x[0]: {FIELDS[0]: x[0], FIELDS[1]: x[1], FIELDS[2]: x[2], FIELDS[3]: x[3]} for x in resp}

        else:
            print('Load from db fail.')


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

class DB(object):

    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database

    def connect(self):
        '''
            数据库的连接
        :return:
        '''
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port=self.port,
            )
        except:
            return None
        return conn

    def select(self, sql):
        conn = self.connect()
        if not conn:
            return "conn db fail", False
        cur = conn.cursor()

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
        finally:
            cur.close()
            conn.close()




    def insert(self, sql):
        conn = self.connect()
        if not conn:
            return "conn db fail", False
        cur = conn.cursor()

        try:
            cur.execute(sql)
            conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def update(self, sql):
        conn = self.connect()
        if not conn:
            return "conn db fail", False
        cur = conn.cursor()

        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Update fail', False

            conn.commit()
            return 'Update succ.', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def delete(self, sql):
        conn = self.connect()
        if not conn:
            return "conn db fail", False
        cur = conn.cursor()

        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Delete fail', False

            conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()


def logic():
    '''
        业务逻辑函数
    :return:
    '''
    while True:
        userinfo = input("Please input user info: ") # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            # userinfo_string = ' '.join(userinfo_list[1:])
            userinfo_string = userinfo_list[1:]

            user = User()
            if action == 'add':
                # monkey1 12 132xxx monkey1@51reboot.com
                # user.add(userinfo_string[0], userinfo_string[1], userinfo_string[2], userinfo_string[3])
                # * 元组 或 列表
                if len(userinfo_string) != 4:
                    msg = 'Add, args length not eq 4.'
                    print(msg)
                    continue
                user.add(*userinfo_string)
            elif action == 'delete':
                pass
            elif action == 'update':
                pass
            elif action == 'find':
                pass
            elif action == 'display':
                pass
            elif action == 'list':
                user.list()
            elif action == 'save':
                Persistence().save()
            elif action == 'load':
                Persistence().load()
            elif action == 'logout':
                pass
            else:
                msg = 'Match action fail.'
                print(msg)

def init():
    '''
        初始化函数
    :return:
    '''
    FILENAME = '51reboot.ini'
    resp, ok = ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        msg = "Read file {} fail, err : {}".format(FILENAME, resp)
        print(msg)
        return msg
    else:
        global DBCONN
        DBCONN = DB(resp['host'], resp['username'], resp['password'], resp['database'])


def main():
    '''
        入口函数
    :return:
    '''
    # init()
    # logic()

    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:

        username = input("Please input your login username: ")
        password = input("Please input your login password: ")

        auth = Auth()
        if auth.login(username, password):
            print("\n\tWelcome to user magage system.\n")
            init()      # 初始化 -> database
            logic()
        else:
            print("username or password valid failed.")
            init_fail_count += 1

    print("Game Over.")

main()