#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
用户管理系统V2
Author: WangXiaoYun
'''

import sys, os, getpass,math,csv
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["UserID", "Name", "Phone", "Company", "Address", "Email"]

_StuDist = {}
_TempDist = {}
_TempDelList = []
_StuInfo = 'StuInfo.txt'
_ExportCsv = 'StuInfo.csv'
_Username = '51reboot'
_Password = '123456'
_UCount = 0
_CCount = 0

def _AddUser():
    x.clear_rows()
    while True:
        for i in range(1,4):
            _Linfo = input('请输入用户信息(help查看帮助信息): ').strip().lower().split(' ')
            if _Linfo[0] == 'exit' or _Linfo[0] == 'quit':
                x.clear_rows()
                print('退出添加用户菜单成功.')
                return
            if i <= 3:
                if _Linfo[0] == 'add':
                    if len(_Linfo) < 3:
                        print('格式输入错误.')
                    elif len(_Linfo) >= 3 and len(_Linfo) <= 7:
                        try:
                            _StuId = 'stu' + str(int(_Linfo[1]))
                        except Exception as e:
                            print(e)
                        _StuName = _Linfo[2]
                        if len(_Linfo) == 3:
                            _StuPhone, _StuCompany, _StuAddress, _StuEmail = 'None', 'None', 'None', 'None'
                        elif len(_Linfo) == 4:
                            if len(_Linfo[3]) == 11:
                                _StuPhone,_StuCompany,_StuAddress,_StuEmail = _Linfo[3],'None','None','None'
                            else:
                                print('用户电话号码\033[1;31m长度为11位\033[0m，格式输入有误，请重新输入.')
                                break
                        elif len(_Linfo) == 5:
                            _StuPhone, _StuCompany, _StuAddress, _StuEmail = _Linfo[3], _Linfo[4], 'None', 'None'
                        elif len(_Linfo) == 6:
                            _StuPhone, _StuCompany, _StuAddress, _StuEmail = _Linfo[3], _Linfo[4], _Linfo[5], 'None'
                        elif len(_Linfo) == 7:
                            if _Linfo[6].find('@') == -1:
                                print('用户Email地址\033[1;31m必须包含@\033[0m，格式输入有误，请重新输入.')
                                break
                            if _StuName == _Linfo[6].split('@')[0]:
                                print("用户姓名 \033[31;1m{}\033[0m 和Email \033[31;1m{}\033[0m 昵称不能相同,请重新输入.".format(_StuName,_Linfo[6]))
                                break
                            else:
                                _StuPhone, _StuCompany, _StuAddress, _StuEmail = _Linfo[3], _Linfo[4], _Linfo[5], _Linfo[6]
                        if _TempDist.__contains__(_StuId) == False:
                            _TempDist[_StuId] = {}
                            _TempDist[_StuId]['name'] = _StuName
                            _TempDist[_StuId]['Phone'] = _StuPhone
                            _TempDist[_StuId]['Company'] = _StuCompany
                            _TempDist[_StuId]['Address'] = _StuAddress
                            _TempDist[_StuId]['Email'] = _StuEmail
                        x.add_row([_StuId, _StuName, _StuPhone, _StuCompany,_StuAddress,_StuEmail])
                        print('用户信息 {} 已加入队列.\n'.format(_StuName))
                    elif len(_Linfo) > 6:
                        print('用户格式输入错误.')
            else:
                print('输入用户信息错误次数过多，退出菜单.')
            if _Linfo[0] == 'list':
                print('\n待录入的学生信息如下: ')
                print(x)
            if _Linfo[0] == 'delete' or _Linfo[0] == 'del':
                for i in range(1, 4):
                    if i <= 3:
                        try:
                            _Number = input('请输入需要删除\033[1;31m未保存\033[0m的用户ID: ').strip().lower()
                        except Exception as e:
                            print(e)
                        if _TempDist.__contains__(_Number) == False:
                            print('用户 {} 信息不存在.\n'.format(_Number))
                        else:
                            _TempDist.pop(_Number)
                            x.clear_rows()
                            for _Item in _TempDist.keys():
                                x.add_row([_Item,_TempDist[_Item]['name'],_TempDist[_Item]['Phone'],_TempDist[_Item]['Company'],_TempDist[_Item]['Address'],_TempDist[_Item]['Email']])
                            print('用户 {} 信息\033[1;31m已删除\033[0m.'.format(_Number))
                            print(x)
                            break
            if _Linfo[0] == 'save':
                for _Item in _TempDist.keys():
                    with open(_StuInfo, 'r') as fs:  # 判断学生ID是否存在
                        if len(fs.readlines()) > 0:
                            fs.seek(0)
                            for _Row in fs.readlines():
                                _StuRow = _Row.strip('\n').split(' ')
                                _Id, _Name, _Phone, _Company, _Address, _Email = _StuRow[0],_StuRow[1],_StuRow[2],_StuRow[3],_StuRow[4],_StuRow[5]
                                if _StuDist.__contains__(_Id) == False:
                                    _StuDist[_Id] = {}
                                    _StuDist[_Id]['name'] = _Name
                                    _StuDist[_Id]['Phone'] = _Phone
                                    _StuDist[_Id]['Company'] = _Company
                                    _StuDist[_Id]['Address'] = _Address
                                    _StuDist[_Id]['Email'] = _Email
                                if _Item == _Id:
                                    if _StuDist.__contains__(_Item) == True:
                                        _TempDelList.append(_Item)
                                    print('用户ID {} 已存在,信息\033[1;31m录入失败\033[0m失败.\n'.format(_Item))
                for _Item in _TempDelList:
                    try:
                        _TempDist.pop(_Item)
                        x.clear_rows()
                        for _Item in _TempDist.keys():
                            x.add_row([_Item, _TempDist[_Item]['name'], _TempDist[_Item]['Phone'],_TempDist[_Item]['Company'], _TempDist[_Item]['Address'],_TempDist[_Item]['Email']])
                    except Exception as e:
                        print(e)
                for _Item in _TempDist.keys():
                    _TempUser = _Item+' '+_TempDist[_Item]['name']+' '+_TempDist[_Item]['Phone']+' '+_TempDist[_Item]['Company']+' '+_TempDist[_Item]['Address']+' '+_TempDist[_Item]['Email']+'\n'
                    with open(_StuInfo, 'a') as fs:
                        fs.write(_TempUser)
                    print('用户ID {} 信息\033[1;31m已保存\033[0m.'.format(_Item))
                print('保存的信息如下: '.format(_Item))
                print(x)
                return
            if _Linfo[0] == 'help':
                print('''
        ## 添加用户信息帮助菜单 ##

