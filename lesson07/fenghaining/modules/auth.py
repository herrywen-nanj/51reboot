import sys
from . import logger



class Auth(object):
    def login(self,username, password):
        """
        用户登录
        :param username:
        :param password:
        :return:
        """
        msg = ''
        flag = True
        #USERINFO = ("1", "1")
        USERINFO = ("51reboot", "123456")
        if username == USERINFO[0] and password == USERINFO[1]:
            msg = '%s用户已登录' % username
            logger.logger(msg)
        else:
            msg = '%s用户登录失败' % username
            flag = False
        return msg, flag

    def logout(self):
        """
        用户退出
        :return:
        """
        sys.exit()
