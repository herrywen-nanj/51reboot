#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/19 20:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 用户登录认证管理系统
# @Software: PyCharm

import getpass

sum_people = ['张三']
name = 'admin'
password = 'admin'
def login():
    print('欢迎登录用户管理系统')
    name = input('请输入用户名：')
    password = getpass.getpass('请输入密码：')
    try:
        if name == 'admin' and password == 'admin':
            main_people()
        elif name != 'admin' or password != 'admin':
            print('用户名或者密码输入有问题，请检查用户名或者密码')
        else:
            exit()
    except Exception as e:
        print(e)
def add():
    '添加用户'
    try:
        add_people = input('请输入添加的用户名或者输入exit退出:')
        if add_people in sum_people:
            print('添加的用户已经存在,请重新输入')
        elif add_people == 'exit':
            exit()
        else:
            sum_people.append(add_people)
            main_people()
    except Exception as e:
        print(e)

def delete():
    '删除用户'
    delete_people = input('请输入删除的用户名或者输入exit退出:')
    try:
        if delete_people in sum_people:
            print('正在删除')
            sum_people.remove(delete_people)
            main_people()
        elif delete_people == 'exit':
            exit()
        else:
            print('不存在此用户')
    except Exception as e:
        print(e)

def mod():
    '修改用户'
    modfiy_before_people = input('请输入需要修改的用户或者输入exit退出：')
    if modfiy_before_people == 'exit':
        exit()
    modfiy_after_people = input('将用户修改为：')
    try:
        if modfiy_before_people in sum_people:
            modfiy_index =sum_people.index(modfiy_before_people)
            sum_people[modfiy_index] = modfiy_after_people
            main_people()
        else:
            print('删除的用户不存在，请检查用户名')
    except Exception as e:
        print(e)

'查询用户list'
def check():
    check_people = input('请输入需要查询的用户或者输入exit退出：')
    try:
        if check_people in sum_people:
            print('查询的用户存在')
            main_people()
        elif check_people == 'exit':
            exit()
        else:
            print('查询的用户不存在，请检查用户名')
    except Exception as e:
        print(e)

'搜查用户find'
def find():
    find_people = input('请输入需要查询的用户或者输入exit退出：')
    try:
        for i,people in enumerate(sum_people):
            if people.find(find_people) != -1:
                print('搜查的用户存在')
                main_people()
            elif find_people == 'exit':
                exit()
            else:
                print('搜查的用户不存在,请检查用户名')
    except Exception as e:
        print(e)

def main_people():
    print('------------------------------')
    print('欢迎登录用户管理系统: \n'
          '1、增加用户请输入：add\n'
          '2、删除用户请输入：delete\n'
          '3、修改用户请输入：mod\n'
          '4、查询用户请输入：check\n'
          '5、搜寻用户请输入：find\n'
          '6、退出请输入：exit')
    print('------------------------------')
    user_input = input('按照上面提示输入：')
    try:
        if user_input == 'add':
            add()
        elif user_input == 'delete':
            delete()
        elif user_input == 'mod':
            mod()
        elif user_input == 'check':
            check()
        elif user_input == 'find':
            find()
        elif user_input == 'exit':
            exit()
        else:
            print('检查输入的选项是不是以上提示的选项，请重新输入')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    login()
