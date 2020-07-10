import config

import pymysql

FILENAME = 'db.ini'

def connect():
    cfg, ok = config.ReadConfig(FILENAME, 'DB')
    if not ok:
        return cfg, False
    try:
        conn = pymysql.connect(
            host = cfg['host'],
            user = cfg['username'],
            password = cfg['password'],
            port = int(cfg['port'])
        )
    except Exception as e:
        return None
    return conn

def db_add(data):
    conn = connect()
    cur = conn.cursor()
    data = (data[1], data[2], data[3], data[4])
    sql_insert = "insert into ops2.users(username, age, tel, email) values(%s, %s, %s, %s);"
    try:
        cur.execute(sql_insert, data)
        conn.commit()
    except pymysql.DatabaseError:
        conn.rollback()
    finally:
        conn.close()

def db_list():
    conn = connect()
    cur = conn.cursor()      
    sql = "select * from ops2.users"
    try:
        cur.execute(sql)
        result = cur.fetchall()
        return result
    except pymysql.DatabaseError:
        conn.rollback
    finally:
        conn.close()

def db_find(data):
    conn = connect()
    cur = conn.cursor()
    data = data[1]
    sql = "select * from ops2.users where username = %s;"
    try:
        cur.execute(sql, data)
        result = cur.fetchall()
    except pymysql.DatabaseError:
        conn.rollback
    finally:
        conn.close()
    return result

def db_delete(data):
    conn = connect()
    cur = conn.cursor()
    data = data[1]
    sql = "delete from ops2.users where username = %s;"
    try:
        cur.execute(sql, data)
        conn.commit()
    except pymysql.DatabaseError:
        conn.rollback
    finally:
        conn.close()

def db_update(data):
    conn = connect()
    cur = conn.cursor()
    value = data[3]
    data = (data[5], data[1])
    sql = "update ops2.users set {} = %s where username = %s;".format(value)
    try:
        cur.execute(sql, data)
        conn.commit()
    except pymysql.DatabaseError:
        conn.rollback
    finally:
        conn.close()