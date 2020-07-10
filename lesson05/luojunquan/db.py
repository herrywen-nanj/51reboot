#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : dbutils
# @Software: PyCharm

import pymysql
import configmgt
from log_utils import Logs

FILENAME = 'dbconfig.ini'
log = Logs()

#数据库链接
def connect():
    cfg,ok = configmgt.ReadConfig(FILENAME,'lxjdb')
    if not ok:
        return cfg,False
    try:
        conn = pymysql.connect(
            host = cfg['host'],
            user = cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except Exception as e:
        return None
    return conn

#数据库增加
def db_insert(data):
    conn = connect()
    cur = conn.cursor()
    sql_insert = "insert into users(username,age,sex,phone,email) values (%s,%s,%s,%s,%s);"
    try:
       cur.execute(sql_insert,data)
       conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()

#数据库删除
def db_delete(username):
    conn = connect()
    cur = conn.cursor()
    sql_delete = "delete from users where username = %s"
    try:
        cur.execute(sql_delete,(username))
        log.info('用户{}删除成功'.format(username))
        conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()


#查询数据库
def db_qurey():
    conn = connect()
    cur = conn.cursor()
    sql = '''select * from users'''
    try:
        cur.execute(sql)
        results = cur.fetchall()
        return results
        # for row in results:
        #     '''username,age,sex,phone,email'''
        #     # username = row[0]
        #     # age = row[1]
        #     # sex = row[2]
        #     # phone = row[3]
        #     # email = row[4]
        #     users.setdefault('username':row[0],)
        #     # print(username,age,sex,phone,email)
        #     print(user)
    except Exception as e:
        raise  e
    finally:
        conn.close()

#更新数据库
def db_update(username,new_username,new_age,new_sex,new_phone,new_email):
    conn = connect()
    cur = conn.cursor()
    results = db_qurey()
    new_list = []
    for x in results:
        if x[0] == username:
            new_list.append(x)
    #如果用户不输入直接回车，则继续使用以前的数据
    if new_username is '':
        new_username = new_list[0][0]
    if new_age is '':
        new_age = new_list[0][1]
    if new_sex is '':
        new_sex = new_list[0][2]
    if new_phone is '':
        new_phone = new_list[0][3]
    if new_email is '':
        new_email = new_list[0][4]
    data = (new_username,new_age,new_sex,new_phone,new_email,username)
    sql_update = "update users set username = %s,age = %s,sex = %s,phone = %s,email = %s where username = %s"
    try:
        cur.execute(sql_update,(data))
        conn.commit()
        log.info('{}用户更新成功'.format(username))
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()


