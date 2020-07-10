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
    username = input("\033[1;35;46m Please input your username: \033[0m\n")
    password = input("\033[1;33;41m Please input your password: \033[0m\n")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("\033[5;30;47m  Please input your operation: \033[0m\n\t")
            # string -> list
            info_list = info.split()
            # print(info)
            # print(info_list)
            action = info_list[0]

            if action == "add":
                #判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
                s = 0
                L = []

                while s < len(RESULT):
                    L.append(info_list[1] in RESULT[s])
                    s+=1

                if True in L:
                    print("\033[5;31m This UserName is exist! Please change!\033[0m")
                    continue
                else:
                    RESULT.append(info_list[1:])
                # 打印结果信息
                    print("\033[1;32m Add {} succ.\033[0m".format(info_list[1]))

            elif action == "delete":
                # .remove
                # 先判断用户是否存在,不存在提示提示重新输入
                s = 0
                L = []

                while s < len(RESULT):
                    L.append(info_list[1] in RESULT[s])
                    s+=1

                if True not in L:
                    print("\033[5;31m This UserName is not exist! Please reinput !\033[0m")
                else:
                    DeleteName = info_list[1]
                    i = 0
                    while i < len(RESULT):
                        if DeleteName in RESULT[i]:
                            DeleteList = RESULT.pop(i)
                            print("\033[1;32m User {} was deleted! \033[0m".format(DeleteName) )
                            break
                        else:
                            i +=1
                            continue
            elif action == "update":
                # 先判断用户是否存在
                s = 0
                L = []

                while s < len(RESULT):
                    L.append(info_list[1] in RESULT[s])
                    s+=1

                if True in L:
                    IndexNum = L.index(True)
                    RESULT[IndexNum] = info_list[1:]
                    print("\033[1;32m Update {} success!\033[0m".format(info_list[1]))
                else:
                    print("\033[5;31m This User is not exist. Please check!\033[0m")
            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if len(RESULT) <= 1:
                    print("\033[1;31m User info is None Data. Please add user info!\033[0m")
                    continue
                # print(RESULT)
                for x in RESULT:
                    print("\n{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("\033[35m-\033[0m" * 50)
            elif action == "find":
                pass
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[5;31m invalid action.\033[0m")
    else:
        # 带颜色闪烁
        print("\033[5;31m username or password error.\033[0m")
        INIT_FAIL_CNT += 1



print("\n\033[1;31m Input {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))





