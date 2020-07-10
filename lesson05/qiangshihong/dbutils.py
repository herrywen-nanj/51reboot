#!/usr/bin/python

import pymysql
from config import configmgt

FILENAME = 'config/mysql_config.ini'

def connect():
    # 获取配置文件 db_connect 章节下字段(字典类型)，成功 ok = True,失败 ok =False
    cfg,ok = configmgt.ReadConfig(FILENAME,'db_connect')
    if not ok:
        return cfg,False
    try:
        # 打开数据库连接
        db_conn = pymysql.connect(
            # 获取配置文件 db_connect 章节下各 key 的值
            host=cfg['host'],
            user=cfg['user'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port'])
        )
        return db_conn
    except:
        return None

def select(sql):
    # 打开数据库连接
    db_conn = connect()
    #如果连接不成功，抛错
    if not db_conn:
        return "conn db fail",False
    # 使用 cursor() 方法创建一个游标对象 cur
    cur = db_conn.cursor()

    try:
        # 使用 execute() 方法执行 SQL 查询
        cur.execute(sql)
        # 使用 fetchall() 方法接收全部的返回结果行.
        rows = cur.fetchall()
        return rows, True
    except Exception as e:
        return e, False
    finally:
        # 关闭游标
        cur.close()
        # 关闭数据库连接
        db_conn.close()

def insert(sql):
    conn = connect()
    if not conn:
        return "conn db fail.",False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return 'succ',True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()
def update(sql):
    conn = connect()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Update fail', False
        cur.execute(sql)
        conn.commit()
        return 'Update succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def delete(sql):
    conn = connect()
    if not conn:
        return "conn db fail.", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        #打印sql执行后影响的行数
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Delete fail', False

        conn.commit()
        return 'Insert succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()


