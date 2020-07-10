#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
用户管理系统V3
Author: WangXiaoYun
'''
import sys, os, getpass,math,csv,LogMgt,ConfigMgt,MysqlOps
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["UserID", "Name", "Phone", "Company", "Address", "Email"]
stuInfo = 'StuInfo.txt'
tempDict = {}

HelpMeu = '''{}
add         : 添加用户信息. 
              eg: add 201 monkey 13288888888 51reboot BeiJing mk@51reboot.com
              # 添加工号为 1 的用户信息
del         : 删除用户信息. 
              eg: del stu1
              # 删除工号为 1 的用户信息
deltemp     : 删除临时列表中的用户信息. 
              eg: deltemp stu1
              # 删除临时列表中工号为 1 的用户信息
update      : 更新用户信息. 
              eg: update stu1 set phone = 13288888888   
              # 更新工号为 2 的用户信息
search      : 搜索用户信息. 
              eg: search stu1
              # 搜索工号为1的用户信息
list        : 列出临时列表中的用户信息
              eg: list
display     : 分页显示所有用户信息. 
              eg: display 3 2  
              # 显示第三页，每页显示 2 行，display不带参数，默认显示第一页，每页显示 5 行
export      : 导出用户信息到csv表格中. 
              eg: export 51reboot.csv
              # export 不带参数则默认导出到 StuInfo.csv，则导出文件名为参数名
save        : 保存用户信息到本地文件中. 
              eg: save
              # 默认保存到本地的 StuInfo.txt 文件中
load        : 加载本地用户信息文件.
              eg: load
help        : 打印帮助信息.
              eg: help
