#!/usr/bin/python
'''
V2.0 存储方式为字典
'''

help_info = '''---------------------------------------------
命令：
> 增: add monkey 12 132xxx monkey@51reboot.com
> 删: delete monkey
> 改: update monkey set age = 18
> 搜: find monkey
> 查: list
>分页: display page 1 pagesize 5
>导出：export
---------------------------------------------
'''
import csv
import sys,os
import json
import datetime
import getpass   #用于隐藏用户输入的字符串，常用来接收密码
from prettytable import PrettyTable   # 将输出内容如表格方式整齐地输出

# 定义变量
USERINFO = {
    'USERNAME':'51reboot',
    'USERPASS':'123456',
    'USERINFO':[]
}
RESULT = {}
FILENAME = "dic.txt"
FIELDS = ['id', 'username', 'age', 'tel', 'email']
NEW_USERID = 1

def init_info():
    if not RESULT.get('userinfo'):
        RESULT.update({'userinfo':{}})
    if not RESULT.get('userid'):
        RESULT.update({'userid':{}})
    if not RESULT.get('addid'):
        RESULT.update({'addid':[]})
    if not RESULT.get('tmp_info'):
        RESULT.update({'tmp_info': {}})

def check_info(user_info,*args):
    if user_info in RESULT.get('userid').keys():
        return False
    else:
        return True

def get_id(id_info):
    global NEW_USERID
    #优先分配被删除最小id
    if len(RESULT['addid']) > 0:
        NEW_USERID = int(RESULT['addid'][0])
        RESULT['addid'].pop(0)
    else:
        # 如果 userid 不为空获取新ID
        if len(id_info) > 0:
            LAST_ID = max(id_info.values())
            NEW_USERID = int(LAST_ID) + 1

def get_user_info(userinfo,*args):
    if userinfo in RESULT['userinfo'].keys():
        getusername = list(RESULT['userid'].keys())[list(RESULT['userid'].values()).index(int(userinfo))]
        RESULT['tmp_info'].update({'getuser':getusername,'getid':userinfo})
        return True
    elif userinfo in RESULT['userid'].keys():
        getuserid = str(RESULT['userid'][userinfo])
        RESULT['tmp_info'].update({'getuser':userinfo,'getid':getuserid})
        return True
    else:
        return False
############################################################################################################

