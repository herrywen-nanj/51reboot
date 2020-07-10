import configparser
import pymysql
from prettytable import PrettyTable
import sys
import logging

FILENAME = "51reboot.ini"
FILEDS = ['id', 'username', 'age', 'tel', 'email']


def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "config init is empty.", False
    if key:
        if section in config.sections():
            return dict(config[section][key]), True
        else:
            return '', False
    else:
        return dict(config[section]), True


def connect():
    cfg, ok = ReadConfig(FILENAME, "db")
    if not ok:
        return cfg, False
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


def addUser(args):
    '''
    add monkey 12 188*** monkey@qq.com
    agrs: monkey 12 188*** monkey@qq.com
    :param args:
    :return:
    '''
    userinfo = args.split()
    if len(userinfo) != 4:
        return "addUser failed, args length != 4", False
    username = userinfo[0]
    conn = connect()
    cur = conn.cursor()
    sql = "select username from users;"
    cur.execute(sql)
    allusers = cur.fetchall()
    usernames = [user[0] for user in allusers]
    if username in usernames:
        return "user {} already exists.".format(username), False
    else:
        age = userinfo[1]
        tel = userinfo[2]
        email = userinfo[3]
        sql = "insert into users(username,age,tel,email) values ('{}','{}','{}','{}');".format(username, age, tel,
                                                                                               email)
        cur.execute(sql)
        conn.commit()
        print("add user {} succ.".format(username))
    cur.close()
    conn.close()


def deleteUser(agrs):
    '''
    delete monkey
    agrs: monkey
    :param agrs:
    :return:
    '''
    userinfo = agrs.split()
    if len(userinfo) != 1:
        return "deleteUser failed, args length != 1", False
    username = userinfo[0]
    conn = connect()
    cur = conn.cursor()
    sql = "select username from users;"
    cur.execute(sql)
    allusers = cur.fetchall()
    usernames = [user[0] for user in allusers]
    if username not in usernames:
        return "user {} not found.".format(username), False
    else:
        sql = "delete from users where username = '{}';".format(username)
        cur.execute(sql)
        conn.commit()
        print("delete user {} succ.".format(username))
        opLog().info("delete user {} succ.".format(username))
    cur.close()
    conn.close()


def updateUser(agrs):
    '''
    update monkey set age = 20
    agrs: monkey set age = 20
    :param agrs:
    :return:
    '''
    userinfo = agrs.split()
    if len(userinfo) != 5:
        return "updateUser failed,args length != 5", False
    if userinfo[1] == "set" and userinfo[-2] == "=":
        username = userinfo[0]
        conn = connect()
        cur = conn.cursor()
        sql = "select username from users;"
        cur.execute(sql)
        allusers = cur.fetchall()
        usernames = [user[0] for user in allusers]
        if username not in usernames:
            return "user {} not found.".format(username), False
        else:
            filed = userinfo[2]
            value = userinfo[-1]
            sql = "update users set {} = '{}' where username = '{}';".format(filed, value, username)
            cur.execute(sql)
            conn.commit()
            print("update user {} succ.".format(username))
        cur.close()
        conn.close()
    else:
        return "Syntax error", False


def listUser():
    conn = connect()
    cur = conn.cursor()
    sql = "select * from users;"
    cur.execute(sql)
    result = cur.fetchall()
    if not result:
        return None
    else:
        retdata = [dict(zip(FILEDS, i)) for i in result]
    xtb = PrettyTable()
    xtb.field_names = FILEDS
    for i in retdata:
        xtb.add_row(i.values())
    print(xtb)


def findUser(agrs):
    '''
    find monkey
    args：monkey
    :param agrs:
    :return:
    '''
    userinfo = agrs.split()
    if len(userinfo) != 1:
        return "findUser failed,args length != 1", False
    username = agrs
    conn = connect()
    cur = conn.cursor()
    sql = "select username from users;"
    cur.execute(sql)
    allusers = cur.fetchall()
    usernames = [user[0] for user in allusers]
    if username not in usernames:
        return "user {} not found.".format(username), False
    else:
        sql = "select * from users where username = '{}';".format(username)
        cur.execute(sql)
        result = cur.fetchall()
        retdata = [dict(zip(FILEDS, i)) for i in result]
    xtb = PrettyTable()
    xtb.field_names = FILEDS
    for i in retdata:
        xtb.add_row(i.values())
    print(xtb)


def displayUser(args):
    '''
    display page 2 pagesize 5
    agrs: page 2 pagesize 5
    default pagesize 5
    :param args:
    :return:
    '''
    userinfo = args.split()
    if len(userinfo) >= 2 and len(userinfo) <= 4:
        if len(userinfo) == 2:
            pagesize = 5
            if userinfo[0] == "page":
                pagenum = int(userinfo[1])
                start = (pagenum - 1) * pagesize
                end = start + pagesize
                # print("start: {},end: {}".format(start,end))
                conn = connect()
                cur = conn.cursor()
                sql = "select * from users;"
                cur.execute(sql)
                result = cur.fetchall()
                if not result:
                    return None
                else:
                    retdata = [list(i) for i in result]
                xtb = PrettyTable()
                xtb.field_names = FILEDS
                for i in retdata[start:end]:
                    xtb.add_row(i)
                print(xtb)
            else:
                return "Syntax error", False
        elif len(userinfo) == 4:
            if userinfo[0] == "page" and userinfo[2] == "pagesize":
                pagenum = int(userinfo[1])
                pagesize = int(userinfo[-1])
                start = (pagenum - 1) * pagesize
                end = start + pagesize
                # print("start: {},end {}".format(start,end))
                conn = connect()
                cur = conn.cursor()
                sql = "select * from users;"
                cur.execute(sql)
                result = cur.fetchall()
                if not result:
                    return None
                else:
                    retdata = [list(i) for i in result]
                xtb = PrettyTable()
                xtb.field_names = FILEDS
                for i in retdata[start:end]:
                    xtb.add_row(i)
                print(xtb)
            else:
                return "Syntax error", False
        else:
            return "displayUser faild,args length !=2 and !=4", False
    else:
        return "Syntax error", False


def logout():
    sys.exit(0)


def opLog():
    logname = "access.log"
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    fh = logging.FileHandler(logname)
    fmt = logging.Formatter(
        '[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s')
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger


def loginAuth(username, password):
    userpassinfo = ('51reboot', '123456')
    if username == userpassinfo[0] and password == userpassinfo[1]:
        return "login succ.", True
    else:
        return "login faild.", False


def logic():
    while True:
        userinfo = input("Please input your action: ")
        info = userinfo.split()
        if len(info) == 0:
            print("input action invald.")
        else:
            action = info[0]
            info_string = ' '.join(info[1:])
            if action == "add":
                addUser(info_string)
            elif action == "delete":
                deleteUser(info_string)
            elif action == "update":
                updateUser(info_string)
            elif action == "list":
                listUser()
            elif action == "find":
                findUser(info_string)
            elif action == "display":
                displayUser(info_string)
            elif action == "logout":
                logout()


def main():
    min_fail_cnt = 0
    max_fail_cnt = 3
    while min_fail_cnt < max_fail_cnt:
        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        msg, ok = loginAuth(username, password)
        if ok:
            print("\n\tWelcome to user magage system.\n")
            opLog().info(msg)
            logic()
        else:
            min_fail_cnt += 1
            print("username or password valid failed.")
            opLog().info(msg)
    print("Input {} times failed,Terminal will exit.".format(max_fail_cnt))


if __name__ == "__main__":
    main()
