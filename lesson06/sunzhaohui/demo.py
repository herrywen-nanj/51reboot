# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-07-01 17:57'


def Decorator_check(func,username='sun'):
    def wrapper(*args,**kwargs):
        print(args)
        print('已检查: {}'.format(username))
        re = func(*args,**kwargs)
        return re
    return wrapper

@Decorator_check
def Add(user):
    print('已添加用户: {}'.format(user))


Add('sunzhaohui')