def add_user(info_list):
    while len(info_list) == 5:
        #检测用户不存在才添加
        if check_info(info_list[1]):
            get_id(RESULT.get('userid'))
            #获取需要更新的key
            USERINFO_UPDATE = RESULT['userinfo']
            #增加 userinfo 字段
            UPDATE_USERINFO_VALUE = {'username':info_list[1],'age':info_list[2],'tel':info_list[3],'email':info_list[4]}
            USERINFO_UPDATE.update({NEW_USERID:UPDATE_USERINFO_VALUE})
            #增加 userid 字段
            RESULT['userid'][info_list[1]] = NEW_USERID
            cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return ("\033[5;31m[INFO] {}\033[0m Add {} succ.\n".format(cur_time, info_list[1]))
        else:
            return ("\033[5;31m{} already exists.\033[0m\n".format(info_list[1]))
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: add [{}] [{}] [{}] [{}]\033[0m\n").format(FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4])

def del_user(info_list):
    while len(info_list) == 2:
            if get_user_info(info_list[1]):
                getusername = RESULT['tmp_info']['getuser']
                getuserid = RESULT['tmp_info']['getid']
                RESULT['userinfo'].pop(str(getuserid))
                RESULT['userid'].pop(getusername)
                RESULT['addid'].append(getuserid)
                addid_res = sorted(RESULT['addid'])
                RESULT['addid'] = addid_res
                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return ("\033[5;31m[INFO] {} \033[0m {} has been deleted.\n".format(cur_time,getusername))
            else:
                return "\033[5;31m{} does not exist.\033[0m\n".format(info_list[1])
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: delete|del [ {}|{} ]\033[0m\n").format(FIELDS[0],FIELDS[1])

def get_list(query_info):
    # 如果没有一条记录， 那么提示为空
    if len(RESULT.get('userid')) == 0:
        return("\033[1;31mEmpty.Please add user information!\033[0m")
    else:
        # 对 userid 进行排序处理
        userid_sort = sorted(RESULT['userid'].items(), key=lambda x: x[1])
        ltab = PrettyTable()
        for i in userid_sort:
            userid = str(i[1])
            ltab.field_names = ['id', 'username', 'age', 'tel', 'email']
            #根据用户ID抓取信息
            get_info = RESULT['userinfo'][userid]
            add_info = [userid,get_info[ltab.field_names[1]], get_info[ltab.field_names[2]], get_info[ltab.field_names[3]],get_info[ltab.field_names[4]]]
            ltab.add_row(add_info)
        return ltab

def get_pageinfo(userinfolist):
    '''
    display page 2 pagesize 5
    :param args: page 2 pagesize 5 ;default pagesize = 5
    page 1 -> 0-4
    切片
    slice
    '''
    if len(userinfolist) == 3:
        if userinfolist[1] != 'page':
            return "syntax error."
        pagesize = 5

    elif len(userinfolist) == 5:
        if userinfolist[1] != 'page' or userinfolist[-2] != 'pagesize':
            return "syntax error."
        pagesize = int(userinfolist[-1])
    else:
        return "syntax error."

    values = [v for k, v in RESULT['userid'].items()]
    # 排序
    values_sort = sorted(values)
    page_value = int(userinfolist[2]) - 1  # 1
    start = page_value * pagesize
    end = start + pagesize
    # 0:5
    # 5:10

    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for id_index in values_sort[start:end]:
        t_user_info = list(RESULT['userinfo'].get(str(id_index)).values())
        # 插入id
        t_user_info.insert(0, id_index)
        xtb.add_row(t_user_info)
    return (xtb)

def find_info(info_list):
    while len(info_list) == 2:
        if get_user_info(info_list[1]):
            getuserid = RESULT['tmp_info']['getid']
            get_info = RESULT['userinfo'][getuserid]
            ftab = PrettyTable()
            ftab.field_names = ['id', 'username', 'age', 'tel', 'email']
            add_info = [getuserid, get_info['username'], get_info['age'],get_info['tel'],get_info['email']]
            ftab.add_row(add_info)
            return (ftab)
        else:
            return ("\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1]))
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: find [ {}|{} ]\033[0m\n".format(FIELDS[0],FIELDS[1]))
def update_info(info_list):
    while len(info_list) == 6:
        if get_user_info(info_list[1]):
            getusername = RESULT['tmp_info']['getuser']
            getuserid = RESULT['tmp_info']['getid']
            if info_list[3] in FIELDS:
                RESULT['userinfo'][getuserid][info_list[3]] = info_list[5]
                cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return ("\033[5;31m[INFO] {} \033[0m {} {} was changed to {}.\n".format(cur_time, getusername,info_list[3], info_list[5]))
            else:
                return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[3])
        else:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1])
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: update [ {}|{} ] set [ {}|{}|{} ] = [ Target field ]\033[0m\n").format(FIELDS[0],FIELDS[1],FIELDS[2],FIELDS[3],FIELDS[4])
def save_info(f):
    # 清空 tmp_info 临时字典
    RESULT['tmp_info'].clear()
    fd = open(f, 'w')
    if f == FILENAME:
        fd.write(json.dumps(RESULT))
        fd.close()

    # print("Save file:{} succ.".format(FILENAME))
def load_info(f):
    if os.path.exists(f):
        fd = open(f, 'r')
        data = fd.read()
        if len(data) > 0:
            global RESULT
            RESULT = json.loads(data)
            fd.close()
def csv_export():
    userid_sort = sorted(RESULT['userid'].items(), key=lambda x: x[1])

    with open('export.csv', 'w', newline="") as csvfile:
        fieldnames = FIELDS
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for i in userid_sort:
            get_id = str(i[1])
            RESULT['userinfo'][get_id].update({'id': str(i[1])})
            writer.writerow(RESULT['userinfo'].get(get_id))
        return "\033[5;32mExport Succeed.\033[0m\n"

def logic():
    # 如果输入无效的操作，则反复操作, 否则输入exit退出
    while True:
        try:
            #读取文件
            load_info(FILENAME)
            #初始化判断
            init_info()
            # 业务逻辑
            info = input("\033[1;35mPlease input your operation: \033[0m")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                res = add_user(info_list)
                print(res)
                #最后保存变量到文件
                save_info(FILENAME)
            elif action == "delete" or action == "del":
                # .remove
                res = del_user(info_list)
                print(res)
                save_info(FILENAME)
            elif action == "find":
                res = find_info(info_list)
                print(res)
            elif action == "update":
                res = update_info(info_list)
                print(res)
                save_info(FILENAME)
            elif action == "list":
                res = get_list(info_list)
                print(res)
            elif action == "display":
                res = get_pageinfo(info_list)
                print(res)
            elif action == "export":
                res = csv_export()
                print(res)
            elif action == "help" or action == "h":
                print(help_info)
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[1;36m输入错误，请输入 help 查看帮助！\033[0m\n")
        except IndexError:
            print('\033[1;36m[Errno] list index out of range.\033[0m\n')
        except FileNotFoundError:
            print('\033[1;36m[Errno] No such file or directory.\033[0m\n')
        except TypeError:
            print('\033[1;36m[Errno] Type Error.\033[0m\n')
        except KeyError:
            print('\033[1;36m[Errno] Key Error.\033[0m\n')
        except Exception as e:
            print(e)

def checkuser(username,password):
    if username == USERINFO.get('USERNAME') and password == USERINFO.get('USERPASS'):
        return True
    else:
        return False

def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = getpass.getpass("Please input your password: ")   #输入密码不可见
        if checkuser(username, password):
            print("\033[1;36mLogin Suceesfully.\033[0m")
            logic()
        else:
            INIT_FAIL_CNT += 1
            if INIT_FAIL_CNT < MAX_FAIL_CNT:
                print("\033[5;35musername or password error！\033[0m\n还剩 {} 次机会.".format(MAX_FAIL_CNT - INIT_FAIL_CNT))
    else:
        print("\n\033[1;31mBye-bye, Input {} failed.\033[0m".format(MAX_FAIL_CNT))

if __name__ == "__main__":
    main()
