import configmgt
import pymysql

"""
查看实验效果函数
def connet():
    cfg, ok = configmgt.ReadConfig('db.ini', 'db_kw')
    if not ok:
        return cfg

    try:
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['user'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )

    except:
        return None
    return conn

def userList(sql):
    conn = connet()
    if not conn:
        return 'conn db fail.', False
    cur = conn.cursor()  # 创建一个游标

    try:
        cur.execute(sql)  # 执行sql语句
        conn.commit()  # 提交执行的sql语句# 从游标里获取所有数据
        data = cur.fetchall()
        return data, True
    except Exception as e:
        return e, False
    finally:
        cur.close() # 关闭游标
        conn.close()  # 关闭连接

def userDelete(sql):
    conn = connet()
    if not conn:
        return 'conn db fail.', False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return 'Delete fail', False
        conn.commit()
        return 'Insert success.', True
    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()

def userUpdate(sql):
    pass

def userAdd(sql):
    conn = connet()
    if not conn:
        return 'conn db fail.', False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
        return 'Insert success.', True
    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()



def userFind(sql):
    conn = connet()
    if not conn:
        return 'conn db fail.', False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return 'Delete fail', False
        conn.commit()

        data = cur.fetchall()
        return data, True

    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()
"""

def sqlOperation(sql, seek=False):
    conn = connet()
    if not conn:
        return 'conn db fail.', False
    cur = conn.cursor()

    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return 'operation fail', False
        conn.commit()

        if seek:
            data = cur.fetchall()
            return data, True
        return 'operation success.', True

    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()



def main():

    def sel():
        sql = "select * from users where username='kw3'"
        msg, ok = userFind(sql)
        if not ok:
            print(msg)
        else:
            print(msg)

    sel()


if __name__ == '__main__':
    main()



