'''
1.登录认证；
2.增删改查和搜索
---------------------------------------------------------------------
    3.1 增 add       举例：add monkey 12 123XXX  mokey@51reboot.com
---------------------------------------------------------------------
    3.2 删 delete    举例：delete monkey
---------------------------------------------------------------------
    3.3 改 update    #update monkey set age = 18
---------------------------------------------------------------------
    3.4 查 list      #list
---------------------------------------------------------------------
    3.5 搜           #find monkey
---------------------------------------------------------------------
3.格式化输出
'''

# 标准模块
import os

# 定义变量
#定义结果变量，空列表
RESULT = []
#定义最少输入次数变量
INIT_FAIL_CNT = 0
#定义最大输入次数变量
MAX_FAIL_CNT = 6
#定义账号密码
USERINFO = ("51reboot", "123456")
FIELDS = ['username','age','tel','email']
RESULT.append(FIELDS)
#循环检查账号密码输入，正确则进入操作动作，6次错误退出
while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username == USERINFO[0] and password == USERINFO[1]:
        D = {
            '增' : "add monkey 12 123XXX  mokey@51reboot.com",
            '改' : "update monkey set age = 18",
            '删' : "delete monkey",
            '查' : "list",
            '查询名字' : "find monkey"
        }
        for i, j in D.items():
            print('\033[1;32m"{}:{}"\033[0m'.format(i, j), end="\n")
            print("-" * 50)
        #循环执行动作
        while True:
            #定义操作动作
            info = input("请输入你的操作：")
            #将字符串转换成列表
            info_list = info.split()

            #定制执行动作变量
            action = info_list[0]
            #增操作
            if action == "add":   #add monkey 12 123XXX  mokey@51reboot.com
                #判断用户是否存在，如果用户存在，提示已经存在，不在添加
                add1 = info_list[1]
                NAME = []
                for i in RESULT:
                    name = i[0]
                    NAME.append(name)
                if add1 in NAME:
                    print('\033[1;31m"用户{}已存在"\033[0m'.format(add1))
                else:
                    RESULT.append(info_list[1:])
                #打印结果信息
                    print('\033[1;32;40m"Add {} success."\033[0m'.format(info_list[1]))
            #删操作
            if action == "delete":
                #.remove 判断是否存在，在就删，不在就提示
                if i in RESULT:
                    name = i[0]
                    name == info_list[1]
                    RESULT.remove(i)
                    print('\033[1;31m"{}用户已经删除"\033[0m'.format(name))
            #改操作
            if action == "update":
                #update age要同时存在
                username = info_list[1]
                where = info_list[2]
                NAME = []
                if where != "set":
                    print('\033[1;31m"错误的操作请重新输入"\033[0m')
                    break

                for i in RESULT:
                    name = i[0]
                    NAME.append(name)
                if username in NAME:
                    idx = NAME.index(username)
                    if info_list[3] == "age":
                        RESULT[idx][1] = info_list[-1]
                        print('\033[1;32m"修改成功"\033[0m')
                    elif info_list[3] == "tel":
                        print('\033[1;32m"修改成功"\033[0m')
                    elif info_list[3] == "email":
                        print('\033[1;32m"修改成功"\033[0m')
                else:
                    print('\033[1;31m"{}用户没有找到"\033[0m'.format(username))
            #查列表操作
            if action == "list":
                # 如果没有一条记录，那个提示为空
                for x in RESULT:
                    #格式化输出
                    print('\033[1;46m"{} {} {} {}"\033[0m'.format(x[0],x[1],x[2],x[3]), end="\t")
                    print()
                    print("-" * 50)
            #寻找列表数据
            if action == "find":
                username = info_list[1]
                #定义一个真实值，如果找到，改变值退出
                FALT_find = False
                for i in RESULT:
                    if i[0] == username:
                        print("{} {} {} {}".format(i[0], i[1], i[2], i[3]), end="")
                        print()
                        FALT_find = True
                #如果不真实，取反
                if not FALT_find:
                    print("{}没在列表中，请添加".format(username))
            #退出操作
            if action == "exit":
                break
        else:
            #其余操作无效
            print('\033[1;31m"无效的操作"\033[0m')
    else:
        # 带颜色
        #账号密码输入错误打印
        print("账号或密码错误")
        #最少输入次数+1，到6退出循环
        INIT_FAIL_CNT += 1
#输入6次错误，打印
print('\033[1;31m"输入{}次错误系统退出"\033[0m'.format(MAX_FAIL_CNT))
