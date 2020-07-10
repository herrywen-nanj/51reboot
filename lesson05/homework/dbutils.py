import pymysql

from configmgt import ReadConfig

FILENAME = '51reboot.ini'

def connnet():
    cfg, ok = ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        return cfg, False
    try:
        # conn = pymysql.connect(
        #     host = "10.0.2.15",
        #     user = "monkey",
        #     password= "123456",
        #     database = "ops",
        #     port = 3306,
        #     )
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
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
        # 增加一行如果查询为空的情况， 如果为空，则返回查询失败
        if len(rows) == 0:
            return '', False
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

    # for i in range(10, 30):
    #     sql = '''insert into users(username,age,tel,email)  values('monkey{}', 12,'132xxx','monkey2@51reboot.com');'''.format(i)
    #     insertMsg, ok = insert(sql)
    #     if not ok:
    #         print(insertMsg)

    # sql = '''delete from users where username = 'monkey10';'''
    # deleteMsg, ok = delete(sql)
    # if not ok:
    #     print(deleteMsg)
    # sql = '''update users set age = 20 where username = 'monkey11';'''
    # msg, ok = update(sql)
    # if not ok:
    #     print(msg)

    sql = '''select * from users;'''
    result, ok = select(sql)
    print(result)
    if not ok:
        print(result)
    else:
        fields = ['id', 'username', 'age', 'tel', 'email']
        # for i in result:
        #     print(dict(zip(fields, i)))
        retdata = [ dict(zip(fields, i)) for i in result ]

        import json
        print(json.dumps(retdata, indent=8))

if __name__ == '__main__':
    main()