# -*- coding:utf-8 -*-
# author: lyl
import json
import re
import logs

# 初始化字段
phone_add = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198,
             130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 133, 149, 153, 173, 177, 180, 181, 189, 191,
             199]
mail_pattern = re.compile(r'([a-zA-Z0-9]([a-zA-Z0-9_]+)(\@))[a-zA-Z0-9]([a-zA-Z0-9_]+)\.(([a-z]+))')


# 检测用户是否存在
def user(target):
    with open('user.txt', 'r') as fd:
        user_info = fd.read()
        if user_info == '':
            user_info = '{}'
        try:
            user_dict = json.loads(user_info)
        except Exception as e:
            print("\033[1;31m用户文件 user.txt 存在异常，请手动修复\033[0m")
            logs.error(e)
            return None, None, None

        if target.isdigit():
            for i in user_dict.keys():
                if user_dict[i]['id'] == int(target):
                    return True, i, int(target)
        else:
            for i in user_dict.keys():
                if i == target:
                    return True, target, int(user_dict[i]['id'])
        return False, "\033[1;31m用户{}不存在\033[0m".format(target), None


# 检测用户登录
def user_login(username, password):
    with open('system_user.txt', 'r+') as fd:
        note = fd.read()
        # 如果用户表为空，则手动赋值
        if note == '':
            note = '{}'
        try:
            user_info_dict = json.loads(note)
        except Exception as e:
            print("\033[1;31m 系统文件 system_user.txt 存在异常，请手动修复\033[0m")
            logs.error(e)
            return False, None
        if username not in user_info_dict.keys() or password != user_info_dict[username]['password']:
            return False, None
        return True, user_info_dict[username]['role']


# 检查用户更新用户更新字段
def user_input(tag, check_world=None):
    return {
        'username': lambda: 0 if check_world is None else input_args(username=check_world),
        'age': lambda: 1 if check_world is None else input_args(age=check_world),
        'tel': lambda: 2 if check_world is None else input_args(phone=check_world),
        'email': lambda: 3 if check_world is None else input_args(mail=check_world),
    }[tag]()


# 检查用户输入内容是否有误
def input_args(username=None, age=None, phone=None, mail=None):
    if username is not None:
        if username.isdigit():
            return "\033[1;31m用户名禁止全为数字\033[0m"
    if age is not None:
        if not age.isdigit():
            return "\033[1;31m年龄有误\033[0m"
    if phone is not None:
        if len(phone) != 11:
            return "\033[1;31m手机号有误\033[0m"
        # 提取用户输入手机号的前三位,并转化为int类型
        head = int(''.join(list(phone[:3])))
        if head not in phone_add:
            return "\033[1;31m手机号有误,暂不支持虚拟运营商!!!\033[0m"
    if mail is not None:
        # 粗略写的正则，凑活着用
        m = mail_pattern.match(mail)
        if m is None:
            return "\033[1;31m邮件格式有误 eg: xxx@xxx.com\033[0m"
    return True


def user_dict():
    with open('user.txt', 'r') as user_fd:
        user_note = user_fd.read()
        if user_note == '':
            return False, "\033[1;31m用户列表为空\033[0m"
        try:
            user_info_dict = json.loads(user_note)
            return True, user_info_dict
        except Exception as e:
            logs.error(e)
            return False, "\033[1;31m id文件 user.txt存在异常，请手动修复\033[0m"


def display(role):
    base = ''' 
list        显示所有用户
find        查找指定用户
display     分页显示用户信息
save        将当前所有用户保存至csv文件   
login_out   退出当前用户
exit        退出系统
'''
    admin = '''add         增加用户
delet       删除指定用户   
update      更新指定用户
load        导入指定csv文件用户
    '''

    if role == 'admin':
        print("\033[1;32m尊贵的管理员，你可以执行下列所有操作\033[0m")
        print("\033[1;32m {}{}\033[0m".format(base, admin))
    else:
        print("\033[1;32mHi 兄弟你可以做下面的操作\033[0m")
        print("\033[1;32m {}\033[0m".format(base))
