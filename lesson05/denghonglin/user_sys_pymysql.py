import sys
from utils import dbutils, readcsv
from prettytable import PrettyTable
import csv

import logging
logging.basicConfig(level = logging.DEBUG, \
                    format = '%(asctime)s   %(filename)s [line: %(lineno)d] %(levelname)s %(message)s',\
                    datefmt='%a  %Y-%m-%d %H:%M:%S', \
                    filename='user_mange_sys.log', \
                    filemode='w')
logger = logging.getLogger(__name__)

# 全局变量
FIELDS = ('id','username','age','tel','email')
FILECSV = "user_list.csv"

def inRed(s):
    return highlight('') + "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
def inGreen(s):
    return highlight('') + "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def inYellow(s):
    return highlight('') + "%s[33;2m%s%s[0m"%(chr(27), s, chr(27))
def inPurple(s):
    return highlight('') + "%s[35;2m%s%s[0m"%(chr(27), s, chr(27))
def highlight(s):
    return "%s[30;2m%s%s[1m"%(chr(27), s, chr(27))


def helpDoc():
    Usage = '''
    {} 
      usage:
        help        : help
        add         : add tom 12 132xxx tom@facebook.com
        update      : udpate tom set age = 18
        list        : list
        find        : find tom
        save        : save  (save data to csv)
        load        : load  (load csv to mysql)
        exit        : quit
    {}
    '''.format('-' * 60, '-' * 60)
    print(Usage)

def auth(username, password):
    SYS_USER = ('admin','admin123')
    if username == SYS_USER[0] and password == SYS_USER[1]:
        logger.debug("[%s] login success." %username)
        return True
        # return "Login success.", True
    else:
        return False
        # return "Login fail.", False

def addUser(args):
    # args = "zhangsan 12 132xxxxxx  zhangsan@126.com"
    # args = args.split()
    if len(args) != 4:
        print(inRed("add user failed, args length != 4."))
    username, age, tel, email = args[0], int(args[1]), args[2], args[3]
    sql = '''insert into users(username,age,tel,email) values('%s', '%s', '%s', '%s');''' %(username,age,tel,email)
    msg, ok = dbutils.insert(sql)
    if not ok:
        print(msg)
    # print(msg)
    logger.debug("adduser [%s] success." %username)
    print(inGreen("add user success."))

def deleteUser(args):
    username = args[0]
    if len(args) == 1:
        sql = '''delete from users where username='%s';''' %username
        msg, ok = dbutils.delete(sql)
        if not ok:
            print(msg)
        print(inGreen('Delete user [%s] success.' %username))
        logger.debug("Delete user [%s] success." %username)
    else:
        print(inRed("Delete user failed, args length != 1."))

def updateUser(args):
    # update tom1 set age = 10
    todo, fuhao = args[1], args[-2]
    if len(args) == 5:
        if todo != 'set' or fuhao != '=':
            print(inYellow("Syntax error."))
        else:
            username, set_field, set_value = args[0], args[2], args[-1]
            sql = '''update users set %s=%s where username='%s';''' %(set_field,set_value,username)
            msg, ok = dbutils.update(sql)
            if not ok:
                print(msg)
            # print(msg)
            print(inGreen("Update user[{}] success.".format(username)))
            logger.debug("update [%s] success. command: %s" %(username,sql))
    else:
        print(inRed("Update user failed, args length != 5."))

def listUser():
    sql  = '''select * from users;'''
    msg, ok = dbutils.select(sql)
    if not ok:
        print(msg)
    tb = PrettyTable()
    tb.field_names = FIELDS
    for i in msg:
        tb.add_row(i)
    print(tb)

def findUser(args):
    # find tom
    username = args[0]
    if len(args) == 1:
        sql  = '''select * from users where username='%s';''' %username
        msg, ok = dbutils.select(sql)
        if not ok:
            print(msg)
        tb = PrettyTable()
        tb.field_names = FIELDS
        for i in msg:
            tb.add_row(i)
        print(tb)
    else:
        print(inYellow('Find user failed, args != 1'))

def mysql2csv():
    sql = '''select * from users;'''
    data, flag = dbutils.select(sql)
    with open(FILECSV, 'w+') as fo:
        csv_writer = csv.writer(fo,dialect='excel')
        csv_writer.writerow(FIELDS)
        for line in data:
            csv_writer.writerow(line)
    print(inGreen('user_data save to csv.'))
    logger.debug("MySQL users save to [%s]" %FILECSV)


def csv2mysql():
    csv_data = readcsv.read_csv(FILECSV)
    for i in csv_data:
        username, age, tel, email = i[1], i[2], i[3], i[4]
        sql = '''insert into users(username,age,tel,email) values('%s', '%s', '%s', '%s');''' %(username,age,tel,email)
        msg, ok = dbutils.insert(sql)
        if not ok:
            print(msg)
        # print(msg)
    logger.debug("Load csv to mysql [%s] success." % FILECSV)
    print(inGreen("Load csv to mysql [%s] success." % FILECSV))

def logout():
    sys.exit(0)

def logic():
    helpDoc()
    while True:
        cmd_str = input("Please input commond: ")
        if len(cmd_str) == 0:
            print("command invalid.")
        cmd_str = cmd_str.split()
        action = cmd_str[0]
        args = cmd_str[1:]
        if action == 'add':
            addUser(args)
        elif action == 'delete':
            deleteUser(args)
        elif action == 'update':
            updateUser(args)
        elif action == 'find':
            findUser(args)
        elif action == 'list':
            listUser()
        elif action == 'save':
            mysql2csv()
        elif action == 'load':
            csv2mysql()
        elif action == 'help':
            helpDoc()
        elif action == 'exit' or action == 'quit':
            logout()
        else:
            print(inYellow("input invalid."))

def main():
    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:
        username = input("Please input username: ")
        password = input("Please input password: ")
        if auth(username, password):
            print(inGreen("{}\nWelcome to User Management System\n{}".format('-'*40,'-'*40)))
            logic()
        else:
            print(inRed("Username or password error."))
            init_fail_count += 1
    print(inYellow("Game Over."))


if __name__ == '__main__':
    main()