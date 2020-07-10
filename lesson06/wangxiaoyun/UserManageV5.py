#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
用户管理系统V5
Author: WangXiaoYun
'''
import sys, os, getpass,math,csv
from prettytable import PrettyTable
from logMgt import logs
from configMgt import configs
from dbOps import db

x = PrettyTable()
x.field_names = ["UserID", "Name", "Phone", "Company", "Address", "Email"]
stuInfo = 'StuInfo.txt'
tempDict = {}

helpMenu = '''{}
load        : 加载用户信息.
              eg: load
add         : 添加用户信息. 
              eg: add 201 monkey 13288888888 51reboot BeiJing mk@51reboot.com
              # 添加工号为 1 的用户信息
del         : 删除用户信息. 
              eg: del stu1
              # 删除工号为 1 的用户信息
update      : 更新用户信息. 
              eg: update stu1 set phone = 13288888888   
              # 更新工号为 2 的用户信息
save        : 保存临时列表中的用户信息. 
              eg: save
deltemp     : 删除临时列表中的用户信息. 
              eg: deltemp stu1
              # 删除临时列表中工号为 1 的用户信息.
list        : 列出临时列表中的用户信息
              eg: list
search      : 搜索用户信息. 
              eg: search stu1
              # 搜索工号为1的用户信息
display     : 分页显示所有用户信息. 
              eg: display 3 2  
              # 显示第三页，每页显示 2 行，display不带参数，默认显示第一页，每页显示 5 行
export      : 导出用户信息到csv表格中. 
              eg: export 51reboot.csv
              # export 不带参数则默认导出到 StuInfo.csv，则导出文件名为参数名
help        : 打印帮助信息.
              eg: help
