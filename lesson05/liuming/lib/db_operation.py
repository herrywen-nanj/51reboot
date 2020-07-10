#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         db_opreation.py
# Description:  封装数据库操作函数
# Author:       Aaron
# Date:         2019/6/24
# -------------------------------------------------------------------------------
import pymysql
from settings import DB_CONN_INFO


# Format of function return
result = {
    "status": 0,
    "msg": "",
    "data": "",
}


# Establish a connection to the database
def connection():
    try:
        conn = pymysql.connect(
            host=DB_CONN_INFO["host"],
            port=DB_CONN_INFO["port"],
            user=DB_CONN_INFO["user"],
            passwd=DB_CONN_INFO["passwd"],
            db=DB_CONN_INFO["db"],
        )
        conn.autocommit(True)
    except Exception as e:
        return False
    return conn


def insert(table_name, data):
    conn = connection()
    if not conn:
        return False

    sql = "insert into {}(username, age, tel, email) values({});".format(
        table_name, ",".join(["'{}'".format(i) for i in data])
    )
    # print(sql)
    try:
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result["status"], result["msg"], result["data"] = 0, "insert success.", ""
    except Exception as e:
        result["status"], result["msg"], result["data"] = 1, e, ""
    finally:
        cursor.close()
        conn.close()
    return result


def delete(table_name, data):
    conn = connection()
    if not conn:
        return False
    sql = "delete from {} where username='{}';".format(table_name, data)
    # print(sql)

    try:
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result["status"], result["msg"], result["data"] = 0, "delete success.", ""
    except Exception as e:
        conn.rollback()
        result["status"], result["msg"], result["data"] = 1, e, ""
    finally:
        cursor.close()
        conn.close()
    return result


def select(table_name):
    conn = connection()
    if not conn:
        return None

    sql = "select * from {};".format(table_name)
    # print(sql)
    try:
        # 游标设置为字典类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        rows = cursor.fetchall()
        result["status"], result["msg"], result["data"] = 0, "query all of user success.", rows
    except Exception as e:
        result["status"], result["msg"], result["data"] = 1, e, ""
    finally:
        cursor.close()
        conn.close()

    return result


def update(table_name, data, where):
    conn = connection()
    if not conn:
        return None

    sql = "update {} set {} where {};".format(
        table_name, ",".join(["{}='{}'".format(k, data[k]) for k in data.keys()]), where)
    # print(sql)
    try:
        # 游标设置为字典类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        result["status"], result["msg"], result["data"] = 0, "update success.", ""
    except Exception as e:
        result["status"], result["msg"], result["data"] = 1, e, ""
    finally:
        cursor.close()
        conn.close()

    return result


def get_one(table_name, data):
    conn = connection()
    if not conn:
        return None

    try:
        sql = "select * from {} where username='{}';".format(table_name, data)
        # print(sql)
        # 游标设置为字典类型
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql)
        row = cursor.fetchone()
        result["status"], result["msg"], result["data"] = 0, "query info of [{}] success.".format(data), row
    except Exception as e:
        result["status"], result["msg"], result["data"] = 1, e, ""
    finally:
        cursor.close()
        conn.close()

    return result


if __name__ == "__main__":
    # res = test()
    # print(res)
    # get_one("users", "user1")
    pass
