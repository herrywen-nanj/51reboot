# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-23 17:59'


import configparser

CONFIG_FILE = 'conf/user_manage.ini'

def ReadConfig(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return "解析配置文件 {} 为空".format(filename), False


    conf_dict = {}
    for sect in config.sections():
        conf_dict[sect] = dict(config[sect])

    return conf_dict,True

def GetConfig():
    return ReadConfig(CONFIG_FILE)