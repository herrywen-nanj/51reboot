#!/usr/bin/python

import configparser
#用来读取配置文件，配置文件的格式跟windows下的ini配置文件相似，可以包含一个或多个节(section), 每个节可以有多个参数（键=值）。
'''
config = configparser.ConfigParser()


config.read('51reboot.ini')
print(config.sections())

print(dict(config['mysqld'])['symbolic-links'])
'''


def ReadConfig(filename, section, key=None):
    config = configparser.ConfigParser()
    config.read(filename)

    #如果配置文件中 没有section（章节）存在，则直接返回
    if not config.sections():
        return  "config init is empty",False

    #如果章节下的 key 字段存在
    if key:
        # 如果 section 字段存在 配置文件的章节中,则返回 section 章节下 key 的值
        if section in config.sections():
            return dict(config[section])[key],True
        # 否则抛出错误
        else:
            return ('{} does not exist.'.format(section)),False
    else:
        return dict(config[section]),True

#result,ok = ReadConfig('mysql_config.ini','mysqld')

#获取配置文件 mysql_config.ini 中 mysqld 章节下socket的值，成功 ok = True,失败 ok =False
# result,ok = ReadConfig('mysql_config.ini','mysqld','socket')
#
# print(ok)
# print(result)

