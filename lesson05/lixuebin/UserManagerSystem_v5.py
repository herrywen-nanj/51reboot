'''
3.1 将列表转换为字典
3.2 分页 --> 根据page和pagesize 进行分页并优雅输出
3.3 持久化数据
3.4 异常处理
3.5 优雅格式化输出
3.6 支持导出数据到csv --> 判断文件是否存在 --> 提示成功或失败
3.7 记录登陆日志 --> 登陆成功 --> log/login.log  登陆失败 --> log/loginFail.log
3.8 记录操作日志 --> add, update, delete, clear 进行记录
3.9 统计用户数量
3.10 清空用户 --> 临时清空 --> 可以reload加载 --> 永久清空 --> 直接修改文件永久清空
3.11 支持从cvs中导入数据 --> 文件存在 --> 文件格式校验 --> 重复数据校验

4.1 改写函数

5.1 数据持久化到MySQL数据库
5.2 使用configparser模块读取配置文件
'''

# 标准模块
import sys
import json
import os
import csv
from datetime import datetime
from prettytable import PrettyTable
import logging
import pymysql
import configparser


# 定义变量
RESULT = {}
RESULT_DICT = {}
RESULT_LIST = []

FIELDS = ['id', 'username', 'age', 'tel', 'email']


def MyConn(filename = 'mysql.ini'):
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        if os.path.isfile(filename):
            connect=pymysql.connect(
                host = config.get('mysqld', 'host'),
                port = config.getint('mysqld', 'port'),
                user = config.get('mysqld', 'user'),
                password = config.get('mysqld', 'password'),
                database = config.get('mysqld', 'database')
        )
            return connect
        else:
            return '配置文件不存在',False
    except Exception as  e:
        return e, False

def curInsert(sql):
    conn = MyConn()
    if not conn:
        return 'conn is failed.', False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        conn.commit()
        return  "\n\033[1;32m Add user success.\033[0m", True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def curDelete(sql):
    conn = MyConn()
    if not conn:
        return 'conn is failed.', False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount !=1:
            return  '"\033[5;31m This UserName is not exist! Please reinput !\033[0m"',False
        else:
            conn.commit()
            return 'delete success!', True

    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def curUpdate(sql):
    conn = MyConn()
    if not conn:
        return 'conn is failed.', False
    cur = conn.cursor()
    try:
        cur.execute(sql)
        if cur.rowcount == 0:
            return 'User is not exists,update failed!' , False

        conn.commit()
        return 'update success', True
    except Exception as e:
        conn.rollback()
        return e, False
    finally:
        cur.close()
        conn.close()

def curSelect(sql):
    conn = MyConn()
    if not conn:
        return 'conn is failed.', False
    cur = conn.cursor()
    try:
        if cur.execute(sql):
            data = cur.fetchall()
            datalist = []
            for i in data:
                datalist.append(list(i))
            return  datalist, True
        else:
            return '\033[5;31m User list is None! Please add user info!\033[0m', False
    except Exception as e:
        return e, False
    finally:
        cur.close()
        conn.close()

def MkDir():
    '''
    检测文件夹,无则创建文件夹
    :return:
    '''
    try:
        if os.path.exists('log') == False:
            os.mkdir('log')
    except Exception as e:
        print(e)


def ClearScreen():
    '''
    清屏
    :return:
    '''
    os.system('clear')


def loginAuth(username, password):
    '''
    登陆验证
    :param username:
    :param password:
    :return: bool
    '''
    try:
        adminInfo = ("51reboot", "123456")
        if username == adminInfo[0].strip() and password == adminInfo[1]:
            return True
        else:
            return False
    except Exception as  e:
        return False


def ShowTable(List):
    '''
    格式化: 接收列表
    :return: 返回格式化的表格
    '''
    try:
        TB = PrettyTable()
        TB.field_names = FIELDS
        for l in List:
            TB.add_row(l)
        return TB
        # TB.clear_rows()
    except ModuleNotFoundError:
        print("Prettytable 模块没有安装,请安装后再使用: pip3.x install prettytable.")
    except Exception as e:
        return False


