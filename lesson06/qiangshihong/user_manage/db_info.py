#!/usr/bin/python
# author: qsh

#!/usr/bin/python

import pymysql

class DB_info(object):
    def __init__(self,host,user,password,database,port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def connect(self):
        # # 获取配置文件 db_connect 章节下字段(字典类型)，成功 ok = True,失败 ok =False
        # cfg, ok = configmgt.ReadConfig(FILENAME, 'db_connect')
        # if not ok:
        #     return cfg, False
        try:
            conn = pymysql.connect(
                self.host,
                self.user,
                self.password,
                self.database,
                self.port,
            )
            # # 创建连接
            # conn = pymysql.connect(
            #     host="localhost",
            #     user="root",
            #     password="123456",
            #     database="ops",
            #     port=3306,
            # )
        except:
            return None
        return conn