#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-07-06
# Filename: parser.py
# Describe:
#*******************************************

import os
import configparser

# define variables
current_path = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.abspath(os.path.dirname(current_path) + '/config/app.conf')

def config_file_parser(sections, key=None):
    '''获取文件配置'''

    config = configparser.ConfigParser()
    config.read(config_file_path)

    check_flag = False
    if sections in config.sections():
        check_flag = True

    if key not in config.options(sections):
        check_flag = True

    if check_flag:
        value = config[sections][key]
        return value

    else:
        return 'sections or key key parameter cannot be empty or does not exist !!!'
