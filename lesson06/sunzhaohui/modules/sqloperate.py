# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-25 16:35'

import pymysql
import sys

from . import config
from . import myprint
from . import db


result,ok =  config.GetConfig()
if ok:
    DB_INFO = result['mysqld']
    host = DB_INFO['host']
    port = int(DB_INFO['port'])
    user = DB_INFO['user']
    password = DB_INFO['password']
    database = DB_INFO['database']
else:
    info = result
    print(info)
    sys.exit()

m = db.Mysql_Connect(host=host,port=port,user=user,password=password,database=database)
result,ok = m.connect()

if ok:
    conn = result
else:
    print(result)
    sys.exit(1)

class SqlOp(object):

    def Insert(self,sql):

        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return '', True
        except Exception as e:
            conn.rollback()
            return myprint.Red_print(e), False
        finally:
            cur.close()
            #conn.close()

    def Delete(self,sql):


        cur = conn.cursor()
        try:
            cur.execute(sql)
            if cur.rowcount == 0:
                return myprint.Red_print('Delete fail'), False
            conn.commit()
            return myprint.Green_Print('Delete succ.'), True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            #conn.close()

    def Update(self,sql):
        cur = conn.cursor()

        try:
            cur.execute(sql)
            conn.commit()
            return myprint.Green_Print('Update succ.'), True
        except Exception as e:
            conn.rollback()
            return myprint.Red_print(e), False
        finally:
            cur.close()
            #conn.close()



    def Select(self,sql):

        cur = conn.cursor()
        try:
            cur.execute(sql)
        except Exception as e:
            return e, False

        else:
            rows = cur.fetchall()
            return rows, True
        finally:
            cur.close()
            #conn.close()




