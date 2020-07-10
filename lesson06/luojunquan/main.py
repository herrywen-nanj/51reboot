#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 16:56
# @Author  : luoxiaojian
# @Site    : 
# @File    : main.py
# @Software: PyCharm
from luojunquan.moudules.People_Manage_System_v5 import PeopleManageSystem
from luojunquan.moudules.Collect_server_information import Collect_Server_Information
from luojunquan.moudules.auth import Auth
# 定义变量
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 4

col = Collect_Server_Information()
_msg = col.collect()

if __name__ == '__main__':
    # 主函数，程序入口
    pms = PeopleManageSystem()
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    auth = Auth(username, password)
    if auth.login():
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
                print('欢迎{}登录用户管理系统'.format(username))
                print("""
                              用户管理系统
                            1-展示用户信息
                            2-增加用户信息
                            3-修改用户信息
                            4-删除用户信息
                            5-获取服务器基础信息
                            0-退出程序
                            """)
                num = int(input('请输入操作编号：'))
                if num == 1:
                    pms.list_all()
                elif num == 2:
                    pms.add()
                elif num == 3:
                    pms.update()
                elif num == 4:
                    pms.delete()
                elif num == 5:
                    _msg
                elif num == 0:
                    auth.logout()
    else:
        print("用户登录失败，请检查输入的用户名或者密码")
        INIT_FAIL_CNT += 1