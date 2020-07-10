# -*- coding:utf-8 -*-
# author: lyl

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./logs/user_manger.log',
                    filemode='a')


def save_log(message, tag='info'):
    if tag == 'info':
        logging.info(message)
    else:
        logging.error(message)



