# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-25 19:16'


import time
import csv
from prettytable import PrettyTable



from .myprint import Yellow_print
from .myprint import Red_print
from .myprint import Green_Print

from  .  import  sqloperate
from . import  check






FIELD_NAMES = ['id','username', 'age', 'tel', 'email']


SqlOp = sqloperate.SqlOp()
Check = check.Check()

class User(object):
    def __init__(self,info_list):
        self.info_list = info_list



    def add_User(self):
        try:
            username = self.info_list[1]
            age = self.info_list[2]
            tel = self.info_list[3]
            email = self.info_list[4]
        except:
            info = Red_print('格式不正确')
            print(info)
            return info, False

        info, ok = Check.Check_User_Exist(username)
        if ok:
            print(info)
        else:
            sql = "insert into users(username,age,tel,email)  values('{}','{}','{}','{}')".format(username, age, tel,
                                                                                                  email)
            # result,ok = insert(sql)
            info, ok = SqlOp.Insert(sql)
            if ok:
                print(Green_Print('添加用户成功'))
            else:
                print(Red_print('添加用户失败:{}'.format(info)))


    def delete_User(self):
        if len(self.info_list) !=2:
            print(Red_print('格式不正确'))
            return '',False



        # 获取输入的可能是用户名或id

        # 尝试输入的是不是整数，则认为根据id删除
        if self.info_list[1].isdigit():
            id = self.info_list[1]
            #判断id是否存在
            info, ok = Check.Check_ID_Exist(id)
            if ok:
                sql = "delete from users where id='{}'".format(id)
                #result,ok = delete(sql)
                info,ok = SqlOp.Delete(sql)
            print (info)

        else:
            # 判断输入的用户名是否存在
            username = self.info_list[1]
            info, ok = Check.Check_User_Exist(username)
            if ok:
                sql = "delete from users where username='{}'".format(username)
                #result,ok=delete(sql)
                info, ok = SqlOp.Delete(sql)
            print(info)

    def update_User(self):
        if len(self.info_list) !=6:
            print(Red_print('参数格式不正确'))
            return '',False

        if self.info_list[-4] != 'set' and self.info_list[-2] != '=':
            info = Red_print('关键字格式不正确')
            return info, False

        username = self.info_list[1]
        user_filed = self.info_list[-3]
        new_value = self.info_list[-1]
        if user_filed not in FIELD_NAMES:
            print(Red_print('字段 {}不存在'.format(user_filed)))
            return '',False

        # 判断用户是否存在
        info,ok =  Check.Check_User_Exist(username)
        if ok:
            sql = "update users set {} = {} where username='{}'".format(user_filed,new_value,username)
            #result,ok = update(sql)
            info, ok = SqlOp.Update(sql)
        print(info)


    def list_User(self):
        x = PrettyTable()
        x.field_names = FIELD_NAMES

        sql = "select * from users"
        #result,ok = select(sql)
        result, ok = SqlOp.Select(sql)

        if ok:
            for row in result:
                x.add_row(list(row))
            print(x)
        else:
            print(result)



    def find_User(self):
        if len(self.info_list) != 2:
            print(Red_print('格式不正确'))
            return '', False

        x = PrettyTable()
        x.field_names = FIELD_NAMES
        username = self.info_list[1].strip()
        sql = "select * from users where username like '%{}%'".format(username)
        #result,ok = select(sql)
        result,ok = SqlOp.Select(sql)
        if ok:
            for row in result:
                row=list(row)
                row[1]=row[1].replace(username,Green_Print(username))
                x.add_row(list(row))
            print(x)
        else:
            print(result)


    def display_User(self):
        x = PrettyTable()
        x.field_names = FIELD_NAMES
        try:
            if self.info_list[1] != 'page':
                info = '缺少关键字 page'
                return Red_print(info),False
        except:
            info = '格式不正确'
            return Red_print(info),False
        try:
            page = int(self.info_list[2])
        except:
            info = '格式不正确'
            return Red_print(info), False
        try:
            pagesize = int(self.info_list[4])
        except:
            pagesize = 5


        sql = 'select * from users'
        result,ok = SqlOp.Select(sql)

        if ok:
            start =  pagesize * (page - 1)
            end  = start + pagesize
            for row in result[start:end]:
                x.add_row(list(row))
            return x,True
        else:
            return result,False







    def export(self):
        time_str = time.strftime('%Y%m%d%H%M%S')
        csv_filename = time_str + '.csv'
        sql = "select * from users"
        #result,ok = select(sql)
        result, ok = SqlOp.Select(sql)
        if ok:
            try:
                with open(csv_filename, "w") as f:
                    writer = csv.writer(f)
                    writer.writerow(FIELD_NAMES)
                    for row in result:
                        writer.writerow(list(row))
                info = Green_Print('已生成csv文件: {} '.format(csv_filename))
                return info,True
            except:
                info = Red_print('导出csv文件失败')
                return info,False
        else:
            info = result
            return info,False