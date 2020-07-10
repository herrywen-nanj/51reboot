import configparser
import os

def ReadConfig(filename,section,key=None):
    """
    读取配置
    :param filename:  file
    :param section: section
    :param key:  section中的每一项
    :return:
    """
    msg = ''
    flag = True
    if  os.path.exists(filename):
        if not os.path.getsize(filename):
            msg = '文件为空'
            flag = False
            return msg, flag
    else:
        msg = '文件不存在'
        flag = False
        return msg,flag

    config = configparser.ConfigParser()
    config.read(filename)
    if not config.sections():
        return 'config init is empty',False

    if key:
        if section in config.sections():
            return config[section][key],True
        else:
            return '',False
    else:
        return config[section],True
if __name__ == '__main__':
    result,ok = ReadConfig('./conf/51reboot.ini','mysqld','socket')
    print(result,ok)
    # config = configparser.ConfigParser()
    # config.read('51reboot.ini')
    # print(config.sections())
    # print(config['mysqld'],type(config['mysqld']))
    # print(config['mysqld']['socket'],type(config['mysqld']['socket']))
    # print(dict(config['mysqld'])['socket'],type(dict(config['mysqld'])['socket']))