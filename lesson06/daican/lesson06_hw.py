"""
用户管理系统
=================V1===================
1、登录认证；
2、增删改查和搜索
    3.1 增 add      # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete   # delete mobkey
    3.3 改 update   # update monkey set age = 18
    3.4 查 list     # list
    3.5 搜 find     # find monkey
3、格式化输出
===================V2=================
1. 数据结构：列表 -> 字典；
2. 分页 display page 1 pagesize 5
3. 文件持久化
4. 异常处理
5. PrettyTable 优雅的格式化输出
6. 扩展：导出csv(可写可不写)
===================V3================
1. 函数
将用户管理系统v2面向过程 升级为 函数式
2. 导出csv
将用户列表导出csv文件
3. 日志审计
通过logging模块，记录用户登录和删除操作即可，其它操作不需要记录。
日志级别为debug
====================V4==================
1. 支持配置文件管理方式
- ConfigParser
2. 存储方式 由文件 改成 数据库
- PyMySQL
===================V5=====================
优化， 改成面向对象的方式。
"""

# 标准模块
import sys
import json
import logging
import datetime
import pymysql
import configparser
from prettytable import PrettyTable
import csv

# 定义变量
RESULT = {}
FIELDS = ('username', 'age', 'tel', 'email')
FILENAME = "51reboot.txt"
FILECSV = "users.csv"
CONFNAME = "loginInfo.ini"


USERINFO = ("51reboot", "123456")

helpinfo = '''{}
1.  增   add         : add monkey 12 132xxx monkey@51reboot.com
2.  删   delete      : delete monkey
3.  改   update      : update monkey set age = 20
4.  查   list        : list
5.  搜   find        : find monkey
6.  分页 display     : display page 2 pagesize 3 
7.  帮助 doc         : show help
8.  退出 exit        : exit
9.  保存 save        : save as 51reboot.txt
10. 加载 load        : load 51reboot.txt
11. 导出CSV saveCsv  : save as users.csv
12. 加载CSV loadCsv  : load from users.csv
13. 存到DB saveDB    : save to DB
14. 加载DB loadDB    : load from DB
{}
'''.format('=' * 70, '=' * 70)


class User(object):
    def __init__(self, input_user_manage_info):
        self.input_user_manage_info = input_user_manage_info

    def add(self):
        list_info = self.input_user_manage_info
        if len(list_info) != 4:
            errMsg = print("Add info invalid, Please add again.")
            return errMsg, False

        # 判断用户是否存在，如果用户存在，提示用户已经存在，不再添加
        username = list_info[0]
        if username in RESULT:
            errMsg = "Username {} already exits.".format(username)
            return errMsg, False
        else:
            RESULT[username] = dict(zip(FIELDS, list_info))
            succMsg = "Add user {} succ.".format(username)
            return succMsg, True

    def delete(self):
        # delete monkey
        username = self.input_user_manage_info[0]
        delete_flag = RESULT.pop(username, None)
        if delete_flag == None:
            errMsg = "User {} not found".format(username)
            return errMsg, False
        else:
            succMsg = "User {} Delete succ.".format(username)
            return succMsg, True

    def update(self):
        ## update monkey set age = 20
        list_info = self.input_user_manage_info
        username = list_info[0]
        where = list_info[1]
        fuhao = list_info[-2]
        if where != "set" or fuhao != "=":
            errMsg = "Update method error!"
            return errMsg, False

        update_field = list_info[-3]
        update_value = list_info[-1]

        if username in RESULT:
            if update_field in RESULT[username]:
                RESULT[username][update_field] = update_value
                succMsg = "Username {} update succ.".format(username)
                return succMsg, True
            else:
                errMsg = "field: {} invalid.".format(update_field)
                return errMsg, False
        else:
            succMsg = "username: {} not found.".format(username)
            return succMsg, True

    def find(self):
        username = self.input_user_manage_info[0]
        userinfo = RESULT.get(username, None)
        if userinfo == None:
            errMsg = "User {} not found.".format(username)
            return errMsg, False
        else:
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            xtb.add_row(userinfo.values())
            return xtb, True

    def list(self):
        # 如果没有一条记录， 那么提示为空
        if len(RESULT) == 0:
            errMsg = "not data."
            return errMsg, False
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for k, v in RESULT.items():
            xtb.add_row(v.values())
        return xtb, True

    def display(self):
        # dispaly page 2 pagesize 5  #显示2页，每页显示5条
        # default = 5
        list_info = self.input_user_manage_info
        if len(list_info) >= 2 and len(list_info) <= 4:
            pagesize = 5
            if len(list_info) == 2:
                if list_info[0] == "page":
                    pagesize = 5
                else:
                    errMsg = "Display info invalid. Please input again."
                    return errMsg, False

            else:
                if list_info[0] == "page" and list_info[2] == "pagesize":
                    pagesize = int(list_info[-1])
                else:
                    errMsg = "Display info invalid. Please input again."
                    return errMsg, False

            page = int(list_info[1]) - 1
            data = []
            for k, v in RESULT.items():
                data.append(v.values())

            # start, end sep
            start = page * pagesize
            end = start + pagesize
            # print("Start: {}, End:{}".format(start, end))

            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for userinfo in data[start:end]:
                xtb.add_row(userinfo)
            return xtb, True
        else:
            errMsg = "Input info invalid, Please input again."
            return errMsg, False


