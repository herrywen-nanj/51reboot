# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-01 15:03'

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

    def session(self):
        pass

    def logout(self):
        print('good bye {}'.format(self.username))
        sys.exit(0)