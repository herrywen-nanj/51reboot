#!/bin/env python3
# -*- coding:utf-8 -*-


from mconf import  ReadConfig
import pymysql
import json


log_filed=["id","name","password"]
# Mysql 连接
def conect():
    result, ok = ReadConfig("mysql.ini", "mydb", "host")
    if not ok: return  result, False
    try:
        conn = pymysql.connect(host=result['host'],
                               user=result['name'],
                               password=result['passwd'],
                               database=result['database'])
    except Exception as e:
        return e,False
    else:
        return conn


# 检查用户信息
def user_check(sql):
    conn = conect()
    if not conn: return "connect db Field", False

    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        data = cur.fetchall()
        redata = [dict(zip(log_filed, i)) for i in data]
        # print(redata)
        rdata = json.dumps(redata, indent=2)
        return rdata,True
    finally:
        cur.close()
        conn.close()

# 添加用户信息
def add_info(sql):
    conn = conect()
    if not conn:
        return "Connet Db failed", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        cur.rollback()
        return e, False
    else:
        return "insert succ", True
    finally:
        cur.close()
        conn.close()

# 删除信息
def del_info(sql):
    conn = conect()
    if not conn: return "Connect Db faild", False

    cur = conn.cursor()
    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount != 1:
            print("Delete False")
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e, False
    else:
        return "Delete Succ",True
    finally:
        cur.close()
        conn.close()

# 修改信息
def update_info(sql):
    conn = conect()

    if not conn: return "Connect Db Faild",True

    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        return e, False
    else:
        return "update succ", True
    finally:
        cur.close()
        conn.close()

# 查找
def search(sql):
    # pass
    conn = conect()
    if not conn: return "connect db failed", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        data = cur.fetchall()
        return data, True
    finally:
        cur.close()
        conn.close()

