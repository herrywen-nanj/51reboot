import sys
import json
from prettytable import PrettyTable
import pymysql
import configmgt
import dbutils

import dbutils
#全局变量
DB_FILE = '51reboot.db'
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {}
class User(object):
    def add(self,args):
        userinfolist = args.split(" ")
        print(userinfolist)
        if len(userinfolist) != 4:
            return "addUser failed, args length != 4"
        username = userinfolist[0]
        if username in RESULT:
            print("Username: {} already exists.".format(username))
        else:
            RESULT[username] = {
                'name': username,
                'age': userinfolist[1],
                'tel': userinfolist[2],
                'email': userinfolist[3],
            }
            print("add user {} secc.".format(username))
    def delete(self,args):
        userinfolist = args.split(" ")
        if len(userinfolist) != 1:
            return "deleteUser failed, args length != 1"
        username = args
        if username in RESULT:
            RESULT.pop(username, None)  # None是什么意思？
        else:
            print("Username: {} is not found".format(username))
    def update(self,args):
        userinfolist = args.split()
        if len(userinfolist) != 5:
            return "updateUser failed, args length != 5"
        where = userinfolist[1]
        wherefuhao = userinfolist[-2]
        if where != 'set' or wherefuhao != '=':
            return 'syntax error.'
        else:
            username = userinfolist[0]
            where_field = userinfolist[2]
            update_value = userinfolist[-1]
            RESULT[username][where_field] = update_value
        print(RESULT)
    def find(self,args):
        username = args
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
    def display(self,args):
        '''
        display page 2 pagesize 5
        :param args: page 2 pagesize 5 ;default pagesize = 5
        page 1 -> 0-4
        切片
        slice
        '''
        userinfolist = args.split()
        if len(userinfolist) == 2:
            if userinfolist[0] != 'page':
                return "syntax error."

            values = [list(v.values()) for k, v in RESULT.items()]
            # print(values)

            page_value = int(userinfolist[1]) - 1  # 1
            pagesize = 5
            start = page_value * pagesize
            end = start + pagesize
            # 0:5
            # 5:10

            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for t_user_info in values[start:end]:
                xtb.add_row(t_user_info)
            print(xtb)

        elif len(userinfolist) == 4:
            if userinfolist[0] != 'page' and userinfolist[-2] != 'pagesize':
                return "syntax error."

            values = [list(v.values()) for k, v in RESULT.items()]
            # print(values)

            page_value = int(userinfolist[1]) - 1  # 1
            pagesize = int(userinfolist[-1])
            start = page_value * pagesize
            end = start + pagesize
            # 0:5
            # 5:10

            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for t_user_info in values[start:end]:
                xtb.add_row(t_user_info)
            print(xtb)
        else:
            return "syntax error."
class Auth(object):
    def login(self,username,password):
        init_fail_count = 0
        max_fail_count = 3
        while init_fail_count < max_fail_count:

            username = input("Please input your login username: ")
            password = input("Please input your login password: ")
            if auth(username, password):
                print("\n\tWelcome to user magage system.\n")
                logic()
            else:
                print("username or password valid failed.")
                init_fail_count += 1

        print("Game Over.")
    def session(self):
        pass
    def logout(self):
        sys.exit(0)
class Persistence(object):
    def save(self):
        msg = ''
        flag = True
        sql_data = load()
        for k, v in RESULT.items():
            if k in sql_data:
                if v != sql_data[k]:
                    sql = ''' update users set age = {},tel='{}',email='{}' where username='{}';
                       '''.format(RESULT[k]['age'], RESULT[k]['tel'], RESULT[k]['email'], RESULT[k]['username'])
                    print(sql)
                    updateMsg, ok = dbutils.update(sql)
                    print('updateMsg:%s' % updateMsg)

            else:
                print('新增数据：%s' % k)
                sql = ''' insert into users(username,age,tel,email) \
                   values('{}',{},'{}','{}');
                   '''.format(RESULT[k]['username'], RESULT[k]['age'], RESULT[k]['tel'], RESULT[k]['email'])
                print(sql)
                insertMsg, ok = dbutils.insert(sql)
                print('insertMsg:%s' % insertMsg)
        for i in sql_data:
            if i not in RESULT:
                # sql='''  '''
                sql = ''' delete from users where username = '{}'; '''.format(i)
                print(sql)
                deleteMsg, ok = dbutils.delete(sql)
                print(deleteMsg)
        return msg, flag
    def load(self):
        fields = ['username', 'age', 'tel', 'email']
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
class DB(object):
    def __init__(self,host,username,password,port):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
    def select(self,sql):
        conn = connect()
        if not conn:
            return 'conn db fail', False
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = cursor.fetchall()
            return rows, True
        finally:
            cursor.close()
            conn.close()
    def insert(self,sql):
        conn = connect()
        if not conn:
            return 'conn db fail', False
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
            return 'Insert succ', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cursor.close()
            conn.close()


def update(self,sql):
    conn = connect()
    if not conn:
        return 'conn db fail', False
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        print('%s行数据受影响' % cursor.rowcount)
        if cursor.rowcount == 0:
            return 'Update fail', False
        conn.commit()
        return 'Update succ', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cursor.close()
        conn.close()
    def delete(self,sql):
        pass
def logic():
    while True:
        userinfo = input("Please inpur user info: ")  # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            userinfo_string = ' '.join(userinfo_list[1:])
            if action == 'add':
                addUser(userinfo_string)
            elif action == 'delete':
                deleteUser(userinfo_string)
            elif action == 'update':
                updateUser(userinfo_string)
            elif action == 'find':
                findUser(userinfo_string)
            elif action == 'display':
                displayUser(userinfo_string)
            elif action == 'list':
                listUser()
            elif action == 'save':
                save()
            elif action == 'load':
                global RESULT
                RESULT = load()
            elif action == 'logout':
                logout()
def main():
    logic()
if __name__ == '__main__':
    main()