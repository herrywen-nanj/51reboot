'''
    1.1. 登录认证；
    1.2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    1.3. 格式化输出
'''

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
'''

# 标准模块
import sys
import json
import os
import csv
from datetime import datetime
from prettytable import PrettyTable

TB = PrettyTable()

# 定义变量
RESULT = {}
RESULT_DICT = {}
RESULT_LIST = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']

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
    os.system('clear')

try:
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        try:
            username = input("\n\033[1;33;44m Please input your username (default:51reboot) \033[0m\n:")
            password = input("\n\033[1;33;41m Please input your password (default:123456) \033[0m\n:")
            ClearScreen()
        except KeyboardInterrupt:
            sys.exit(0)
        if username == USERINFO[0].strip() and password == USERINFO[1]:
            try:
                with open('log/login.log', 'a+') as inlog:
                    logTime = datetime.now().strftime('%Y-%m-%d %T')
                    inlog.write("\033[32m{}: Admin {} login succeed!\033[0m\n".format(logTime, USERINFO[0]))
            except Exception as e:
                print(e)
            # print('''
            # 1. Add user info:       \033[31madd username age tel email\033[0m
            # 2. Delete user:         \033[31mdelete username\033[0m
            # 3. Update user info:    \033[31mupdate username set (age|tel|email) = new info\033[0m
            # 4. Find user info:      \033[31mfind username\033[0m
            # 5. Show tables:         \033[31mlist\033[0m
            # ''')
            TAB = PrettyTable()
            print('\n\t\033[5;31;47m北京第三区交通委提醒您：道路千万条，安全第一条。操作不规范，亲人两行泪\033[0m\n')
            Title = ['Serial', 'Description', 'Command']
            TAB.field_names = Title
            TAB.add_row(['1', 'Add user info', '\033[31madd username age tel email.\033[0m'])
            TAB.add_row(['2', 'Delete user', '\033[31mdelete username.\033[0m'])
            TAB.add_row(['3', 'Update user info', '\033[31mupdate username set (age|tel|email) = new info.\033[0m'])
            TAB.add_row(['4', 'Find user info', '\033[31mfind username.\033[0m'])
            TAB.add_row(['5', 'Show tables', '\033[31mlist.\033[0m'])
            TAB.add_row(['6', 'Pagination display', '\033[31mdisplay page 1 pagesize 5.\033[0m'])
            TAB.add_row(['7', 'Count of users', '\033[31mcount.\033[0m'])
            TAB.add_row(['8', 'Clear users table', '\033[31mclear.\033[0m'])
            TAB.add_row(['9', 'Reload when temporarily emptied', '\033[31mreload.\033[0m'])
            TAB.add_row(['10', 'Export csv file', '\033[31mexport [path/filename].Default "csv/UserData+unixtime.csv"\033[0m'])
            TAB.add_row(['11', 'From csv file import data', '\033[31mimport "path/filename"\033[0m'])
            TAB.add_row(['12', 'Exit UserManager system', '\033[31mexit/Ctrl + C/Ctrl + D"\033[0m'])
            TAB.align['Description'] = 'l'
            TAB.align['Command'] = 'l'
            print(TAB)
            print()
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
                        '\033[5;31m You input format is error. Please input (add|delete|update|find) (username age tel email)!\033[0m')
                    continue
                else:
                    Data = info_list[1:]

                if action == "add":
                    try:
                        if len(info_list) != 5:
                            print(
                                "\n\033[5;31m The format you entered is incorrect, {} added failed\033[0m".format(
                                    info_list[1]))
                        elif info_list[1] in RESULT:
                            print("\n\033[5;31m {} is exists! Please change!\033[0m".format(info_list[1]))
                        else:
                            RESULT_DICT = dict(zip(FIELDS, Data))
                            RESULT[info_list[1]] = RESULT_DICT
                            # 打印结果信息
                            print("\n\033[1;32m Add user {} success.\033[0m".format(info_list[1]))
                            fd = open('data/Table_date.file', 'w')
                            fd.write(json.dumps(RESULT))
                            fd.close()
                            logTime = datetime.now().strftime('%Y-%m-%d %T')
                            with open('log/action.log', 'a+') as ActionLog:
                                ActionLog.write('{}: admin {} add user {} succeed!\n'.format(logTime, USERINFO[0], info_list[1]))
                    except Exception as e:
                        print(e)

                elif action == "delete":
                    try:
                        if len(info_list) != 2:
                            print('\033[5;31m Please enter "delete  username" to delete user !\033[0m')
                        elif info_list[1] in RESULT:
                            RESULT.pop(info_list[1])
                            print("\033[1;32m Delete {} success.\033[0m".format(info_list[1]))
                            fd = open('data/Table_date.file', 'w')
                            fd.write(json.dumps(RESULT))
                            fd.close()
                            logTime = datetime.now().strftime('%Y-%m-%d %T')
                            with open('log/action.log', 'a+') as ActionLog:
                                ActionLog.write(
                                    '{}: admin {} delete user {} succeed!\n'.format(logTime, USERINFO[0], info_list[1]))
                        else:
                            print("\033[5;31m This UserName is not exist! Please reinput !\033[0m")
                    except Exception as e:
                        print(e)

                elif action == "update":
                    # 先判断用户是否存在
                    try:
                        if info_list[1] in RESULT:
                            if info_list[2] != 'set':
                                print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(
                                    info_list[1]))
                            elif info_list[2] == 'set' and info_list[3] == 'age':
                                RESULT[info_list[1]]['age'] = info_list[-1]
                                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))
                                # 写日志
                                logTime = datetime.now().strftime('%Y-%m-%d %T')
                                with open('log/action.log', 'a+') as ActionLog:
                                    ActionLog.write(
                                        '{}: admin {} update user {} age {}\n.'.format(logTime, USERINFO[0], info_list[1],
                                                                                     info_list[-1]))
                            elif info_list[2] == 'set' and info_list[3] == 'tel':
                                RESULT[info_list[1]]['tel'] = info_list[-1]
                                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))
                                # 写日志
                                logTime = datetime.now().strftime('%Y-%m-%d %T')
                                with open('log/action.log', 'a+') as ActionLog:
                                    ActionLog.write(
                                        '{}: admin {} update user {} tel {}\n.'.format(logTime, USERINFO[0], info_list[1],
                                                                                     info_list[-1]))
                            elif info_list[2] == 'set' and info_list[3] == 'email':
                                RESULT[info_list[1]]['email'] = info_list[-1]
                                print("\033[1;32m Update {} {} success!\033[0m".format(info_list[1], info_list[3]))
                                logTime = datetime.now().strftime('%Y-%m-%d %T')
                                with open('log/action.log', 'a+') as ActionLog:
                                    ActionLog.write(
                                        '{}: admin {} update user {} email {}\n.'.format(logTime, USERINFO[0], info_list[1],
                                                                                       info_list[-1]))
                            elif info_list[2] == 'set' and info_list[3] == 'username':
                                print("\033[5;31m You could't change Username ! \033[0m")
                            else:
                                print('\033[5;31m You could only change age|tel|email !\033[0m')
                            fd = open('data/Table_date.file', 'w')
                            fd.write(json.dumps(RESULT))
                            fd.close()
                        else:
                            print("\033[5;31m This User is not exist. Please check!\033[0m")
                    except IndexError:
                        print('\033[5;31m Please input "update {} set (age|tel|email) = new data!\033[0m"'.format(
                            info_list[1]))

                elif action == "list":
                    try:
                        # 如果没有记录， 那么提示为空
                        if len(RESULT) < 1:
                            print("\033[1;31m User info is None. Please add user info!\033[0m")
                            continue
                        else:

                            for i in RESULT:
                                # print(i)
                                Tab_List = list(RESULT[i].values())
                                RESULT_LIST.append(Tab_List)
                                # print(RESULT_LIST)
                                # print(RESULT)
                            TB.field_names = FIELDS
                            for i in RESULT_LIST:
                                TB.add_row(i)
                            RESULT_LIST.clear()
                            print(TB)
                            TB.clear_rows()
                    except Exception as e:
                        print(e)

                elif action == "find":
                    try:
                        if len(info_list) != 2:
                            print('\033[5;31m Please enter "find  username" to find user!\033[0m')
                        elif info_list[1] in RESULT:
                            Find_List = list(RESULT[info_list[1]].values())
                            TB.field_names = FIELDS
                            TB.add_row(Find_List)
                            print(TB)
                            TB.clear_rows()
                        else:
                            print('\033[5;31m This user does not exists!\033[0m')
                    except Exception as e:
                        print(e)

                # 统计用户数量
                elif action == "count":
                    try:
                        if len(RESULT) == 0:
                            print("\033[5;31m User data is None! Plase add User data!\033[0m")
                        else:
                            print(
                                "\n\033[32m There are a total of \033[5;32m{}\033[0m \033[32musers\033[0m".format(
                                    len(RESULT)))
                    except Exception as e:
                        print(e)

                elif action == "clear":
                    try:
                        if len(RESULT) != 0:
                            RESULT.clear()
                            ack = input(
                                '\n\033[31mUser data has been temporarily emptied, whether user data is permanently emptied?\n用户信息已经临时被清空,需要永久清空吗?\n(y/n):\033[0m')
                            if ack == 'y':
                                fd = open('data/Table_date.file', 'w')
                                fd.write(json.dumps(RESULT))
                                fd.close()
                                print("\033[5;31m User data has been permanently emptied!\033[0m")
                                # 写日志
                                logTime = datetime.now().strftime('%Y-%m-%d %T')
                                with open('log/action.log', 'a+') as ActionLog:
                                    ActionLog.write('{}: admin {} clear userdata.\n'.format(logTime, USERINFO[0]))
                            else:
                                print('\n\033[1;31m临时清空文件需要重新加载请输入命令: reload\033[0m')
                                continue
                        else:
                            print("\n\033[32m There are a total of {} users\033[0m".format(len(RESULT)))
                    except Exception as e:
                        print(e)

                # 分页实现
                elif action == 'display':
                    '''
                    page 1 pagesize 5
                    '''
                    PageDict = {}
                    PageList = []

                    try:
                        PageDict['page'] = int(info_list[2])
                        PageDict['pagesize'] = int(info_list[-1])
                        for i in RESULT:
                            # print(i)
                            Page_List = list(RESULT[i].values())
                            PageList.append(Page_List)
                        # 分页
                        i = PageDict['page']
                        j = PageDict['pagesize']
                        if j * i <= len(PageList) + 1:
                            Page = PageList[j * (i - 1):j * i]
                            TB.field_names = FIELDS
                            for l in Page:
                                TB.add_row(l)
                            print(TB)
                            TB.clear_rows()
                            print('\n\033[32m This is page {} pagesize {}\033[0m'.format(i, j))

                        elif j > len(PageList):
                            print("\n\033[5;31m The Pagesize set too lager!\033[0m")
                        elif j < 1:
                            print("\n\033[5;31m You must have to set a value of Pagesize!\033[0m")
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
                        unixTime = datetime.now().strftime('%s')
                        csvList = []
                        for i in RESULT:
                            List = list(RESULT[i].values())
                            csvList.append(List)
                        # 如果用户输入两个参数 后面当作文件名字
                        if len(info_list) == 2:
                            dirInfo = info_list[1]
                            with open('{}.csv'.format(dirInfo), 'w', newline='') as csvf:
                                csvfwrite = csv.writer(csvf)
                                csvfwrite.writerow(FIELDS)
                                for i in csvList:
                                    csvfwrite.writerow(i)
                                # 用户自定义文件判断成功与否并写日志
                                if os.path.isfile('{}.csv'.format(info_list[1])):
                                    print("\033[32m Export csv file succeed! File is '{}.csv'".format(dirInfo))
                                    logTime = datetime.now().strftime('%Y-%m-%d %T')
                                    with open('log/action.log', 'a+') as ActionLog:
                                        ActionLog.write(
                                            '{}: admin {} export csv file succeed!\n'.format(logTime, USERINFO[0]))
                        # 如果用户只输入了export,导出至默认路径默认文件
                        elif len(info_list) == 1:
                            with open('csv/UserData{}.csv'.format(unixTime), 'w', newline='') as csvf:
                                csvfwrite = csv.writer(csvf)
                                csvfwrite.writerow(FIELDS)
                                for i in csvList:
                                    csvfwrite.writerow(i)
                                # 默认文件存在判断成功与否并写日志
                                if os.path.isfile('csv/UserData{}.csv'.format(unixTime)):
                                    print("\033[32m Export csv file succeed! File is 'csv/UserData{}.csv'\033[0m".format(unixTime))
                                    logTime = datetime.now().strftime('%Y-%m-%d %T')
                                    with open('log/action.log', 'a+') as ActionLog:
                                        ActionLog.write('{}: admin {} export csv file succeed!\n.'.format(logTime, USERINFO[0]))
                        else:
                            print('\033[31mExport file failed! Please check!\033[0m')
                    except Exception as e:
                        print(e)

                # 从csv文件中导入用户信息,临时导入,输入y后保存成永久信息
                elif action == "import":
                    try:
                        if len(info_list) != 2:
                            print("\033[31m Please enter true argv of path/filename. Example: 'import csv/123.csv'\33[0m")
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
                                    print("\033[31m The {} of csvfile is wrong! Please check format of file!\33[0m".format(i[0]))
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
                                print('\033[32m {} succeed ! {} repeat ! {} format error!\033[0m'.format(len(dataList), len(repeatList), len(formatErrorList)))
                                dataAck = input('\033[31m 导入的数据需要永久保存吗?\n[y/n]:\033[0m')
                                if dataAck == 'y':
                                    fd = open('data/Table_date.file', 'w')
                                    fd.write(json.dumps(RESULT))
                                    fd.close()
                                    logTime = datetime.now().strftime('%Y-%m-%d %T')
                                    with open('log/action.log', 'a+') as ActionLog:
                                        ActionLog.write('{}: admin {} 导入并保存数据 succeed!\n'.format(logTime, USERINFO[0]))
                    except Exception as e:
                        print(e)

                elif action == "reload":
                    try:
                        fd = open('data/Table_date.file', 'r')
                        RESULT = json.loads(fd.read())
                        fd.close()
                    except Exception as e:
                        print(e)

                elif action == "exit":
                    ClearScreen()
                    print(''' \t ___________
\t <   拜拜   >
\t -----------
\t        \   ^__^
\t         \  (oo)\_______
\t            (__)\       )\/\\
\t                ||----w |
\t                ||     ||
\t          ===================
''')
                    sys.exit(0)

                else:
                    print("\033[5;31m invalid action.\033[0m")
        else:
            # 带颜色闪烁
            try:
                print("\033[5;31m username or password error.\033[0m")
                with open('loginFail.log', 'a+') as failog:
                    logTime = datetime.now().strftime('%Y-%m-%d %T')
                    failog.write("\033[31m{}: Admin {} login failed!\033[0m\n".format(logTime, USERINFO[0]))
                INIT_FAIL_CNT += 1
            except Exception as e:
                print(e)
    print("\n\033[1;31m Input {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
except Exception as e:
    print(''' ___________
\t< 非正常退出 >
\t -----------
\t        \   ^__^
\t         \  (oo)\_______
\t            (__)\       )\/\\
\t                ||----w |
\t                ||     ||
\t          ===================
''')