class Auth(object):

    def login(self, username, password):
        '''
            验证账号和密码是否正确，如果正确返回True，否则返回False
            '''
        if username == USERINFO[0] and password == USERINFO[1]:
            return "Login succ", True
        else:
            return "Login fail", False

    def logout(self):
        sys.exit()

class DB(object):

    # def __init__(self, host, username, password, port):
    #     self.host = host
    #     self.username = username
    #     self.password = password
    #     self.port = port

    def ReadConfig(self, filename, section, key=None):
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

    def connect(self):
        cfg, ok = self.ReadConfig(CONFNAME, 'mysql')
        # print(cfg['host'])
        if not ok:
            return cfg, False
        else:
            try:
                conn = pymysql.connect(
                    host=cfg['host'],
                    user=cfg['user'],
                    password=cfg['password'],
                    database=cfg['database'],
                    port=int(cfg['port']),
                )
            except:
                return None
            return conn

    def select(self, sql):
        conn = self.connect()
        # if not conn:
        #     return "conn db fail", False
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
        # print(conn)
        # if not conn:
        #     return "conn db fail", False
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

class Persistence(object):

    def readFile(self):
        '''读取文件内容到内存'''
        try:
            with open(FILENAME, 'r') as fd:
                dateStr = fd.read()
                date = json.loads(dateStr)
                return date, True
        except Exception as e:
            return {}, False
        # try:
        #     # 1、打开文件
        #     fd = open(FILENAME, 'r')
        # except Exception as e:
        #     print("Read file fail, filename: {} not found.\n".format(FILENAME))
        # # 2. 操作文件 read
        # data = fd.read()
        # RESULT = json.loads(data)
        # # 3. 关闭文件
        # fd.close()
        # print("Load file:{} succ.".format(FILENAME))

    def writeFile(self):
        with open(FILENAME, 'w') as fd:
            fd.write(json.dumps(RESULT))
        return "Save succ", True

    def saveCsv(self):
        with open(FILECSV, 'w', newline='') as datacsv:
            csvwriter = csv.writer(datacsv, dialect="excel")
            csvwriter.writerow(['username', 'age', 'tel', 'email'])
            for x in RESULT.keys():
                csvwriter.writerow([x, RESULT[x]["age"], RESULT[x]["tel"], RESULT[x]["email"]])
        return "Save CSV succ", True

    def loadCsv(self):
        try:
            csv_file = csv.reader(open(FILECSV, 'r'))
            for x in csv_file:
                if x[0] == 'username':
                    continue
                else:
                    RESULT[x[0]] = {'username': x[0], 'age': x[1], 'tel': x[2], 'email': x[3]}
            return "Load users.csv succ", True
        except Exception as e:
            return e, False

    def loadDB(self):
        '''
        从数据库中加载到内存中
        :return:
        '''
        sql = "SELECT {} FROM users;".format(','.join(FIELDS))
        # print(sql)
        DBop = DB()
        resp, ok = DBop.select(sql)
        if ok:
            global RESULT
            # RESULT = [ dict(zip(FIELDS, x)) for x in resp] # 输出{'username': 'monkey11', 'age': 12, 'tel': '132xxx', 'email': 'monkey2@51reboot.com'}
            # RESULT = [ {FIELDS[0]: x[0], FIELDS[1]:x[1], FIELDS[2]:x[2], FIELDS[3]:x[3]} for x in resp ]
            RESULT = {x[0]: {FIELDS[0]: x[0], FIELDS[1]: x[1], FIELDS[2]: x[2], FIELDS[3]: x[3]} for x in resp}
            # 转换成 'monkey11': {'username': 'monkey11', 'age': 12, 'tel': '132xxx', 'email': 'monkey2@51reboot.com'}

        else:
            print('Load from db fail.')

    def saveDB(self):
        '''
        存储到数据库中
        '''
        '''
        1、查询插入的用户是否存在，是通过用户名判断；
        2、如果用户存在，则提示用户已存在，否则写入到数据库中。
        '''
        for username, info in RESULT.items():
            sql = "SELECT {} FROM users WHERE username = '{}';".format(','.join(FIELDS), username)
            # print(sql)
            DBop = DB()

            resp, ok = DBop.select(sql)  # select需要一个单独的判断是否为空的情况
            if not ok:
                fields_string = ','.join(FIELDS)  # "name,age,tel,email"
                values_string = "'{}', {}, '{}', '{}'".format(info['username'], info['age'], info['tel'], info['email'])
                # "'monkey', 12, '132xxxx','monkey@qq.com'"
                sql = '''INSERT INTO users({}) VALUES({})'''.format(fields_string, values_string)
                # print(sql)
                resp, ok = DBop.insert(sql)
                if ok:
                    print('username: {} save succ.\n'.format(username))
                else:
                    print('username: {} save fail.\n'.format(username))
            else:
                print('username: {} already exists.\n'.format(username))

    def log(self,msg: str):
        logging.basicConfig(level=logging.DEBUG,
                            format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                            filename='agent.log',  # 日志存储文件名
                            filemode='a+'  # append 追加方式
                            )
        logging.info(msg)
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(cur_time + "  : " + msg)