def ActionGuide():
    '''
    操作指引
    :return:
    '''
    try:
        TAB = PrettyTable()
        print('\n\t\033[5;31;47m北京第三区交通委提醒您：道路千万条，安全第一条。操作不规范，亲人两行泪\033[0m\n')
        Title = ['Serial', 'Description', 'Command']
        TAB.field_names = Title
        row = [
            ['1', 'Add user info', '\033[31madd username age tel email.\033[0m']
            , ['2', 'Delete user', '\033[31mdelete username.\033[0m']
            , ['3', 'Update user info', '\033[31mupdate username set (age|tel|email) = new info.\033[0m']
            , ['4', 'Find user info', '\033[31mfind username.\033[0m']
            , ['5', 'Show tables', '\033[31mlist.\033[0m']
            , ['6', 'Pagination display', '\033[31mdisplay page 1 [pagesize 5].\033[0m']
            , ['7', 'Count of users', '\033[31mcount.\033[0m']
            # , ['8', 'Export csv file', '\033[31mexport [path/filename].Default "csv/UserData+unixtime.csv"\033[0m']
            # , ['9', 'From csv file import data', '\033[31mimport "path/filename"\033[0m']
            , ['8', 'Exit UserManager system', '\033[31mexit/Ctrl + C/Ctrl + D"\033[0m']
        ]
        for i in row:
            TAB.add_row(i)
        TAB.align['Description'] = 'l'
        TAB.align['Command'] = 'l'
        print(TAB)
        print()
    except Exception as  e:
        print("显示指导信息失败")


def PrintTalk(content):
    print(''' \n
    \t   ___________
    \t < {} >
    \t   -----------
    \t        \   ^__^
    \t         \  (oo)\_______
    \t            (__)\       )\/\\
    \t                ||----w |
    \t                ||     ||
    \t          ===================
    '''.format(content))


def Save(File):
    '''
    持久保存
    :param File:
    :return:
    '''
    try:
        with open(File, 'w') as fd:
            fd.write(json.dumps(RESULT))
    except Exception as e:
        return False

def AddUser(info_list, table='users'):
    '''
    添加用户
    :param info_list:
    :return:
    '''
    try:
        if len(info_list[1:]) != 4:
            print("\n\033[5;31m The format you entered is incorrect, {} added failed\033[0m".format(info_list[1]))
            # print("\n\033[5;31m {} is exists! Please change!\033[0m".format(info_list[1]))
        else:
            sql = '''insert into {} (username,age,tel,email) values ('{}',{},'{}','{}');'''.format(table,info_list[1],info_list[2],info_list[3],info_list[4])
            msg, ok = curInsert(sql)
            if ok:
                print(msg)
            else:
                print(msg)
            # 打印结果信息
    except Exception as  e:
        return False


def DeleteUser(info_list,table='users'):
    '''
    删除用户
    :param info_list:
    :return:
    '''
    try:
        if len(info_list) != 2:
            print('\033[5;31m Please enter "delete  username" to delete user !\033[0m')
        else:
            sql = '''delete from {} where username = '{}';'''.format(table, info_list[1])
            msg, ok = curDelete(sql)
            if ok:
                LOG("log/action.log", '{} has been deleted!'.format(info_list[1]))
                print(msg)
    except Exception as  e:
        return False


def UpdateInfo(info_list,table='users'):
    '''
    修改用户信息
    :param info_list:
    :return:
    '''
    name=info_list[1]
    try:
        if info_list[2] != 'set':
            return '\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(name),False
        sql = '''update {} set {}='{}' where username='{}';'''.format(table, info_list[3], info_list[-1], name)
        msg, ok = curUpdate(sql)
        if ok:
            Find(['find',name])
            return msg, True
        else:
            return msg, False
    except Exception as e:
        print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(
            info_list[1]))


def Find(info,table='users'):
    '''
    查找用户
    :return:
    '''
    Find_List = []
    # if len(info) != 2:
    #     print('\033[5;31m Please enter "find  username" to find user!\033[0m')
    sql = '''select * from {} where username = '{}';'''.format(table,info[1])
    msg, ok = curSelect(sql)
    if ok:
      print(ShowTable(msg))
      print("\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
          len(msg)))
    else:
        print(msg)


