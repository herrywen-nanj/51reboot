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
USERINFO = ("liq", "liq")


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        while True:
            # 业务逻辑
            info = input("请输入操作指令(add,delete,update,list,find,exit): ")
            if info == "add":
                add_list = input("请输入用户信息：")
                add_list1 = add_list.split()
                if len(add_list1) == 4:
                    RESULT.append(add_list1)
            elif info == "delete":
                remov = input('请输入要删除的人的姓名：')
                for re in RESULT:
                    if re[0] == remov:
                        RESULT.remove(re)
            elif info == "update":
                upda = input('请输入修改资料者的姓名：')
                for ud in range(len(RESULT)):
                    if upda == RESULT[ud][0]:
                        item = ['name','age','iphone','mail']
                        updat = input('请输入修改项(name,age,iphone,mail)：')
                        data = input('请输入修改后内容：')
                        if updat in item:
                            if 'name' == updat:
                                RESULT[ud][0] = data
                            elif 'age' == updat:
                                RESULT[ud][1] = data
                            elif 'iphone' == updat:
                                RESULT[ud][2] = data
                            elif 'mail' == updat:
                                RESULT[ud][3] = data
                            else:
                                print('未知项：{}'.format(updat))

            elif info == "list":
                # print('{} {} {} {}'.format('name','age','iphone','mail'))
                for list_for in RESULT:
                    print('{} {} {} {}'.format(list_for[0],list_for[1],list_for[2],list_for[3]))
            elif info == "find":
                find = input('请输入查询人姓名：')
                for find_list in RESULT:
                    if find in find_list:
                        print(find_list)
                    else:
                        print('姓名输入错误')
            elif info == "exit":
                sys.exit()
            else:
                print("invalid action.")
    else:
        # 带颜色
        print("username or password error.")
        INIT_FAIL_CNT += 1

print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))
