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
RESULT_dic2 = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("2", "2")
# FIELDS = ['username', 'age', 'tel', 'email']
# RESULT.append(FIELDS)
FILENAME = "51reboot.txt"
LOG_FILE = "51reboot.log"

print('账号 密码都为数字  2  ')

try:
    if os.path.exists(FILENAME):
        fd = open(FILENAME, 'r')
        data = fd.read()
        # print(data)
        fd.close()
        RESULT_dic2 = eval(data)
        print(RESULT_dic2)
        print(type(RESULT_dic2))
    else:
        fd = open(FILENAME, 'w')
        fd.close()
except Exception as e:
    print(e)
finally:
    pass

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input('请输入您的账号: ')
    # password = input('请输入您的密码: ')
    password = getpass.getpass('请输入您的密码: ')
    if username == USERINFO[0] and password == USERINFO[1]:
        # print('\033[1;32m登录成功,请按照此格式操作用户信息:  action  username  age  tel  email \033[0m')
        # 操作提示

        while True:
            # 业务逻辑
            try:
                info = input('please input your operation: ')
                # add wu 13988888888 mingetty@foxmial.com
                info_list = info.split()  # 使字符串变成列表  默认空格分隔   str.split('2')
                action = ''
                action = info_list[0]
                oper_len = len(info_list)  ###   操作输入的列长度
                # print(oper_len)
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
                        print('\033[1;31mage changed from {} to {}\033[0m'.format(age_b,dic_up['age']))
                        print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, info_list[1],'age'))

                        # print(RESULT_dic2)

                    elif info_list[3] == 'tel':
                        dic_up = RESULT_dic2[info_list[1]]
                        # print('tel change before is {} '.format(dic_up['tel']))
                        tel_b = dic_up['tel']
                        dic_up['tel'] = info_list[-1]
                        print('\033[1;31mtel changed from  {} to {}\033[0m'.format(tel_b,dic_up['tel']))
                        print("\033[1;36m %s ==> Update  %s  %s  succeed\033[0m" % (cur_time, info_list[1],'tel'))
                        # print(RESULT_dic2)

                    elif  info_list[3] == 'mail':
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
                fd = open(FILENAME,'w')
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






