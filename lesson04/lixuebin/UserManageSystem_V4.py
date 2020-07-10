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
'''

# 标准模块
import sys
import json
import os
import csv
from datetime import datetime
from prettytable import PrettyTable
import logging


# 定义变量
RESULT = {}
RESULT_DICT = {}
RESULT_LIST = []

FIELDS = ['username', 'age', 'tel', 'email']


def MkDir():
    '''
    检测文件夹,无则创建文件夹
    :return:
    '''
    try:
        if os.path.exists('log') == False:
            os.mkdir('log')
        if os.path.exists('data') == False:
            os.mkdir('data')
        if os.path.exists('csv') == False:
            os.mkdir('csv')
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
            , ['6', 'Pagination display', '\033[31mdisplay page 1 pagesize 5.\033[0m']
            , ['7', 'Count of users', '\033[31mcount.\033[0m']
            , ['8', 'Clear users table', '\033[31mclear.\033[0m']
            , ['9', 'Reload when temporarily emptied', '\033[31mreload.\033[0m']
            , ['10', 'Export csv file', '\033[31mexport [path/filename].Default "csv/UserData+unixtime.csv"\033[0m']
            , ['11', 'From csv file import data', '\033[31mimport "path/filename"\033[0m']
            , ['12', 'Exit UserManager system', '\033[31mexit/Ctrl + C/Ctrl + D"\033[0m']
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

def AddUser(info_list):
    '''
    添加用户
    :param info_list:
    :return:
    '''
    try:
        if len(info_list[1:]) != 4:
            print("\n\033[5;31m The format you entered is incorrect, {} added failed\033[0m".format(info_list[1]))
        elif info_list[1] in RESULT:
            print("\n\033[5;31m {} is exists! Please change!\033[0m".format(info_list[1]))
        else:
            RESULT_DICT = dict(zip(FIELDS, Data))
            RESULT[info_list[1]] = RESULT_DICT
            # 打印结果信息
            print("\n\033[1;32m Add user {} success.\033[0m".format(info_list[1]))
            # 保存到文件
            Save('data/Table_date.file')
    except Exception as  e:
        return False


def DeleteUser(info_list):
    '''
    删除用户
    :param info_list:
    :return:
    '''
    try:
        if len(info_list) != 2:
            print('\033[5;31m Please enter "delete  username" to delete user !\033[0m')
        elif info_list[1] in RESULT:
            RESULT.pop(info_list[1])
            LOG("log/action.log", '{} has been deleted!'.format(info_list[1]))
            print("\033[1;32m Delete {} success.\033[0m".format(info_list[1]))
            Save('data/Table_date.file')
        else:
            print("\033[5;31m This UserName is not exist! Please reinput !\033[0m")
    except Exception as  e:
        return False


def UpdateInfo(info_list):
    '''
    修改用户信息
    :param info_list:
    :return:
    '''
    try:
        if info_list[1] in RESULT:
            if info_list[2] != 'set':
                print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(info_list[1]))
            elif info_list[2] == 'set' and info_list[3] == 'age':
                RESULT[info_list[1]]['age'] = info_list[-1]
                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))

            elif info_list[2] == 'set' and info_list[3] == 'tel':
                RESULT[info_list[1]]['tel'] = info_list[-1]
                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))

            elif info_list[2] == 'set' and info_list[3] == 'email':
                RESULT[info_list[1]]['email'] = info_list[-1]
                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))

            elif info_list[2] == 'set' and info_list[3] == 'username':
                print("\033[5;31m You could't change Username ! \033[0m")
            else:
                print('\033[5;31m You could only change age|tel|email !\033[0m')
            Save('data/Table_date.file')
        else:
            print("\033[5;31m This User is not exist. Please check!\033[0m")
    except Exception as e:
        print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(
            info_list[1]))


def Find(info):
    '''
    查找用户
    :return:
    '''
    Find_List = []
    if len(info) != 2:
        print('\033[5;31m Please enter "find  username" to find user!\033[0m')
    elif info[1] in RESULT:
        l = list(RESULT[info[1]].values())
        Find_List.append(l)
        print(ShowTable(Find_List))
    else:
        print('\033[5;31m This user does not exists!\033[0m')


def Count():
    '''
    统计用户数量
    :return:
    '''
    if len(RESULT) != 0:
        PrintTalk("共\033[5;32m{}\033[0m个用户".format(len(RESULT)))
        return True
    else:
        return False


def Clear():
    '''
    清空用户
    :return:
    '''
    if len(RESULT) != 0:
        RESULT.clear()
        ack = input(
            '\n\033[31mUser data has been temporarily emptied, whether user data is permanently emptied?\n用户信息已经临时被清空,需要永久清空吗?\n(y/n):\033[0m')
        if ack in ['y', 'Y', 'yes']:
            Save('data/Table_date.file')
            print("\033[5;31m User data has been permanently emptied!\033[0m")
        else:
            print('\n\033[1;31m临时清空用户列表后,添加用户会清空原有用户,需要重新加载请输入命令: reload\033[0m')
            return True
            # continue
    else:
        return False


def List():

    try:
        if len(RESULT) < 1:
            print("\033[5;31m User data is None! Plase add User data!\033[0m")
            return False
            # continue
        else:
            for i in RESULT:
                Tab_List = list(RESULT[i].values())
                RESULT_LIST.append(Tab_List)
            print(ShowTable(RESULT_LIST))
            RESULT_LIST.clear()
            print("\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
                len(RESULT)))
            return True
    except Exception as e:
        return False


def PositionAction(i, j):
    '''
    :param i: i = page
    :param j: j = pagesize //default == 5
    :return: Page
    '''
    PageDict = {}
    PageList = []
    for user in RESULT:
        Page_List = list(RESULT[user].values())
        PageList.append(Page_List)
    # 分页
    if j * i <= len(PageList) + 1:
         Page = PageList[j * (i - 1):j * i]
         print(ShowTable(Page))
         return True
    if j > len(PageList):
        Page = PageList[j * (i - 1):j * i]
        print(ShowTable(Page))
        return True
    elif j * i - j < len(PageList):
        Page = PageList[j * i - j:]
        print(ShowTable(Page))
        return True
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
        j = 5
        if PositionAction(i, j):
            return True, i, j
        else:
            return False, i, j
    elif info_list[1] == 'page' and info_list[3] == 'pagesize':
        i = int(info_list[2])
        j = int(info_list[-1])
        if PositionAction(i, j):
            return True, i, j
        else:
            return False, i, j


def Reload(file):
    if os.path.isfile(file):
        with open(file, 'r') as fd:
            RESULT = json.loads(fd.read())
        return True
    else:
        return False


def EXfile(info_list):
    dirInfo = info_list[1]
    with open('{}.csv'.format(dirInfo), 'w', newline='') as csvf:
        csvfwrite = csv.writer(csvf)
        csvfwrite.writerow(FIELDS)
        for i in csvList:
            csvfwrite.writerow(i)
        # 用户自定义文件判断成功与否
        if os.path.isfile('{}.csv'.format(info_list[1])):
            return True
        else:
            return False


def EXDefaultFile():
    unixTime = datetime.now().strftime('%s')
    with open('csv/UserData{}.csv'.format(unixTime), 'w', newline='') as csvf:
        csvfwrite = csv.writer(csvf)
        csvfwrite.writerow(FIELDS)
        for i in csvList:
            csvfwrite.writerow(i)
        # 默认文件存在判断成功
        if os.path.isfile('csv/UserData{}.csv'.format(unixTime)):
            return True
        else:
            return False


def Export(info_list):
    dirInfo = info_list[1]
    unixTime = datetime.now().strftime('%s')
    global csvList
    csvList = []
    for i in RESULT:
        List = list(RESULT[i].values())
        csvList.append(List)
    # 如果用户输入两个参数 后面当作文件名字
    if len(info_list) == 2:
        if EXfile(info_list):
            print("\033[32m Export csv file succeed! File is '{}.csv'".format(dirInfo))
    # 如果用户只输入了export,导出至默认路径默认文件
    elif len(info_list) == 1:
        if EXDefaultFile(info_list):
            print("\033[32m Export csv file succeed! File is 'csv/UserData{}.csv'\033[0m".format(unixTime))
    else:
        print('\033[31mExport file failed! Please check!\033[0m')


def Import(info_list):
    if len(info_list) != 2:
        print(
            "\033[31m Please enter true argv of path/filename. Example: 'import csv/123.csv'\33[0m")
    elif os.path.isfile(info_list[1]) == False:
        print("\033[31m The file is not exists! Please check!\33[0m")
    else:
        impData = csv.reader(open('{}'.format(info_list[1]), 'r'))
        dataList = []
        formatErrorList = []
        repeatList = []

        for i in impData:
            if len(i) != len(FIELDS):
                formatErrorList.append(i)
                print(
                    "\033[31m The {} of csvfile is wrong! Please check format of file!\33[0m".format(
                        i[0]))
                continue
            elif i[0] in RESULT:
                repeatList.append(i)
                print("\033[31m This user of {} is repeat! Please check!\33[0m".format(i[0]))
                continue
                # 重复数据校验
            else:
                dataList.append(i)
        lengthRST = len(RESULT)
        for d in dataList[1:]:
            RESULT_DICT = dict(zip(FIELDS, d))
            RESULT[d[1]] = RESULT_DICT
        if len(RESULT) != lengthRST:
            print('\033[32m Import file {} succeed ! \033[0m'.format(info_list[1]))
            print('\033[32m {} succeed ! {} repeat ! {} format error!\033[0m'.format(len(dataList),
                                                                                     len(
                                                                                         repeatList),
                                                                                     len(
                                                                                         formatErrorList)))
            dataAck = input('\033[31m 导入的数据需要永久保存吗?\n[y/n]:\033[0m')
            if dataAck == 'y':
                Save('data/Table_date.file')



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

def Action(user_info):
    while True:
        # 业务逻辑
        try:
            info = input("\n\033[1;31;47m 请开始你的表演 \033[0m\n\t:")
        except KeyboardInterrupt:
            sys.exit(0)
        # string -> list
        info_list = info.split()

        try:
            action = info_list[0]
        except IndexError:
            print(
                '\033[5;31m You input format is error. Please input (add|delete|update|find|count|list|clear|export|import|display) (username age tel email)!\033[0m')
            continue
        else:
            global Data
            Data = info_list[1:]
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
            if not Clear():
                print("\n\033[32m There are a total of {} users\033[0m".format(len(RESULT)))
        # 分页实现
        elif action == 'display':

            try:
                if Position(info_list)[0]:
                    print('\n\033[32m This is page {} pagesize {}\033[0m'.format(Position(info_list)[1],
                                                                                 Position(info_list)[2]))
                else:
                    print("\n\033[5;31m You set page or pagesize value is wrong!\033[0m")
            except ValueError:
                print("\n\033[5;31m You must have to set a value of pagesize or page!\033[0m")
            except Exception as e:
                print(e)
                continue
        # 导出用户信息到csv文件中,可以选择路径进行导出,也可以只输入export命令默认导出到csv路径下
        elif action == "export":
            try:
                Export(info_list)
            except Exception as e:
                print(e)
        # 从csv文件中导入用户信息,临时导入,输入y后保存成永久信息
        elif action == "import":
            try:
                Import(info_list)
            except Exception as e:
                print(e)
        elif action == "reload":
            try:
                if Reload('data/Table_date.file'):
                    print("重载成功\033[5;32m{}\033[0m个用户".format(RESULT))
                else:
                    print("持久化文件不存在,重载失败")
            except Exception as e:
                print(e)
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
                try:
                    fd = open('data/Table_date.file', 'r')
                    RESULT = json.loads(fd.read())
                    fd.close()
                except IOError:
                    pass
                except Exception as e:
                    print(e)
                    pass
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
