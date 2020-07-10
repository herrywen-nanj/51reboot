#!/usr/bin/python

#from 第六天.作业.user_manage.action import logic
Login_user = '51reboot'
Login_pass = '123456'

class Login_Check(object):
    def __init__(self,username,userpass):
        self.name = username
        self._passwd = userpass

    def checkuser(self):
        if Login_user == self.name and Login_pass == self._passwd:
            return True
        else:
            return False