def opLogic():
    #业务逻辑
    while True:
        # 业务逻辑
        info = input("Please input your operation:").strip()  # 去前后空格
        # string -> list
        info_list = info.split()
        if len(info) == 0:  # 如果为空， 则提示
            print("Input info invalid, Please input again.")
            continue
        action = info_list[0]
        input_user_manage_info = info_list[1:]
        Userop = User(input_user_manage_info)
        Loginfo = Persistence()
        if action == "add":
            # add monkey 12 132xxx monkey@51reboot.com
            addMsg, ok = Userop.add()
            message = "{}, State: {}, Result: {}".format(action, ok, addMsg)
            Loginfo.log(message)
        elif action == "delete":
            delMsg, ok = Userop.delete()
            message = "{}, State: {}, Result: {}".format(action, ok, delMsg)
            Loginfo.log(message)
        elif action == "update":
            updateMsg, ok = Userop.update()
            message = "{}, State: {}, Result: {}".format(action, ok, updateMsg)
            Loginfo.log(message)
        elif action == "list":
            listMsg, ok = Userop.list()
            if not ok:
                message = "{}, State: {}, Result: {}".format(action, ok, listMsg)
                Loginfo.log(message)
            else:
                print(listMsg)
        elif action == "find":
            findMsg, ok = Userop.find()
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, findMsg))
            else:
                print(findMsg)
        elif action == "save":
            writeMsg, ok = Loginfo.writeFile()
            message = "{}, State: {}, Result: {}".format(action, ok, writeMsg)
            Loginfo.log(message)
        elif action == "load":
            readMsg, ok = Loginfo.readFile()
            if not ok:
                message = "{}, State: {}, Result: {}".format(action, ok, readMsg)
                Loginfo.log(message)
            else:
                global RESULT
                # 局部变量要修改全局变量的值，需要用global关键字声明。
                RESULT = readMsg
                message = "{}, State: {}".format(action, ok)
                Loginfo.log(message)
            print(RESULT)
        elif action == "saveCsv":
            csvMsg, ok = Loginfo.saveCsv()
            message = "{}, State: {}, Result: {}".format(action, ok, csvMsg)
            Loginfo.log(message)
        elif action == "loadCsv":
            loadcsvMsg, ok = Loginfo.loadCsv()
            print(RESULT)
            message = "{}, State: {}, Result: {}".format(action, ok, loadcsvMsg)
            Loginfo.log(message)

        elif action == "loadDB":
            Loginfo.loadDB()
            print(RESULT)

        elif action == "saveDB":
            Loginfo.saveDB()

        elif action == "display":
            disMsg, ok = Userop.display()
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, disMsg))
            else:
                print(disMsg)
        elif action == "doc":
            print(helpinfo)
        elif action == "exit":
            Userlogin = Auth()
            Userlogin.logout()
        else:
            print("\033[31m invalid action\033[0m")

def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username:")
        password = input("Please input your password:")
        Userlogin = Auth()
        loginMsg, ok = Userlogin.login(username,password)
        Loginfo = Persistence()
        if not ok:
            Loginfo.log(loginMsg)
            INIT_FAIL_CNT += 1   #登录失败次数+1
            continue
        # print("Login succ\n\n")
        Loginfo.log(loginMsg)

        opLogic()
    print("\033[31m \nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

if __name__ == '__main__':
    main()