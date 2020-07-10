# -*- coding:utf-8 -*-
# author: lyl

import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./log/user_manger.log',
                    filemode='w')


def info(user, message):
    log_note = "user: " + user + ' ' + 'message: ' + ' '.join(message)
    logging.info(log_note)


def error(message):
    message = str(message)
    log_note = ' '.join(message)
    logging.info(log_note)
