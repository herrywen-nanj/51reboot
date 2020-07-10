import configparser
import pymysql
from prettytable import PrettyTable
import sys

# 全局变量
DBCONN = None
RESULT = {}
FIELDS = ('username','age','tel','email')

def helpDoc():
    Usage = '''
    {} 
      usage:
        help        : help
        add         : add tom 12 132xxx tom@facebook.com
        update      : udpate tom set age = 18
        list        : list
        find        : find tom
        save        : save  
        load        : load  
        exit        : quit
    {}
    '''.format('-' * 60, '-' * 60)
    print(Usage)

class User(object):

    def add(self, username, age, tel, email):
        if username in RESULT:
            print("Username: {} already exists".format(username))
        else:
            RESULT[username] = {'name': username,'age': age, 'tel': tel,'email': email}
            print("Add user {} seccess.".format(username))

    def delete(self, name):
        if name in RESULT:
            RESULT.pop(name, None)
            print("Username: {} delete success.".format(name))
        else:
            print("Username: {} not found.".format(name))

    def update(self, name, field, value):
        if name in RESULT:
            RESULT[name][field] = value
            print("Update {}-{} update success..".format(name,field))
        else:
            print("Username: {} not found.".format(name))

    def list(self):
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(v.values())
        print(xtb)

    def find(self,name):
        if name in RESULT:
            # print(RESULT[name])
            res = RESULT[name]
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(list(res.values()))
            print(xtb)
        else:
            print("Username: {} not found.".format(name))

    def display(self, page,pagesize=5):
        # display page 2 pagesize 5
        values = [ list(v.values()) for k, v in RESULT.items() ]
        # print(values)
        page_value = int(page) - 1  # 1
        start = page_value * pagesize
        end = start + pagesize
        print(start,end,values[start:end])
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for t_user_info in values[start:end]:
            xtb.add_row(t_user_info)
        print(xtb)

class Auth(object):

    def login(self, username, password):
        userpassinfo = ('admin','admin123')
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
            resp, ok = DBCONN.select(sql)
            if not ok:
                fields_string = ','.join(FIELDS)  # "name,age,tel,email"
                values_string = "'{}', {}, '{}', '{}'".format(info['name'], info['age'], info['tel'], info['email'])
                sql = '''INSERT INTO {}({}) VALUES({})'''.format(TABLE, fields_string, values_string)
                print(sql)
                resp, ok = DBCONN.insert(sql)
                if ok:
                    print('username: {} save success.\n'.format(username))
                else:
                    print('username: {} save fail.\n'.format(username))
            else:
                print('username: {} already exists.\n'.format(username))

    def load(self):
        TABLE = 'users'
        sql = "SELECT {} FROM {};".format(','.join(FIELDS),TABLE)
        print(sql)
        resp, ok = DBCONN.select(sql)
        print("---> resp: {}".format(resp))
        if ok:
            global RESULT
            RESULT = {x[0]:{FIELDS[0]:x[0], FIELDS[1]:x[1], FIELDS[2]:x[2], FIELDS[3]:x[3]} for x in resp}
        else:
            print('Load from DB fail.')

def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "Config init is empty", False
    if key:
        if section in config.sections():
            return dict(config[section])[key], True
        else:
            return 'section not found', False
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
        try:
            conn = pymysql.connect(
                host = self.host,
                user = self.username,
                password = self.password,
                database = self.database,
                port = self.port,
            )
        except:
            return None
        return conn

    def select(self, sql):
        conn = self.connect()
        if not conn:
            return "Connect DB fail.", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = cur.fetchall()
            # 增加一行如果查询为空的情况，如果为空，则查询失败
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
            return "Connect DB fail.", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return "Insert Success.", True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def update(self, sql):
        conn = self.connect()
        if not conn:
            return "Connect DB fail.", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            print(cur.rowcount)
            if  cur.rowcount == 0:
                return "Update Fail.", False
            conn.commit()
            return "Update Success.", True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def delete(self, sql):
        conn = self.connect()
        if not conn:
            return "Connect DB fail.", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return "Delete Fail.", False
            conn.commit()
            return "Delete Success.", True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()


def logic():
    """
    业务逻辑函数
    :return:
    """
    while True:
        cmd_str = input("Please input commond: ")
        if len(cmd_str) == 0:
            print("command invalid.")
        else:
            cmd_list = cmd_str.split()
            action = cmd_list[0]
            # args = ' '.join(cmd_list[1:])
            args = cmd_list[1:]

            user = User()
            if action == 'add':
                # zhangsan 12 132111xxx  zhangsan@126.com
                # user.add(args[0], args[1], args[2], args[3])
                # * 元组 或 列表
                if len(args) != 4:
                    msg = "Add, args length not eq 4"
                    print(msg)
                    continue
                user.add(*args)
            elif action == 'delete':
                if len(args) != 1:
                    return "deleteUser failed, args length != 1"
                args = args[0]
                user.delete(args)
            elif action == 'update':
                # update lisi set age = 13;
                if len(args) != 5:
                    print("Update fail, args length != 5")
                if args[1] != 'set' and args[3] != '=':
                    print("syntax error.")
                else:
                    user.update(args[0],args[2],args[4])
            elif action == 'find':
                name = args[0]
                user.find(name)
            elif action == 'display':
                # display page 2 pagesize 5
                if  len(args) == 2 and args[0] == 'page':
                    page = args[1]
                    user.display(page)
                # elif  len(args) == 4 and args[0] == 'page' and args[1] == 'pagesize':
                #     page, pagesize = args[1], args[3]
                #     user.display(page,pagesize)
                else:
                    print("syntax error.")
            elif action == 'list':
                user.list()
            elif action == 'save':
                Persistence().save()
            elif action == 'load':
                Persistence().load()
            elif action == 'exit' or action == 'quit':
                sys.exit(0)
            else:
                print("input invalid.")
                helpDoc()


def init():
    """
    初始化函数
    :return:
    """
    FILENAME = "conf/DBConfig.ini"
    resp, ok = ReadConfig(FILENAME, 'dbinfo')
    if not ok:
        msg = "Read file {} fail, err: {}".format(FILENAME, resp)
        print(msg)
        return msg
    else:
        global DBCONN
        DBCONN = DB(resp['host'], resp['user'], resp['password'], resp['database'])
        # sql = 'SELECT * FROM users;'
        # print(db.select(sql))
def main():
    """
    入口函数
    :return:
    """
    # init()
    # logic()
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        username = input("Please input username: ")
        password = input("Please input password: ")
        auth = Auth()
        if auth.login(username, password):
            print("{}\nWelcome to User Management System\n{}".format('-'*40,'-'*40))
            init()   # 初始化database
            logic()
        else:
            print("Username or password error.")
            init_fail_count += 1
    print("Game Over.")


main()