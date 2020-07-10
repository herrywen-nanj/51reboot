#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : logutils
# @Software: PyCharm
import logging,os,time

TODAY = time.strftime('%Y-%m-%d', time.localtime())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, "{}-People_Manage_System_v5.log".format(TODAY))


def Logs():
    # 其中有个name参数，默认值为root
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(filename=LOG_FILE_PATH, mode='a', encoding='utf-8')

    # # 再创建一个handler，用于输出到控制台
    # ch = logging.StreamHandler()

    # 定义handler的输出格式formatter
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    # ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger