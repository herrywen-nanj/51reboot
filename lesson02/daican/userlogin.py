"""
用户管理系统
1、登录认证；
2、增删改查和搜索
    3.1 增 add      # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete   # delete mobkey
    3.3 改 update   # update monkey 18 139xxx 51reboot@qq.com
    3.4 查 list     # list
    3.5 搜 find     # find monkey
3、格式化输出
"""

#标准模块
import sys

#定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot", "123456")
FIELDS = ['username', 'age', 'tel', 'email']
RESULT.append(FIELDS)

#判断用户是否存在
def check_user(name):
    for x in RESULT:
        if name == x[0]:
            return True
    return False

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    name = input("Please input your name:")
    password = input("Please input your password:")
    if name == USERINFO[0] and password == USERINFO[1]:
        #如果输入无效的操作，则反复操作，否则输入exit退出
        while True:
            #业务逻辑
            info = input("Please input your operation:")
            #string -> list
            info_list = info.split()

            # print(info)
            # print(info_list)
            action = info_list[0]
            if action == "add":
                # 判断用户是否存在，如果用户存在，提示用户已经存在，不再添加
                # 输入 add monkey 12 132xxx monkey@51reboot.com
                if check_user(info_list[1]):
                    print("用户添加失败，{}已存在".format(info_list[1]))
                else:
                    RESULT.append(info_list[1:])
                    # 打印添加的结果信息
                    print("Add user {} success".format(info_list[1]))

            elif action == "delete":
                # delete monkey
                if check_user(info_list[1]):
                    for x in RESULT:
                        if x[0] == info_list[1]:
                            RESULT.remove(x)
                            print("Delete user {} success.".format(info_list[1]))
                else:
                    print("用户删除失败，用户{}不存在".format(info_list[1]))

            elif action == "update":
                # update monkey 18 139xxx 51reboot@qq.com
                if check_user(info_list[1]):
                    for x in RESULT:
                        if x[0] == info_list[1]:
                            RESULT.remove(x)
                            RESULT.append(info_list[1:])
                            print("Update user {} success.".format(info_list[1]))
                else:
                    print("用户更新失败，用户{}不存在".format(info_list[1]))

            elif action == "list":
                #如果没有一条记录，那么提示为空
                # print(RESULT)
                for x in RESULT:
                    print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                    print()
                    print("-" * 50)

            elif action == "find":
                for x in RESULT:
                    if x[0] == info_list[1]:
                        print("{} {} {} {}".format(x[0], x[1], x[2], x[3]), end="\t")
                        print()
                        print("-" * 50)

            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[31m invalid action\033[0m")
    else:
        #带颜色
        print("\033[31m username or password error.\033[0m")
        INIT_FAIL_CNT += 1

print("\033[31m \nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