exit        : 退出菜单.
              eg: exit
{}'''.format('-' * 80, '-' * 80)

#功能函数
def loginAuth(inUsername,inPassword):
    #从配置文件中读取登录验证的用户密码
    username,ok = ConfigMgt.ReadConfig('config.ini','Login','username')
    password, ok = ConfigMgt.ReadConfig('config.ini', 'Login', 'password')
    if inUsername == username and inPassword == password:
        return 'Login succ.',True   # 返回当前状态
    else:
        return 'Login failed.',False

def exitMeu():
    x.clear_rows()
    exitMes = 'User Management System Exit Successfully.'
    LogMgt.UserLog(exitMes)     #记录日志
    sys.exit(exitMes)

def listTempUser(args):
    x.clear_rows()
    tempDict = tempUserDict(args)
    for Item in tempDict.keys():
        stuId,stuName,stuPhone,stuCompany,stuAddress,stuEmail = Item,tempDict[Item]['name'],tempDict[Item]['Phone'],tempDict[Item]['Company'],tempDict[Item]['Address'],tempDict[Item]['Email']
        x.add_row([stuId, stuName,stuPhone,stuCompany,stuAddress,stuEmail])
    print('\n查看待录入的用户信息: ')
    print(x)

def loadUser():  # 从数据库读取用户信息
    sql = '''select * from yusers;'''

    try:
        stuList,result,ok = MysqlOps.main('select',sql)
    except Exception as e:
        loadMes = str(e)
        LogMgt.UserLog(loadMes)
        print(loadMes)
        loadMes = 'User Information Loading Failed.'
        LogMgt.UserLog(loadMes)
        stuList = 'None'
        ok = False
    else:
        if result == 'No data found in the table.':
            loadMes,stuList,ok = 'No data in the table.',[],True
        elif stuList == []:
            loadMes = "Table 'ops.yusers' doesn't exist, 请查看 readme.md 创建表 ops.yusers"
            sys.exit(loadMes)
        else:
            loadMes = 'User Information Loading successfully.'
            LogMgt.UserLog(loadMes)
            ok = True
    return stuList,loadMes,ok

def ckUserFormat(args):
    if len(args) < 3:   #判断用户输入的格式长度
        Mes = '格式输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)
    elif len(args) >= 3 and len(args) <= 7:
        try:   #输入非 int 类型会报错
            stuId = 'stu' + str(int(args[1]))
        except Exception as e:
            Mes = str(e)    # try 捕获的内容也写入日志
            LogMgt.UserLog(Mes)
            print(Mes)
            stuId = 'None'  # try 捕获到异常后，_StuId 需要传一个默认值，否则报错
        stuName = args[2]
        if len(args) == 3:
            stuPhone, stuCompany,stuAddress,stuEmail,ok,rMsg = 'None','None','None','None',True,''
        elif len(args) == 4:
            if len(args[3]) == 11:   #手机号长度判断
                stuPhone,stuCompany,stuAddress,stuEmail,ok,rMsg = args[3],'None','None','None',True,''
            else:
                stuPhone,stuCompany,stuAddress, stuEmail,ok,rMsg = 'None','None','None','None',False,'用户电话号码\033[1;31m长度为11位\033[0m，格式输入有误，请重新输入.'
                LogMgt.UserLog(rMsg)
        elif len(args) == 5:
            stuPhone,stuCompany,stuAddress, stuEmail,ok,rMsg = args[3],args[4],'None','None',True,''
        elif len(args) == 6:
            stuPhone,stuCompany,stuAddress,stuEmail,ok,rMsg = args[3], args[4],args[5],'None',True,''
        elif len(args) == 7:
            if args[6].find('@') == -1:   #邮件格式是否包含 @ 判断
                stuPhone,stuCompany,stuAddress,stuEmail,ok,rMsg = args[3],args[4],args[5],'None',False,'用户Email地址\033[1;31m必须包含@\033[0m，格式输入有误，请重新输入.'
                LogMgt.UserLog(rMsg)
            else:
                stuPhone,stuCompany,stuAddress,stuEmail,ok,rMsg = args[3],args[4],args[5],args[6],True,''
        return stuId,stuName,stuPhone,stuCompany,stuAddress,stuEmail,ok,rMsg
    elif len(args) > 6:
        Mes = '用户格式输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)

def tempUserDict(args):
    if len(args) >= 3 and len(args) <= 7:    #用户输入的长度符合条件才允许进入
        stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail,ok,rMsg = ckUserFormat(args)
        if stuId != 'None':
            if ok == True:
                if tempDict.__contains__(stuId) == False:
                    tempDict[stuId] = {}
                    tempDict[stuId]['name'] = stuName
                    tempDict[stuId]['Phone'] = stuPhone
                    tempDict[stuId]['Company'] = stuCompany
                    tempDict[stuId]['Address'] = stuAddress
                    tempDict[stuId]['Email'] = stuEmail
                    x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                    Mes = '用户信息 \033[31;1m{}\033[0m 已加入队列.'.format(stuName)
                    LogMgt.UserLog(Mes)
                    print(Mes+'\n')
                else:
                    Mes = '该用户ID \033[31;1m{}\033[0m 已存在.添加失败.'.format(stuId)
                    LogMgt.UserLog(Mes)
                    print(Mes)
            else:
                print(rMsg)
    return tempDict

def addUser(args):
    ckUserFormat(args)
    tempUserDict(args)

def delTemp(args):
    tempDict = tempUserDict(args)
    if len(args) < 2:
        Mes = '指令输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)
    else:
        try:
            userID = args[1]
            if userID.find('stu') == -1:
                delUserID = 'stu' + str(int(userID))
        except Exception as e:
            Mes = str(e)
            LogMgt.UserLog(Mes)
            print(Mes)
        else:
            if tempDict.__contains__(userID) == True:
                tempDict.pop(userID)
                Mes = '用户ID \033[31;1m{}\033[0m 从队列中删除成功.'.format(userID)
                LogMgt.UserLog(Mes)
                print(Mes)
            else:
                Msg = '用户ID {} 不存在.'.format(userID)
                LogMgt.UserLog(Msg)
                print(Msg)

def delUser(args):
    if len(args) < 2:
        Mes = '指令输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)
    else:
        x.clear_rows()
        delUserID = args[1]
        tempUser = []
        stuList,Mes,ok =loadUser()    #读取数据库用户信息

        if stuList == []:
            print('用户ID {} 不存在.'.format(delUserID))
        for Row in stuList:
            tempUser.append(Row['UserID'])

            if delUserID not in tempUser:
                Msg = '用户ID {} 不存在.'.format(delUserID)
                LogMgt.UserLog(Msg)
                print(Msg)
            else:
                for Row in stuList:
                    if Row['UserID'] == delUserID:
                        stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail = delUserID,Row['Name'],Row['Phone'],Row['Company'],Row['Address'],Row['Email']
                        Sql = '''delete from yusers where UserID = "{}"'''.format(delUserID)
                        x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                        ok = MysqlOps.main('delete', Sql)
                    if not ok:
                        Msg = '用户ID {} 删除失败.'.format(delUserID)
                        LogMgt.UserLog(Msg)
                        print(Msg)
                    else:
                        Msg = '用户ID {} 删除成功.'.format(delUserID)
                        LogMgt.UserLog(Msg)
                        print(Msg)

def saveUser(args):
    if len(args) == 1:
        x.clear_rows()
        tempDelList = []
        stuList,Mes,ok = loadUser()

        tempDict = tempUserDict(args)
        for Row in stuList:
            for Item in tempDict.keys():
                if Item == Row['UserID']:
                    tempDelList.append(Item)    #获取数据库内的用户ID

        for Item in tempDelList:
            tempDict.pop(Item)     #判断待录入的用户ID 与数据库中的用户 ID 是否冲突
            Mes = '用户ID {} 已存在,信息\033[1;31m录入失败\033[0m.'.format(Item)
            LogMgt.UserLog(Mes)
            print(Mes+'\n')

        if len(tempDict) >= 1:   #至少存在一个有效的待录入的用户信息
            for Item in tempDict.keys():
                stuId,stuName,stuPhone,stuCompany,stuAddress,stuEmail = Item,tempDict[Item]['name'],tempDict[Item]['Phone'],tempDict[Item]['Company'],tempDict[Item]['Address'],tempDict[Item]['Email']
                Sql = '''insert into yusers values('{}','{}','{}','{}','{}','{}');'''.format(stuId,stuName,stuPhone,stuCompany,stuAddress,stuEmail)
                x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                ok = MysqlOps.main('insert',Sql)
                if not ok:
                    Mes = '用户ID {} 保存失败.'.format(stuId)
                    LogMgt.UserLog(Mes)
                    print(Mes)
                else:
                    Mes = '用户ID {} 保存成功.'.format(stuId)
                    LogMgt.UserLog(Mes)
                    print(Mes+' 保存成功的用户信息如下: '.format(Item))
                    print(x)
        else:    #如果待录入的用户 ID 都和本地文件中的用户 ID 冲突
            Mes = '缓存列表为空, 保存失败.'
            LogMgt.UserLog(Mes)
            print(Mes)
    else:
        saveMsg = '指令错误'
        LogMgt.UserLog(saveMsg)
        print(saveMsg)

def updateInfo(args):
    if len(args) < 6:
        Mes = '指令输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)
    else:
        x.clear_rows()
        updateID = args[1]
        ops = args[3].strip().lower()
        value = args[5].strip().lower()
        if args[2].strip().lower() != 'set' and args[4].strip().lower() != '=':
            #格式判断,格式为: update stu1 set Phone = 13288888888
            Msg = '指令输入错误.'
            LogMgt.UserLog(Msg)
            print(Msg)
        else:
            if ops != 'userid' and ops != 'name' and ops != 'phone' and ops != 'company' and ops != 'address' and ops != 'email':
                Msg = '指令输出错误.不包含关键字参数 UserID,Name,Phone,Company,Address,Email.'
                LogMgt.UserLog(Msg)
                print(Msg)
            else:
                tempUser = []
                stuList,Mes,ok =loadUser()    #读取数据库用户信息

                for Row in stuList:
                    tempUser.append(Row['UserID'])

                if updateID not in tempUser:
                    Msg = '用户ID {} 不存在.'.format(updateID)
                    LogMgt.UserLog(Msg)
                    print(Msg)
                else:
                    for Row in stuList:
                        if Row['UserID'] == updateID:
                            stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail = updateID,Row['Name'],Row['Phone'],Row['Company'],Row['Address'],Row['Email']
                            x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                            Sql = '''update yusers set {} = "{}" where UserID = "{}";'''.format(ops,value,updateID)
                            ok = MysqlOps.main('update',Sql)
                            if not ok:
                                Mes = '用户ID {} 更新失败.'.format(updateID)
                                LogMgt.UserLog(Mes)
                                print(Mes)
                            else:
                                print('更新前的用户信息: ')
                                print(x)
                                x.clear_rows()
                                if ops == 'userid':
                                    x.add_row([value, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                                elif ops == 'name':
                                    x.add_row([updateID, value, stuPhone, stuCompany, stuAddress, stuEmail])
                                elif ops == 'phone':
                                    x.add_row([updateID, stuName, value, stuCompany, stuAddress, stuEmail])
                                elif ops == 'company':
                                    x.add_row([updateID, stuName, stuPhone, value, stuAddress, stuEmail])
                                elif ops == 'address':
                                    x.add_row([updateID, stuName, stuPhone, stuCompany, value, stuEmail])
                                elif ops == 'email':
                                    x.add_row([updateID, stuName, stuPhone, stuCompany, stuAddress, value])
                                Mes = '用户ID {} 更新成功.'.format(updateID)
                                LogMgt.UserLog(Mes)
                                print('\n'+Mes + ' 更新后的用户信息如下: ')
                                print(x)

def searchInfo(args):
    if len(args) < 2:
        Mes = '指令格式输入错误.'
        LogMgt.UserLog(Mes)
        print(Mes)
    else:
        x.clear_rows()
        stuList,Mes,ok = loadUser()
        searchID = args[1]
        tempList = []
        for Row in stuList:
            stuID = Row['UserID']
            tempList.append(stuID)    #获取数据库内的用户ID

        if searchID not in tempList:
            Mes = '用户ID {} 不存在.'.format(searchID)
            LogMgt.UserLog(Mes)
            print(Mes)
        else:
            for Row in stuList:
                if Row['UserID'] == searchID:
                    stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail = searchID, Row['Name'],Row['Phone'],Row['Company'],Row['Address'],Row['Email']
                    x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                    print('用户ID {} 搜索的信息如下: '.format(searchID))
                    print(x)

def displayInfo(args):
    x.clear_rows()
    stuList, Mes, ok = loadUser()
    Cnt = len(stuList)     #获取数据库中用户信息的数量
    Mes = '当前一共有 {} 条用户数据.'.format(Cnt)
    LogMgt.UserLog(Mes)
    print(Mes+'\n')

    if ok == True:   #成功读取本地用户文件后返回的状态码
        for Row in stuList:
            stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail = Row['UserID'], Row['Name'], Row['Phone'], Row['Company'], Row['Address'], Row['Email']
            x.add_row([stuId, stuName,stuPhone,stuCompany,stuAddress,stuEmail])
        #设置显示属性,_Linfo为列表
        if len(args) == 1:
            Page, Page1, Item = 1, 0, 5  # 设置页脚数和每页显示行数
            LogMgt.UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(Page, Page1, Item))
        elif len(args) == 3:
            Page, Item, Page1 = int(args[1]), int(args[2]), int(args[2])
            LogMgt.UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(Page,Page1,Item))
            if Page * Item > Cnt:
                Mes = '当前查询的数据超过当前用户总数,将显示最后 {} 条用户数据'.format(args[2])
                print(Mes)
                Page, Page1 = int(round(Cnt / Item)), int(Cnt - int(args[2]))
                LogMgt.UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(Page, Page1, Item))
        else:
            Mes = '格式输入错误.'
            LogMgt.UserLog(Mes)
            print(Mes)
        for i in range(0, Cnt):
            Page2 = int(Page1 + Item)    #设置起始页和结束页
            # print(_Page1,_Page2)
            try:
                print(x.get_string(start=Page1, end=Page2))    #分页显示用户信息
            except Exception as e:
                Mes ='请输出正确的查询格式.eg: display 4 1'
                LogMgt.UserLog(Mes)
                print(Mes)
            else:
                Mes = '当前第 {} 页, 一共 {} 页.'.format(Page, int(math.ceil(Cnt / Item)))  # 设置当前页和总页数
                LogMgt.UserLog(Mes)
                print(Mes+'\n')
                Page1 = int(Page2)
                i += Item
                Page += 1
                if Page1 >= Cnt and Page >= int(round(Cnt / Item)):   #判断当前页是否大于等于总页数
                    Mes = '到底了.'
                    LogMgt.UserLog(Mes)
                    print(Mes)
                    break
                Mes = '请按回车翻页: '
                LogMgt.UserLog(Mes)
                input(Mes)
    else:    #数据库内容为空等
        Mes = '\033[31;1m显示出错.\033[0m'
        LogMgt.UserLog(Mes)
        print(Mes)

def exportInfo(Page2):   #导出用户信息，获取用户是否输入导出的文件名
    if len(Page2) == 1:
        exportCsv = 'StuInfo.csv'    #用户未输入导出的文件名，这是默认值
    else:
        csvName = ''.join(Page2[1])
        if csvName.find('.csv') == -1:    #用户输入的文件名不包含csv，则自动补上
            exportCsv = csvName + '.csv'
        else:
            exportCsv = csvName     #用户输入的文件名格式符合条件
    stuList, Mes, ok = loadUser()
    if ok == True:
        try:
            with open(exportCsv, 'w') as csvfile:
                writeCsv = csv.writer(csvfile)
                writeCsv.writerow(["UserID", "Name", "Phone", "Company", "Address", "Email"])  # 先写入columns_name
                for Row in stuList:
                    Id, Name, Phone, Company, Address, Email = Row['UserID'], Row['Name'], Row['Phone'], Row['Company'], Row['Address'], Row['Email']
                    writeCsv.writerow([Id, Name, Phone, Company, Address, Email])
        except Exception as e:
            Mes = str(e)
            LogMgt.UserLog(Mes)
            print(Mes)
        Mes = '用户信息导出到 \033[31;1m{}\033[0m 成功'.format(exportCsv)
        LogMgt.UserLog(Mes)
        print(Mes)
    else:    #如数据库内容为空
        Mes = '\033[31;1m导出失败.\033[0m'
        LogMgt.UserLog(Mes)
        print(Mes)

def opsMeu():   #操作函数
    while True:
        for i in range(1, 4):
            Linfo = input('请: ').strip().lower().split(' ')
            if Linfo[0] == 'add':
                addUser(Linfo)
            elif Linfo[0] == 'exit':
                exitMeu()
            elif Linfo[0] == 'load':
                stuDict, Mes, ok = loadUser()
                if ok == True:
                    print(Mes)
                else:
                    print(Mes)
            elif Linfo[0] == 'list':
                listTempUser(Linfo)
            elif Linfo[0] == 'deltemp':
                delTemp(Linfo)
            elif Linfo[0] == 'save':
                saveUser(Linfo)
            elif Linfo[0] == 'del':
                delUser(Linfo)
            elif Linfo[0] == 'update':
                updateInfo(Linfo)
            elif Linfo[0] == 'search':
                searchInfo(Linfo)
            elif Linfo[0] == 'display':
                displayInfo(Linfo)
            elif Linfo[0] == 'export':
                exportInfo(Linfo)
            elif Linfo[0] == 'help':
                print(HelpMeu)
            else:
                Command = Linfo[0]   #输入指令判断
                if Command != 'add' and Command != 'exit' and Command != 'load' and Command != 'list' and Command != 'deltemp' and Command != 'save' \
                    and Command != 'del' and Command != 'update' and Command != 'search' and Command != 'diaplay' and Command != 'export' and Command != 'help':
                    Mes = '输入指令错误，请输入 help 查看帮助.'
                    LogMgt.UserLog(Mes)
                    print(Mes)

def Main():    #主函数
    UCount = 0
    while True:
        UCount += 1
        # 用户密码次数校验
        if UCount > 3:
            Mes = '用户名或密码输入次数大于3次，程序退出.'
            LogMgt.UserLog(Mes)
            sys.exit(Mes)
        else:
            inUser = input('Username: ')
            inPass = getpass.getpass('Password: ')
            inMes,ok = loginAuth(inUser,inPass)
            if ok == False:
                LogMgt.UserLog('username: {}, password: {}, {}'.format(inUser,inPass,inMes))
                print(inMes+'\n')
            elif ok == True:
                LogMgt.UserLog('username: {}, password: {}, {}'.format(inUser,inPass,inMes))
                print(inMes+'\n',HelpMeu)
                x.clear_rows()
                x.clear_rows()
                opsMeu()

if __name__ == "__main__":    #入口函数
    Main()