def Count(table='users'):
    '''
    统计用户数量
    :return:
    '''
    sql = '''select count(*) from {};'''.format(table)
    msg, ok = curSelect(sql)

    if ok:
        PrintTalk("共\033[5;32m{}\033[0m个用户".format(msg[0][0]))
        return True
    else:
        return False


def List(table='users'):

    try:
        sql =  '''select * from {}'''.format(table)
        msg, ok = curSelect(sql)
        if type(msg) == list:
            print(ShowTable(msg))
            print("\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
                len(msg)))
            msg.clear()
            return True
        else:
            return False
    except Exception as e:
        return False


def PositionAction(i, j=5, table='users'):
    '''
    :param i: i = page
    :param j: j = pagesize //default == 5
    :return: Page
    '''
    sql = '''select * from {}'''.format(table)
    PageList, ok = curSelect(sql)
    Lth=len(PageList)
    print(PageList)
    if ok:
    # 分页
        if j * i <= Lth + 1:
             Page = Lth[j * (i - 1):j * i]
             print(ShowTable(Page))
             return True
        elif j > len(PageList):
            Page = PageList[j * (i - 1):]
            print(ShowTable(Page))
            return True, j, i
        elif j * i - j < len(PageList):
            Page = PageList[j * i - j:]
            print(ShowTable(Page))
            return True, j, i
        else:
            return False, j, i
    else:
        return False


def Position(info_list):
    '''
    Default pagesize == 5
    :param info_list:
    :return:
    '''
    if info_list[1] == 'page' and 'pagesize' not in info_list:
        i = int(info_list[2])
        if PositionAction(i):
            print('\n\033[32m This is page {} pagesize 5\033[0m'.format(i))
            return True
        else:
            print("\n\033[5;31m You set page or pagesize value is wrong!\033[0m")
            return False
    elif info_list[1] == 'page' and info_list[3] == 'pagesize':
        try:
            i = int(info_list[2])
            j = int(info_list[-1])
            if PositionAction(i, j):
                print('\n\033[32m This is page {} pagesize {}\033[0m'.format(i , j))
                return True
            else:
                print("\n\033[5;31m You set page or pagesize value is wrong!\033[0m")
                return False
        except Exception as e:
            return False


def Reload(file):
    if os.path.isfile(file):
        with open(file, 'r') as fd:
            RESULT = json.loads(fd.read())
        return True
    else:
        return False


def EXfile(info_list,table='users'):
    try:
        dirInfo = info_list[1]
        sql = '''select * from {} into outfile '/tmp/{}.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n';'''.format(table, dirInfo)
        msg, ok = curInsert(sql)
        if ok:
            # 用户自定义文件判断成功与否
            if os.path.isfile('/tmp/{}.csv'.format(info_list[1])):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False


def EXDefaultFile(table='users'):
    unixTime = datetime.now().strftime('%s')
    print(unixTime)
    try:
        sql = '''select * from {} into outfile '/tmp/usersInfo_{}.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n';'''.format(table, unixTime)
        msg, ok = curInsert(sql)
        if ok:
        # 默认文件存在判断成功
            if os.path.isfile('/tmp/usersInfo_{}.csv'.format(unixTime)):
                return True
            else:
                return False
        else:
            return False
    except Exception as e:
        print(e)
        return False


def Export(info_list):
    dirInfo = info_list[1]
    unixTime = datetime.now().strftime('%s')
    # 如果用户输入两个参数 后面当作文件名字
    if len(info_list) == 2:
        if EXfile(info_list):
            msg = "\033[32m Export csv file succeed! File is '/tmp/{}.csv'".format(dirInfo)
            return msg, True
        else:
            msg = '\033[31mExport file failed!\033[0m'
            return msg, False
    # 如果用户只输入了export,导出至默认路径默认文件
    elif len(info_list) == 1:
        if EXDefaultFile():
            msg = "\033[32m Export csv file succeed! File is 'tmp/userInfo_{}.csv'\033[0m".format(unixTime)
            return msg, True
        else:
            msg = '\033[31mExport file failed! \033[0m'
            return msg, False
    else:
        msg = '\033[31m输入错误\033[0m'
        return msg, False


