"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys
import json
import datetime
from prettytable import PrettyTable


RESULT = {}
FILENAME = "51reboot.db"
FIELDS = ("name", "age", "tel", "email")


def readFile():
    '''
    读取文件内容到内存
    '''
    try:
        with open(FILENAME, 'r') as fd:
            dataStr = fd.read()
            data = json.loads(dataStr)
            return data, True
    except Exception as e:
        return {}, False


def writeFile():
    '''
    写内存数据到文件
    '''
    with open(FILENAME, 'w') as fd:
        fd.write(json.dumps(RESULT))
    return "Save succ", True


def login(username, password):
    '''
    登录
    '''
    # 临时定义，常规方式从数据库红获取
    user_password_info_t = ('1', '1')
    if username == user_password_info_t[0] and password == user_password_info_t[1]:
        return 'Login succ', True
    else:
        return 'Login fail', False


def logout():
    '''
    退出
    '''
    sys.exit()

def addUser(input_user_manage_info:list):
    '''
    添加用户
    '''
    # monkey 12 132xxx monkey@51reboot.com
    if len(input_user_manage_info) != 4:
        errMsg = "Add info invalid, Please add again."
        return errMsg, False

    # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
    username = input_user_manage_info[0]
    if username in RESULT:
        errMsg = "Username {} already exists.".format(username)
        return errMsg, False
    else:
        RESULT[username] = dict(zip(FIELDS, input_user_manage_info))
        succMsg = "Add {} succ.".format(username)
        return succMsg, True

def deleteUser(input_user_manage_info:list):
    '''
    删除用户
    '''
    # delete monkey1
    username = input_user_manage_info[0]
    isSucc = RESULT.pop(username, None)
    if isSucc == None:
        errMsg = "User {} not found.".format(username)
        return errMsg, False
    else:
        succMsg = "User {} Delete succ.".format(username)
        return succMsg, True

def updateUser(input_user_manage_info:list):
    '''
    修改用户
    '''
    # update monkey1 set age = 20
    print(input_user_manage_info)
    if len(input_user_manage_info) != 5:
        errMsg = "Update info invalid, Input again."
        return errMsg, False

    username = input_user_manage_info[0]
    update_field = input_user_manage_info[2]
    update_value = input_user_manage_info[-1]
    if input_user_manage_info[1] != "set" or input_user_manage_info[-2] != "=":
        errMsg = "Update format invalid error."
        return errMsg, False

    if username in RESULT:
        if update_field in RESULT[username]:
            RESULT[username][update_field] = update_value
            succMsg = "Username {} update succ.".format(username)
            return succMsg, True
        else:
            errMsg = "field: {} invalid.".format(update_field)
            return errMsg, False
    else:
        succMsg = "username: {} not found.".format(username)
        return succMsg, True

def listUser():
    '''
    列出所有用户
    '''
    # 如果没有一条记录， 那么提示为空
    if len(RESULT) == 0:
        errMsg = "not data."
        return errMsg, False

    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    return xtb, True

def displayUser(input_user_manage_info:list):
    '''
    用户信息分页
    '''
    # dispaly page 2 pagesize 5
    # default = 5
    if len(input_user_manage_info) >= 2 and len(input_user_manage_info) <= 4:

        pagesize = 5
        if len(input_user_manage_info) == 2:
            if input_user_manage_info[0] == "page":
                pagesize = 5
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        else:
            if input_user_manage_info[0] == "page" and input_user_manage_info[2] == "pagesize":
                pagesize = int(input_user_manage_info[-1])
            else:
                errMsg = "Display info invalid. Please input again."
                return errMsg, False

        page = int(input_user_manage_info[1]) - 1
        data = []
        for k, v in RESULT.items():
            data.append(v.values())

        # start, end sep
        start = page * pagesize
        end = start + pagesize
        # print("Start: {}, End:{}".format(start, end))

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for userinfo in data[start:end]:
            xtb.add_row(userinfo)
        return xtb, True
    else:
        errMsg = "Input info invalid, Please input again."
        return errMsg, False


def findUser(input_user_manage_info):
    '''
    搜索指定用户
    '''
    # 查找
    username = input_user_manage_info[0]
    userinfo = RESULT.get(username, None)
    if userinfo == None:
        errMsg = "Username {} not found.".format(username)
        return errMsg, False
    else:
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(userinfo.values())
        return xtb, True


def opLogic():
    '''
    业务逻辑
    '''
    while True:
        info = input("Please input your operation: ").strip()
        info_list = info.split()

        if len(info) == 0:  # 如果为空， 则提示
            print("Input info invalid, Please input again.")
            continue

        action = info_list[0]
        input_user_manage_info = info_list[1:]

        if action == "add":
            addMsg, ok = addUser(input_user_manage_info)
            print("{}, State: {}, Result: {}".format(action, ok, addMsg))
        elif action == "delete":
            delMsg, ok = deleteUser(input_user_manage_info)
            print("{}, State: {}, Result: {}".format(action, ok, delMsg))
        elif action == "update":
            updateMsg, ok = updateUser(input_user_manage_info)
            print("{}, State: {}, Result: {}".format(action, ok, updateMsg))
        elif action == "list":
            listMsg, ok = listUser()
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, listMsg))
            else:
                print(listMsg)
        elif action == "find":
            findMsg, ok = findUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, findMsg))
            else:
                print(findMsg)
        elif action == "save":
            writeMsg, ok = writeFile()
            print("{}, State: {}, Result: {}".format(action, ok, writeMsg))
        elif action == "load":
            readMsg, ok = readFile()
            if ok:
                global RESULT
                # 局部变量要修改全局变量的值，需要用global关键字声明。
                RESULT = readMsg
                print("{}, State: {}".format(action, ok))
            else:
                print("{}, State: {}, Result: {}".format(action, ok, readMsg))
        elif action == "display":
            disMsg, ok = displayUser(input_user_manage_info)
            if not ok:
                print("{}, State: {}, Result: {}".format(action, ok, disMsg))
            else:
                print(disMsg)
        elif action == "doc":
            pass
        elif action == "exit":
            logout()
        else:
            print("invalid action.")


def main():
    '''
    入口函数
    '''

    # 变量
    init_fail_cnt = 0
    max_fail_cnt = 6

    while init_fail_cnt < max_fail_cnt:
        username = input("Please input your username: ")
        password = input("Please input your password: ")

        loginMsg, ok = login(username, password)
        if not ok:
            print(loginMsg)
            init_fail_cnt += 1
            continue

        print("Login succ\n\n")

        opLogic()

    print("\nInput {} failed, Terminal will exit.".format(max_fail_cnt))





if __name__ == '__main__':
    main()
