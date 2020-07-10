# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-25 16:35'

import pymysql
import sys

from . import config
from . import myprint

'''
CONFIG_FILE = 'user_manage.ini'

DB_INFO, ok = configmgt.ReadConfig(CONFIG_FILE, 'mysqld')
if ok:
    DB_HOST = DB_INFO['host']
    DB_PORT = int(DB_INFO['port'])
    DB_USER = DB_INFO['user']
    DB_PASSWORD = DB_INFO['password']
    DB_DATABASE = DB_INFO['database']
else:
    info = DB_INFO
    print(info)
    sys.exit()
'''

result,ok =  config.GetConfig()
if ok:
    DB_INFO = result['mysqld']
    DB_HOST = DB_INFO['host']
    DB_PORT = int(DB_INFO['port'])
    DB_USER = DB_INFO['user']
    DB_PASSWORD = DB_INFO['password']
    DB_DATABASE = DB_INFO['database']
else:
    info = result
    print(info)
    sys.exit()

def db_connect():
    try:
        conn = pymysql.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_DATABASE,
                port=DB_PORT,
            )
        return conn,True
    except Exception as e:
        return e,False

def Insert(sql):
    result,ok = db_connect()
    if ok:
        conn = result
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
            conn.close()
    else:
        return result,False
def Delete(sql):
    result,ok = db_connect()
    if ok:
        conn = result
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
            conn.close()
    else:
        return result, False
def Update(sql):
    result,ok = db_connect()
    if ok:
        conn = result
        cur = conn.cursor()

        try:
            cur.execute(sql)
            #print(cur.rowcount)
            #if cur.rowcount == 0:
            #    return Red_print('Update fail'), False

            conn.commit()
            return myprint.Green_Print('Update succ.'), True
        except Exception as e:
            conn.rollback()
            return myprint.Red_print(e), False
        finally:
            cur.close()
            conn.close()

    else:
        return result, False

def Select(sql):
    result, ok = db_connect()
    if ok:
        conn = result
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
            conn.close()

    else:
        return result, False
       #return Red_print(result), False
