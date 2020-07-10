'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add
    3.2 删 delete
    3.3 改 update
    3.4 查 list
    3.5 搜 find
3. 格式化输出
'''

# 标准模块
import sys

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot","123456")
FIELDS = ['username','age','tel','email']
RESULT.append(FIELDS)
user_cnt = []


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username：")
    password = input("Please input your password：")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            info = input("Please input your operation：")
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在, 如果用户存在，提示用户已经存在，不存在就添加
                username = info_list[1]
                if len(RESULT) == 1:
                    RESULT.append(info_list[1:])
                    print("\033[0;31;1mAdd user {} success.\033[0m".format(username))
                elif len(RESULT) > 1:
                    user_cnt = []
                    for i in range(1,len(RESULT)):
                        user_cnt.append(RESULT[i][0])
                    if info_list[1] in user_cnt:
                        print("\033[0;31;1m用户 {} 已存在，无需添加.\033[0m".format(username))
                    else:
                        RESULT.append(info_list[1:])
                        print("\033[0;31;1mAdd user {} success.\033[0m".format(username))
            elif action == "delete":
                username = info_list[1]
                user_cnt = []
                for i in range(1,len(RESULT)):
                    user_cnt.append(RESULT[i][0])
                if username in user_cnt:
                    i = 0
                    while i < len(RESULT):
                        if RESULT[i][0] == username:
                            RESULT.pop(i)
                            print("\033[0;31;1mDelete user {} success.\033[0m".format(username))
                            # print(RESULT)
                        i += 1
                else:
                    print("\033[0;31;1m用户 {} 不存在.\033[0m".format(username))
            elif action == "update":
                username = info_list[1]
                age = info_list[2]
                tel = info_list[3]
                email = info_list[4]
                user_cnt = []
                for i in range(1,len(RESULT)):
                    user_cnt.append(RESULT[i][0])
                if username in user_cnt:
                    i = 0
                    while i < len(RESULT):
                        if RESULT[i][0] == username:
                            RESULT[i][1] = age
                            RESULT[i][2] = tel
                            RESULT[i][3] = email
                            print("\033[0;31;1mUpdate {} update success.\033[0m".format(username))
                        i += 1
                else:
                    print("\033[0;31;1m用户 {} 不存在.\033[0m".format(username))
            elif action == "list":
                if len(RESULT) == 1:
                    print("\033[0;31;1m{}\t{}\t{}\t{}\033[0m".format(RESULT[0][0],RESULT[0][1],RESULT[0][2],RESULT[0][3]),end='\t')
                    print()
                    print("-" * 50)
                elif len(RESULT) > 1:
                    for x in RESULT:
                        print("\033[0;31;1m{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}\033[0m".format(x[0],x[1],x[2],x[3],''), end='\t')
                        print()
                        print("-" * 50)
            elif action == "find":
                username = info_list[1]
                user_cnt = []
                for i in range(1,len(RESULT)):
                    user_cnt.append(RESULT[i][0])
                if username in user_cnt:
                    i = 0
                    while i < len(RESULT):
                        if RESULT[i][0] == username:
                            age = RESULT[i][1]
                            tel = RESULT[i][2]
                            email = RESULT[i][3]
                            print("\033[0;31;1m{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}\033[0m".format(RESULT[0][0],RESULT[0][1],RESULT[0][2],RESULT[0][3],''), end='\t')
                            print()
                            print("-" * 50)
                            print("\033[0;31;1m{0:^10}\t{1:{4}^10}\t{2:^10}\t{3:^10}\033[0m".format(username,age,tel,email,''), end='\t')
                            print()
                            print("-" * 50)
                        i += 1
                else:
                    print("\033[0;31;1m用户 {} 不存在.\033[0m".format(username))
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[0;31;1minvalid action.\033[0m")
    else:
        print("\033[0;31;1musername or password error.\033[0m")
        INIT_FAIL_CNT += 1

print("\n\033[0;31;1mInput {} times failed,Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
