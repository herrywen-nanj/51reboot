# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Maxwell'


import os
import configparser


def LoadConfig(filename, section, key=None):
    # load_config_message = ''
    # load_config_flag = ''
    config = configparser.ConfigParser()
    try:
        config.read(filename)
        if not config.sections():
            load_config_message = 'The config file [%s] is empty, please check!' % filename
            load_config_flag = False
        if section not in config.sections():
            load_config_message = 'Error! The section [%s] can not be found in the config file [%s]' % (section, filename)
            load_config_flag = False
        else:
            if key:
                if key in config[section]:
                    load_config_message = config[section][key]
                    load_config_flag = True
                # in case key can not be found
                else:
                    print()
                    load_config_message = 'Error! The key [%s] can not be found in the section [%s] of config file [%s]' % (key, section, filename)
                    load_config_flag = False
            else:
                load_config_message = dict(config[section])
                load_config_flag = True
    except Exception as e:
        load_config_message = e
        load_config_flag = False
    finally:
        return  load_config_message, load_config_flag



