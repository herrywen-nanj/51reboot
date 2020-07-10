# CREATE DATABASE IF NOT EXISTS ops  DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
# CREATE TABLE users (id  INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,username varchar(32),age int, tel varchar(11), email varchar(50));

import pymysql

class DBOp(object):
    def __init__(self,host,user,password,port,db):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.db = db

    def connet(self):
        try:
            conn = pymysql.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                port = self.port,
                database = self.db
                 )
        except:
            return None
        return conn

    def insert(self,sql):
        conn = self.connet()
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

    def update(self,sql):
        conn = self.connet()
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
            conn.close()\

    def select(self,sql):
        conn = self.connet()
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

    def delete(self, sql):
        conn = self.connet()
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

#
# if __name__ == '__main__':
#     host = "localhost"
#     user = "root"
#     password = "root123"
#     database = "ops"
#     port = 3306
#     db = DBOp(host,user,password,port)
#     # sql = '''insert into users(username,age,tel,email) values('lisi122', 120, '112211xxxx', 'lisi1211@126.com');'''
#     # sql = '''update users set age=100 where username='haha';'''
#     # sql = '''select * from users;'''
#     sql = '''delete from users where username='lisi102';'''
#     # db.insert(sql)
#     # db.update(sql)
#     # print(db.select(sql))
#     db.delete(sql)
