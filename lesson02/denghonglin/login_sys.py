#!/usr/bin/env python
###############################
# function: login_system
# author: dhl
# date:	2019-05-24
# env: python3
###############################

import sys

user_data = dict()

def create_user():
    prompt = '【注册】请输入用户名: '
    while True:
        username = input(prompt)
        if username in user_data:
            prompt = '此用户已被注册，请重新输入: '
            continue
        else:
            break
    pwd = input('请输入密码: ') 
    user_data[username] = pwd
    print('注册成功.')  


def showmenu():
    print('''
     |--- 1、查询 ---|
     |--- 2、创建 ---|
     |--- 3、修改 ---|
     |--- 4、删除 ---|
     |--- 5、退出 ---|
''')
    prompt = '\n请输入指令代码: '
    while True:
        flag = False
        while not flag:
            choice = input(prompt)
            if choice == '1':
                name = input('请输入用户名: ')
                if name in user_data:
                    print('查询结果: %s' %user_data[name])
                else:
                    print('信息不存在!')

            if choice == '2':
                create_user()

            if choice == '3':
                name = input('请输入要修改的用户: ')
                if name in user_data:
                    user_data[name] = input('修改为:')
                    #user_data.update(name)
                else:
                    print('信息不存在!')
  
            if choice == '4':
                name = input('请输入要删除的用户: ')
                if name in user_data:
                    user_data.pop(name)
                else:
                    print('信息不存在!')
            
            if choice == '5':
                sys.exit()

            if choice.lower() not in '1234':
                print('输入的代码指令有误, 请重新输入: ')
            else:
                flag = True
            
        if choice.lower() == 'q':
            break



def login_sys():
    print('数据: %s' %user_data)
    prompt = '【登录】请输入用户名: '
    while True:
        username = input(prompt)
        if username in user_data:
            pwd = input('请输入密码: ')
            if pwd == user_data[username]:
                print("系统登录成功.\n")
                showmenu()
        else:
            print('用户不存在!')
            choice = input("是否创建: (y/n)")
            if choice.lower() == 'y':
                create_user()
            elif choice.lower() == 'n':
                sys.exit()
            else:
                print('输入有误,继续...')
                continue

if __name__ == '__main__':
    login_sys()
