'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''

# 标准模块
import sys
import os
import json
import datetime
import getpass
from prettytable import PrettyTable

# 定义变量
RESULT = []
RESULT_dic = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
FIELDS = ("name", "age", "tel", "email")
# RESULT.append(FIELDS)
FILENAME = "51reboot.txt"
LOG_FILE = "51reboot.log"

print('账号 密码都为数字  2  ')


def readfile():
    try:
        with open(FILENAME, 'r') as fd:
            datastr = fd.read()
            # print(datastr,type(datastr))
            data = json.loads(datastr)
            # print(data,type(data))
            return data, True
    except Exception as e:
        return {}, False


# readfile()

def writefile():
    with open(FILENAME, 'w') as fd:
        fd.write(json.dumps(RESULT_dic))
        return "save success", True


def login(username, passwd):
    user_info = ("1", "1")
    if username == user_info[0] and passwd == user_info[1]:
        return "login succ", True
    else:
        return "login false", False


def logout():
    sys.exit()


def addUser(input_info: list):
    if len(input_info) != 5:
        print('\033[1;32m 请输入正确操作 add username  age  tel  mail')
        return False
    username = input_info[1]
    if username in RESULT:
        errMsg = "User {} is already exists".format(username)
        return errMsg;
        False
    else:
        try:
            RESULT.append(input_info[1:])
            RESULT_dic[username] = {'name': input_info[1], 'age': input_info[2], 'tel': input_info[3],
                                    'mail': input_info[4]}
            # print("\033[1;36m %s ==> Add    %s  succeed\033[0m" % (cur_time, info_list[1]))
            succMsg = "{} ==> Add {} succ".format(cur_time, username)
            return succMsg, True
            print(RESULT_dic)
        except Exception as e:
            print(e)
        else:
            pass


def deleteUser(input_info: list):
    if len(input_info) != 2:
        print('\033[1;32m 请输入正确操作 delete username')
        return False

    username = input_info[1]
    if username in RESULT:
        del RESULT_dic[username]
        succMsg = "{} ==> delete {}  succ".format(cur_time, username)
        return succMsg;
        True
    else:
        errMsg = 'User {} is not exists'.format(username)
        return errMsg, False


def updateUser(input_info: list):
    try:
        if len(input_info) == 1 or len(input_info) != 6:
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
        elif input_info[2] != 'set' or input_info[-2] != '=':
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
        elif input_info[1] not in RESULT_dic:
            print('User {} is not exists'.format(input_info[1]))
        elif input_info[3] == 'age':
            dic_up = RESULT_dic[input_info[1]]
            # print('age change before is {} '.format(dic_up['age']))
            age_b = dic_up['age']
            dic_up['age'] = input_info[-1]
            print('\033[1;31mage changed from {} to {}\033[0m'.format(age_b, dic_up['age']))
            print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, username, 'age'))

            # print(RESULT_dic2)

        elif input_info[3] == 'tel':
            dic_up = RESULT_dic[input_info[1]]
            # print('tel change before is {} '.format(dic_up['tel']))
            tel_b = dic_up['tel']
            dic_up['tel'] = input_info[-1]
            print('\033[1;31mtel changed from  {} to {}\033[0m'.format(tel_b, dic_up['tel']))
            print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, input_info[1], 'tel'))
            # print(RESULT_dic2)

        elif input_info[3] == 'mail':
            pass
        else:
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
    except Exception as e:
        print(e)

def listUser(input_info: list):
    if len(RESULT_dic) == 0:
        errMsg = "not data"
        return errMsg,False
    xtb = PrettyTable()
    xtb.field_names = FIELDS
    for k, v in RESULT.items():
        xtb.add_row(v.values())
    return xtb, True
def displayUser (input_info: list):
    if len(input_info) >= 2 and len(input_info) <= 4:


try:
    if os.path.exists(FILENAME):
        readfile()
    else:
        writefile()
except Exception as e:
    print(e)
finally:
    pass

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input('请输入您的账号: ')
    # password = input('请输入您的密码: ')
    passwd = getpass.getpass('请输入您的密码: ')
    login(username, passwd)

    while True:
        # 业务逻辑
        try:
        # add wu 13988888888 mingetty@foxmial.com
        addUser()
        cur_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print(e)
        finally:
            pass

if action == "add":
    if oper_len != 5:
        print('\033[1;32m 请输入正确操作 add username  age  tel  mail')
    else:
        if info_list[1] in RESULT_dic2:
            print('User {} is already exists'.format(info_list[1]))
        else:
            try:
                RESULT.append(info_list[1:])
                RESULT_dic = {'name': info_list[1], 'age': info_list[2], 'tel': info_list[3],
                              'mail': info_list[4]}
                RESULT_dic2[info_list[1]] = RESULT_dic
                print("\033[1;36m %s ==> Add    %s  succeed\033[0m" % (cur_time, info_list[1]))
                # print(RESULT)
                # print(RESULT_dic)
                print(RESULT_dic2)
            except Exception as e:
                print(e)
            else:
                pass

