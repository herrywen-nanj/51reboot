#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : configmgt
# @Software: PyCharm
import configparser

class ConfigMgt(object):

    def ReadConfig(self,filename,section,key=None):
        config = configparser.ConfigParser()
        config.read(filename)
        if not config.sections():
            return "config init is empty", False
        if key:
            if section in config.sections():
                return dict(config[section])[key], True
            else:
                return '', False
        else:
            return dict(config[section]), True