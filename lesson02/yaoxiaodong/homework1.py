import json

user = {'yxd':'yxd'}
massage = {1 : '登陆', 2 : '注册', 3 : '修改'}

def login(name,passwd):
    if name in user.keys() and passwd == user[name]:
        print('登陆成功')
        return 'ok'
    else:
        print('用户名或密码错误')
        return 'error'


def register(name,passwd):
    if name in user.keys():
        print('已经有账户，跳转到登陆界面.....')
        data = login(name,passwd)
        return data
    else:
        user[name] = passwd
        return '{}已经成功注册'.format(name)

def chance(name,old_passwd):
    data = login(name,old_passwd)
    if data == 'ok':
        new_passwd = input('输入新密码：')
        user[name] = new_passwd
    else:
        return '密码错误'

if __name__ == '__main__':
    for k,v in massage.items():
        print('\t{}：{}'.format(k,v))
    num = input('input your number: ')
    if num.isdigit():
        num = int(num)
        name = input('输入你要{}的用户名：'.format(massage[num]))
        passwd = input('输入你要{}的密码：'.format(massage[num]))
        if num == 1:
            login(name,passwd)
        elif num == 2:
            register(name,passwd)
        elif num == 3:
            chance(name,old_passwd=passwd)

    else:
        print('输入范围内的数字')


print('\n',user)

