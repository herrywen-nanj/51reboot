#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
Mysql数据库操作模块
Author: Wangxiaoyun
'''
import pymysql,json,ConfigMgt,LogMgt,sys

'''
#数据库建库建表.
#create database ops default character set utf8 collate utf8_unicode_ci;
use ops;
create table yusers
(
UserID varchar(32) not null,
Name varchar(32) not null,
Phone varchar(11),
Company varchar(100),
Address varchar(1000),
Email varchar(100)
);
'''

def Connect():
    userName,ok = ConfigMgt.ReadConfig('config.ini','Mysql','user')
    passWord, ok = ConfigMgt.ReadConfig('config.ini', 'Mysql', 'password')
    Host, ok = ConfigMgt.ReadConfig('config.ini', 'Mysql', 'host')
    dataBase, ok = ConfigMgt.ReadConfig('config.ini', 'Mysql', 'database')
    Port, ok = ConfigMgt.ReadConfig('config.ini', 'Mysql', 'port')
    try:
        conn = pymysql.connect(
            host = Host,
            user = userName,
            password = passWord,
            database = dataBase,
            port = int(Port),
        )
    except Exception as e:
        connMes = str(e)
        LogMgt.UserLog(connMes)
        sys.exit(connMes)
    else:
        connMes = 'Mysql connection successfully.'
        LogMgt.UserLog(connMes)
        return conn,connMes

def Insert(sql):
    conn,connMes = Connect()
    if not conn:
        connMeg = '[Insert] MySQL connection failed.'
        LogMgt.UserLog(connMeg)
        return connMeg,False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
        sqlMsg = 'Executed SQL: {}.'.format(sql)
        inserMsg = 'Insert succ.'
        LogMgt.UserLog(sqlMsg)
        LogMgt.UserLog(inserMsg)
        return inserMsg,True
    except Exception as e:
        conn.rollback()
        inserMsg = str(e)
        LogMgt.UserLog(inserMsg)
        return inserMsg,False
    finally:
        inserMsg = '[Insert] MySQL disconnect.'
        LogMgt.UserLog(inserMsg)
        cur.close()
        conn.close()

def Delete(sql):
    conn,connMes = Connect()
    if not conn:
        deleteMsg = '[Delete] MySQL connection failed.'
        LogMgt.UserLog(deleteMsg)
        return deleteMsg,False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            deleteMsg = 'Delete fail.'
            LogMgt.UserLog(deleteMsg)
            return deleteMsg,False
        else:
            sqlMsg = 'Executed SQL: {}.'.format(sql)
            deleteMsg ='Delete succ'
            LogMgt.UserLog(deleteMsg)
            conn.commit()
        LogMgt.UserLog(sqlMsg)
        return deleteMsg,True
    except Exception as e:
        conn.rollback()
        deleteMsg = str(e)
        LogMgt.UserLog(deleteMsg)
        return deleteMsg,False
    finally:
        deleteMsg = '[delete] MySQL disconnect.'
        LogMgt.UserLog(deleteMsg)
        cur.close()
        conn.close()

def Update(sql):
    conn,connMes = Connect()
    if not Connect():
        updateMsg = '[Update] MySQL connection failed.'
        LogMgt.UserLog(updateMsg)
        return updateMsg,False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            updateMsg = 'MySQL update failed.'
            LogMgt.UserLog(updateMsg)
            return updateMsg,False
        else:
            conn.commit()
            sqlMsg = 'Executed SQL: {}.'.format(sql)
            updateMsg = 'MySQL update successfully.'
            LogMgt.UserLog(sqlMsg)
            LogMgt.UserLog(updateMsg)
            return updateMsg,True
    except Exception as e:
        conn.rollback()
        updateMsg = str(e)
        LogMgt.UserLog(updateMsg)
        return updateMsg,False
    finally:
        updateMsg = '[update] MySQL disconnect.'
        LogMgt.UserLog(updateMsg)
        cur.close()
        conn.close()

def Select(sql):
    conn,connMes = Connect()
    if not conn:
        selectMsg = '[Select] MySQL connection failed.'
        LogMgt.UserLog(selectMsg)
        return selectMsg,False
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except Exception as e:
        selectMsg = str(e)
        LogMgt.UserLog(selectMsg)
        return selectMsg,False
    else:
        rows = cur.fetchall()
        if len(rows) == 0:
            return 'No data found in the table.', False
        else:
            return rows, True
    finally:
        selectMsg = '[select] MySQL disconnect.'
        LogMgt.UserLog(selectMsg)
        cur.close()
        conn.close()

def main(ops,sql):
    if ops.strip().lower() == 'select':
        result,ok = Select(sql)
        if not ok:
            retdata = []
            return retdata,result,ok
        else:
            fields = ['UserID','Name','Phone','Company','Address','Email']
            retdata = [dict(zip(fields, i)) for i in result]    #生成列表格式
            # data = json.dumps(retdata, indent=4)   #生成json格式
            return retdata,result,ok
    elif ops.strip().lower() == 'insert':
        result, ok = Insert(sql)
        if not ok:
            return ok
        else:
            return ok
    elif ops.strip().lower() == 'delete':
        result,ok = Delete(sql)
        if not ok:
            return ok
        else:
            return ok
    elif ops.strip().lower() == 'update':
        result,ok = Update(sql)
        if not ok:
            return ok
        else:
            return ok

# if __name__ == '__main__':
#     sql = '''select * from yusers;'''
#     retdata= main('select',sql)
#     print(retdata)