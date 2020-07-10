'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    3.6 分页             #display page 1 pagesize 2
3. 格式化输出
'''

# 标准模块
import sys
import os
import json
from prettytable import PrettyTable



# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("1", "1")
# USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
FLAG=True
try:
    with open('userinfo.txt','r') as f:
        RESULT = json.loads(f.read())
except FileNotFoundError as e:
    os.system('touch userinfo.txt')

while INIT_FAIL_CNT < MAX_FAIL_CNT and FLAG:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            info ="""
            1 增 add           # add monkey 12 132xxx monkey@51reboot.com
            2 删 delete        # delete monkey
            3 改 update        # update monkey set age = 18
            4 查 list          # list
            5 搜 find          # find monkey
            6 分页显示         # display page 1 pagesize 2
            7 保存             # save   
            """
            print('*'*80)
            print(info)
            print('*' * 80)
            # 业务逻辑
            info = input("Please input your operation: ")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                #判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                if info_list[1] in RESULT.keys():
                    print('用户已存在，请重新输入')
                    continue
                else:
                    RESULT[info_list[1]] = {"age":info_list[2],"tel":info_list[3],"email":info_list[4]}
                    # 打印结果信息
                    print("Add {} succ.".format(info_list[1]))
            elif action == "delete":
                # .remove
                if info_list[1] in RESULT.keys():
                    RESULT.pop(info_list[1])
                    print('%s已删除' % info_list[1])
                    continue
                else:
                    print('%s不存在'%info_list[1])




            elif action == "update":
                # update monkey1 set age = 20
                username = info_list[1]
                where = info_list[2]
                fuhao = info_list[-2]
                tmp = []
                if where != "set" or fuhao != "=":
                    print("Update method error.")
                    continue

                if info_list[1] not in RESULT.keys():
                    print('用户%s不存在' % info_list[1])

                else:
                    if RESULT[info_list[1]].get(info_list[3],None) == None:
                        print('%s字段不存在' % info_list[3])
                    else:
                        RESULT[info_list[1]][info_list[3]] = info_list[-1]
                        print('用户%s,%s已更新' % (info_list[1],info_list[3]))
                    continue

            elif action == "list":
                xtb = PrettyTable()
                xtb.field_names=['username', 'age', 'tel', 'email']
                # 如果没有一条记录， 那么提示为空
                if len(RESULT)<1:
                    print('列表为空')
                    continue

                for k,v in RESULT.items():
                    tmp = []
                    tmp.append([k,v['age'],v['tel'],v['email']])
                    xtb.add_row(tmp[0])
                print(xtb)
            elif action == "find":
                xtb = PrettyTable()
                xtb.field_names = ['username', 'age', 'tel', 'email']

                if info_list[1] in RESULT.keys():
                    tmp = []
                    tmp.append([info_list[1], RESULT.get(info_list[1],None)['age'], RESULT.get(info_list[1],None)['tel'], RESULT.get(info_list[1],None)['email']])
                    xtb.add_row(tmp[0])
                    print(xtb)
                else:
                    print('%s不存在'%info_list[1])

            elif action == "save":
                with open('userinfo.txt','w') as f:
                    f.write(json.dumps(RESULT))
                print('数据保存成功')
            elif action == "display":
                # 分页 display page 1 pagesize 5

                xtb = PrettyTable()
                xtb.field_names = ['username', 'age', 'tel', 'email']

                page = int(info_list[2])
                pagesize = int(info_list[-1])

                if info_list[1] != "page" or info_list[3] != "pagesize":
                    print("Display method error.")
                    continue
                tmp = []
                for k, v in RESULT.items():
                    tmp.append([k, v['age'], v['tel'], v['email']])
                    # xtb.add_row(tmp[-1])
                # print(tmp[(page-1)*pagesize:(page-1)*pagesize+pagesize])
                for i in tmp[(page-1)*pagesize:(page-1)*pagesize+pagesize]:
                    xtb.add_row(i)
                print(xtb)

            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1



print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
