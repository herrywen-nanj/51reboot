import pymysql
from .myparse import getconfig

DBHOST = getconfig('Config.ini', 'dbconfig')


def connnet():
    try:

        conn = pymysql.connect(
            host = DBHOST['host'],
            user = DBHOST['username'],
            password= DBHOST['password'],
            database = DBHOST['database'],
            port = int(DBHOST['port']),
            )
    except:
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

def update():
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
        return rows, True
    finally:
        cur.close()
        conn.close()

def exist(sql):
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
        if cur.rowcount != 1:
            return 'Delete fail', False
        conn.commit()
        return 'Delete succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def clear(sql):
    conn = connnet()
    if not conn:
        return "conn db fail", False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        #print(cur.rowcount)
        if cur.rowcount == 0:
            return 'Clear tables fail', False

        conn.commit()
        return 'Clear tables succ.', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def main():

    #for i in range(10, 30):
    #    sql = '''insert into users(username,age,tel,email)  values('monkey{}', 12,'132xxx','monkey2@51reboot.com');'''.format(i)
    #    insertMsg, ok = insert(sql)
    #    if not ok:
    #        print(insertMsg)

    #sql = '''delete from users where username = 'monkey10';'''
    #deleteMsg, ok = delete(sql)
    #if not ok:
    #    print(deleteMsg)
    sql = ''' select * from ops.users where username like 'monkey101%';'''
    existMsg,ok = exist(sql)
    print(existMsg,ok)

if __name__ == '__main__':
    main()
