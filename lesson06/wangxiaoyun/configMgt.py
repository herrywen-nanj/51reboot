#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
配置文件管理模块
Author: Wangxiaoyun
'''
import configparser,os,sys
from logMgt import logs

class configs(object):
    def __init__(self,filename,section,key=None):
        self.filename = filename
        self.section = section
        self.key = key

    def read(self):
        if not os.path.exists(self.filename):  # 判断配置文件是否存在
            msg = '{} 配置文件丢失, 程序退出.'.format(self.filename)
            log = logs(msg)
            log.mgt()
            sys.exit(msg)

        # 读取配置文件
        config = configparser.ConfigParser()
        config.read(self.filename)

        if not config.sections():
            msg = '{} configuration init is empty'.format(self.filename)
            log = logs(msg)
            log.mgt()
            return msg, False

        if self.key:
            if self.section in config.sections():
                msg = 'configuration file {} {} {} loaded successfully.'.format(self.filename,self.section,self.key)
                log = logs(msg)
                log.mgt()
                return dict(config[self.section])[self.key], True
            else:
                msg = 'configuration file {} format error.'.format(self.filename)
                log = logs(msg)
                log.mgt()
                return msg, False
        else:
            msg = 'ConfigMgt has no key parameter.'
            log = logs(msg)
            log.mgt()
            return dict(config[self.section]), True

# Config = config('config.ini','Login','username')
# print(Config.read())