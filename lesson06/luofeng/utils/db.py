#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-07-06
# Filename: db.py
# Describe:
#*******************************************

import sys
import json
import os.path
import pymysql
from logzero import logger
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from parser import config_file_parser

class SQLOperation(object):
    '''数据库管理'''

    def __init__(self):
        self.host = config_file_parser('DATABASE', 'db_host')
        self.user = config_file_parser('DATABASE', 'db_user')
        self.passwd = config_file_parser('DATABASE', 'db_pass')
        self.dbname = config_file_parser('DATABASE', 'db_name')
        self.port = config_file_parser('DATABASE', 'db_port')

    def __get_db_conn__(self):
        '''连接数据库'''
        return pymysql.connect(host = self.host, port = int(self.port), user = self.user, password = self.passwd, database = self.dbname)

    def __exec_sql__(self, sql):
        conn = self.__get_db_conn__()
        cursor = conn.cursor()

        try:
            cursor.execute(sql)
            conn.commit()
            return True

        except Exception as e:
            conn.rollback()
            return False

        finally:
            conn.close()

    def insert(self, username, age, tel, email, address):
        '''插入用户信息'''
        sql = "insert into userinfo(username, age, tel, email, address) value('%s', '%s', '%s', '%s', '%s')" %(username, age, tel, email, address)

        result = self.__exec_sql__(sql)
        if result:
            logger.info('{} data insert db is success..'.format(username))
        else:
            logger.error('Data was inserted failed !!!')

    def select(self, username):
        '''查询用户信息'''
        sql = "select * from userinfo where username = '%s'" %(username)
        conn = self.__get_db_conn__()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchone()
            return data

        except Exception as e:
            logger.error(e)
            return False

        finally:
            conn.close()

    def delete(self, username):
        '''删除用户信息'''
        sql = "delete from userinfo where username = '%s'" %(username)
        result = self.__exec_sql__(sql)
        if result:
            logger.info('{} data has been successfully deleted.'.format(username))
        else:
            logger.error('User data deletion error !!!')

    def update(self, username, age, tel, email, address):
        '''更新用户信息'''
        sql = "update userinfo set username='%s', age='%s', tel='%s', email='%s', address='%s' where username = '%s'" %(username, age, tel, email, address, username)

        print(sql)
        result = self.__exec_sql__(sql)
        if result:
            logger.info('{} data has been successfully updated.'.format(username))
        else:
            logger.error('User data updated error !!!')
