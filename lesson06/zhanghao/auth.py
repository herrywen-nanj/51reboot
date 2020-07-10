import sys

userpassinfo = ('51reboot', '123456')


class Auth(object):
    def login(self, username, password):
        if username == userpassinfo[0] and password == userpassinfo[1]:
            return "login succ.", True
        else:
            return "login faild.", False

    def logout(self):
        sys.exit(0)
