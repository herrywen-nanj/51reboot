'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 列出来 list          # list
    3.5 查找 find          # select monkey
3. 格式化输出
'''

# 标准模块
import sys


# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_COUNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)


while INIT_FAIL_CNT < MAX_FAIL_COUNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            # string -> list
            info_list = info.split()

            # print(info)
            # print(info_list)
            action = info_list[0]
            if action == "add":
                #判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                for i in RESULT:
                    if info_list[1] == i[0]:
                        print('用户已存在，请重新输入')
                        break
                RESULT.append(info_list[1:])
                # 打印结果信息
                print("Add {} succ.".format(info_list[1]))
            elif action == "delete":
                # .remove
                tmp = []
                for i in RESULT:
                    if info_list[1] == i[0]:
                        tmp.append(i)
                        break
                else:
                    print('%s值不存在'%info_list[1])
                for j in tmp:
                    RESULT.remove(j)
                    print('%s删除成功' % info_list[1])



            elif action == "update":
                tmp = []
                for i in RESULT:
                    if info_list[1] == i[0]:
                        tmp.append(i)
                        break
                else:
                    print('%s值不存在' % info_list[1])




                if info_list[2] == 'set':
                    for i in FIELDS:
                        if info_list[3] == i:
                            tmp[0][1] = info_list[5]
                            print('修改成功')
                            break
                    else:
                        print('%s为非法字段'%info_list[3])
                else:
                    print('修改字段有误')


            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if len(RESULT)<=1:
                    print('列表为空')
                    break
                # print(RESULT)
                for x in RESULT:
                    print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("-" * 50)
            elif action == "select":
                tmp=[]
                for i in RESULT:
                    # if i[0].find(info_list[1])>0:
                    if i[0]==info_list[1]:
                        tmp.append(i)
                for j in tmp:
                    print(j)


            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1



print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_COUNT))