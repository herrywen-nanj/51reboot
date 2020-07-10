#!/usr/bin/python
#coding:UTF-8
import logging,logging.handlers
def WriteLog(filename):
    logger = logging.getLogger()
    if not logger.handlers:
        log_filename = filename

        log_level = logging.DEBUG
        format = logging.Formatter('%(asctime)s | %(filename)s | %(funcName)s | %(levelname)s | %(message)s')

        handler = logging.handlers.RotatingFileHandler(log_filename, mode='a')
        handler.setFormatter(format)

        logger.addHandler(handler)
        logger.setLevel(log_level)
    return logger
