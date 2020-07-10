'''
create table users(
	username varchar(32) not null,
	age int not null,
	sex char(2) not null CHECK (sex LIKE '男' OR sex LIKE '女'),
	phone char(11) not null CHECK (LEN(phone)=11),
	email varchar(32) not null
);
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : dbutils
# @Software: PyCharm

import pymysql
from luojunquan.utils.log_utils import Logs
from luojunquan.moudules.configmgt import ConfigMgt
import os

CONFIG_FILE = 'conf/dbconfig.ini'
Current_DIR = os.path.abspath(os.path.dirname(__file__))
Home_Dir = os.path.dirname(Current_DIR)
CONFIG_FILE = os.path.join(Home_Dir,CONFIG_FILE)

log = Logs()
configmgt = ConfigMgt()

class Sql_Util(object):
    #数据库链接
    def connect(self):
        cfg,ok = configmgt.ReadConfig(CONFIG_FILE, 'lxjdb')
        if not ok:
            return cfg,False
        try:
            conn = pymysql.connect(
                host = cfg['host'],
                user = cfg['username'],
                password=cfg['password'],
                database=cfg['database'],
                port=int(cfg['port']),
            )
        except Exception as e:
            return None
        return conn

    #数据库增加
    def db_insert(self,sql_insert,data):
        conn = self.connect()
        cur = conn.cursor()
        try:
           cur.execute(sql_insert,data)
           conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            conn.close()

    #数据库删除
    def db_delete(self,username):
        conn = self.connect()
        cur = conn.cursor()
        sql_delete = "delete from users where username = %s"
        try:
            cur.execute(sql_delete,(username))
            log.info('用户{}删除成功'.format(username))
            conn.commit()
        except Exception as e:
            conn.rollback()
        finally:
            conn.close()

    #查询数据库
    def db_qurey(self):
        conn = self.connect()
        cur = conn.cursor()
        sql = '''select * from users'''
        try:
            cur.execute(sql)
            results = cur.fetchall()
            return results
            # for row in results:
            #     '''username,age,sex,phone,email'''
            #     # username = row[0]
            #     # age = row[1]
            #     # sex = row[2]
            #     # phone = row[3]
            #     # email = row[4]
            #     users.setdefault('username':row[0],)
            #     # print(username,age,sex,phone,email)
            #     print(user)
        except Exception as e:
            raise  e
        finally:
            conn.close()

    #更新数据库
    def db_update(self,username,new_username,new_age,new_sex,new_phone,new_email):
        conn = self.connect()
        cur = conn.cursor()
        results = self.db_qurey()
        new_list = []
        for x in results:
            if x[0] == username:
                new_list.append(x)
        #如果用户不输入直接回车，则继续使用以前的数据
        if new_username is '':
            new_username = new_list[0][0]
        if new_age is '':
            new_age = new_list[0][1]
        if new_sex is '':
            new_sex = new_list[0][2]
        if new_phone is '':
            new_phone = new_list[0][3]
        if new_email is '':
            new_email = new_list[0][4]
        data = (new_username,new_age,new_sex,new_phone,new_email,username)
        sql_update = "update users set username = %s,age = %s,sex = %s,phone = %s,email = %s where username = %s"
        try:
            cur.execute(sql_update,(data))
            conn.commit()
            log.info('{}用户更新成功'.format(username))
        except Exception as e:
            conn.rollback()
        finally:
            conn.close()


sql = Sql_Util()
print(sql.connect())