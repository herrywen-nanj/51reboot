# 标准模块
import sys,json,logging,pymysql
import configmgt,dbutils


# 第三方模块
from prettytable import PrettyTable

FIELDS = ['username', 'age', 'tel', 'email']
RESULT = {}
class DB(object):
    def insert(self):
        for i, x in RESULT.items():
            b = list(RESULT[i].values())
            sql_insert = '''insert into users(username,age,tel,email)  values('{}', {},'{}','{}');'''.format(b[0], b[1],b[2], b[3])
            dbutils.insert(sql_insert)
    def load(self):
       # sql_select = '''select username,age,tel,email from users;'''
        sql_select = "select {} from users".format(','.join(FIELDS))
        rows, ok = dbutils.select(sql_select)
        if ok:
           # global RESULT
            RESULT = { x[0] : {FIELDS[0] : x[0] ,FIELDS[1] :x[1] ,FIELDS[2] : x[2],FIELDS[3] : x[3] }for x in rows}
            return RESULT
            #print(RESULT)
        #return RESULT
RESULT=DB().load()
print(RESULT)
