import pymysql
from . import ReadConfig


class MySQLHelper(object):
    def __init__(self):
        self.FILENAME = "/Users/superlk/PycharmProjects/xly1/lesson05/liukai/homework/config.ini"
        self.conn = self.connect()

    def connect(self):
        cfg, ok = ReadConfig.ReadConfig(self.FILENAME, 'mysql')
        if not ok:
            return False
        try:
            conn = pymysql.connect(
                host=cfg['host'],
                user=cfg['user'],
                password=cfg['password'],
                database=cfg['db'],
                port=int(cfg['port'])
            )
        except Exception as e:
            print("mysql connect error ", e)
            return None
        return conn

    def insert(self, sql):
        conn = self.conn
        if not conn:
            return "conn is none", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return 'insert success', True
        except Exception as e:
            print("insert error", e)
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def update(self, sql):
        conn = self.conn
        if not conn:
            return "conn is none", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            if cur.rowcount != 1:
                return 'update fail', False
            conn.commit()
            return 'update success', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def select(self, sql):
        conn = self.conn
        if not conn:
            return "conn is none", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            # if cur.rowcount != 1:
            #     return 'select all  fail', False
            result = cur.fetchall()
            return result, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def get_one(self, sql):
        conn = self.conn
        if not conn:
            return "conn is none", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            if cur.rowcount != 1:
                return 'get on  fail', False
            result = conn.fetchone()
            return result, True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()

    def delete(self, sql):
        conn = self.conn
        if not conn:
            return "conn is none", False
        cur = conn.cursor()
        try:
            cur.execute(sql)
            if cur.rowcount != 1:
                return 'delete fail', False
            conn.commit()
            return 'delete success', True
        except Exception as e:
            conn.rollback()
            return e, False
        finally:
            cur.close()
            conn.close()
