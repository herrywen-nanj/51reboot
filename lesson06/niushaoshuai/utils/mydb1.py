import pymysql
from .myparse import getconfig

DBHOST = getconfig('Config.ini', 'dbconfig')

class DB(object):
    def __init__(self):
        try:

            self.conn = pymysql.connect(
                host = DBHOST['host'],
                user = DBHOST['username'],
                password= DBHOST['password'],
                database = DBHOST['database'],
                port = int(DBHOST['port']),
                )
            self.cur = self.conn.cursor()
        except:
            return None


    def insert(self,sql):
        if not self.conn:
            return "conn db fail", False

        try:
            self.cur.execute(sql)
            self.conn.commit()
            return 'Insert succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False


    def update(self):
        if not self.conn:
            return "conn db fail", False

        try:
            self.cur.execute(sql)
            if self.cur.rowcount == 0:
                return 'Update fail', False

            self.conn.commit()
            return 'Update succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False



    def select(self,sql):
        if not self.conn:
            return "conn db fail", False

        try:
            self.cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = self.cur.fetchall()
            return rows, True


    def exist(self,sql):
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.execute(sql)
        except Exception as e:
            return e, False
        else:
            rows = self.cur.fetchall()
            return rows, True

    def delete(self,sql):
        if not self.conn:
            return "conn db fail", False

        try:
            self.cur.execute(sql)
            if self.cur.rowcount != 1:
                return 'Delete fail', False
            self.conn.commit()
            return 'Delete succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False


    def clear(self,sql):
        if not self.conn:
            return "conn db fail", False

        try:
            self.cur.execute(sql)
            if self.cur.rowcount == 0:
                return 'Clear tables fail', False
            self.conn.commit()
            return 'Clear tables succ.', True
        except Exception as e:
            self.conn.rollback()
            return e, False

    def __del__(self):
        self.cur.close()
        self.conn.close()



