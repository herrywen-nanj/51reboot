#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
日志模块
Author: WangXiaoyun
'''
import logging,os

class logs(object):
    def __init__(self,*args):
        self.log = args

    def mgt(self):
        '''
        Logs must be string type.
        '''
        name = 'info.log'
        try:  # 捕获非 string 类型日志
            if isinstance(self.log, tuple) or isinstance(self.log, list):
                format = ' '.join(self.log)
            else:  # 其他类型日志转 string 类型
                format = str(self.log)

            if not os.path.exists(name):  # 判断日志文件是否存在
                os.mknod(name)
            logging.basicConfig(level=logging.DEBUG,  # 定义日志格式
                                format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                                filename=name,
                                filemode='a')
            logging.debug(format)
        except Exception as e:
            print(e)

# L = logs('test log.')
# print(L.mgt())