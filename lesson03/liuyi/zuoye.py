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
import json




# 定义变量
RESULT = {}
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "admin")
FIELDS = ['username', 'age', 'tel', 'email']
FLAG=True

while INIT_FAIL_CNT < MAX_FAIL_CNT:
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
            print('#'*80)
            print(info)
            print('#' * 80)
            # 业务逻辑
            info = input("Please input your operation: ")

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
                    print('已删除' , info_list[1])
                    continue
                else:
                    print('不存在',info_list[1])




            elif action == "update":
                username = info_list[1]
                where = info_list[2]
                fuhao = info_list[-2]
                tmp = []
                if where != "set" or fuhao != "=":
                    print("Update method error.")
                    continue

                if info_list[1] not in RESULT.keys():
                    print('用户不存在' , info_list[1])

                else:
                    if RESULT[info_list[1]].get(info_list[3],None) == None:
                        print('字段不存在' ,info_list[3])
                    else:
                        RESULT[info_list[1]][info_list[3]] = info_list[-1]
                        print('用户已更新' , (info_list[1],info_list[3]))
                    continue

            elif action == "list":
                pass
            elif action == "find":
                pass
            elif action == "save":
                with open('userinfo.txt','w') as f:
                    f.write(json.dumps(RESULT))
                print('数据保存成功')

    else:
        print("username or password error.")
        INIT_FAIL_CNT += 1



print("\nInput {} failed, Terminal will exit.".format(MAX_FAIL_CNT))