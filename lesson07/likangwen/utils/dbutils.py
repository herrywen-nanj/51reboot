from config import configmgt
import pymysql
import sys, os

class DBOperation():
    def __init__(self):
        pass

    def connet(self):
        cfg, ok = configmgt.ReadConfig('config/db.ini', 'db_config')
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

    def sqlOperation(self, sql, seek=False):
        conn = self.connet()
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

    d = DBOperation()
    d.connet()

    sql = "select * from users"
    msg, ok = d.sqlOperation(sql, seek=True)
    print(msg)
    print(ok)
    """"""


if __name__ == '__main__':
    sys.path.append(os.path.dirname(sys.path[0]))



