#!/bin/env python3
# -*- coding:utf-8 -*-



import logging
# 日志记录
def log_info(message):
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                        filename='access.log',
                        filemode='a'
                        )
    logging.debug(message)