import sys

class Auth(object):
    def __init__(self):
        self.username = 'admin'
        self.password = 'admin123'

    def login(self,uname,pwd):
        if uname == self.username and pwd == self.password:
            return True
        else:
            return False

    def logout(self):
        sys.exit(0)
#
# if __name__ == '__main__':
#     u = input('u: ')
#     p = input('p: ')
#     auth = Auth()
#     auth.login(u,p)
