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

# 返回结果
RESULT = []
# 初始化错误数
INIT_FAIL_CNT = 0
# 最大错误数
MAX_FAIL_CNT = 6
# 初始化用户信息
# USERINFO = ("51reboot", "123456")
USERINFO = ("a", "a")
# 字段注释
FIELDS = ['姓名', '年龄', '电话', '地址', '邮箱']

# 输入错误小于Max_FAIL_CNT时，可以进入
while INIT_FAIL_CNT < MAX_FAIL_CNT:
    # 接收用户名，如果用户名为空，提醒
    input_username = input("Please input your username: ")
    if not input_username:
        print('请输入用户名')
        continue
    # 接收密码，如果为空，提醒
    input_password = input("Please input your password: ")
    if not input_password:
        print('请输入密码')
        continue

    # 判断密码是否正确
    if input_username == USERINFO[0] and input_password == USERINFO[1]:
        # 正确，进入管理系统循环
        while True:
            # 接收用户操作,如果为空，循环
            user_input_operation = input("请输入你的操作(h\help): ")
            if not user_input_operation:
                continue

            # 用户输入分割
            user_input_split = user_input_operation.split()

            # 判断操作类型
            user_operation = user_input_split[0]
            # 新增用户操作
            if user_operation == "add":
                # 获取用户信息，定义新用户列表
                new_name = user_input_split[1]
                new_age = user_input_split[2]
                new_tel = user_input_split[3]
                new_addr = user_input_split[4]
                new_mail = user_input_split[5]
                new_user = [new_name, new_age, new_tel, new_addr, new_mail]

                # 获取用户名
                if not RESULT:
                    RESULT.append(new_user)
                    print('用户添加成功')
                    print('{} {} {} {} {}'.format(new_name, new_age, new_tel, new_addr, new_mail, end="\t"))
                    continue

                # 迭代当前用户列表
                tmp_user_name_list = []
                for user_name_db in RESULT:
                    tmp_user_name_list.append(user_name_db[0])

                # 判断是否用户名称已经存在
                if new_name in tmp_user_name_list:
                    print('用户已存在，请重新输入')
                    break
                else:
                    RESULT.append(new_user)
                    print('用户添加成功')
                    print('{} {} {} {} {}'.format(new_name, new_age, new_tel, new_addr, new_mail, end="\t"))
                    continue


            elif user_operation == "delete":
                pass
            elif user_operation == "update":
                pass


            # 打印当前用户信息
            elif user_operation == "list":
                print("{:5} {:5} {:10} {:10} {:15}".format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4]))
                # 如果没有信息打印提示
                if not RESULT:
                    print('当前没有用户')
                    continue
                else:
                    for user_info in RESULT:
                        print(
                            "{:5} {:5} {:5} {:5} {:10}".format(user_info[0], user_info[1], user_info[2], user_info[3],
                                                               user_info[4]))

            elif user_operation == "find":

                # 获取要查询的用户名称
                new_name = user_input_split[1]

                # 打印字段名称
                print("{:5} {:5} {:10} {:10} {:15}".format(FIELDS[0], FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4]))
                # 如果没有信息打印提示
                if not RESULT:
                    print('当前没有用户')
                # 迭代当前用户列表
                tmp_user_name_list = []
                for user_name_db in RESULT:
                    tmp_user_name_list.append(user_name_db[0])
                # 判断是否查询到用户
                if new_name == tmp_user_name_list:
                    print("{:5} {:5} {:5} {:5} {:10}".format(user_info[0], user_info[1], user_info[2], user_info[3],
                                                             user_info[4], end="\t"))
                else:
                    print('用户不存在')

            elif user_operation == "exit":
                sys.exit(0)

            elif user_operation == 'help' or user_operation == 'h':
                print(
                    """
                    add           # add monkey 33 132xxx 北京 monkey@51reboot.com 
                    delete        # delete monkey   
                    update        # update monkey set age = 18
                    list          # list 
                    find          # find monkey
                    exit          # 退出
                    """)
        else:
            INIT_FAIL_CNT += 1
            if MAX_FAIL_CNT - INIT_FAIL_CNT == 0:
                print('您输入的用户名和密码错误，请稍后再试')
            else:
                print('您输入的用户名或密码错误，请重新输入,还有%s次机会' % (MAX_FAIL_CNT - INIT_FAIL_CNT))
