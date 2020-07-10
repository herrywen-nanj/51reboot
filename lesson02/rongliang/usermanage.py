'''
1，登录认证
2，增删改查和搜索
    add           add  user age tel email
    del           del  user
    update        update user age tel email
    list          list
    find          find user
3，格式化输出（没实现）

'''
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ('51reboot','123456')
FLELDS = ['info_list[1]name','age','tel','email']

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input username :")
    password = input("Please input password :")
    if username == USERINFO[0] and password == USERINFO[1]:
        while True:
            info = input('Please input userinfo :')
            info_list = info.split( )

            action = info_list[0]
            list_2 = [i for k in RESULT for i in k]
            if action == 'add':
                if info_list[1] not in list_2:
                    RESULT.append(info_list[1:])
                    print(info_list[1],'已添加')
                else:
                    print(info_list[1], '已存在')
            elif action == 'del':
                del_list = [x for x in RESULT if info_list[1] in x[0]]
                RESULT.remove(del_list[0])
            elif action == 'update':
                for i in range(len(RESULT)):
                    if info_list[1] in list_2:
                        RESULT[i]=info_list[1:]
                        print(RESULT)
                    else:
                        print(info_list[1], '不存在')
            elif action == 'list':
                if len(RESULT) == 0:
                    print("当前没有信息，请添加用户信息")
                else:
                    for x in RESULT:
                        print('{} {} {} {}'.format(x[0],x[1],x[2],x[3]),end='\t')
                        print()
            elif action == 'find':
                for i in range(len(RESULT)):
                    if info_list[1] in list_2:
                        print(RESULT[i])
                    else:
                        print(info_list[1], '不存在')
            elif action == 'exit':
                exit()
     #       else:
                print('invalid action')
    else:
        print("username or password error.")
        INIT_FAIL_CNT += 1