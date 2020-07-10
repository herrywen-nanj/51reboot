# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-06-25 19:17'


def Green_Print(str):
    str = '\033[0;32m {}\033[0m'.format(str)
    return str


def Red_print(str):
    str = '\033[0;31m {}\033[0m'.format(str)
    return str

def Yellow_print(str):
    str = '\033[0;33m {}\033[0m'.format(str)
    return str
