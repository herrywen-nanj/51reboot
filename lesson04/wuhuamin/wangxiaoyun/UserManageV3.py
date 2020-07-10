#!/usr/local/python36/bin/python3.6
# -*- coding: utf-8 -*-
'''
用户管理系统V3
Author: WangXiaoYun
'''
import sys, os, getpass,math,csv,logging
from prettytable import PrettyTable
x = PrettyTable()
x.field_names = ["UserID", "Name", "Phone", "Company", "Address", "Email"]
_StuInfo = 'StuInfo.txt'
_TempDict = {}

_HelpMeu = '''{}
add         : 添加用户信息. 
              eg: add 201 monkey 13288888888 51reboot BeiJing mk@51reboot.com
              # 添加工号为 1 的用户信息
del         : 删除用户信息. 
              eg: del 1
              # 删除工号为 1 的用户信息
deltemp     : 删除临时列表中的用户信息. 
              eg: deltemp 1
              # 删除临时列表中工号为 1 的用户信息
update      : 更新用户信息. 
              eg: update 2 Jack 18988888888 51reboot Shanghai JK@51reboot.com   
              # 更新工号为 2 的用户信息
search      : 搜索用户信息. 
              eg: search 1
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
def _UserLog(*_AllLog):
    '''_AllLog: 输出的日志内容.
    _AllLog 必须是string 类型.
    '''
    try:   #传值非 string 类型会报错
        if isinstance(_AllLog,tuple) or isinstance(_AllLog,list):   #解析传值为tuple和list类型
            _FormatLog = ' '.join(_AllLog)
        else:   #其他类型日志转 string 类型
            _FormatLog = str(_AllLog)
        _LogName = './info.log'    #定义日志文件名
        if not os.path.exists(_LogName):   #日志文件不存在则创建
            os.mknod(_LogName)
        logging.basicConfig(level=logging.DEBUG,    #定义日志格式
                            format='[%(asctime)s] - [%(threadName)5s] - [%(filename)s-line:%(lineno)d] [%(levelname)s] %(message)s',
                            filename=_LogName,
                            filemode='a')
        logging.debug(_FormatLog)
    except Exception as e:
        print(e)

def _LoginAuth(username,password):
    _UserAuth = ('51reboot','123456')
    if username == _UserAuth[0] and password == _UserAuth[1]:
        return 'Login succ.',True   # 返回当前状态
    else:
        return 'Login failed.',False

def _ExitMeu():
    x.clear_rows()
    _Mes = 'exit succ.'
    _UserLog(_Mes)     #记录日志
    sys.exit(_Mes)

def _ListTempUser(_Linfo):
    x.clear_rows()
    _TempDict = _TempUserDict(_Linfo)
    for _Item in _TempDict.keys():
        _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _Item,_TempDict[_Item]['name'],_TempDict[_Item]['Phone'],_TempDict[_Item]['Company'],_TempDict[_Item]['Address'],_TempDict[_Item]['Email']
        x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
    print('\n查看待录入的用户信息: ')
    print(x)

def _LoadUser():  # 读取本地的用户信息，把本地用户信息转成字典处理
    _StuDict = {}
    try:
        with open(_StuInfo, 'r') as fs:
            if len(fs.readlines()) > 0:
                fs.seek(0)
                for _Row in fs.readlines():
                    _StuRow = _Row.strip('\n').split(' ')
                    _Id,_Name,_Phone,_Company,_Address,_Email = _StuRow[0],_StuRow[1],_StuRow[2],_StuRow[3],_StuRow[4],_StuRow[5]
                    _StuDict[_Id] = [_Name,_Phone,_Company,_Address,_Email]
    except Exception as e:
        _Mes = str(e)
        _UserLog(_Mes)
        print(_Mes)
        _LMes = 'load fail.'
        _UserLog(_LMes)
        _Ok = False
    else:
        _LMes = 'load succ.'
        _UserLog(_LMes)
        _Ok = True
    return _StuDict,_LMes,_Ok

def _CkUserFormat(_Linfo):
    if len(_Linfo) < 3:   #判断用户输入的格式长度
        _Mes = '格式输入错误.'
        _UserLog(_Mes)
        print(_Mes)
    elif len(_Linfo) >= 3 and len(_Linfo) <= 7:
        try:   #输入非 int 类型会报错
            _StuId = 'stu' + str(int(_Linfo[1]))
        except Exception as e:
            _Mes = str(e)    # try 捕获的内容也写入日志
            _UserLog(_Mes)
            print(_Mes)
            _StuId = 'None'  # try 捕获到异常后，_StuId 需要传一个默认值，否则报错
        _StuName = _Linfo[2]
        if len(_Linfo) == 3:
            _StuPhone, _StuCompany,_StuAddress,_StuEmail,_Ok,_RMsg = 'None','None','None','None',True,''
        elif len(_Linfo) == 4:
            if len(_Linfo[3]) == 11:   #手机号长度判断
                _StuPhone,_StuCompany,_StuAddress,_StuEmail,_Ok,_RMsg = _Linfo[3],'None','None','None',True,''
            else:
                _StuPhone,_StuCompany,_StuAddress, _StuEmail,_Ok,_RMsg = 'None','None','None','None',False,'用户电话号码\033[1;31m长度为11位\033[0m，格式输入有误，请重新输入.'
                _UserLog(_RMsg)
        elif len(_Linfo) == 5:
            _StuPhone,_StuCompany,_StuAddress, _StuEmail,_Ok,_RMsg = _Linfo[3],_Linfo[4],'None','None',True,''
        elif len(_Linfo) == 6:
            _StuPhone,_StuCompany,_StuAddress, _StuEmail,_Ok,_RMsg = _Linfo[3], _Linfo[4],_Linfo[5],'None',True,''
        elif len(_Linfo) == 7:
            if _Linfo[6].find('@') == -1:   #邮件格式是否包含 @ 判断
                _StuPhone,_StuCompany, _StuAddress, _StuEmail,_Ok,_RMsg = _Linfo[3],_Linfo[4],_Linfo[5],'None',False,'用户Email地址\033[1;31m必须包含@\033[0m，格式输入有误，请重新输入.'
                _UserLog(_RMsg)
            if _StuName == _Linfo[6].split('@')[0]:
                _StuPhone,_StuCompany, _StuAddress, _StuEmail,_Ok,_RMsg = _Linfo[3],_Linfo[4],_Linfo[5],'None',False,"用户姓名 \033[31;1m{}\033[0m 和Email \033[31;1m{}\033[0m 昵称不能相同,请重新输入.".format(_StuName, _Linfo[6])
                _UserLog(_RMsg)
            else:
                _StuPhone,_StuCompany, _StuAddress, _StuEmail,_Ok,_RMsg = _Linfo[3],_Linfo[4],_Linfo[5],_Linfo[6],True,''
        return _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail,_Ok,_RMsg
    elif len(_Linfo) > 6:
        _Mes = '用户格式输入错误.'
        _UserLog(_Mes)
        print(_Mes)

def _TempUserDict(_Linfo):
    if len(_Linfo) >= 3 and len(_Linfo) <= 7:    #用户输入的长度符合条件才允许进入
        _StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail,_Ok,_RMsg = _CkUserFormat(_Linfo)
        if _StuId != 'None':
            if _Ok == True:
                if _TempDict.__contains__(_StuId) == False:
                    _TempDict[_StuId] = {}
                    _TempDict[_StuId]['name'] = _StuName
                    _TempDict[_StuId]['Phone'] = _StuPhone
                    _TempDict[_StuId]['Company'] = _StuCompany
                    _TempDict[_StuId]['Address'] = _StuAddress
                    _TempDict[_StuId]['Email'] = _StuEmail
                    x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
                    _Mes = '用户信息 \033[31;1m{}\033[0m 已加入队列.'.format(_StuName)
                    _UserLog(_Mes)
                    print(_Mes+'\n')
                else:
                    _Mes = '该用户ID \033[31;1m{}\033[0m 已存在.添加失败.'.format(_StuId)
                    _UserLog(_Mes)
                    print(_Mes)
            else:
                print(_RMsg)
    return _TempDict

def _AddUser(_Linfo):
    _CkUserFormat(_Linfo)
    _TempUserDict(_Linfo)

def _DelTemp(_Linfo):
    _TempDict = _TempUserDict(_Linfo)
    if len(_Linfo) < 2:
        _Mes = '指令输入错误.'
        _UserLog(_Mes)
        print(_Mes)
    else:
        try:
            _DelUserID = 'stu' + str(int(_Linfo[1]))
        except Exception as e:
            _Mes = str(e)
            _UserLog(_Mes)
            print(_Mes)
        _TempDict.pop(_DelUserID)
        _Mes = '用户ID \033[31;1m{}\033[0m 从队列中删除成功.'.format(_DelUserID)
        _UserLog(_Mes)
        print(_Mes)

def _WriteInfo(_StuDict):   #用户信息写入文件操作
    with open(_StuInfo, 'w') as fs:
        for _Row in _StuDict.keys():
            _Id,_Name,_Phone,_Company,_Address,_Email = _Row,_StuDict[_Row][0],_StuDict[_Row][1],_StuDict[_Row][2],_StuDict[_Row][3],_StuDict[_Row][4]
            _UserInfo = _Id + ' ' + _Name + ' ' + _Phone + ' ' + _Company + ' ' + _Address + ' ' + _Email + '\n'
            fs.write(_UserInfo)

def _DelUser(_Linfo):
    if len(_Linfo) < 2:
        _Mes = '指令输入错误.'
        _UserLog(_Mes)
        print(_Mes)
    else:
        x.clear_rows()
        _StuDict,_Mes,_Ok = _LoadUser()    #读取本地用户信息
        _DelID = _Linfo[1]
        _LoadUserList = []
        _DelMes = True
        for _Item in _StuDict.keys():
            _LoadUserList.append(_Item)
        if _DelID not in _LoadUserList:
            _DelMes = False
        else:
            _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _DelID,_StuDict[_DelID][0],_StuDict[_DelID][1],_StuDict[_DelID][2],_StuDict[_DelID][3],_StuDict[_DelID][4]
            x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
            _StuDict.pop(_DelID)

        _WriteInfo(_StuDict)   #处理过的用户信息写入本地文件
        _Mes = '用户ID {} 删除成功'.format(_DelID)
        _UserLog(_Mes)
        print(_Mes,'删除的用户信息如下: ')
        print(x)
        if _DelMes == False:
            _Mes = '用户ID {} 信息不存在.'.format(_DelID)
            _UserLog(_Mes)
            print(_Mes)

def _SaveUser(_Linfo):
    x.clear_rows()
    _TempDelList = []
    _StuDict,_Mes,_Ok = _LoadUser()
    _TempDict = _TempUserDict(_Linfo)
    for _Row in _StuDict.keys():
        for _Item in _TempDict.keys():
            if _Item == _Row:
                if _StuDict.__contains__(_Item) == True:
                    _TempDelList.append(_Item)    #获取本地文件内的用户ID

    for _Item in _TempDelList:
        _TempDict.pop(_Item)     #判断待录入的用户ID 与本地文件中的用户 ID 冲突
        _Mes = '用户ID {} 已存在,信息\033[1;31m录入失败\033[0m.'.format(_Item)
        _UserLog(_Mes)
        print(_Mes+'\n')

    if len(_TempDict) >= 1:   #至少存在一个有效的待录入的用户信息
        for _Item in _TempDict.keys():
            _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _Item,_TempDict[_Item]['name'],_TempDict[_Item]['Phone'],_TempDict[_Item]['Company'],_TempDict[_Item]['Address'],_TempDict[_Item]['Email']
            _TempUser = _StuId+' '+_StuName+' '+_StuPhone+' '+_StuCompany+' '+_StuAddress+' '+_StuEmail
            x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
            with open(_StuInfo,'a') as fs:
                fs.write(_TempUser)
            _Mes = '用户ID {} 信息\033[1;31m已保存\033[0m.'.format(_Item)
            _UserLog(_Mes)
            print(_Mes)
        print('保存成功的用户信息如下: '.format(_Item))
        print(x)
    else:    #如果待录入的用户 ID 都和本地文件中的用户 ID 冲突
        _Mes = '缓存列表为空, 保存失败.'
        _UserLog(_Mes)
        print(_Mes)

def _UpdateInfo(_Linfo):
    x.clear_rows()
    try:
        _UpdateId = 'stu' + str(int(_Linfo[1]))
    except Exception as e:
        _Mes = str(e)
        _UserLog(_Mes)
        print(_Mes)
    _StuDict, _Mes, _Ok = _LoadUser()    #读取本地用户信息
    if len(_Linfo) < 3:
        _Mes = '格式输入错误.'
        _UserLog(_Mes)
        print(_Mes)
    else:
        if _StuDict.__contains__(_UpdateId) == False:    #判断待修改的用户 ID 是否存在于本地文件中
            _Mes = '该用户ID {} 不存在.请重新输入.'.format(_Linfo[1])
            _UserLog(_Mes)
            print(_Mes)
        else:
            _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _UpdateId,_StuDict[_UpdateId][0],_StuDict[_UpdateId][1],_StuDict[_UpdateId][2],_StuDict[_UpdateId][3],_StuDict[_UpdateId][4]
            x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
            _Id, _Name, _Phone, _Company, _Address, _Email, _Ok, _RMsg =  _CkUserFormat(_Linfo)
            _UserInfo = '{} {} {} {} {} {}\n'.format(_Id, _Name, _Phone, _Company, _Address, _Email)
            _Mes = '\033[1;31m修改成功.\033[0m'
            _UserLog(_Mes)
            print(_Mes,'\n\n修改前的用户信息: ')
            print(x)
            x.clear_rows()
            x.add_row([_Id, _Name, _Phone, _Company, _Address, _Email])
            print('修改后的用户信息: ')
            print(x)

            with open(_StuInfo, 'r') as fs:
                _Lines = fs.readlines()
            with open(_StuInfo, 'w') as fs:
                for _Line in _Lines:
                    if _Id in _Line:
                        continue  #重写到文件时，过滤匹配到的
                    fs.write(_Line)    #未匹配到的写入文件，update新增的也写入文件
                fs.write(_UserInfo)

def _SearchInfo(_Linfo):
    if len(_Linfo) < 2:
        _Mes = '指令输入错误.'
        _UserLog(_Mes)
        print(_Mes)
    else:
        x.clear_rows()
        _StuDict, _Mes, _Ok = _LoadUser()
        try:
            _SearchId = 'stu' + str(int(_Linfo[1]))
        except Exception as e:
            _Mes = str(e)
            _UserLog(_Mes)
            print(_Mes)
        _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _SearchId,_StuDict[_SearchId][0],_StuDict[_SearchId][1],_StuDict[_SearchId][2],_StuDict[_SearchId][3],_StuDict[_SearchId][4]
        x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
        _Mes = '搜索的用户ID {}'.format(_SearchId)
        _UserLog(_Mes)
        print('\n'+_Mes + '信息如下: ')
        print(x)

def _DisplayInfo(_Linfo):
    x.clear_rows()
    _StuDict, _Mes, _Ok = _LoadUser()
    _Cnt = len(_StuDict)     #获取本地文件中用户的数量
    _Mes = '当前一共有 {} 条用户数据.'.format(_Cnt)
    _UserLog(_Mes)
    print(_Mes+'\n')
    if _Ok == True:   #成功读取本地用户文件后返回的状态码
        for _Item in _StuDict.keys():
            _StuId,_StuName,_StuPhone,_StuCompany,_StuAddress,_StuEmail = _Item,_StuDict[_Item][0],_StuDict[_Item][1],_StuDict[_Item][2], _StuDict[_Item][3],_StuDict[_Item][4]
            x.add_row([_StuId, _StuName, _StuPhone, _StuCompany, _StuAddress, _StuEmail])
        #设置显示属性,_Linfo为列表
        if len(_Linfo) == 1:
            _Page, _Page1, _Item = 1, 0, 5  # 设置页脚数和每页显示行数
            _UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(_Page, _Page1, _Item))
        elif len(_Linfo) == 3:
            _Page, _Item, _Page1 = int(_Linfo[1]), int(_Linfo[2]), int(_Linfo[2])
            _UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(_Page, _Page1, _Item))
            if _Page * _Item > _Cnt:
                _Mes = '当前查询的数据超过当前用户总数,将显示最后 {} 条用户数据'.format(_Linfo[2])
                print(_Mes)
                _Page, _Page1 = int(round(_Cnt / _Item)), int(_Cnt - int(_Linfo[2]))
                _UserLog('当前第 {} 页, 从 {} 行开始读取, 每页显示 {} 行'.format(_Page, _Page1, _Item))
        else:
            _Mes = '格式输入错误.'
            _UserLog(_Mes)
            print(_Mes)
        for i in range(0, _Cnt):
            _Page2 = int(_Page1 + _Item)    #设置起始页和结束页
            # print(_Page1,_Page2)
            print(x.get_string(start=_Page1, end=_Page2))    #分页显示用户信息
            _Mes = '当前第 {} 页, 一共 {} 页.'.format(_Page, int(math.ceil(_Cnt / _Item)))     #设置当前页和总页数
            _UserLog(_Mes)
            print(_Mes+'\n')
            _Page1 = int(_Page2)
            i += _Item
            _Page += 1
            if _Page1 >= _Cnt and _Page >= int(round(_Cnt / _Item)):   #判断当前页是否大于等于总页数
                _Mes = '到底了.'
                _UserLog(_Mes)
                print(_Mes)
                break
            _Mes = '请按回车翻页: '
            _UserLog(_Mes)
            input(_Mes)
    else:    #读取本地用户信息失败，如本地用户文件丢失等
        _Mes = '\033[31;1m显示出错.\033[0m'
        _UserLog(_Mes)
        print(_Mes)

def _ExportInfo(_Linfo):   #导出用户信息，获取用户是否输入导出的文件名
    if len(_Linfo) == 1:
        _ExportCsv = 'StuInfo.csv'    #用户未输入导出的文件名，这是默认值
    else:
        _CsvName = ''.join(_Linfo[1])
        if _CsvName.find('.csv') == -1:    #用户输入的文件名不包含csv，则自动补上
            _ExportCsv = _CsvName + '.csv'
        else:
            _ExportCsv = _CsvName     #用户输入的文件名格式符合条件
    _StuDict, _Mes, _Ok = _LoadUser()
    if _Ok == True:
        try:
            with open(_ExportCsv, 'w') as csvfile:
                _WriteCsv = csv.writer(csvfile)
                _WriteCsv.writerow(["UserID", "Name", "Phone", "Company", "Address", "Email"])  # 先写入columns_name
                for _Item in _StuDict.keys():
                    _Id, _Name, _Phone, _Company, _Address, _Email = _Item, _StuDict[_Item][0], _StuDict[_Item][1],_StuDict[_Item][2], _StuDict[_Item][3],_StuDict[_Item][4]
                    _WriteCsv.writerow([_Id, _Name, _Phone, _Company, _Address, _Email])
        except Exception as e:
            _Mes = str(e)
            _UserLog(_Mes)
            print(_Mes)
        _Mes = '用户信息导出到 \033[31;1m{}\033[0m 成功'.format(_ExportCsv)
        _UserLog(_Mes)
        print(_Mes)
    else:    #如本地文件丢失导致读取失败
        _Mes = '\033[31;1m导出失败.\033[0m'
        _UserLog(_Mes)
        print(_Mes)

def _OpsMeu():   #操作函数
    while True:
        for i in range(1, 4):
            _Linfo = input('请: ').strip().lower().split(' ')
            if _Linfo[0] == 'add':
                _AddUser(_Linfo)
            elif _Linfo[0] == 'exit':
                _ExitMeu()
            elif _Linfo[0] == 'load':
                _StuDict, _Mes, _Ok = _LoadUser()
                if _Ok == True:
                    print(_Mes)
                else:
                    print(_Mes)
            elif _Linfo[0] == 'list':
                _ListTempUser(_Linfo)
            elif _Linfo[0] == 'deltemp':
                _DelTemp(_Linfo)
            elif _Linfo[0] == 'save':
                _SaveUser(_Linfo)
            elif _Linfo[0] == 'del':
                _DelUser(_Linfo)
            elif _Linfo[0] == 'update':
                _UpdateInfo(_Linfo)
            elif _Linfo[0] == 'search':
                _SearchInfo(_Linfo)
            elif _Linfo[0] == 'display':
                _DisplayInfo(_Linfo)
            elif _Linfo[0] == 'export':
                _ExportInfo(_Linfo)
            elif _Linfo[0] == 'help':
                print(_HelpMeu)
            else:
                _Command = _Linfo[0]   #输入指令判断
                if _Command != 'add' and _Command != 'exit' and _Command != 'load' and _Command != 'list' and _Command != 'deltemp' and _Command != 'save' \
                    and _Command != 'del' and _Command != 'update' and _Command != 'search' and _Command != 'diaplay' and _Command != 'export' and _Command != 'help':
                    _Mes = '输入指令错误，请输入 help 查看帮助.'
                    _UserLog(_Mes)
                    print(_Mes)

def _Main():    #主函数
    _UCount = 0
    while True:
        _UCount += 1
        # 用户密码次数校验
        if _UCount > 3:
            _Mes = '用户名或密码输入次数大于3次，程序退出.'
            _UserLog(_Mes)
            sys.exit(_Mes)
        else:
            _InUser = input('Username: ')
            _InPass = getpass.getpass('Password: ')
            _InMes,_Ok = _LoginAuth(_InUser,_InPass)
            if _Ok == False:
                _UserLog('username: {}, password: {}, {}'.format(_InUser,_InPass,_InMes))
                print(_InMes+'\n')
            elif _Ok == True:
                _UserLog('username: {}, password: {}, {}'.format(_InUser,_InPass,_InMes))
                print(_InMes+'\n',_HelpMeu)
                x.clear_rows()
                _OpsMeu()

if __name__ == "__main__":    #入口函数
    _Main()
