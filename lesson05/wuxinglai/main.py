
# 标准模块
import sys
import json
import pymysql
# 第三方模块
from prettytable import PrettyTable
import configmgt
# 全局变量
FILENAME = 'my.ini'
#DB_FILE = '51reboot.db'
FIELDS=('id', 'name', 'age', 'mail', 'phone')
RESULT = {}


def auth(username, password):
    userpassinfo = ('admin', '1')
    if username == userpassinfo[0] and password == userpassinfo[1]:
        return True
    else:
        return False
def showmenu():
   print('\033[1;32;40m')
   print('*' * 50)
   print('''\n\t\033[1;32;40m欢迎登陆用户管理系统\033[1;32;40m\n''')
   print('*' * 50)
   print('\033[0m')
   print('''\033[1;34;40m\n\t系统功能菜单\n\033[0m''')
   print('''\033[1;36;40m增加用户:add username age tel mail''')
   print('''删除用户:del username''')
   print('''更改用户:update username set age|tel|mail = args''')
   print('''查找用户:find username''')
   print('''列出所有用户:list''')
   print('''分页查找:display page 2 pagesize 5''')
   print('\033[0m')
def connnet():
    cfg, ok = configmgt.ReadConfig(FILENAME, 'rebootdb')
    if not ok:
        return cfg, False
    try:
        conn = pymysql.connect(
            host=cfg['host'],
            user=cfg['username'],
            password=cfg['password'],
            database=cfg['database'],
            port=int(cfg['port']),
        )
    except:
        return None
    return conn
def addUser(args):
    '''
    add monkey1 12 132xxx monkey1@qq.com

    args = "monkey1 12 132xxx monkey1@qq.com"
    :return:
    '''
    userinfolist = args.split(" ")
    if len(userinfolist) != 4:
        return "\033[5;31;40maddUser failed, args length != 4\033[0m"
    try:
     age =int(userinfolist[1])
    except ValueError:
          print("\033[5;31;40mAge Must be Number\033[0m")
          return False
        
    username = userinfolist[0]
    if username in RESULT  and age:

        print("\033[1;31;40mUsername: {} already exists.\033[0m".format(username))
    else:  
           RESULT[username] = {
              'name'  : username,
              'age'   : userinfolist[1],
              'tel'   : userinfolist[2],
              'email' : userinfolist[3],
        }
           print("\033[1;32;40mUsername: {} user Add succ.\033[0m".format(username))

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




def listsql():
    '''
    查询数据库并加载到内存中
    :return: dict
    '''
    db = connnet()
    if not db:
       return "conn db fail", False
    sql='''select * from users '''
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    data=cursor.fetchall()
    db.close()
    tmplist=list(data)
    RESULT={}
    i = 0
    while i <= len(tmplist)-1:
      RESULT[list(tmplist[i])[0]]= dict(zip(FIELDS, list(tmplist[i])[0:]))
      i += 1
   # print(RESULT)
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
      xtb.add_row(v.values())
    print(xtb)



'''未启用的函数
def listUser():
    
   # 打印所有用户信息
   # :return:
   
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
 
      try:
        xtb.add_row(v.values())
      except Exception as e:
          print("First load Please!")
    print(xtb)
'''
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

#def save():
    '''
    写内存中的数据到磁盘中
    :return:
    '''
 #   with open(DB_FILE, 'w') as fd:
  #      fd.write(json.dumps(RESULT))

def savesql():

    db = connnet()
    if not db:
     return "conn db fail", False
    cursor = db.cursor()
    for k, v in RESULT.items():
        tmpv = list(v.values())
        sql = "insert into users(username,age,tel,email)  values( '{}', {},'{}','{}')".format((tmpv[0]), tmpv[1], tmpv[2], tmpv[3])
        try:
         cursor.execute(sql)
         db.commit()
        except:
         db.rollback()
    db.close()
    if len(RESULT) == 0:
      print("No user Add  and Save")
    RESULT.clear()

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
                savesql()
            elif action == 'delete':
                deleteUser(userinfo_string)
            elif action == 'update':
                updateUser(userinfo_string)
            elif action == 'find':
                findUser(userinfo_string)
            elif action == 'display':
                displayUser(userinfo_string)
            elif action == 'list':
                listsql()
            elif action == 'save':
                savesql()
            elif action == 'load':
                global RESULT
                RESULT = load()
            elif action == 'logout' or action == 'exit':
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
            showmenu()
            logic()
        else:
            print("username or password valid failed.")
            init_fail_count += 1

    print("Game Over.")


if __name__ == '__main__':
    main()