exit        : 退出菜单.
              eg: exit
{}'''.format('-' * 80, '-' * 80)

class auth(object):
    def __init__(self,username,password):
        self.inUsername = username
        self.inPassword = password

    def login(self):
        # 从配置文件中读取登录验证的用户密码
        retdata = configs('config.ini', 'Login', 'username')
        result = configs('config.ini', 'Login', 'password')
        username, ok = retdata.read()
        password,ok = result.read()

        if self.inUsername == username and self.inPassword == password:
            mes = 'username: {}, password: {}, Login succ.'.format(self.inUsername, self.inPassword)
            log = logs(mes)
            log.mgt()
            print('Login succ.')
            return True  # 返回当前状态
        else:
            mes = 'username: {}, password: {}, Login failed.'.format(self.inUsername, self.inPassword)
            log = logs(mes)
            log.mgt()
            print('Login failed.')
            return False

    def logout(self):
        x.clear_rows()
        mes = 'User Management System Exit Successfully.'
        log = logs(mes)    # 记录日志
        log.mgt()
        sys.exit(mes)

class users(object):
    def __init__(self,args):
        self.args = args

    def load(self):
        sql = '''select * from yusers;'''
        try:
            retdata = db('select',sql)
            stuList, ok = retdata.select()
        except Exception as e:
            mes = str(e)
            log = logs(mes)
            log.mgt()
            print(mes)
            mes = 'User Information Loading Failed.'
            log = logs(mes)
            log.mgt()
            stuList = 'None'
            ok = False
        else:
            if stuList == []:
                mes = "The 'ops.yusers'table is empty,now."
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                mes = 'User Information Loading successfully.'
                log = logs(mes)
                log.mgt()
                ok = True
        return stuList, mes, ok

    def checks(self):
        if len(self.args) < 3:  # 判断用户输入的格式长度
            mes = '格式输入错误.'
            log = logs(mes)
            log.mgt()
            print(mes)
        elif len(self.args) >= 3 and len(self.args) <= 7:
            try:  # 输入非 int 类型会报错
                stuId = 'stu' + str(int(self.args[1]))
            except Exception as e:
                mes = str(e)  # try 捕获的内容也写入日志
                log = logs(mes)
                log.mgt()
                print(mes)
                stuId = 'None'  # try 捕获到异常后，stuId 需要传一个默认值，否则报错
            stuName = self.args[2]
            if len(self.args) == 3:
                stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes = 'None', 'None', 'None', 'None', True, ''
            elif len(self.args) == 4:
                if len(self.args[3]) == 11:  # 手机号长度判断
                    stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes = self.args[3], 'None', 'None', 'None', True, ''
                else:
                    stuPhone, stuCompany, stuAddress, stuEmail, ok = 'None', 'None', 'None', 'None', False
                    rmes = '用户电话号码\033[1;31m长度为11位\033[0m，格式输入有误，请重新输入.'
                    log = logs(rmes)
                    log.mgt()
            elif len(self.args) == 5:
                stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes = self.args[3], self.args[4], 'None', 'None', True, ''
            elif len(self.args) == 6:
                stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes = self.args[3], self.args[4], self.args[5], 'None', True, ''
            elif len(self.args) == 7:
                if self.args[6].find('@') == -1:  # 邮件格式是否包含 @ 判断
                    stuPhone, stuCompany, stuAddress, stuEmail, ok = self.args[3], self.args[4], self.args[5], 'None', False
                    rmes = '用户Email地址\033[1;31m必须包含@\033[0m，格式输入有误，请重新输入.'
                    log = logs(rmes)
                    log.mgt()
                else:
                    stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes = self.args[3], self.args[4], self.args[5],self.args[6], True, ''
            return stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail, ok, rmes
        elif len(self.args) > 6:
            mes = '用户格式输入错误.'
            log = logs(mes)
            log.mgt()
            print(mes)

    def leng(self,condition,length):    #指令长度判断
        cond = condition.strip().lower()
        if cond == 'deltemp' or cond == 'del' or cond == 'save' or cond == 'search':
            if len(self.args) != length:
                mes = '指令输入错误.'
                log = logs(mes)
                log.mgt()
                print(mes)
                return False
            else:
                return True
        if cond == 'update':
            if len(self.args) < length:
                mes = '指令输入错误.'
                log = logs(mes)
                log.mgt()
                print(mes)
                return False
            else:
                return True

    def temp(self):
        if len(self.args) >= 3 and len(self.args) <= 7:  # 用户输入的长度符合条件才允许进入
            stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail, ok, rmeg = self.checks()
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
                        mes = '用户信息 {} 已加入队列.'.format(stuName)
                        log = logs(mes)
                        log.mgt()
                        print(mes + '\n')
                    else:
                        mes = '该用户ID {} 已存在.添加失败.'.format(stuId)
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                else:
                    print(rmeg)
        return tempDict

    def delTemp(self):
        ok = self.leng('deltemp',2)
        if ok:
            tempDict = self.temp()
            try:
                userID = self.args[1]
                if userID.find('stu') == -1:
                    delUserID = 'stu' + str(int(userID))
                else:
                    delUserID = userID
            except Exception as e:
                mes = str(e)
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                if tempDict.__contains__(delUserID) == True:
                    tempDict.pop(delUserID)
                    mes = '用户ID {} 从队列中删除成功.'.format(delUserID)
                    log = logs(mes)
                    log.mgt()
                    print(mes)
                else:
                    mes = '用户ID {} 不存在.'.format(delUserID)
                    log = logs(mes)
                    log.mgt()
                    print(mes)

    def add(self):
        self.temp()

    def Del(self):
        ok = self.leng('del',2)
        if ok:
            x.clear_rows()
            try:
                userID = self.args[1]
                if userID.find('stu') == -1:
                    delUserID = 'stu' + str(int(userID))
                else:
                    delUserID = userID
            except Exception as e:
                mes = str(e)
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                tempUser = []
                stuList, mes, ok = self.load()

                if stuList == []:
                    print('用户ID {} 不存在.'.format(delUserID))
                for Row in stuList:
                    tempUser.append(Row['UserID'])

                if delUserID not in tempUser:
                    mes = '用户ID {} 不存在.'.format(delUserID)
                    log = logs(mes)
                    log.mgt()
                    print(mes)
                else:
                    for Row in stuList:
                        if Row['UserID'] == delUserID:
                            stuId = delUserID
                            stuName = Row['Name']
                            stuPhone = Row['Phone']
                            stuCompany = Row['Company']
                            stuAddress = Row['Address']
                            stuEmail = Row['Email']

                            Sql = '''delete from yusers where UserID = "{}"'''.format(delUserID)
                            x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                            retdata = db('delete', Sql)
                            result, ok = retdata.delete()
                    if not ok:
                        mes = '用户ID {} 删除失败.'.format(delUserID)
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                    else:
                        mes = '用户ID {} 删除成功.'.format(delUserID)
                        log = logs(mes)
                        log.mgt()
                        print(mes)

    def list(self):
        x.clear_rows()
        tempDict = self.temp()
        for Item in tempDict.keys():
            stuId = Item
            stuName = tempDict[Item]['name']
            stuPhone = tempDict[Item]['Phone']
            stuCompany = tempDict[Item]['Company']
            stuAddress = tempDict[Item]['Address']
            stuEmail = tempDict[Item]['Email']
            x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
        print('\n查看待录入的用户信息: ')
        print(x)

    def save(self):
        ok = self.leng('save', 1)
        if ok:
            x.clear_rows()
            tempDelList = []
            stuList, mes, ok = self.load()

            tempDict = self.temp()
            for Row in stuList:
                for Item in tempDict.keys():
                    if Item == Row['UserID']:
                        tempDelList.append(Item)  # 获取数据库内的用户ID

            for Item in tempDelList:
                tempDict.pop(Item)  # 判断待录入的用户ID 与数据库中的用户 ID 是否冲突
                mes = '用户ID {} 已存在,信息\033[1;31m录入失败\033[0m.'.format(Item)
                log = logs(mes)
                log.mgt()
                print(mes + '\n')

            if len(tempDict) >= 1:  # 至少存在一个有效的待录入的用户信息
                for Item in tempDict.keys():
                    stuId = Item
                    stuName = tempDict[Item]['name']
                    stuPhone = tempDict[Item]['Phone']
                    stuCompany = tempDict[Item]['Company']
                    stuAddress = tempDict[Item]['Address']
                    stuEmail = tempDict[Item]['Email']

                    sql = '''insert into yusers values('{}','{}','{}','{}','{}','{}');'''.format(stuId, stuName,stuPhone, stuCompany,stuAddress, stuEmail)
                    x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                    retdata = db('insert', sql)
                    stuList, ok = retdata.insert()
                    if not ok:
                        mes = '用户ID {} 保存失败.'.format(stuId)
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                    else:
                        mes = '用户ID {} 保存成功.'.format(stuId)
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                print('保存成功的用户信息如下: ')
                print(x)
            else:  # 如果待录入的用户 ID 都和本地文件中的用户 ID 冲突
                mes = '缓存列表为空, 保存失败.'
                log = logs(mes)
                log.mgt()
                print(mes)
        else:
            mes = '指令错误'
            log = logs(mes)
            log.mgt()
            print(mes)

    def update(self):
        ok = self.leng('save', 6)
        if ok:
            x.clear_rows()
            updateID = self.args[1]
            ops = self.args[3].strip().lower()
            value = self.args[5].strip().lower()
            if self.args[2].strip().lower() != 'set' and self.args[4].strip().lower() != '=':
                # 格式判断,格式为: update stu1 set Phone = 13288888888
                mes = '指令输入错误.'
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                if ops != 'userid' and ops != 'name' and ops != 'phone' and ops != 'company' and ops != 'address' and ops != 'email':
                    mes = '指令输出错误.不包含关键字参数 UserID,Name,Phone,Company,Address,Email.'
                    log = logs(mes)
                    log.mgt()
                    print(mes)
                else:
                    tempUser = []
                    stuList, mes, ok = self.load()   # 读取数据库用户信息

                    for Row in stuList:
                        tempUser.append(Row['UserID'])

                    if updateID not in tempUser:
                        mes = '用户ID {} 不存在.'.format(updateID)
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                    else:
                        for Row in stuList:
                            if Row['UserID'] == updateID:
                                stuId = updateID
                                stuName = Row['Name']
                                stuPhone = Row['Phone']
                                stuCompany = Row['Company']
                                stuAddress = Row['Address']
                                stuEmail = Row['Email']

                                x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                                sql = '''update yusers set {} = "{}" where UserID = "{}";'''.format(ops, value,stuId)
                                retdata = db('update', sql)
                                stuList, ok = retdata.update()
                                if not ok:
                                    mes = '用户ID {} 更新失败.'.format(updateID)
                                    log = logs(mes)
                                    log.mgt()
                                    print(mes)
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
                                    mes = '用户ID {} 更新成功.'.format(updateID)
                                    log = logs(mes)
                                    log.mgt()
                                    print('\n' + mes + ' 更新后的用户信息如下: ')
                                    print(x)

    def search(self):
        ok = self.leng('search', 2)
        if ok:
            x.clear_rows()
            stuList, mes, ok = self.load()
            searchID = self.args[1]
            tempList = []
            for Row in stuList:
                stuID = Row['UserID']
                tempList.append(stuID)  # 获取数据库内的用户ID

            if searchID not in tempList:
                mes = '用户ID {} 不存在.'.format(searchID)
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                for Row in stuList:
                    if Row['UserID'] == searchID:
                        stuId = searchID
                        stuName = Row['Name']
                        stuPhone = Row['Phone']
                        stuCompany = Row['Company']
                        stuAddress = Row['Address']
                        stuEmail = Row['Email']

                        x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
                        print('用户ID {} 搜索的信息如下: '.format(searchID))
                        print(x)

    def display(self):
        x.clear_rows()
        stuList, mes, ok = self.load()
        cnt = len(stuList)  # 获取数据库中用户信息的数量
        mes = '当前一共有 {} 条用户数据.'.format(cnt)
        log = logs(mes)
        log.mgt()
        print(mes + '\n')

        if ok:  # 成功读取本地用户文件后返回的状态码
            for Row in stuList:
                stuId = Row['UserID']
                stuName = Row['Name']
                stuPhone = Row['Phone']
                stuCompany = Row['Company']
                stuAddress = Row['Address']
                stuEmail = Row['Email']
                x.add_row([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
            # 设置显示属性,_Linfo为列表
            if len(self.args) == 1:
                page, page1, item = 1, 0, 5  # 设置页脚数和每页显示行数
                mes = '当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(page, page1, item)
                log = logs(mes)
                log.mgt()
                print(mes)
            elif len(self.args) == 3:
                page, item, page1 = int(self.args[1]), int(self.args[2]), int(self.args[2])
                mes = ('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(page, page1, item))
                log = logs(mes)
                log.mgt()
                print(mes)
                if page * item > cnt:
                    mes = '当前查询的数据超过当前用户总数,将显示最后 {} 条用户数据'.format(self.args[2])
                    print(mes)
                    Page, Page1 = int(round(cnt / item)), int(cnt - int(self.args[2]))
                    mes = '当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(Page, Page1, item)
                    log = logs(mes)
                    log.mgt()
                    print(mes)
            else:
                mes = '格式输入错误.'
                log = logs(mes)
                log.mgt()
                print(mes)
            for i in range(0, cnt):
                Page2 = int(page1 + item)  # 设置起始页和结束页
                # print(_Page1,_Page2)
                try:
                    print(x.get_string(start=page1, end=Page2))  # 分页显示用户信息
                except Exception as e:
                    mes = '请输出正确的查询格式.eg: display 4 1'
                    log = logs(mes)
                    log.mgt()
                    print(mes)
                else:
                    mes = '当前第 {} 页, 一共 {} 页.'.format(page, int(math.ceil(cnt / item)))  # 设置当前页和总页数
                    log = logs(mes)
                    log.mgt()
                    print(mes + '\n')
                    page1 = int(Page2)
                    i += item
                    page += 1
                    if page1 >= cnt and page >= int(round(cnt / item)):  # 判断当前页是否大于等于总页数
                        mes = '到底了.'
                        log = logs(mes)
                        log.mgt()
                        print(mes)
                        break
                    mes = '请按回车翻页: '
                    log = logs(mes)
                    log.mgt()
                    input(mes)
        else:  # 数据库内容为空等
            mes = '\033[31;1m显示出错.\033[0m'
            log = logs(mes)
            log.mgt()
            print(mes)

    def export(self):  # 导出用户信息，获取用户是否输入导出的文件名
        if len(self.args) == 1:
            exportCsv = 'StuInfo.csv'  # 用户未输入导出的文件名，这是默认值
        else:
            csvName = ''.join(self.args[1])
            if csvName.find('.csv') == -1:  # 用户输入的文件名不包含csv，则自动补上
                exportCsv = csvName + '.csv'
            else:
                exportCsv = csvName  # 用户输入的文件名格式符合条件
        stuList, mes, ok = self.load()
        if ok == True:
            try:
                with open(exportCsv, 'w') as csvfile:
                    writeCsv = csv.writer(csvfile)
                    writeCsv.writerow(["UserID", "Name", "Phone", "Company", "Address", "Email"])  # 先写入columns_name
                    for Row in stuList:
                        stuId = Row['UserID']
                        stuName = Row['Name']
                        stuPhone = Row['Phone']
                        stuCompany = Row['Company']
                        stuAddress = Row['Address']
                        stuEmail = Row['Email']
                        writeCsv.writerow([stuId, stuName, stuPhone, stuCompany, stuAddress, stuEmail])
            except Exception as e:
                mes = str(e)
                log = logs(mes)
                log.mgt()
                print(mes)
            else:
                mes = '用户信息导出到 \033[31;1m{}\033[0m 成功'.format(exportCsv)
                log = logs(mes)
                log.mgt()
                print(mes)
        else:  # 如数据库内容为空
            mes = '\033[31;1m导出失败.\033[0m'
            log = logs(mes)
            log.mgt()
            print(mes)

class menu(object):
    def __init__(self):
        pass

    def ops(self):
        while True:
            info = input('请: ').strip().lower().split(' ')
            command = info[0]
            if command == 'add':
                retdata = users(info)
                retdata.add()
            elif command == 'list':
                retdata = users(info)
                retdata.list()
            elif command == 'deltemp':
                retdata = users(info)
                retdata.delTemp()
            elif command == 'load':
                retdata = users('')
                retdata.load()
            elif command == 'del':
                retdata = users(info)
                retdata.Del()
            elif command == 'save':
                retdata = users(info)
                retdata.save()
            elif command == 'update':
                retdata = users(info)
                retdata.update()
            elif command == 'search':
                retdata = users(info)
                retdata.search()
            elif command == 'display':
                retdata = users(info)
                retdata.display()
            elif command == 'export':
                retdata = users(info)
                retdata.export()
            elif command == 'exit':
                retdata = auth('','')
                retdata.logout()
            elif command == 'help':
                print(helpMenu)
            else:
                mes = '输入指令错误，请输入 help 查看帮助.'
                log = logs(mes)
                log.mgt()
                print(mes)

class mains(object):
    def __init__(self):
        pass

    def entry(self):
        UCount = 0
        while True:
            UCount += 1
            if UCount > 3:    # 用户密码次数校验
                mes = '用户名或密码输入次数大于3次，程序退出.'
                log = logs(mes)
                log.mgt()
                sys.exit(mes)
            else:
                inUser = input('Username: ')
                inPass = getpass.getpass('Password: ')
                retdata = auth(inUser,inPass)
                ok = retdata.login()

                if ok:
                    x.clear_rows()
                    print(helpMenu)
                    menu.ops('')

if __name__ == '__main__':
    mains.entry('')