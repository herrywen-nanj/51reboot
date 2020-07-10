# 标准模块
import sys
import json

# 自定义模块
from configmgt import ReadConfig
from dbutils import select, insert, delete, update

# 第三方模块
from prettytable import PrettyTable



# 全局变量
DB_FILE = '51reboot.db'
DB_CONFIG_INI = '51reboot.ini'
FIELDS = ['name', 'age', 'tel', 'email']
RESULT = {}
_ = {
    'monkey1': {'name': 'monkey1', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey2': {'name': 'monkey2', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey3': {'name': 'monkey3', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey4': {'name': 'monkey4', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey5': {'name': 'monkey5', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey6': {'name': 'monkey6', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
    'monkey7': {'name': 'monkey7', 'age': '12', 'tel': '132xxx', 'email': 'monkey@qq.com'},
}
# RESULT = [
#     {'name' : 'monkey1', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'},
#     {'name' : 'monkey2', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'},
# ]

# TMP_RESULT = {
#     'monkey1' : {'name' : 'monkey1', 'age' : 12, 'tel' : '132xxx', 'email' : 'monkey1@qq.com'}
# }

def auth(username, password):
    userpassinfo = ('51reboot', '123456')
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
        RESULT[username] = {
            'name'  : username,
            'age'   : userinfolist[1],
            'tel'   : userinfolist[2],
            'email' : userinfolist[3],
        }
        print("add user {} secc.".format(username))

def deleteUser(args):
    '''
    delete monkey1
    args = monkey1
    :param args:
    :return:
    '''
    print(RESULT)
    userinfolist = args.split(" ")
    if len(userinfolist) != 1:
        return "deleteUser failed, args length != 1"

    username = args
    if username in RESULT:
        RESULT.pop(username, None)
        print("delete user {} secc.".format(username))
    else:
        print("Username: {} not found.".format(username))

def updateUser(args):
    '''
    update monkey1 set age = 20
    :param args: monkey1 set age = 20
    :return:
    '''
    print(RESULT)
    userinfolist = args.split()
    if len(userinfolist) != 5:
        return "updateUser failed, args length != 5"

    where = userinfolist[1]
    wherefuhao = userinfolist[-2]

    if where != 'set' or wherefuhao != '=':
        return 'syntax error.'
    else:
        username = userinfolist[0]
        where_field = userinfolist[2]
        update_value = userinfolist[-1]
        RESULT[username][where_field] = update_value

    print(RESULT)

def listUser():
    '''
    打印所有用户信息
    :return:
    '''
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    print(xtb)

def findUser(args):
    '''
    find monkey1
    :param args: = monkey1
    :return:
    '''
    username = args
    if username in RESULT:
        userinfo = RESULT[username]  # userinfo是字典
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(list(userinfo.values()))
        print(xtb)
    else:
        print("Username: {} not found.".format(username))

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

def saveDB():
    '''
    存储到数据库中
    :return:
    '''


    for username, info in RESULT.items():
        sql = "SELECT {} FROM 51reboot_users WHERE name = '{}';".format(','.join(FIELDS), username)
        print(sql)
        resp, ok = select(sql)  # select需要一个单独的判断是否为空的情况
        if not ok:
            fields_string = ','.join(FIELDS)
            values_string = "'{}', {}, '{}', '{}'".format(info['name'], info['age'], info['tel'], info['email'])
            sql = '''INSERT INTO 51reboot_users({}) VALUES({})'''.format(fields_string, values_string)
            print(sql)
            resp, ok = insert(sql)
            if ok:
                print('username: {} save succ.'.format(username))
            else:
                print('username: {} save fail.'.format(username))
        else:
            print('username: {} already exists.'.format(username))

def loadDB():
    '''
    从数据库中加载到内存中
    :return:
    '''
    sql = "SELECT {} FROM 51reboot_users;".format(','.join(FIELDS))
    print(sql)
    resp, ok = select(sql)
    if ok:
        global RESULT
        RESULT = [ dict(zip(FIELDS, x)) for x in resp]
    else:
        print('Load from db fail.')

def save():
    '''
    写内存中的数据到磁盘中
    :return:
    '''
    with open(DB_FILE, 'w') as fd:
        fd.write(json.dumps(RESULT))

def load():
    '''
    读磁盘的数据加载到内存中
    :return: dict
    '''
    with open(DB_FILE, 'r') as fd:
        data = fd.read()
        if not len(data):
            return {}
        else:
            return json.loads(data)

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
            elif action == 'save':
                save()
            elif action == 'load':
                global RESULT
                RESULT = load()
            elif action == 'logout':
                logout()


def main():
    '''
    入口函数
    '''

    loadDB()
    print(RESULT)
    return
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