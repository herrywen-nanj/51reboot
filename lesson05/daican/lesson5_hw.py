'''
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
'''

import sys
import logging
import datetime
import pymysql
import configparser
from prettytable import PrettyTable

RESULT = {}
FIELDS = ('username', 'age', 'tel', 'email')
CONFNAME = "loginInfo.ini"

helpinfo = '''{}
#以下操作均直接对数据库操作
1.  增   add         : add monkey 12 132xxx monkey@51reboot.com
2.  删   delete      : delete monkey
3.  改   update      : update monkey set age = 20
4.  查   list        : list user info from db
5.  搜   find        : find monkey
6.  分页 display     : display page 2 pagesize 3 
7.  帮助 doc         : show help
8.  退出 exit        : exit
{}
'''.format('=' * 70, '=' * 70)

def log(msg:str):
    logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                    filename='agent.log',  #日志存储文件名
                    filemode='a+'  #append 追加方式
                    )
    logging.info(msg)
    cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(cur_time + "  : " + msg)

def login(username, password):
    '''
    验证账号和密码是否正确，如果正确返回True，否则返回False
    '''
    user_passwd_t = ("51reboot", "123456")
    if username == user_passwd_t[0] and password == user_passwd_t[1]:
        return "Login succ", True
    else:
        return "Login fail", False

def logout():
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

def connect():
    cfg, ok = ReadConfig(CONFNAME, 'mysql')
    print(cfg['host'])
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

def addUser(input_user_manage_info:list):
    if len(input_user_manage_info) != 4:
        errMsg = print("Add info invalid, Please add again.")
        return errMsg, False

    #判断用户是否存在，如果用户存在，提示用户已经存在，不再添加
    username = input_user_manage_info[0]
    conn = connect()
    # if not conn:
    #     return "connect db fail", False
    cur = conn.cursor()  # 创建游标
    cur.execute("select username from users;")
    allusers = [ user[0] for user in cur.fetchall() ]
    if username in allusers:
        errMsg = "Username {} already exits.".format(username)
        return  errMsg, False
    else:
        try:
            age = input_user_manage_info[1]
            tel = input_user_manage_info[2]
            email = input_user_manage_info[3]
            sql = "insert into users(username,age,tel,email) values ('{}','{}','{}','{}');".format(username, age, tel, email)
            cur.execute(sql)
            conn.commit()
            succMsg = "User {} Add succ".format(username)
            return succMsg, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()  # 关闭游标
            conn.close()  # 关闭连接

def deleteUser(input_user_manage_info:list):
    # delete monkey
    username = input_user_manage_info[0]
    conn = connect()
    # if not conn:
    #     return "connect db fail", False
    cur = conn.cursor()  # 创建游标
    cur.execute("select username from users;")
    allusers = [user[0] for user in cur.fetchall()]
    if username not in allusers:
        errMsg = "User {} not exits.".format(username)
        return errMsg, False
    else:
        try:
            sql = "delete from users where username = '{}';".format(username)
            cur.execute(sql)
            # print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Delete fail', False
            conn.commit()
            succMsg = "User {} delete succ".format(username)
            return succMsg, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

def updateUser(input_user_manage_info:list):
    # update monkey set age = 20
    username = input_user_manage_info[0]
    where = input_user_manage_info[1]
    fuhao = input_user_manage_info[-2]
    if where != "set" or fuhao != "=":
        errMsg = "Update method error!"
        return  errMsg, False

    conn = connect()
    # if not conn:
    #     return "connect db fail", False
    cur = conn.cursor()  # 创建游标
    cur.execute("select username from users;")
    allusers = [user[0] for user in cur.fetchall()]
    if username not in allusers:
        errMsg = "User {} not exits.".format(username)
        return errMsg, False
    else:
        try:
            update_field = input_user_manage_info[-3]
            update_value = input_user_manage_info[-1]
            # sql = '''update users set age = 20 where username = 'monkey11';'''
            sql = "update users set {} = '{}' where username = '{}';".format(update_field, update_value, username)
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                errMsg = "Update fail"
                return errMsg, False
            conn.commit()
            succMsg = "User {} update succ.".format(username)
            return succMsg, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

