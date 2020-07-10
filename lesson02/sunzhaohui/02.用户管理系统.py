'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey   或 delete id  1
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
#RESULT.append(FIELDS)


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        print('\033[0;32;0m 登录成功!\033[0m')
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            #如果输入为空，跳入下次循环
            if info == '':
                continue
            # string -> list
            info_list = info.split()

            # print(info)
            # print(info_list)
            action = info_list[0]
            if action == "add":
                #判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                username = info_list[1]

                #获取当前用户名的列表
                current_username_list = []
                current_id_list = []
                for filed in RESULT:
                    current_username_list.append(filed[0])
                    print('当前用户{}'.format(filed[0]))

                user_number = len(current_username_list)

                #判断用户是否在列表里

                if username in current_username_list:
                    print('\033[0;35;0m用户已存在,不可以添加\033[0m')
                    continue
                else:
                    #给用户信息添加id
                    #info_list.insert(1,user_number)
                    #print(info_list[1:])
                    RESULT.append(info_list[1:])
                    # 打印结果信息
                    print("\033[0;32;0m Add {} succ.\033[0m".format(info_list[1]))
            elif action == "delete":
                # .remove

                current_username_list = []
                current_id_list = []
                #得到所有用户名放到一个列表
                for x in RESULT:
                    current_username_list.append(x[0])
                #如果输入关键字等2 ，是用用户名删除
                if len(info_list) == 2:
                    username = info_list[1]

                    #判断输入的用户名是否在列表里
                    if username  not in current_username_list:
                        print('没有这个用户\033[0;35;0m{}\033[0m'.format(username))
                        continue
                    for x in RESULT:
                        if username == x[0]:
                            RESULT.remove(x)
                            print('\033[0;32;0m已删除{}\033[0m'.format(username))
                #如果输入的关健字等3
                elif len(info_list) == 3:
                        #判断第一个关机字等''
                        if info_list[1] == 'id':
                            id_number = int(info_list[2])
                            if id_number <=0 or id_number > len(RESULT):
                                print('id \033[0;35;0m{}\033[0m没有找到'.format(id_number))
                                continue
                            else:
                                x = RESULT[id_number - 1]
                                RESULT.remove(x)
                                print('\033[0;32;0m已删除{}\033[0m'.format(id_number))
                else:
                    print('invalid action: you can input \033[0;32;1m help \033[0m')

            elif action == "update":
                # update monkey set age = 18

                #重新分割输入的信息，最大分割3个
                info_list = info.split(maxsplit=3)
                #
                #关键字 update = info_list[0]
                username = info_list[1]
                #关键字 set = info_list[2]

                #把输入的key 和 value 单独赋值
                user_filed_value = info_list[3]

                #再把输入的key 和 value 分割提取
                user_filed = user_filed_value.split('=')[0].strip()
                user_value = user_filed_value.split('=')[1].strip()

                #当前用户放到一个列表里
                current_username_list = []
                for user_info in RESULT:
                    current_username_list.append(user_info[0])
                #判断修改的用户是否在列表里
                if username in current_username_list:
                    if 'set' in info and '=' in info and user_filed in FIELDS:
                        #获取用户的index
                        user_index = current_username_list.index(username)
                        #获取用户信息列表
                        user_info = RESULT[user_index]


                        if user_filed == 'username':
                            source_value = user_info[0]
                            user_info[0] = user_value
                            print('用户 {} 的字段 {} 值 已由 \033[0;32;0m{}\033[0m 改为 \033[0;35;0m{}\33[0m'.format(username,user_filed,source_value,user_value))
                            # 修改用户数据后，提交到信息列表里
                            info_list[user_index] = user_info
                        elif user_filed == 'age':
                            source_value = user_info[1]
                            user_info[1] = user_value
                            print('用户 {} 的字段 {} 值 已由 \033[0;32;0m{}\033[0m 改为 \033[0;35;0m{}\33[0m'.format(username,user_filed,source_value,user_value))
                            # 修改用户数据后，提交到信息列表里
                            info_list[user_index] = user_info
                        elif user_filed == 'tel':
                            source_value = user_info[2]
                            user_info[2] = user_value
                            print('用户 {} 的字段 {} 值 已由 \033[0;32;0m{}\033[0m 改为 \033[0;35;0m{}\33[0m'.format(username,user_filed,source_value,user_value))
                            # 修改用户数据后，提交到信息列表里
                            info_list[user_index] = user_info
                        elif user_filed == 'email':
                            source_value = user_info[3]
                            user_info[3] = user_value
                            print('用户 {} 的字段 {} 值 已由 \033[0;32;0m{}\033[0m 改为 \033[0;35;0m{}\33[0m'.format(username,user_filed,source_value,user_value))
                            # 修改用户数据后，提交到信息列表里
                            info_list[user_index] = user_info
                        else:
                            print('invalid action: you can input \033[0;32;1m help \033[0m')

                else:
                    print('没有该用户: {}'.format(username))





            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                # print(RESULT)
                #print("{} {} {} {} {}".format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3],FIELDS[4]))
                #print("-" * 50)
                #展示时添加字段
                FIELDS.insert(0,'id')
                RESULT.insert(0,FIELDS)
                id = 0
                for x in RESULT:

                    if id == 0:
                        print("{} {} {} {} {}".format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4]))
                    else:
                        print("{} {} {} {} {}".format(id,x[0], x[1], x[2], x[3]), end="\t")
                        print()
                    print("-" * 50)
                    id = id + 1
                #展示完移除字段
                FIELDS.remove('id')
                RESULT.remove(FIELDS)
            elif action == "find":
                #定义一个空列表，用于存放展示的内容
                find_list = []
                #获取要查找的用户名
                username = info_list[1].strip()
                #当前用户放到一个列表里
                current_username_list = []
                for user_info in RESULT:
                    current_username_list.append(user_info[0])
                    print('find 当前用户名{}'.format(user_info[0]))
                if username in current_username_list:
                    #得到用户的index
                    user_index = current_username_list.index(username)
                    #得到find 用户的信息列表
                    user_info = RESULT[user_index]
                    #给用户赋值id
                    user_id  = user_index + 1
                    user_info.insert(0,user_id)
                    #给字段插入'id'
                    FIELDS.insert(0, 'id')
                    find_list.append(FIELDS)
                    find_list.append(user_info)
                    for x in find_list:
                        print("{} {} {} {} {}".format(x[0], x[1], x[2], x[3],x[4]), end="\t")
                        print()
                        print("-" * 50)
                    user_info.remove(user_id)
                    FIELDS.remove('id')
                else:
                    print('用户不存在')

            elif action == "exit":
                sys.exit(0)
            elif action == 'help':
                print(
                """
                 
                add           # add monkey 12 132xxx monkey@51reboot.com 
                              # 添加 对应字段名称: username age tel email
                delete        #只能 根据用户名 或 id 删除
                              # delete monkey   
                              # delete id  1
                update        # 修改 根据用户名 和 字段名称
                              # update monkey set age = 18
                list          # list 
                find          # find monkey
                exit          # 退出
                """)
            else:
                print('invalid action: you can input \033[0;32;1m help \033[0m')
    else:
        # 带红颜色
        #print("username or password error.")
        print('\033[0;31;0m username or password error. \033[0m')
        INIT_FAIL_CNT += 1
        if INIT_FAIL_CNT < MAX_FAIL_CNT:
            print('还有\033[0;31;0m {} \033[0m 次机会，否则程序将会退出'.format(MAX_FAIL_CNT - INIT_FAIL_CNT))


#次数带颜色
print("\nInput \033[0;31;0m {}\033[0m failed, Terminal will exit.".format(MAX_FAIL_CNT))