添加用户信息(以空格分割): .

add             # 添加用户信息,eg: add UserID [Name] [Phone] [Company] [Address] [Email]. 至少需要提供 UserID 和 Name.
delete|del      # 删除某条未保存的用户信息.
save            # 保存待录入的用户信息.
list            # 查看待录入的用户信息.
exit|quit       # 退出添加用户信息菜单，不保存待录入的用户信息.
help            # 查看帮助菜单.
''')
                break
            if _Linfo[0] != 'add' and _Linfo[0] != 'del' and _Linfo[0] != 'delete' and _Linfo[0] != 'save' and _Linfo[0] != 'list' and _Linfo[0] != 'exit' and _Linfo[0] != 'quit':
                print('输入指令错误，请输入 help 查看帮助.')

def _SearchUser():
    with open(_StuInfo, 'r') as fs:  # 读取用户信息
        if len(fs.readlines()) > 0:
            fs.seek(0)
            for _Row in fs.readlines():
                _StuRow = _Row.strip('\n').split(' ')
                _Id,_Name,_Phone,_Company,_Address,_Email = _StuRow[0],_StuRow[1],_StuRow[2],_StuRow[3],_StuRow[4],_StuRow[5]
                _StuDist[_Id] = [_Name,_Phone,_Company,_Address,_Email]
    while True:
        x.clear_rows()
        _Quary = input('请输入需要查询的用户信息(help查看帮助信息): ').strip().lower().split(' ')
        if _Quary[0] == 'search':
            if len(_Quary) < 2:
                print('格式输入错误.')
            else:
                if _Quary[1] in _StuDist.keys():  # 精确匹配用户ID
                    _MatchCount = 0
                    _QuaryInfo = ','.join(_StuDist[_Quary[1]]).strip('\n').split(',')
                    _Name, _Phone, _Company, _Address, _Email = _QuaryInfo
                    x.add_row([_Quary[1],_Name,_Phone,_Company,_Address,_Email])
                    _MatchCount += 1
                    print(x)
                    print('Matched \033[31;1m%s\033[0m recodes!' % _MatchCount)
                else:
                    x.clear_rows()
                    # 模糊匹配用户其他信息.
                    _MatchCount = 0
                    for _k, _v in _StuDist.items():
                        for _Info in _v:
                            if _Info.lower().find(_Quary[1]) != -1:
                                _QuaryInfo = ','.join(_v).strip('\n').split(',')
                                _Name, _Phone, _Company, _Address, _Email = _QuaryInfo
                                x.add_row([_k, _Name, _Phone, _Company, _Address, _Email])
                                _MatchCount += 1
                    print(x)
                    print('Matched \033[31;1m%s\033[0m recodes!' % _MatchCount)
        if _Quary[0] == 'help':
            print('''
     ## 搜索用户信息帮助菜单 ##

