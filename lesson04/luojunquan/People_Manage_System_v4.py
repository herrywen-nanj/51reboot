#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 21:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 用户登录认证管理系统V3
# @Software: PyCharm

"""
1. 登录认证；
2.添加: add username age sex phone_number email_address
3.删除: delete user_name
4.修改: update user_name set field_name = value
5.列出: list
6.查找: find user_name
7.分页: display page 1 pagesize 5
8.导出(csv格式文件): save
9.导入(指定的csv格式): load
10.退出: exit
"""
# 标准模块
import csv
import os
import sys
import getpass
import re
import time
from prettytable import PrettyTable

# 定义变量
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
FILENAME = '51reboot.csv'
USERINFO = {'51reboot': {"password": "123456"}}
# Student_all = {'name':'张三', 'age':12,'sex':'男','phone':13993845165,'email':'q@qq.com'}
Student_all = {}
phone_add = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198,
             130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 133, 149, 153, 173, 177, 180, 181, 189, 191,
             199]
mail_pattern = re.compile(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$')

People_Tips =  """\033[36m
        你可以进行的操作:
        1.添加, 示例: add username age sex phone_number email_address
        2.删除, 示例: delete user_name
        3.修改, 示例: update user_name set field_name = value
        4.列出, 示例: list
        5.查找, 示例: find user_name
        6.分页, 示例: display page 1 pagesize 5
        7.导出(csv格式文件), 示例: save
        8.导入(指定的csv格式), 示例: load
        9.退出, 示例: exit
\033[0m"""

TODAY = time.strftime('%Y-%m-%d', time.localtime())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 日志文件所在路径
LOG_FILE_PATH = os.path.join(BASE_DIR, "{}-People_Manage_System_v4.log".format(TODAY))

# 定义功能函数
# 检测用户登录
def check_user_login(user_name, pass_word):
    if user_name not in USERINFO.keys() or USERINFO[user_name]['password'] != pass_word:
        return False
    else:
        log.info("user [{}] login success.".format(user_name))
    return True
# 检测用户登录
def check_user_permission(user_name):
    return USERINFO[user_name]
# 检测用户是否存在
def check_user(name):
    if Student_all.__contains__(name):
        return True
    return False
# 检查用户输入内容是否有误
def check_input_type(age=None, phone=None, mail=None):
    if age is not None:
        if not age.isdigit():
            return "\033[1;31m年龄有误\033[0m"
    if phone is not None:
        if len(phone) != 11:
            return "\033[1;31m手机号有误\033[0m"
        # 提取用户输入手机号的前三位,并转化为int类型
        head = int(''.join(list(phone[:3])))
        if head not in phone_add:
            return "\033[1;31m手机号有误,暂不支持虚拟运营商!!!\033[0m"
    if mail is not None:
        # 粗略写的正则，凑活着用
        m = mail_pattern.match(mail)
        if m is None:
            return "\033[1;31m邮件格式有误 eg: xxx@xxx.com\033[0m"
    return True
# 增加用户
def add(infolist, user_name):  # 之所以写infolist是因为如果定义成info_list 不符合PEP8规范
    global Student_all
    # add monkey 12 13987654321 monkey@51reboot.com
    # 检测用户输入，长度必须为5，个字段分别为：动作、姓名、年龄、手机号、邮箱
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    if len(infolist) != 6:
        return "\033[1;31m输入有误，请检查输入内容 eg: add monkey 12 132xxx monkey@51reboot.com\033[0m"
    tag = check_input_type(age=infolist[2], phone=infolist[4], mail=infolist[5])
    name = infolist[1]
    if tag is not True:
        return tag
    elif tag is True:
        if check_user(name):
            log.info('用户{}已经存在'.format(name))
            print("\033[1;31m添加失败{}已存在\033[0m".format(name))
        else:
            print("\033[1;31m{}用户添加成功\033[0m".format(name))
            log.info('用户{}添加成功'.format(name))
    # if check_user(name):
    #     log.info('用户{}已经存在'.format(name))
    #     print("\033[1;31m添加失败{}已存在\033[0m".format(name))
    Student_all[name] = {"age": info_list[2], "sex": info_list[3], "tel": info_list[4], "email": info_list[5]}
    # print(Student_all)
    return True
# 删除用户
def delete(infolist, user_name):
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    # delete monkey
    if len(infolist) != 2:
        return "\033[1;31m输入有误，请检查输入内容 eg: delete monkey\033[0m"
    name = infolist[1]
    if check_user(name):
        Student_all.pop(name)
        log.info('用户{}删除成功'.format(name))
        print(["\033[1;32;40m用户{}删除成功\033[0m".format(name)])
    return "\033[1;31m用户{}删除失败，无此用户\033[0m".format(name)
# 更新用户
def update(infolist, user_name):
    # ['username', 'age', 'tel', 'email']
    # update monkey set age = 18
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    if Student_all.__contains__(infolist[1]):
        # print(Student_all.__contains__(infolist[1]))
        Student_all[info_list[1]]['age'] = info_list[5]
        log.info('用户{}更新成功'.format(info_list[1]))
        print('用户{}更新成功'.format(infolist[1]))
        # return "\033[1;32;40m用户{}更新成功\033[0m".format(infolist[1])
# 精确查找
def find(user_name):
    if check_user(user_name):
        if Student_all.get(user_name):
            table()
        else:
            print("User {} not found.".format(username))
    return False
#优雅的格式化输出
def table():
    tb = PrettyTable()
    for x in Student_all.keys():
        tb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
        tb.add_row([x, Student_all[x]['age'], Student_all[x]['sex'], Student_all[x]['tel'], Student_all[x]['email']])
    print(tb)
#保存用户
def save():
    with open(FILENAME, 'w',newline='') as f:
        csv_writer = csv.writer(f,dialect='excel')
        csv_writer.writerow(['用户名', '年龄', '性别', '电话', 'E-mail'])
        for x in Student_all.keys():
            csv_writer.writerow([x, Student_all[x]['age'], Student_all[x]['sex'], Student_all[x]['tel'], Student_all[x]['email']])
        print("\033[32m数据保存在{}中！\033[0m".format(FILENAME))
#重载用户
def load():
    global Student_all
    try:
        csv_file = csv.reader(open(FILENAME,'r'))
        for x in csv_file:
            if x[0] == '用户名':
                continue
            else:
                Student_all[x[0]] = {'age':x[1],'sex':x[2],'tel':x[3],'email':x[4]}
        print("\033[32m成功从{}获取到数据！\033[0m".format(FILENAME))
    except Exception as e:
        print(e)
#分页
def display():
    page = int(info_list[2])
    pagesize = int(info_list[4])
    data = list(Student_all.keys())
    tb = PrettyTable()
    if (page - 1) * pagesize <= len(data):
        for x in data[(page - 1) * pagesize:page * pagesize]:
            tb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
            tb.add_row(
                [x, Student_all[x]['age'], Student_all[x]['sex'], Student_all[x]['tel'], Student_all[x]['email']])
    else:
        # 如果现有数据只能生成一页分页
        for x in data[0:pagesize]:
            tb.field_names = ['用户名', '年龄', '性别', '电话', 'E-mail']
            tb.add_row(
                [x, Student_all[x]['age'], Student_all[x]['sex'], Student_all[x]['tel'], Student_all[x]['email']])
    print(tb)

#日志模块
def Logs():
    import logging

    # 其中有个name参数，默认值为root
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(filename=LOG_FILE_PATH, mode='a', encoding='utf-8')

    # # 再创建一个handler，用于输出到控制台
    # ch = logging.StreamHandler()

    # 定义handler的输出格式formatter
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    # ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger

log = Logs()
while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    # 设置密码输入为非明文方式，IDE 下不可用
    password = getpass.getpass(prompt="Please input your password: ")
    login_tag = check_user_login(username, password)
    if login_tag:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        print(People_Tips)
        while True:
            # 业务逻辑
            name_age_sex_phone = input('请分别输入姓名、年龄、性别、手机号、邮箱，中间以空格形式：')
            info_list = name_age_sex_phone.split()
            try:
                action = info_list[0]
            except Exception as e:
                print('检查输入的格式',e)
                # print('检查输入的格式',e)
            if action == "add":
                name = info_list[1]
                try:
                    add(info_list,username)
                except Exception as e:
                    print(e)
            elif action == "delete":
                # .remove
                try:
                    delete(info_list, username)
                except Exception as e:
                    print(e)
            elif action == "update":
                update(info_list, username)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空
               if len(Student_all) == 0:
                   print('没有用户数据')
               else:
                   table()
            elif action == "find":
                try:
                    find(info_list[1])
                except Exception as e:
                    print(e)
            elif action == 'save':
                save()
            elif action == 'load':
                load()
            elif action == 'display':
                display()
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[1;31minvalid action.\033[0m")
    else:
        # 带颜色
        print("\033[1;31musername or password error.\033[0m")
        INIT_FAIL_CNT += 1
print("\033[1;31m\nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
