#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         settings.py
# Description:  程序默认配置文件
# Author:       Aaron
# Date:         2019/6/24
# -------------------------------------------------------------------------------
import os
import time


TODAY = time.strftime('%Y-%m-%d', time.localtime())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 日志级别
LOG_LEVEL = "DEBUG"
# # 日志存放目录
# LOG_DIR = os.path.join(BASE_DIR, "logs")
# 程序运行主日志
LOG_FILE_PATH = os.path.join(BASE_DIR, "{}-u_m_s_demon_v4.log".format(TODAY))
# 用户名密码文件所在路径
PASSWD_FILE_PATH = os.path.join(BASE_DIR, "passwd.ini")
#
USER_INFO_FILE_PATH = os.path.join(BASE_DIR, "users.csv")

# mysql数据库连接信息
DB_CONN_INFO = {
    "db": "u_m_s",
    "host": "192.168.56.101",
    "port": 3306,
    "user": "root",
    "passwd": "123456",
}

# 视图文件(./u_m_s_demo/views.py)中每多增加一个提供用户操作的功能(函数)选项，都需要添加到该字典中
OPERATION_FUNC_DICT = {
    "help": "output_prompt",
    "add": "add_user",
    "delete": "del_user",
    "update": "update_user",
    "list": "list_user",
    "find": "find_user",
    "display": "display_user",
    "save": "save_user",
    "load": "load_user",
    "logout": "logout",
    "exit": "quit_program",
}

# 用作判断用户是否已登录
SESSION = {}
