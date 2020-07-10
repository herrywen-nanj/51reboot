# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-25 16:16'

import logging


from . import config

'''
CONFIG_FILE = 'user_manage.ini'
LOG_INFO,ok = configmgt.ReadConfig(CONFIG_FILE, 'log')
if ok:
    LogFile = LOG_INFO['logfile']
else:
    info = LOG_INFO
    print(info)
    sys.exit()
'''
result,ok = config.GetConfig()
if ok:
    LogFile = result['log']['logfile']
else:
    print(result)

def recordLog(filename):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s  %(message)s',
                        filename=filename,
                        filemode='a'
                        )
    return logging


def WriteLog():
    return  recordLog(LogFile)


