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

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input('请输入您的账号: ')
    password = input('请输入您的密码: ')
    if username == USERINFO[0] and password == USERINFO[1]:
        print('\033[1;32m登录成功,请按照此格式操作用户信息:  action  username  age  tel  email \033[0m')
        # 操作提示
        OPERS = ('add', 'delete', 'update', 'list', 'find', 'exit')
        OPERSCH = ('添加', '删除', '更改', '查询', '搜索', '退出')
        print('action:', end='\t\t')
        for i in range(0, 6):
            # print('%s--%s'%(OPERS[i],OPERSCH[i]),end='\t')
            print('{}/{}'.format(OPERS[i], OPERSCH[i]), end='\t\t')
        print('')
        while True:
            info = input('please input your operation: ')
            info_list = info.split()   #使字符串变成列表  默认空格分隔   str.split('2')
            action = info_list[0]
            oper_len = len(info_list)###   操作输入的列长度


            if action == OPERS[0]:###   add
                RESULT.append(info_list[1:])
                print("\033[1;36m Add %s 's message succeed\033[0m"%(info_list[1]))
            elif action == OPERS[1]:###  delete
                #  list.remove(list[])
                sss = input('\033[1;31m 确认是否要删除 yes / no : \033[0m')
                if sss == 'yes':
                    usrnn = info_list[1]
                    #print(usrnn)
                    CON = len(RESULT)
                    print(CON)
                    for j in range(0, CON):
                        if usrnn in RESULT[j]:
                            print(j)
                            RESULT.remove(RESULT[j])
                            #RESULT.remove(info_list[1])
                            print("\033[1;36m Delete %s 's message succeed\033[0m" % (info_list[1]))
                            break
                        # else:
                        #     print('用户不存在')
                else:
                    pass
            elif action == OPERS[2]:###    update
                CON = len(RESULT)
                usrnn = info_list[1]

                for k in range(0, CON):
                    if usrnn in RESULT[k]:
                        print(k)
                        RESULT.remove(RESULT[k])
                        # RESULT.remove(info_list[1])
                        RESULT.append(info_list[1:])
                        print("\033[1;36m UPDATE %s 's message succeed\033[0m" % (info_list[1]))
                        #RESULT.remove(info_list[1])
                        #RESULT.append(info_list[1:])
            elif action == 'list':
                # 如果没有一条记录, 那么提示为空
                #print(RESULT)
                for x in RESULT:
                    print("| {}\t\t\t|\t\t\t{}\t\t\t|\t\t\t\t\t{}\t\t\t\t\t|\t\t\t{}\t\t|".format(x[0], x[1], x[2], x[3]), end="\t")
                    #print("\t{} \t|\t{} \t|\t{} \t|\t{} ".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("-" * 120)

            elif action == 'find':
                #print(info_list[1])
                #print(type(info_list[1]))
                usrnn = info_list[1]
                #print(usrnn)
                #print(info_list)
                #print(RESULT)
                CON = len(RESULT)
                #print(CON)
                for y in range(0,CON):
                    if usrnn in RESULT[y]:
                        print(RESULT[y])
                    # else:
                    #     print('%s is not found'%(usrnn))
            elif action == 'exit':
                sys.exit(0)
            else:
                print("invalid action.")

    elif username != USERINFO[0]:
        print('\033[1;31m账号输入有误,您还有%d次机会,请重新输入\033[0m' % (MAX_FAIL_CNT - INIT_FAIL_CNT - 1))
        INIT_FAIL_CNT = INIT_FAIL_CNT + 1
    else:
        print('\033[1;31m密码输入有误,,您还有%d次机会,请重新输入\033[0m' % (MAX_FAIL_CNT - INIT_FAIL_CNT - 1))
        INIT_FAIL_CNT = INIT_FAIL_CNT + 1
