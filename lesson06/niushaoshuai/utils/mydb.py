import pymysql


class DB(object):

    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.database = database
        self.conn = None

    def connect(self):
        try:

            self.conn = pymysql.connect(
                host = self.host,
                user = self.username,
                password= self.password,
                database = self.database,
                port = self.port,
                )
            self.cur = self.conn.cursor()
        except:
            return None


    def insert(self,sql):
        self.connect()
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
        self.connect()
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
        self.connect()
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
        self.connect()
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
        self.connect()
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
        self.connect()
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
        self.connect()
        if not self.conn:
            return "conn db fail", False
        try:
            self.cur.close()
            self.conn.close()
        except:
            pass
    def close(self):
        self.__del__()



