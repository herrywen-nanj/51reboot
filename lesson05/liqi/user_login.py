#!/usr/bin/python
'''
增加
删除
修改
列出
搜索
分页
退出
保存
加载
日志
csv
'''


# 标准模块
import sys
import json
from operation_db import insert,update,select,delete


# 第三方模块
from prettytable import PrettyTable


# 全局变量
DB_FILE = '51reboot.db'
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {}

def auth(username, password):
    userpassinfo = ('liq', '123456')
    if username == userpassinfo[0] and password == userpassinfo[1]:
        return True
    else:
        return False

def addUser(args):
    '''
    add monkey1 12 132xxx monkey1@qq.com
    args = "monkey1 12 132xxx monkey1@qq.com"
    :return:
    '''
    userinfolist = args.split(" ")
    if len(userinfolist) != 4:
        return "addUser failed, args length != 4"

    username = userinfolist[0]
    if username in RESULT:
        print("Username: {} already exists.".format(username))
    else:
        sql = '''insert into users(username,age,tel,email)  values('{}','{}','{}','{}');'''.format(username,userinfolist[1],userinfolist[2],userinfolist[3])
        data,ok = insert(sql)
        print(data)
        # RESULT[username] = {
        #     'name'  : username,
        #     'age'   : userinfolist[1],
        #     'tel'   : userinfolist[2],
        #     'email' : userinfolist[3],
        # }
        # print("add user {} secc.".format(username))

def deleteUser(args):
    '''
    delete monkey1
    args = monkey1
    :param args:
    :return:
    '''
    userinfolist = args.split(" ")
    if len(userinfolist) != 1:
        return "deleteUser failed, args length != 1"

    sql = '''delete from users where username = "{}"'''.format(userinfolist[1])
    delete(sql)
    # if username in RESULT:
    #     # RESULT.pop(username, None)
    #     sql = '''delete from users where username = {}'''.format(username)
    #     print(sql)
    #     delete(sql)
    #     print("delete user {} secc.".format(username))
    # else:
    #     print("Username: {} not found.".format(username))

def updateUser(args):
    '''
    update monkey1 set age = 20
    :param args: monkey1 set age = 20
    :return:
    '''
    userinfolist = args.split()
    print(userinfolist[-1])
    print(userinfolist)
    if len(userinfolist) != 5:
        return "updateUser failed, args length != 5"

    where = userinfolist[1]
    wherefuhao = userinfolist[-2]

    if where != 'set' or wherefuhao != '=':
        return 'syntax error.'
    else:
        sql = '''update users set {} = {} where username = "{}";'''.format(userinfolist[2],userinfolist[-1],userinfolist[0])
        data,ok = update(sql)
        print(data)
        # username = userinfolist[0]
        # where_field = userinfolist[2]
        # update_value = userinfolist[-1]
        # RESULT[username][where_field] = update_value

    # print(RESULT)

def listUser():
    '''
    打印所有用户信息
    :return:
    '''
    sql = '''select * from users;'''
    data,ok = select(sql)
    print(data)
    # xtb = PrettyTable()
    #     # xtb.field_names = FIELDS
    #     # for k, v in RESULT.items():
    #     #     xtb.add_row(v.values())
    #     # print(xtb)

def findUser(args):
    '''
    find monkey1
    :param args: = monkey1
    :return:
    '''
    userinfolist = args.split()
    print(userinfolist)
    sql = '''select * from users where username = "{}";'''.format(userinfolist[0])
    data,ok = select(sql)
    print(data)
    # if username in RESULT:
    #     userinfo = RESULT[username]  # userinfo是字典
    #     xtb = PrettyTable()
    #     xtb.field_names = FIELDS
    #     xtb.add_row(list(userinfo.values()))
    #     print(xtb)
    # else:
    #     print("Username: {} not found.".format(username))

def displayUser(args):
    '''
    display page 2 pagesize 5
    :param args: page 2 pagesize 5 ;default pagesize = 5
    page 1 -> 0-4
    切片
    slice
    '''
    userinfolist = args.split()
    if len(userinfolist) == 2:
        if userinfolist[0] != 'page':
            return "syntax error."

        values = [ list(v.values()) for k, v in RESULT.items() ]
        # print(values)

        page_value = int(userinfolist[1]) - 1  # 1
        pagesize = 5
        start = page_value * pagesize
        end = start + pagesize
        # 0:5
        # 5:10

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for t_user_info in values[start:end]:
            xtb.add_row(t_user_info)
        print(xtb)

    elif len(userinfolist) == 4:
        if userinfolist[0] != 'page' and userinfolist[-2] != 'pagesize':
            return "syntax error."

        values = [list(v.values()) for k, v in RESULT.items()]
        # print(values)

        page_value = int(userinfolist[1]) - 1  # 1
        pagesize = int(userinfolist[-1])
        start = page_value * pagesize
        end = start + pagesize
        # 0:5
        # 5:10

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for t_user_info in values[start:end]:
            xtb.add_row(t_user_info)
        print(xtb)
    else:
        return "syntax error."

# def save():
#     '''
#     写内存中的数据到磁盘中
#     :return:
#     '''
#     with open(DB_FILE, 'w') as fd:
#         fd.write(json.dumps(RESULT))

# def load():
#     '''
#     读磁盘的数据加载到内存中
#     :return: dict
#     '''
#
#     sql = '''select username,age,tel,email from users;'''
#
#     with open(DB_FILE, 'r') as fd:
#         data = fd.read()
#         if not len(data):
#             return {}
#         else:
#             return json.loads(data)

def logout():
    '''
    退出整个脚本
    break for、while
    :return:
    '''
    sys.exit(0)

def logic():
    while True:
        userinfo = input("Please inpur user info: ") # add monkey 12 132xx monkey!@qq.com
        if len(userinfo) == 0:
            print("invalid input.")
        else:
            userinfo_list = userinfo.split()
            action = userinfo_list[0]
            userinfo_string = ' '.join(userinfo_list[1:])
            if action == 'add':
                addUser(userinfo_string)
            elif action == 'delete':
                deleteUser(userinfo_string)
            elif action == 'update':
                updateUser(userinfo_string)
            elif action == 'find':
                findUser(userinfo_string)
            elif action == 'display':
                displayUser(userinfo_string)
            elif action == 'list':
                listUser()
            # elif action == 'save':
            #     save()
            # elif action == 'load':
            #     global RESULT
            #     RESULT = load()
            elif action == 'logout':
                logout()


def main():
    '''
    入口函数
    '''
    '''
    while True:
        userinfo = input("Please input userinfo: ")
        # if not len(userinfo):
        #     print("invalid input.")
        #     continue
        # addUser(userinfo)
        # deleteUser(userinfo)
        # listUser()
        # findUser(userinfo)
        # updateUser(userinfo)
        displayUser(userinfo)
    '''

    init_fail_count = 0
    max_fail_count = 3
    while init_fail_count < max_fail_count:

        username = input("Please input your login username: ")
        password = input("Please input your login password: ")
        if auth(username, password):
            print("\n\tWelcome to user magage system.\n")
            logic()
        else:
            print("username or password valid failed.")
            init_fail_count += 1

    print("Game Over.")


if __name__ == '__main__':
    main()
