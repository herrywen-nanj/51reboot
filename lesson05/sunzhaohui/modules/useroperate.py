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



USERINFO = ("51reboot", "123456")
CONFIG_FILE = 'conf/user_manage.ini'
FIELD_NAMES = ['id','username', 'age', 'tel', 'email']

def Login_Authentication(username,password):
    if username == USERINFO[0] and password == USERINFO[1]:
        return True
    else:
        return False

def Check_User_Exist(username:str):

    sql = "select * from users where username ='{}'".format(username)
    #result,ok = select(sql)
    result,ok = sqloperate.Select(sql)
    if ok:
        rows = result
        if rows:
            return Yellow_print("用户{} 已存在".format(username)),True
        else:
            return Yellow_print("用户{} 不存在".format(username)),False
    else:
        return result,False


def Check_ID_Exist(id:str):
    sql = "select * from users where id ='{}'".format(id)
    #result, ok = select(sql)
    result,ok = sqloperate.Select(sql)
    if ok:
        rows = result
        if rows:

            return "id {} 存在".format(id), True
        else:
            return Yellow_print("id {} 不存在".format(id)), False
    else:
        return result, False

def add_User(info_list:list):
    try:
        username = info_list[1]
        age = info_list[2]
        tel = info_list[3]
        email = info_list[4]
    except:
        info = Red_print('格式不正确')
        print(info)
        return info,False
    info,ok = Check_User_Exist(username)
    if ok:
        print(info)
    else:
        sql = "insert into users(username,age,tel,email)  values('{}','{}','{}','{}')".format(username,age,tel,email)
        #result,ok = insert(sql)
        info,ok = sqloperate.Insert(sql)
        if ok:
            print(Green_Print('添加用户成功'))
        else:
            print(Red_print('添加用户失败:{}'.format(info)))



def delete_User(info_list:list):
    if len(info_list) !=2:
        print(Red_print('格式不正确'))
        return '',False



    # 获取输入的可能是用户名或id

    # 尝试输入的是不是整数，则认为根据id删除
    if info_list[1].isdigit():
        id = info_list[1]
        #判断id是否存在
        info, ok = Check_ID_Exist(id)
        if ok:
            sql = "delete from users where id='{}'".format(id)
            #result,ok = delete(sql)
            info,ok = sqloperate.Delete(sql)
        print (info)

    else:
        # 判断输入的用户名是否存在
        username = info_list[1]
        info, ok = Check_User_Exist(username)
        if ok:
            sql = "delete from users where username='{}'".format(username)
            #result,ok=delete(sql)
            info, ok = sqloperate.Delete(sql)
        print(info)

def update_User(info_list:list):
    if len(info_list) !=6:
        print(Red_print('参数格式不正确'))
        return '',False

    if info_list[-4] != 'set' and info_list[-2] != '=':
        info = Red_print('关键字格式不正确')
        return info, False

    username = info_list[1]
    user_filed = info_list[-3]
    new_value = info_list[-1]
    if user_filed not in FIELD_NAMES:
        print(Red_print('字段 {}不存在'.format(user_filed)))
        return '',False

    # 判断用户是否存在
    info,ok =  Check_User_Exist(username)
    if ok:
        sql = "update users set {} = {} where username='{}'".format(user_filed,new_value,username)
        #result,ok = update(sql)
        info, ok = sqloperate.Update(sql)
    print(info)


def list_User():
    x = PrettyTable()
    x.field_names = FIELD_NAMES

    sql = "select * from users"
    #result,ok = select(sql)
    result, ok = sqloperate.Select(sql)

    if ok:
        for row in result:
            x.add_row(list(row))
        print(x)
    else:
        print(result)



def find_User(info_list:list):
    if len(info_list) != 2:
        print(Red_print('格式不正确'))
        return '', False

    x = PrettyTable()
    x.field_names = FIELD_NAMES
    username = info_list[1].strip()
    sql = "select * from users where username like '%{}%'".format(username)
    #result,ok = select(sql)
    result,ok = sqloperate.Select(sql)
    if ok:
        for row in result:
            row=list(row)
            row[1]=row[1].replace(username,Green_Print(username))
            x.add_row(list(row))
        print(x)
    else:
        print(result)


def display_User(info_list:list):
    x = PrettyTable()
    x.field_names = FIELD_NAMES
    try:
        if info_list[1] != 'page':
            info = '缺少关键字 page'
            return Red_print(info),False
    except:
        info = '格式不正确'
        return Red_print(info),False
    try:
        page = int(info_list[2])
    except:
        info = '格式不正确'
        return Red_print(info), False
    try:
        pagesize = int(info_list[4])
    except:
        pagesize = 5


    sql = 'select * from users'
    #result,ok = select(sql)
    result, ok = sqloperate.Select(sql)

    if ok:
        start =  pagesize * (page - 1)
        end  = start + pagesize
        for row in result[start:end]:
            x.add_row(list(row))
        return x,True
    else:
        return result,False







def export():
    time_str = time.strftime('%Y%m%d%H%M%S')
    csv_filename = time_str + '.csv'
    sql = "select * from users"
    #result,ok = select(sql)
    result, ok = sqloperate.Select(sql)
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
def help():
    help_info = '''
            帮助信息:
            有效字段依次顺序: 'username', 'age', 'tel', 'email'
            增加:  add monkey 12 13200000001 monkey@51reboot.com
            删除: 
               - delete monkey 
               - delete 1 
            修改: 
               - update monkey set age = 18
               - update monkey set tel = 13200000002
               - update monkey set email = xxx@51reboot.com
            列出: list
            查找: find monkey (用户名模糊查询)
            分页： 
                - display page 2 pagesize 5
                - display page 2
            导出: export
            退出: exit
            '''
    return help_info