支持精确查询用户ID,模糊查询用户姓名等其他信息.

search ID       # 搜索用户信息.
exit|quit       # 退出搜索用户信息菜单.
help            # 查看帮助菜单.
''')
        if _Quary[0] == 'exit' or _Quary[0] == 'quit':
            x.clear_rows()
            print('成功退出用户查询菜单.')
            return
        if _Quary[0] != 'exit' and _Quary[0] != 'quit' and _Quary[0] != 'search' and _Quary[0] != 'help':
            print('输入指令错误，请输入 help 查看帮助.')

def _DelUser():
    while True:
        x.clear_rows()
        with open(_StuInfo, 'r') as fs:  #读取本地的用户信息
            if len(fs.readlines()) > 0:
                fs.seek(0)
                for _Row in fs.readlines():
                    _StuRow = _Row.strip('\n').split(' ')
                    _Id, _Name, _Phone, _Company, _Address, _Email = _StuRow[0], _StuRow[1], _StuRow[2], _StuRow[3],_StuRow[4], _StuRow[5]
                    _StuDist[_Id] = [_Name, _Phone, _Company, _Address, _Email]
        _Linfo = input('请输入需要删除的用户信息(help查看帮助信息): ').strip().lower().split(' ')
        if _Linfo[0] == 'search':
            print('\033[31;1m欢迎进入用户查询菜单\033[0m.')
            _SearchUser()
        if _Linfo[0] == 'exit' or _Linfo[0] == 'quit':
            print('退出删除用户菜单成功.')
            return
        if _Linfo[0] == 'help':
            print('''
          ## 删除用户信息帮助菜单 ##

