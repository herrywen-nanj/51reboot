"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@data.com
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

# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
FIELDS = ("name", "age", "tel", "email")
ENABLE_DOC = True
FILENAME = "data.txt"
helpDoc = '''{}
add         : add monkey 12 132xxx monkey@data.com
update      : udpate monkey set age = 20
list        : xxx
find        : find monkey
display     : display page 2 page_size 3
doc         : enable/disable docstring
exit        : quit
save        : save data.txt
load        : load data.txt
{}
'''.format('-'*70, '-'*70)
def loginAuth(username,password):
    USERINFO = ("admin", "admin")
    if username == USERINFO[0] and password == USERINFO[1]:
        return True
    else:
        return False

def addUser(info_list):
    if len(info_list)-1 != 4:
        print("Action info invalid, Please add again.")
        return False
        # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
    username = info_list[1]
    if username in RESULT:
        print("Username {} already exists.".format(username))
        return False
    else:
        RESULT[username] = dict(zip(FIELDS, info_list[1:]))
        print("Add {} succ.".format(username))
        return True

def delUser(info_list):
    try:
        username = info_list[1]
        isSucc = RESULT.pop(username, None)
        if isSucc == None:
          print("User {} not found.".format(username))
        else:
           print("User {} Delete succ.".format(username))
    except Exception as e:
        print("请输入删除的用户名：")

def  update(info_list):
 while True:
    # update monkey set age = 20
    if len(info_list) != 6:
        print("Update info invalid, Input again.")
        break
    username = info_list[1]
    update_field = info_list[-3]
    update_value = info_list[-1]
    if info_list[2] != "set" or info_list[-2] != "=":
        print("Update format invalid error.")
        break

    if username in RESULT:
        if update_field in RESULT[username]:
            RESULT[username][update_field] = update_value
            print("Username {} update succ.".format(username))
            break
        else:
            print("field: {} invalid.".format(update_field))
            continue
    else:
        print("username: {} not found.".format(username))
        break

def listUsers(info_list):
    if len(RESULT) == 0:
        print("not data.")

    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    print(xtb)

def findUser(info_list):
  try:
    username = info_list[1]
    userinfo = RESULT.get(username, None)
    if userinfo == None:
        print("Username {} not found.".format(username))
    else:
        xtb = PrettyTable()
        xtb.field_names = FIELDS
        xtb.add_row(userinfo.values())
        print(xtb)
  except Exception as e:
      print("请输入查找的用户名：")

def Save():
   # FILENAME = "data.txt"
    # save
    # 1. 打开文件 file describe
    fd = open(FILENAME, 'w')
    # 2. 操作文件 read / write
    fd.write(json.dumps(RESULT))
    # 3. 关闭文件
    fd.close()
    print("Save file:{} succ.".format(FILENAME))
def Load():
    # load

    try:
        # 1. 打开文件 file describe
        fd = open(FILENAME, 'r')
    except Exception as e:
        print("Read file fail, filename: {} not found.\n".format(FILENAME))
        return False

    # 2. 操作文件 read / write
    data = fd.read()
    RESULT = json.loads(data)

    # 3. 关闭文件
    fd.close()
    print("Load file:{} succ.".format(FILENAME))
    return RESULT

def DisPlay(info_list):
    if len(info_list[1:]) >= 2 and len(info_list[1:]) <= 4:

        pagesize = 5
        if len(info_list[1:]) == 2:
            if info_list[1] == "page":
                pagesize = 5
            else:
                print("Display info invalid. Please input again.")


        else:
            if info_list[1] == "page" and info_list[3] == "pagesize":
                pagesize = int(info_list[-1])
            else:
                print("Display info invalid. Please input again.")


        page = int(info_list[2]) - 1
        data = []
        for k, v in RESULT.items():
            data.append(v.values())

        # start, end sep
        start = page * pagesize
        end = start + pagesize
        print("Start: {}, End:{}".format(start, end))

        xtb = PrettyTable()
        xtb.field_names = FIELDS
        for userinfo in data[start:end]:
            xtb.add_row(userinfo)
        print(xtb)
    else:
        print("Input info invalid, Please input again.")



def DOC():
    global ENABLE_DOC
    doc_action = 'disable' if ENABLE_DOC else 'enable'
    doc_action_bool = True if ENABLE_DOC else False
    if ENABLE_DOC:
                    input("You are {} docString, Please enter: ".format(doc_action))
                    ENABLE_DOC = False
    else:
                    input("You are {} docString, Please enter: ".format(doc_action))
                    ENABLE_DOC = True





while INIT_FAIL_CNT < MAX_FAIL_CNT:

    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if loginAuth(username,password):
        print("\033[1;32m欢迎用户 {}登录后台系统\033[0m".format(username))
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            if ENABLE_DOC:
                print(helpDoc)

            # add monkey 12 132xxx monkey@data.com
            info = input("Please input your operation: ").strip()  # 去前后空格
            info_list = info.split()
            if len(info) == 0: # 如果为空， 则提示
                print("Input info invalid, Please input again.")
                continue
            action = info_list[0]
            if action == "add":
                addUser(info_list)

            elif action == "delete":
                # delete monkey1

                delUser(info_list)

            elif action == "update":
                update(info_list)

            elif action == "list":
                listUsers(info_list)
                # 如果没有一条记录， 那么提示为空


            elif action == "find":
                # 查找
                findUser(info_list)

            elif action == "save":
                Save()

            elif action == "load":
              Load()

            elif action == "display":
                # dispaly page 2 pagesize 5
                # default = 5
                DisPlay(info_list)

            elif action == "doc":
                DOC()

            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")

    else:
        # 带颜色
        print("\033[1;31;40musername or password error!\033[0m")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