def listUser():
    # 如果没有一条记录， 那么提示为空
    conn = connect()
    # if not conn:
    #     return "connect db fail", False
    cur = conn.cursor()  # 创建游标
    try:
        sql = "select * from users;"
        cur.execute(sql)
        rows = cur.fetchall()
        # 增加一行如果查询为空的情况， 如果为空，则返回查询失败
        if len(rows) == 0:
            return "not data", False
        else:
            result = [dict(zip(FIELDS, i)) for i in rows]
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for i in result:
                xtb.add_row(i.values())
            # for k, v in result.items():
            #     xtb.add_row(v.values())
            return xtb, True
    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()

def displayUser(input_user_manage_info:list):
    # dispaly page 2 pagesize 5
    # default = 5
    if len(input_user_manage_info) >= 2 and len(input_user_manage_info) <= 4:
        pagesize = 5
        if len(input_user_manage_info) == 2:
            if input_user_manage_info[0] == "page":
                pagesize = 5
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        else:
            if input_user_manage_info[0] == "page" and input_user_manage_info[2] == "pagesize":
                pagesize = int(input_user_manage_info[-1])
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        page = int(input_user_manage_info[1]) - 1

        conn = connect()
        # if not conn:
        #     return "connect db fail", False
        cur = conn.cursor()  # 创建游标
        try:
            sql = "select * from users;"
            cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = cur.fetchall()
            # 增加一行如果查询为空的情况， 如果为空，则返回查询失败
            if len(rows) == 0:
                return "not data", False
            else:
                result = [list(i) for i in rows]
                # start, end
                start = page * pagesize
                end = start + pagesize

                xtb = PrettyTable()
                xtb.field_names = FIELDS
                for userinfo in result[start:end]:
                    xtb.add_row(userinfo)
                return xtb, True
        finally:
            cur.close()
            conn.close()
    else:
        errMsg = "Input info invalid, Please input again."
        return errMsg, False

def findUser(input_user_manage_info):
    username = input_user_manage_info[0]
    conn = connect()
    # if not conn:
    #     return "connect db fail", False
    cur = conn.cursor()  # 创建游标
    cur.execute("select username from users;")
    allusers = [user[0] for user in cur.fetchall()]
    if username not in allusers:
        errMsg = "User {} not exits.".format(username)
        return errMsg, False
    else:
        try:
            sql = "select * from users where username = '{}';".format(username)
            cur.execute(sql)
            rows = cur.fetchall()
            result = [dict(zip(FIELDS, i)) for i in rows]
            xtb = PrettyTable()
            xtb.field_names = FIELDS
            for i in result:
                xtb.add_row(i.values())
            return xtb, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

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
        if action == "add":
            # add monkey 12 132xxx monkey@51reboot.com
            addMsg, ok = addUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, addMsg)
            log(message)
        elif action == "delete":
            delMsg, ok = deleteUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, delMsg)
            log(message)
        elif action == "update":
            updateMsg, ok = updateUser(input_user_manage_info)
            message = "{}, State: {}, Result: {}".format(action, ok, updateMsg)
            log(message)
        elif action == "list":
            listMsg, ok = listUser()
            if not ok:
                message = "{}, State: {}, Result: {}".format(action, ok, listMsg)
                log(message)
            else:
                print(listMsg)
        elif action == "find":
            findMsg, ok = findUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, findMsg))
            else:
                print(findMsg)
        elif action == "display":
            disMsg, ok = displayUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, disMsg))
            else:
                print(disMsg)
        elif action == "doc":
            print(helpinfo)
        elif action == "exit":
            logout()
        else:
            print("\033[31m invalid action\033[0m")

def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username:")
        password = input("Please input your password:")
        loginMsg, ok = login(username,password)
        if not ok:
            log(loginMsg)
            INIT_FAIL_CNT += 1   #登录失败次数+1
            continue
        log(loginMsg)

        opLogic()
    print("\033[31m \nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))

if __name__ == '__main__':
    main()