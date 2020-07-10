import sys
from .dbutils import DBOp
from . import configmgt

from prettytable import PrettyTable
import csv
import logging
logging.basicConfig(level = logging.DEBUG, \
                    format = '%(asctime)s   %(filename)s [line: %(lineno)d] %(levelname)s %(message)s',\
                    datefmt='%a  %Y-%m-%d %H:%M:%S', \
                    filename='user_mange_sys.log', \
                    filemode='w')
logger = logging.getLogger(__name__)



class UserOp(object):
    def __init__(self,conf,sections):
        self.FIELDS = ('id','username','age','tel','email')
        self.conf = conf
        self.secitons = sections
        self.cfg = configmgt.ReadConfig(self.conf, sections)
        host = self.cfg['host'],
        user = self.cfg['user'],
        password = self.cfg['password'],
        database = self.cfg['database'],
        port = int(self.cfg['port']),
        self.DBOp = DBOp(host,user,password,port,database)

    def addUser(self,args):
        # args = "zhangsan 12 132xxxxxx  zhangsan@126.com"
        # args = args.split()
        if len(args) != 4:
            print("add user failed, args length != 4.")
        username, age, tel, email = args[0], int(args[1]), args[2], args[3]
        sql = '''insert into users(username,age,tel,email) values('%s', '%s', '%s', '%s');''' % (username, age, tel, email)
        msg, ok = DBOp.insert(sql)
        if not ok:
            print(msg)
        # print(msg)
        logger.debug("adduser [%s] success." % username)
        print("add user success.")

    def deleteUser(self,args):
        username = args[0]
        if len(args) == 1:
            sql = '''delete from users where username='%s';''' %username
            msg, ok = DBOp.delete(sql)
            if not ok:
                print(msg)
            print('Delete user [%s] success.' %username)
            logger.debug("Delete user [%s] success." %username)
        else:
            print("Delete user failed, args length != 1.")

    def updateUser(self,args):
        # update tom1 set age = 10
        todo, fuhao = args[1], args[-2]
        if len(args) == 5:
            if todo != 'set' or fuhao != '=':
                print("Syntax error.")
            else:
                username, set_field, set_value = args[0], args[2], args[-1]
                sql = '''update users set %s=%s where username='%s';''' %(set_field,set_value,username)
                msg, ok = DBOp.update(sql)
                if not ok:
                    print(msg)
                # print(msg)
                print("Update user[{}] success.".format(username))
                logger.debug("update [%s] success. command: %s" %(username,sql))
        else:
            print("Update user failed, args length != 5.")

    def listUser(self):
        sql  = '''select * from users;'''
        msg, ok = DBOp.select(sql)
        if not ok:
            print(msg)
        tb = PrettyTable()
        tb.field_names = self.FIELDS
        for i in msg:
            tb.add_row(i)
        print(tb)

    def findUser(self,args):
        # find tom
        username = args[0]
        if len(args) == 1:
            sql  = '''select * from users where username='%s';''' %username
            msg, ok = DBOp.select(sql)
            if not ok:
                print(msg)
            tb = PrettyTable()
            tb.field_names = self.FIELDS
            for i in msg:
                tb.add_row(i)
            print(tb)
        else:
            print('Find user failed, args != 1')

    # def mysql2csv(self):
    #     sql = '''select * from users;'''
    #     data, flag = dbutils.select(sql)
    #     with open(FILECSV, 'w+') as fo:
    #         csv_writer = csv.writer(fo,dialect='excel')
    #         csv_writer.writerow(FIELDS)
    #         for line in data:
    #             csv_writer.writerow(line)
    #     print('user_data save to csv.')
    #     logger.debug("MySQL users save to [%s]" %FILECSV)
    #
    #
    # def csv2mysql(self):
    #     csv_data = readcsv.read_csv(FILECSV)
    #     for i in csv_data:
    #         username, age, tel, email = i[1], i[2], i[3], i[4]
    #         sql = '''insert into users(username,age,tel,email) values('%s', '%s', '%s', '%s');''' %(username,age,tel,email)
    #         msg, ok = dbutils.insert(sql)
    #         if not ok:
    #             print(msg)
    #         # print(msg)
    #     logger.debug("Load csv to mysql [%s] success." % FILECSV)
    #     print("Load csv to mysql [%s] success." % FILECSV)