def Import(info_list,table='users'):
    if len(info_list) != 2:
        print(
            "\033[31m Please enter true argv of path/filename. Example: 'import csv/123.csv'\33[0m")
    else:
        if os.path.isfile(info_list[1]):
            file = input('您将要导入的文件是{},确认请输入y/Y:'.format(info_list[1]))
            if file in ['y','Y','yes','Yes','YES']:
                sql = '''load data local infile '{}' into table {} fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n';'''.format(info_list[1],table)
                msg, ok = curInsert(sql)
                if ok:
                    print("文件导入成功.")
                else:
                    print("文件导入失败")
        else:
            print("文件不存在")



# logging.basicConfig(level = logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    # datefmt = '%Y-%m-%d  %H:%M:%S %a'')

def LOG(logfile, message):
    '''
    定义log函数
    :return:
    '''
    # 创建一个logger
    logger = logging.getLogger('UserManagerSystem')
    logger.setLevel(logging.DEBUG)

    # 建立一个filenhandler把日志记录在文件,级别debug
    fl = logging.FileHandler(logfile)
    fl.setLevel(logging.DEBUG)

    # 设置日志格式
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(message)s")
    fl.setFormatter(formatter)

    # 将handler添加在logger对象中
    logger.addHandler(fl)
    logger.debug(message)

def Action():
    while True:
        # 业务逻辑
        try:
            info = input("\n\033[1;31;47m 请开始你的表演 \033[0m\n\t:")
            info_list = info.split()
            action = info_list[0]
        except KeyboardInterrupt:
            sys.exit(0)
        # string -> list
        except Exception as e:
            print('\033[5;31m You input format is error. Please input (add|delete|update|find|count|list|clear|export|import|display) (username age tel email)!\033[0m')
            continue
        #     #
        # else:
        #     global Data
        #     Data = info_list[1:]
        if action == "add":
            AddUser(info_list)
        elif action == "delete":
            DeleteUser(info_list)
        elif action == "update":
            UpdateInfo(info_list)
        elif action == "list":
            # 如果没有记录， 那么提示为空
            List()
        elif action == "find":
            Find(info_list)
        # 统计用户数量
        elif action == "count":
            Count()
        elif action == "clear":
            pass
            # if not Clear():
            #     print("\n\033[32m There are a total of {} users\033[0m".format(len()))
        # 分页实现
        elif action == 'display':
            Position(info_list)
        # 导出用户信息到csv文件中,可以选择路径进行导出,也可以只输入export命令默认导出到csv路径下
        elif action == "export":
            msg, ok = Export(info_list)
            if ok:
                print(msg)
            else:
                print(msg)
        # 从csv文件中导入用户信息,临时导入,输入y后保存成永久信息
        elif action == "import":
            Import(info_list)
        elif action == "exit":
            ClearScreen()
            PrintTalk("欢迎下次光临")
            sys.exit(0)

        elif action == "help":
            ActionGuide()

        else:
            print("\033[5;31m invalid action.\033[0m")

def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 3
    try:
        while INIT_FAIL_CNT < MAX_FAIL_CNT:
            try:
                MkDir()
                username = input("\n\033[1;33;44m Please input your username (default:51reboot) \033[0m\n:")
                password = input("\n\033[1;33;41m Please input your password (default:123456) \033[0m\n:")
                ClearScreen()
            except KeyboardInterrupt:
                sys.exit(0)
            if loginAuth(username, password):
                LOG('log/login.log', '{} is loged in!'.format(username))
                ActionGuide()
                # 如果输入无效的操作，则反复操作, 否则输入exit退出
                Action()
            else:
                # 带颜色闪烁
                try:
                    print("\033[5;31m username or password error.\033[0m")
                    LOG('log/login.log', '{} is loged fialed!'.format(username))
                    INIT_FAIL_CNT += 1
                except Exception as e:
                    print(e)
        print("\n\033[1;31m Input {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
    except KeyboardInterrupt:
        PrintTalk("非正常退出")
    except Exception as e:
        PrintTalk("非正常退出")

if __name__ == '__main__':
    main()