elif action == "delete":
    if oper_len != 2:
        print('\033[1;32m 请输入正确操作 delete username')
    else:
        if info_list[1] not in RESULT_dic2:
            print('User {} is not exists'.format(info_list[1]))
        else:
            del RESULT_dic2[info_list[1]]
            print("\033[1;36m %s ==> Delete  %s  succeed\033[0m" % (cur_time, info_list[1]))
            print(RESULT_dic2)

    # elif action == "delete":
    #     # .remove
    #     # delete
    #     delete_flag = False
    #     for i in RESULT:
    #         name = i[0]
    #         # if name == username:
    #         if name == info_list[1]:
    #             RESULT.remove(i)
    #             # print("[DEBUG] {} {}".format(cur_time, info))
    #             print("\033[1;36m %s ==> delete %s  succeed\033[0m" % (cur_time, info_list[1]))
    #             delete_flag = True
    #     if not delete_flag:
    #         print("\033[1;32m User {} not found.\033[0m".format(info_list[1]))

elif action == "update":
    try:
        if oper_len == 1 or oper_len != 6:
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
        elif info_list[2] != 'set' or info_list[-2] != '=':
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
        elif info_list[1] not in RESULT_dic2:
            print('User {} is not exists'.format(info_list[1]))
        elif info_list[3] == 'age':
            dic_up = RESULT_dic2[info_list[1]]
            # print('age change before is {} '.format(dic_up['age']))
            age_b = dic_up['age']
            dic_up['age'] = info_list[-1]
            print('\033[1;31mage changed from {} to {}\033[0m'.format(age_b, dic_up['age']))
            print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, info_list[1], 'age'))

            # print(RESULT_dic2)

        elif info_list[3] == 'tel':
            dic_up = RESULT_dic2[info_list[1]]
            # print('tel change before is {} '.format(dic_up['tel']))
            tel_b = dic_up['tel']
            dic_up['tel'] = info_list[-1]
            print('\033[1;31mtel changed from  {} to {}\033[0m'.format(tel_b, dic_up['tel']))
            print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, info_list[1], 'tel'))
            # print(RESULT_dic2)

        elif info_list[3] == 'mail':
            pass
        else:
            print('\033[1;32m 请输入正确操作: update username set age/tel/mail = new\033[0m')
    except Exception as e:
        print(e)

elif action == "list":
    # 如果没有一条记录， 那么提示为空
    try:
        xtb = PrettyTable()
        xtb.field_names = ["username", "age", "tel", "mail"]
        # va = RESULT_dic2[info_list[1]]

        # print(RESULT)

        for i in RESULT_dic2.items():
            # print(i[1])
            dic_v = i[1]
            # print(dic_v)
            # print(dic_v['name'])
            list_tmp = []
            for k, v in dic_v.items():
                # print(v)
                list_tmp.append(v)
                # print(list_tmp)

                # dic = {"name": "jin", "age": 18, "sex": "male"}
                # for key2, value2 in dic.items():
                #     print(key2, value2)

            xtb.add_row(list_tmp)
        print(xtb)
    except Exception as e:
        print(e)
    else:
        pass

    # elif action == 'list':
    #     # 如果没有一条记录, 那么提示为空
    #     # print(RESULT)
    #     xtb = PrettyTable()
    #     xtb.field_names = []
    #
    # if len(RESULT_dic2) == 0:
    #     print('user data is none')
    # else:
    #     pass
elif action == 'find':
    if oper_len != 2:
        print('\033[1;32m 请输入正确操作 find username\033[0m')
    else:
        # 如果没有一条记录， 那么提示为空
        try:
            xtb = PrettyTable()
            xtb.field_names = ["username", "age", "tel", "mail"]

            if info_list[1] in RESULT_dic2:
                # print(RESULT_dic2[info_list[1]])
                dic_find = RESULT_dic2[info_list[1]]
                print(dic_find)
                list_tmp = []
                for k, v in dic_find.items():
                    # print(v)
                    list_tmp.append(v)
                    # print(list_tmp)
                xtb.add_row(list_tmp)
                print(xtb)
            else:
                print('\033[32m User {} is not found\033[0m'.format(info_list[1]))
        except Exception as e:
            print(e)
        else:
            pass
elif action == "save":
    fd = open(FILENAME, 'w')
    try:
        fd.write(json.dumps(RESULT_dic2))
    except Exception as e:
        print(e)
    finally:
        fd.close()

elif action == "load":
    pass
elif action == "display":
    try:
        # display page 1 pagesize 5  ===>  1 页 前5行
        # display page 2 pagesize 6  ===>  1 页 前6行
        if oper_len != 5:
            print('\033[1;31m 请输入正确操作: display page 1 pagesize 5 \033[0m')
        else:
            xtb = PrettyTable()
            xtb.field_names = ["username", "age", "tel", "mail"]
            for i in RESULT_dic2.items():
                dic_d = i[1]
                print(dic_d)
                list_tmp = []
                for k, v in dic_d.items():
                    # print(v)
                    list_tmp.append(v)
                xtb.add_row(list_tmp)
            # print(xtb)
            print(xtb)
    except Exception as e:
        print(e)

elif action == 'exit':
    sys.exit(0)
else:
    print("invalid action....")

elif username != USERINFO[0]:
print('\033[1;31m账号输入有误,您还有%d次机会,请重新输入\033[0m' % (MAX_FAIL_CNT - INIT_FAIL_CNT - 1))
INIT_FAIL_CNT = INIT_FAIL_CNT + 1
else:
print('\033[1;31m密码输入有误,,您还有%d次机会,请重新输入\033[0m' % (MAX_FAIL_CNT - INIT_FAIL_CNT - 1))
INIT_FAIL_CNT = INIT_FAIL_CNT + 1
