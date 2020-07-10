# -*- coding:utf-8 -*-
# author: lyl
import hashlib
import user_manger
from models import user


def user_help(username='', Help=False):
    base = ''' 
    list        显示所有用户
    find        查找指定用户
    display     分页显示用户信息
    export      将当前所有用户保存至csv文件   
    exit        退出系统
    add         增加用户
    delet       删除指定用户   
    update      更新指定用户
    help        查看帮助信息
        '''
    if Help:
        format_print(True, "{}".format(base))
    else:
        format_print(True, "Hello {} 欢迎登陆，本系统支持如下功能".format(username))
        format_print(True, "{}".format(base))


def md5cmd(password):
    # 加盐操作
    md5 = hashlib.md5(b'51reboot')
    md5.update(password.encode())
    # 返回输入字符串的md5
    return md5.hexdigest()


def auth(username, password):
    try:
        tag = user.select().where(user.username == username).get()
    except Exception as e:
        message = e.__str__()
        # 对返回信息进行判断，确认是数据库无法连接，还是用户不存在
        if '2003,' in message:
            print(e)
            return False
        else:
            return False

    try:
        if md5cmd(password) == tag.password:
            return True
    except:
        return False


def logout():
    exit(0)


def logic():
    while True:
        userinfo = input("Please inpur user info: ")  # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            userinfo_string = ' '.join(userinfo_list[1:])
            if action == 'add':
                user_manger.addUser(userinfo_string)
            elif action == 'delete':
                user_manger.deleteUser(userinfo_string)
            elif action == 'update':
                user_manger.updateUser(userinfo_string)
            elif action == 'find':
                user_manger.findUser(userinfo_string)
            elif action == 'display':
                user_manger.displayUser(userinfo_string)
            elif action == 'list':
                user_manger.listUser()
            elif action == 'export':
                user_manger.ExportUser(userinfo_string)
            elif action == 'logout':
                logout()
            elif action == 'help':
                user_help(Help=True)


def format_print(tag, *args):
    if tag:
        print("\033[1;32m{}\033[0m".format(*args))
    else:
        print("\033[1;31m{}\033[0m".format(*args))
