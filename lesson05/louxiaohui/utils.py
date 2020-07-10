#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql
from configmgt import readconfig
import sys


dbinfo, ok = readconfig('config.ini', 'dbinfo')


def connnet():
    dbinfo['port'] = int(dbinfo['port'])
    try:
        conn = pymysql.connect(**dbinfo)
    except Exception as e:
        print (e)
        return None
    return conn


def insert(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return 'Insert succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()


def update(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Update fail', False

        conn.commit()
        return 'Update succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()


def select(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
    except Exception as e:
        return e, False
    else:
        rows = cur.fetchall()
        if len(rows) == 0:
            return "Empty set.", False
        else:
            return rows, True
    finally:
        cur.close()
        conn.close()


def delete(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
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


def main():

    #for i in range(10, 30):
    #    sql = '''insert into users(username,age,tel,email)  values('monkey{}', {},'132xxx','monkey{}@51reboot.com');'''.format(i, i ,i)
    #    insertMsg, ok = insert(sql)
    #    if not ok:
    #        print(insertMsg)

    # sql = '''delete from users where username = 'monkey10';'''
    # deleteMsg, ok = delete(sql)
    # if not ok:
    #     print(deleteMsg)
    # sql = '''update users set age = 20 where username = 'monkey11';'''
    # msg, ok = update(sql)
    # if not ok:
    #     print(msg)

    sql = '''select * from users limit 2;'''
    result, ok = select(sql)
    if not ok:
        print(result)
    else:
        fields = ['id', 'username', 'age', 'tel', 'email']
        # for i in result:
        #     print(dict(zip(fields, i)))
        retdata = [ dict(zip(fields, i)) for i in result ]
        import json
        print(json.dumps(retdata, indent=4))


#if __name__ == '__main__':
#    main()
