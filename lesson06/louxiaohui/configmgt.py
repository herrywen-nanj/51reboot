#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def readconfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)
    section_list = config.sections()
    # print (section_list)
    if not section_list or section not in section_list:
        return "config init is empty or section {} does not exist".format(section), False
    if key:
        return config.get(section, key), True
    else:
        return dict(config.items(section)), True

#result, ok = readconfig('config.ini', 'dbinfo')
#print(result)
