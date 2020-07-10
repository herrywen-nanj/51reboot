#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
配置文件管理模块
Author: Wangxiaoyun
'''
import configparser,os,sys,LogMgt

def ReadConfig(filename, section, key=None):
    if not os.path.exists(filename):  # 判断配置文件是否存在
       configMsg = '{} 配置文件丢失, 程序退出.'.format(filename)
       LogMgt.UserLog(configMsg)
       sys.exit(configMsg)

    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(filename)

    if not config.sections():
        configMsg = '{} configuration init is empty'.format(filename)
        LogMgt.UserLog(configMsg)
        return configMsg, False

    if key:
        if section in config.sections():
            configMsg = 'configuration file {} {} {} loaded successfully.'.format(filename,section,key)
            LogMgt.UserLog(configMsg)
            return dict(config[section])[key], True
        else:
            configMsg = 'configuration file {} format error.'.format(filename)
            LogMgt.UserLog(configMsg)
            return configMsg, False
    else:
        configMsg = 'ConfigMgt has no key parameter.'
        LogMgt.UserLog(configMsg)
        return dict(config[section]), True

'''
username,ok = ReadConfig('config.ini','Login','username')
'''