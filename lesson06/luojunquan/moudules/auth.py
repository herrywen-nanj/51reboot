#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/3 22:27
# @Author  : luoxiaojian
# @Site    : 
# @File    : auth.py
# @Software: PyCharm
import sys

USERINFO = ("51reboot", "123456")

class Auth(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == USERINFO[0] and self.password == USERINFO[1]:
            return True
        else:
            return False

    def logout(self):
        print('good bye {}'.format(self.username))
        sys.exit(0)