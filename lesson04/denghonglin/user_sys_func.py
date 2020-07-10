"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add tom 14 132xxx tom@facebook.com
    3.2 删 delete        # delete tom
    3.3 改 update        # update tom set age = 19
    3.4 查 list          # list
    3.5 搜 find          # find tom
3. 格式化输出
"""
import sys
import logging
import re
from prettytable import PrettyTable
import csv

RESULT = {'zhangsan': ['zs123', '13211001100', 'zhangsan@126.com']}
MATCH_MAIL = re.compile(r'^\w+@(\w+\.)+(com|cn|net)$')
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 3
SYS_USER = ('admin','admin123')
FIELDS = ("账号", "密码", "电话", "邮箱")
FILENAME = "6-user_data.txt"
CSVFILE = 'user_data.csv'

logging.basicConfig(level = logging.DEBUG, \
                    format = '%(asctime)s   %(filename)s [line: %(lineno)d] %(levelname)s %(message)s',\
                    datefmt='%a  %Y-%m-%d %H:%M:%S', \
                    filename='user.log', \
                    filemode='w')
logger = logging.getLogger(__name__)

Usage = '''{}
add         : add tom 12 132xxx tom@facebook.com
update      : udpate tom set age = 18
list        : xxx
find        : find tom
display     : display page 2 page_size 3
doc         : enable/disable docstring
exit        : quit
save        : save userData.txt
load        : load userData.txt
{}
'''.format('-'*70, '-'*70)
def inRed(s):
    return highlight('') + "%s[31;2m%s%s[0m"%(chr(27), s, chr(27))
def inGreen(s):
    return highlight('') + "%s[32;2m%s%s[0m"%(chr(27), s, chr(27))
def inYellow(s):
    return highlight('') + "%s[33;2m%s%s[0m"%(chr(27), s, chr(27))
def highlight(s):
    return "%s[30;2m%s%s[1m"%(chr(27), s, chr(27))

def readData(datafile):
    udata = {}
    with open(datafile) as fo:
        for line in fo.readlines():
            line = line.strip()
            username = line.split()[0]
            einfo = line.split()[1:]
            udata[username] = einfo
    return udata

def listUser(datafile):
    tb = PrettyTable()
    userdata = readData(datafile)
    for k,v in userdata.items():
        tb.field_names = FIELDS
        tb.add_row([k, v[0],v[1],v[2]])
    print(tb)

def addUser():
    # user_data = readData(datafile)
    user_data = RESULT
    username = input('plz input username:')
    if username in user_data.keys():
        print(inYellow("user is exist."))
        exit(0)
    pwd, phone, mail = input('input password: '), input('phone: '), input('email: ')
    user_data[username] = [pwd,phone,mail]

def updateUser(cmdStr):
    # update tom set age = 19
    cmd = cmdStr.split()
    if len(cmd) != 6:
        print(inRed('cmd invalid.'))
    uname, sfield, sval = cmd[1], cmd[3], cmd[5]
    k_v = {'pwd':0, 'tel':1, 'mail':3}
    if uname in RESULT and cmd[0] == 'update' and cmd[2] == 'set' and cmd[4] == '=':
        RESULT[uname][k_v[sfield]] = sval
        print(RESULT)
    else:
        print(inYellow('%s not found' %uname))

def delUser(cmdStr):
    cmd = cmdStr.split()
    if len(cmd) == 2 and cmd[0] == 'delete' and cmd[1] in RESULT.keys():
        del RESULT[cmd[1]]
    else:
        print(inRed('cmd invalid or username not found'))
    print(RESULT)

def saveCsv():
    with open(CSVFILE,'w+') as f:
        csv_writer = csv.writer(f,dialect='excel')
        csv_writer.writerow([FIELDS])
        for line in RESULT.keys():
            csv_writer.writerow([line,RESULT[line][0],RESULT[line][1],RESULT[line][2]])
    print(inGreen('user_data save to csv.'))

def loadFile(filename):
    ufile = csv.reader(open(filename, 'r'))
    for line in ufile:
        if line[0] == "账号":
            continue
        else:
            RESULT[line[0]] = [line[1],line[2],line[3]]
    print(inGreen('load file.'))

def display():
    pass

def showmenu():
    des = '''{}
    add         : add tom 12 132xxx tom@facebook.com
    update      : udpate tom set age = 18
    list        : xxx
    find        : find tom
    display     : display page 2 page_size 3
    doc         : enable/disable docstring
    exit        : quit
    save        : save userData.txt
    load        : load userData.txt
    {}
    '''.format('-' * 70, '-' * 70)
    print(des)

def login(uname,pwd):
    if uname == SYS_USER[0] and pwd == SYS_USER[1]:
        logger.debug('%s login success.' %uname)
        return True
    else:
        return False


def main():
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        uname = input("usernmae: ")
        pwd = input('password: ')
        if login(uname,pwd):
            while True:
                cmd = input('plz input command: ')
                action = cmd.split()[0]
                if action == 'add':
                    addUser()
                elif action == 'update':
                    updateUser(cmd)

                """
                因最近项目上线，未完待续...
                """





if __name__ == '__main__':
    main()

    """
    USER_DATA = "6-user_data.txt"
    # listUser(USER_DATA)
    # addUser(USER_DATA)

    # str1 = 'update zhangsan set pwd  = 10'
    str2 = 'delete zhangsan'
    # updateUser(str1)
    delUser(str2)
    # loginAuth(USER_DATA)
    """