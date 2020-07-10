import dbutils
import config
import log
import sys

log = log.Log()

FILEDS = ['username', 'age', 'tel', 'email']
FILENAME = "51reboot.ini"

cfg = config.CONFIG()
msg, ok = cfg.readconfig(FILENAME, 'db')
if ok:
    db = dbutils.DB(msg['host'], msg['user'], msg['password'], int(msg['port']))


class User(object):
    def add(self, name, age, tel, email):
        res, ok = db.select("select username from users where username = '{}';".format(name))
        if not ok:
            fields_string = ','.join(FILEDS)
            values_string = "'{}', {}, '{}', '{}'".format(name, age, tel, email)
            sql = '''INSERT INTO users({}) VALUES({});'''.format(fields_string, values_string)
            db.insert(sql)
        else:
            print("username: {} already exists.".format(name))

    def delete(self, name):
        res, ok = db.select("select username from users where username = '{}';".format(name))
        if ok:
            sql = "delete from users where username = '{}';".format(name)
            msg, ok = db.delete(sql)
            log.opLog().info(msg)
        else:
            print("username: {} not found.".format(name))

    def update(self, name, field, value):
        res, ok = db.select("select username from users where username = '{}';".format(name))
        if ok:
            sql = '''update users set {} = '{}' where username = '{}';'''.format(field, value, name)
            db.update(sql)
        else:
            print('username: {} not found.'.format(name))

    def find(self, name):
        data, ok = db.select("select * from users where username = '{}';".format(name))
        if ok:
            return data
        else:
            print('username: {} not found.'.format(name))

    def list(self):
        data, ok = db.select("select * from users;")
        return data

    def display(self, page, pagesize=5):
        if page and not pagesize:
            pagesize = 5
            start = (int(page) - 1) * pagesize
            end = start + pagesize
            sql = "select * from users;"
            res, ok = db.select(sql)
            if ok:
                result = [list(i) for i in res]
                return result[start:end]
        elif page and pagesize:
            start = (int(page) - 1) * int(pagesize)
            end = start + int(pagesize)
            sql = "select * from users;"
            res, ok = db.select(sql)
            if ok:
                result = [list(i) for i in res]
                return result[start:end]
