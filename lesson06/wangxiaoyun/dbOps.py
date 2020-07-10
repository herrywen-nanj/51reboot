#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
Mysql数据库操作模块
Author: Wangxiaoyun
'''
import pymysql,json,sys
from logMgt import logs
from configMgt import configs

class db(object):
    '''
    #数据库建库建表.
    #create database ops default character set utf8 collate utf8_unicode_ci;
    use ops;
    create table yusers
    (
    UserID varchar(32) not null,
    Name varchar(32) not null,
    Phone varchar(11),
    Company varchar(100),
    Address varchar(1000),
    Email varchar(100)
    );
    '''
    def __init__(self,ops,sql):
        self.ops = ops
        self.sql = sql

    def conns(self):
        filename = 'config.ini'
        users = configs(filename, 'Mysql', 'user')
        word = configs(filename, 'Mysql', 'password')
        hosts = configs(filename, 'Mysql', 'host')
        data = configs(filename,'Mysql', 'database')
        ports = configs(filename,'Mysql', 'port')

        username,ok = users.read()
        password,ok = word.read()
        host,ok = hosts.read()
        database,ok = data.read()
        port,ok = ports.read()

        try:
            conn = pymysql.connect(
                host=host,
                user=username,
                password=password,
                database=database,
                port=int(port),
            )
        except Exception as e:
            mes = str(e)
            log = logs(mes)
            log.mgt()
            sys.exit(mes)
        else:
            mes = 'Mysql connection successfully.'
            log = logs(mes)
            log.mgt()
            return conn, mes

    def checks(self):
        conn, mes = self.conns()
        if not conn:
            meg = '[{}] MySQL connection failed.'.format(self.ops)
            log = logs(mes)
            log.mgt()
            return meg, False
        cur = conn.cursor()
        return cur,conn

    def modify(self):
        cur,conn = self.checks()
        try:
            cur.execute(self.sql)
            if cur.rowcount == 0:
                msg = '{} fail.'.format(self.ops)
                log = logs(msg)
                log.mgt()
                return msg, False
            else:
                sqlMsg = 'Executed SQL: {}.'.format(self.sql)
                msg = '{} succ'.format(self.ops)
                log1 = logs(msg)
                log1.mgt()
                conn.commit()
                log2 = logs(sqlMsg)
                log2.mgt()
                return msg, True
        except Exception as e:
            conn.rollback()
            msg = str(e)
            log = logs(msg)
            log.mgt()
            return msg, False
        finally:
            msg = '[{}] MySQL disconnect.'.format(self.ops)
            log = logs(msg)
            log.mgt()
            cur.close()
            conn.close()

    def insert(self):
        cur,conn = self.checks()

        try:
            cur.execute(self.sql)
            conn.commit()
            sqlMsg = 'Executed SQL: {}.'.format(self.sql)
            msg = 'Insert succ.'
            log1 = logs(sqlMsg)
            log1.mgt()
            log2 = logs(msg)
            log2.mgt()
            return msg, True
        except Exception as e:
            conn.rollback()
            msg = str(e)
            log = logs(msg)
            log.mgt()
            return msg, False
        finally:
            inserMsg = '[Insert] MySQL disconnect.'
            log = logs(inserMsg)
            log.mgt()
            cur.close()
            conn.close()

    def delete(self):
        msg,ok = self.modify()
        return msg, ok

    def update(self):
        msg,ok = self.modify()
        return msg,ok

    def select(self):
        cur, conn = self.checks()

        try:
            cur.execute(self.sql)
        except Exception as e:
            msg = str(e)
            log = logs(msg)
            log.mgt()
            return msg, False
        else:
            rows = cur.fetchall()
            if len(rows) == 0:
                retdata = []
                # return 'No data found in the table.', False
                return retdata,False
            else:
                fields = ['UserID', 'Name', 'Phone', 'Company', 'Address', 'Email']
                retdata = [dict(zip(fields, i)) for i in rows]  # 生成列表格式
                # data = json.dumps(retdata, indent=4)   #生成json格式
                return retdata, True
        finally:
            msg = '[select] MySQL disconnect.'
            log = logs(msg)
            log.mgt()
            cur.close()
            conn.close()

# if __name__ == '__main__':
#     sql = '''select * from yusers;'''
#     retdata = db('select',sql)
#     result, ok = retdata.select()
#     print(ok)

    # sql = '''insert into yusers values('stu2','bob','12188888888','None','None','None');'''
    # retdata = db('insert',sql)
    # result,ok = retdata.insert()
    # print(result)

    # sql = '''update yusers set Phone = '18955555555' where UserID = 'stu1';'''
    # retdata = db('update',sql)
    # result,ok = retdata.update()
    # print(result)

    # sql = '''delete from yusers where UserID = "stu2";'''
    # retdata = db('delete',sql)
    # result,ok = retdata.delete()
    # print(result)
    # print(ok)

