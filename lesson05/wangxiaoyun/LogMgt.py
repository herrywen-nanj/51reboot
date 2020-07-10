#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
日志模块
Author: WangXiaoyun
'''
import logging,os

def UserLog(*Logs):
    '''
    Logs must be string type.
    '''
    logName = './info.log'

    try:   #捕获非 string 类型日志
        if isinstance(Logs,tuple) or isinstance(Logs,list):
            formatLog = ' '.join(Logs)
        else:   #其他类型日志转 string 类型
            formatLog = str(Logs)

        if not os.path.exists(logName):   #判断日志文件是否存在
            os.mknod(logName)
        logging.basicConfig(level=logging.DEBUG,    #定义日志格式
                            format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                            filename=logName,
                            filemode='a')
        logging.debug(formatLog)
    except Exception as e:
        print(e)
