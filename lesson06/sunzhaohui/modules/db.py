# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-01 11:11'


import pymysql

class Mysql_Connect(object):
    def __init__(self,host,port,user,password,database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
           conn = pymysql.connect(
               host=self.host,
               port=self.port,
               user=self.user,
               password=self.password,
               database=self.database

                )
           return conn,True
        except Exception as e:
            print('error')
            return e,False


