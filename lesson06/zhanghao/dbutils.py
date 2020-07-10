import pymysql


class DB(object):
    def __init__(self, host, username, password, port, db='ops'):
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.db = db

    def select(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.db,
                port=self.port,
            )
        except:
            return "conn db fail."
        else:
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                return e
            else:
                rows = cur.fetchall()
                if len(rows) == 0:
                    return '', False
                else:
                    return rows, True
            finally:
                cur.close()
                conn.close()

    def insert(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.db,
                port=self.port,
            )
        except:
            return "db conn fail."
        else:
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                return e
            else:
                conn.commit()
                return 'insert succ.', True
            finally:
                cur.close()
                conn.close()

    def update(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.db,
                port=self.port,
            )
        except:
            return "db conn fail."
        else:
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                return e
            else:
                conn.commit()
                return 'update succ.', True
            finally:
                cur.close()
                conn.close()

    def delete(self, sql):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.db,
                port=self.port,
            )
        except:
            return "db conn fail."
        else:
            cur = conn.cursor()
            try:
                cur.execute(sql)
            except Exception as e:
                return e
            else:
                conn.commit()
                return 'delete succ.', True
            finally:
                cur.close()
                conn.close()