del|delete ID     # 删除用户信息.
search            # 进入用户查询菜单.
exit|quit         # 退出删除用户菜单.
''')
        if _Linfo[0] == 'del' or _Linfo[0] == 'delete':
            if len(_Linfo) < 2:
                print('格式输入错误.')
            else:
                if _StuDist.__contains__(_Linfo[1]) == False:
                    print('该学生ID {} 不存在.请重新输入.'.format(_Linfo[1]))
                else:
                    x.clear_rows()
                    for _Row in _StuDist.keys():
                        if _Linfo[1] == _Row:
                            _Id, _Name, _Phone, _Company, _Address, _Email = _Row,_StuDist[_Row][0],_StuDist[_Row][1],_StuDist[_Row][2],_StuDist[_Row][3],_StuDist[_Row][4]
                            x.add_row([_Id,_Name,_Phone,_Company,_Address,_Email])
                            print(x)
                    _Result = input('是否删除[Yy|Nn]: ').strip().lower()
                    if _Result == 'y':
                        _StuDist.pop(_Linfo[1])
                        print('\033[31;1m删除成功\033[0m.')
                        with open(_StuInfo, 'w') as fs:
                            for _Row in _StuDist.keys():
                                _Id,_Name,_Phone,_Company,_Address,_Email = _Row, _StuDist[_Row][0],_StuDist[_Row][1], _StuDist[_Row][2], _StuDist[_Row][3],_StuDist[_Row][4]
                                _UserInfo = _Id+' '+_Name+' '+_Phone+' '+_Company+' '+_Address+' '+_Email+'\n'
                                fs.write(_UserInfo)
                    else:
                        print('取消删除成功.')
        if _Linfo[0] != 'del' and _Linfo[0] != 'delete' and _Linfo[0] != 'search' and _Linfo[0] != 'exit' and _Linfo[0] != 'quit':
            print('输入指令错误，请输入 help 查看帮助.')

def _UpdateUser():
    while True:
        x.clear_rows()
        with open(_StuInfo, 'r') as fs:  #读取本地的用户信息
            if len(fs.readlines()) > 0:
                fs.seek(0)
                for _Row in fs.readlines():
                    _StuRow = _Row.strip('\n').split(' ')
                    _Id, _Name, _Phone, _Company, _Address, _Email = _StuRow[0], _StuRow[1], _StuRow[2], _StuRow[3],_StuRow[4], _StuRow[5]
                    _StuDist[_Id] = [_Name, _Phone, _Company, _Address, _Email]
        _Linfo = input('请输入需要更新的学生ID(help查看帮助信息): ').strip().lower().split(' ')
        if _Linfo[0] == 'search':
            print('\033[31;1m欢迎进入用户查询菜单\033[0m.')
            _SearchUser()
        if _Linfo[0] == 'exit' or _Linfo[0] == 'quit':
            print('退出删除用户菜单成功.')
            return
        if _Linfo[0] == 'help':
            print('''
    ## 修改用户信息帮助菜单 ##

修改用户信息(以空格分割): 

