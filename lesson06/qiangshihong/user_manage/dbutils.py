#!/usr/bin/python

from .db_info import DB_info
from config import configmgt

FILENAME = 'config/mysql_config.ini'

class DB_Command(object):

    def connect():
        # 获取配置文件 db_connect 章节下字段(字典类型)，成功 ok = True,失败 ok =False
        cfg, ok = configmgt.ReadConfig(FILENAME, 'db_connect')
        if not ok:
            return cfg, False
        conn_info = DB_info(cfg['host'], cfg['user'], cfg['password'], cfg['database'], int(cfg['port']))
        db_conn = conn_info.connect()
        return db_conn


    def select(sql):
        # 打开数据库连接
        db_conn = DB_Command.connect()
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
        db_conn = DB_Command.connect()
        #如果连接不成功，抛错
        if not db_conn:
            return "conn db fail",False
        # 使用 cursor() 方法创建一个游标对象 cur
        cur = db_conn.cursor()
        try:
            cur.execute(sql)
            db_conn.commit()
            return 'succ',True
        except Exception as e:
            db_conn.rollback()
            return e, False
        finally:
            cur.close()
            db_conn.close()
    def update(sql):
        db_conn = DB_Command.connect()
        # 如果连接不成功，抛错
        if not db_conn:
            return "conn db fail", False
        # 使用 cursor() 方法创建一个游标对象 cur
        cur = db_conn.cursor()

        try:
            cur.execute(sql)
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Update fail', False
            cur.execute(sql)
            db_conn.commit()
            return 'Update succ.', True
        except Exception as e:
            db_conn.rollback()
            return e, False
        finally:
            cur.close()
            db_conn.close()

    def delete(sql):
        db_conn = DB_Command.connect()
        # 如果连接不成功，抛错
        if not db_conn:
            return "conn db fail", False
        # 使用 cursor() 方法创建一个游标对象 cur
        cur = db_conn.cursor()

        try:
            cur.execute(sql)
            #打印sql执行后影响的行数
            print(cur.rowcount)
            if cur.rowcount == 0:
                return 'Delete fail', False

            db_conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            db_conn.rollback()
            return e, False
        finally:
            cur.close()
            db_conn.close()


