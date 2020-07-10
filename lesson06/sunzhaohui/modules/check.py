# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-01 16:42'

from .myprint import Yellow_print
from .myprint import Red_print
from .myprint import Green_Print

from  .  import  sqloperate


SqlOp = sqloperate.SqlOp()

class Check(object):
    def Check_User_Exist(self,username: str):

        sql = "select * from users where username ='{}'".format(username)
        # result,ok = select(sql)
        result, ok = SqlOp.Select(sql)
        if ok:
            rows = result
            if rows:
                return Yellow_print("用户{} 已存在".format(username)), True
            else:
                return Yellow_print("用户{} 不存在".format(username)), False
        else:
            return result, False

    def Check_ID_Exist(self,id: str):
        sql = "select * from users where id ='{}'".format(id)
        # result, ok = select(sql)
        result, ok = SqlOp.Select(sql)
        if ok:
            rows = result
            if rows:

                return "id {} 存在".format(id), True
            else:
                return Yellow_print("id {} 不存在".format(id)), False
        else:
            return result, False