update       # 修改用户信息.eg: update UserID Name [Phone] [Company] [Address] [Email]. 至少需要提供 UserID 和 Name.
search       # 进入用户查询菜单.
exit|quit    # 退出修改用户菜单.
    ''')
        if _Linfo[0] == 'update':
            if len(_Linfo) < 3:
                print('格式输入错误.')
            else:
                if _StuDist.__contains__(_Linfo[1]) == False:
                    print('该学生ID {} 不存在.请重新输入.'.format(_Linfo[1]))
                else:
                    x.clear_rows()
                    for _Row in _StuDist.keys():
                        if _Linfo[1] == _Row:
                            _Id,_Name,_Phone,_Company,_Address,_Email = _Row,_StuDist[_Row][0],_StuDist[_Row][1],_StuDist[_Row][2],_StuDist[_Row][3],_StuDist[_Row][4]
                            print('修改前的用户信息: ')
                            x.add_row([_Id, _Name, _Phone, _Company, _Address, _Email])
                            print(x)
                            _Name = _Linfo[2]
                            if len(_Linfo) == 4:
                                if len(_Linfo[3]) == 11:
                                    _Phone = _Linfo[3]
                                else:
                                    print('用户电话号码\033[1;31m长度为11位\033[0m，格式输入有误，请重新输入.')
                                    break
                            elif len(_Linfo) == 5:
                                _Company = _Linfo[4]
                            elif len(_Linfo) == 6:
                                _Address = _Linfo[5]
                            elif len(_Linfo) == 7:
                                if _Linfo[6].find('@') == -1:
                                    print('用户Email地址\033[1;31m必须包含@\033[0m，格式输入有误，请重新输入.')
                                    break
                                elif _Name == _Linfo[6].split('@')[0]:
                                    print("用户姓名 \033[31;1m{}\033[0m 和Email \033[31;1m{}\033[0m 昵称不能相同,请重新输入.".format(_Name,_Linfo[6]))
                                    break
                                else:
                                    _Email = _Linfo[6]
                            x.clear_rows()
                            print('修改后的用户信息: ')
                            x.add_row([_Id, _Name, _Phone, _Company, _Address, _Email])
                    print(x)
                    _Rebuild = '{} {} {} {} {} {}\n'.format(_Id, _Name, _Phone, _Company, _Address, _Email)
                    _Result = input('是否修改[Yy|Nn]: ').strip().lower()
                    if _Result == 'y':
                        with open(_StuInfo, 'r') as fs:
                            _Lines = fs.readlines()
                        with open(_StuInfo, 'w') as fs:
                            for _Line in _Lines:
                                if _Id in _Line:
                                    continue
                                fs.write(_Line)
                            fs.write(_Rebuild)
                            print('用户ID \033[31;1m{}\033[0m 信息已更新.\n'.format(_Id))
                    else:
                        print('已取消修改用户信息.')
        if _Linfo[0] != 'update' and _Linfo[0] != 'search' and _Linfo[0] != 'exit' and _Linfo[0] != 'quit':
            print('输入指令错误，请输入 help 查看帮助.')

def _FindAll():
    while True:
        x.clear_rows()
        _Linfo = input('欢迎进入用户信息菜单(help查看帮助信息): ').strip().lower().split(' ')
        if _Linfo[0] == 'help':
            print('''
        ## 用户信息帮助菜单 ##

分页显示所有用户信息.

