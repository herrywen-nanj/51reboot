# CREATE DATABASE IF NOT EXISTS ops  DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
# CREATE TABLE users (id  INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,username varchar(32),age int, tel varchar(11), email varchar(50));

import pymysql
# import configmgt
from . import configmgt

FILENAME = "/home/vagrant/51reboot/zuoye/day5/utils/db_config.cfg"
SECTIONS = "dbinfo"

def connet():
    cfg, ok = configmgt.ReadConfig(FILENAME, SECTIONS)
    if not ok:
        return cfg, False
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

def insert(sql):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return "Insert Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def update(sql):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if  cur.rowcount == 0:
            return "Update Fail.", False
        conn.commit()
        return "Update Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def select(sql):
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
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
    conn = connet()
    if not conn:
        return "Connect DB fail.", False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return "Delete Fail.", False
        conn.commit()
        return "Delete Success.", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

# def main():
# #     # insert
#     for i in range(10):
#         sql = '''insert into users(username,age,tel,email) values('lisi{}', 20, '15710xxxx', 'lisi{}@126.com');'''.format(i,i)
#         # sql = '''delete from users where username='lisi{}';'''.format(i)
#         msg, ok = delete(sql)
#         if not ok:
#             print(msg)
#         print(msg)

    # delete
    # sql = '''delete from users where username='lisi1';'''
    # msg, ok = delete(sql)
    # if not ok:
    #     print(msg)
    # print(msg)

    # update
    # sql = '''update users set age=100 where username='lisi2';'''
    # msg, ok = update(sql)
    # if not ok:
    #     print(msg)
    # print(msg)

    # select
#     sql = '''select * from users;'''
#     result, ok = select(sql)
#     if not ok:
#         print(result)
#     else:
#         fields = ['id','username','age','tel','email']
#         # for i in result:
#         #     print(dict(zip(fields,i)))
#         retdata = [dict(zip(fields,i)) for i in result ]
#         import json
#         print(json.dumps(retdata, indent=4))
#
# if __name__ == '__main__':
#     main()
#     sql  = '''select * from users'''
#     # select(sql)
#     msg, ok = select(sql)
#     if not ok:
#         print(msg)
#     print(msg)