find         # 列出所有用户信息.eg: find [第几页] [每页显示几行]
search       # 进入用户查询菜单.
export       # 导出用户信息到 csv 文件.
exit|quit    # 退出删除用户菜单.
''')
        if _Linfo[0] == 'search':
            print('\033[31;1m欢迎进入用户查询菜单\033[0m.')
            _SearchUser()
        if _Linfo[0] == 'exit' or _Linfo[0] == 'quit':
            print('退出用户信息菜单成功.')
            return
        if _Linfo[0] == 'find':
            with open(_StuInfo, 'r') as fs:  # 读取本地的用户信息
                _Cnt = len(fs.readlines())
                print('当前一共有 {} 条用户数据.\n'.format(_Cnt))
                if _Cnt > 0:
                    fs.seek(0)
                    for _Row in fs.readlines():
                        _StuRow = _Row.strip('\n').split(' ')
                        _Id,_Name,_Phone,_Company,_Address,_Email = _StuRow[0],_StuRow[1],_StuRow[2],_StuRow[3],_StuRow[4],_StuRow[5]
                        x.add_row([_Id,_Name,_Phone,_Company,_Address,_Email])
                    if len(_Linfo) == 1:
                        _Page,_Page1,_Item = 1,0,5   #设置页脚数和每页显示行数
                    elif len(_Linfo) == 3:
                        _Page,_Item,_Page1 = int(_Linfo[1]),int(_Linfo[2]),int(_Linfo[2])
                        if _Page * _Item > _Cnt:
                            print('当前查询的数据超过当前用户总数,将显示最后 {} 条用户数据'.format(_Linfo[2]))
                            _Page,_Page1 = int(round(_Cnt/_Item)),int(_Cnt - int(_Linfo[2]))
                    else:
                        print('格式输入错误.')
                    for i in range(0,_Cnt):
                        _Page2 = int(_Page1 + _Item)
                        # print(_Page1,_Page2)
                        print(x.get_string(start=_Page1,end=_Page2))
                        print('当前第 {} 页, 一共 {} 页.\n'.format(_Page,int(math.ceil(_Cnt/_Item))))
                        _Page1 = int(_Page2)
                        i += _Item
                        _Page += 1
                        if _Page1 >= _Cnt and _Page >= int(round(_Cnt/_Item)):
                            print('到底了.')
                            break
                        input('请按回车翻页: ')
        if _Linfo[0] == 'export':
            with open(_StuInfo, 'r') as fs:  # 读取用户信息
                if len(fs.readlines()) > 0:
                    fs.seek(0)
                    for _Row in fs.readlines():
                        _StuRow = _Row.strip('\n').split(' ')
                        _Id, _Name, _Phone, _Company, _Address, _Email = _StuRow[0], _StuRow[1], _StuRow[2], _StuRow[3],_StuRow[4], _StuRow[5]
                        _StuDist[_Id] = [_Name, _Phone, _Company, _Address, _Email]
            try:
                with open(_ExportCsv,'w') as csvfile:
                    _WriteCsv = csv.writer(csvfile)
                    _WriteCsv.writerow(["UserID", "Name", "Phone", "Company", "Address", "Email"])    # 先写入columns_name
                    for _Item in _StuDist.keys():
                        _Id, _Name, _Phone, _Company, _Address, _Email = _Item, _StuDist[_Item][0], _StuDist[_Item][1], _StuDist[_Item][2], _StuDist[_Item][3], _StuDist[_Item][4]
                        _WriteCsv.writerow([_Id, _Name, _Phone, _Company, _Address, _Email])
            except Exception as e:
                print(e)
            print('用户信息导出到 \033[31;1m{}\033[0m 成功'.format(_ExportCsv))

        if _Linfo[0] != 'find' and _Linfo[0] != 'search' and _Linfo[0] != 'exit' and _Linfo[0] != 'quit' and _Linfo[0] != 'export':
            print('输入指令错误，请输入 help 查看帮助.')

def _ExitSystem():
    _QuaryResult = str(input('请问是否退出菜单[Yy|Nn):').lower())
    if _QuaryResult == 'n':
        pass
    else:
        sys.exit('已成功退出菜单.')

# 判断用户信息文件是否存在
if os.path.exists(_StuInfo) == False:
    os.mknod(_StuInfo)

while True:
    _UCount += 1
    # 用户密码次数校验
    if _UCount > 3:
        sys.exit('用户名或密码输入次数大于3次，程序退出.')
    else:
        _InUser = input('Username: ')
        _InPass = getpass.getpass('Password: ')
        if _InUser != _Username or _InPass != _Password:
            print('用户名或密码错误.')
        else:
            print('登录成功.')
            while True:  # 选择菜单防重复登录
                print('\n菜单: \n'
                      '1. 添加用户信息(command: add|delete|list|save|help).\n'
                      '2. 删除用户信息(command: delete|search|help).\n'
                      '3. 更新用户信息(command: update|search|help).\n'
                      '4. 搜索用户信息(command: search|help).\n'
                      '5. 显示所有用户信息(command: find|search|export|help).\n'
                      '6. 退出.\n')
                try:
                    _Choose = int(input('请选择菜单编号: '))
                except ValueError:
                    print('请输入数字.')
                    _CCount += 1
                    if _CCount >= 3:
                        sys.exit('菜单编码输入错误次数太多，退出菜单.')
                except Exception as e:
                    print(e)
                else:
                    if _Choose == 1:
                        _AddUser()
                    elif _Choose == 2:
                        _DelUser()
                    elif _Choose == 3:
                        _UpdateUser()
                    elif _Choose == 4:
                        _SearchUser()
                    elif _Choose == 5:
                        _FindAll()
                    elif _Choose == 6:
                        _ExitSystem()
                    else:
                        print('菜单编号不存在，请重新输入.')
                        _CCount += 1
                        if _CCount >= 3:
                            sys.exit('菜单编码输入错误次数太多，退出菜单.')