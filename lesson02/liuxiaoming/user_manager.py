import sys
import re

re_email = re.compile(r'^[a-zA-Z0-9\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
RESULT = [['lxm', '19', '19', '20'], ['zs', '19', '19', '19']]
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("admin", "admin")

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("请输入登录用户名: ")
    password = input("请输入密码: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        while True:
            info = input("请输入你的操作:")
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                name = input("请输入要新增的用户名:\n")
                for user in RESULT:
                    if name == user[0]:
                        print("该用户已经存在！")
                    else:
                        add_age = input("请输入用户的年龄:\n")
                        if add_age.isdigit():
                            add_tel = input("请输入用户的手机号:\n")
                            if len(add_tel) != 11:
                                print("\033[31m\n手机号码位数不正确.\033[0m")
                            elif not add_tel.isdigit():
                                print("\033[31m\n手机号码必须是数字.\033[0m")
                                print("-------------------------------------")
                            else:
                                add_email = input("请输入用户的email:\n")
                                if re_email.match(add_email):
                                    new_list = [name, add_age, add_tel, add_email]
                                    RESULT.append(new_list)
                                    print("用户{}添加成功！".format(name))
                                else:
                                    print("\033[31m\n邮箱格式不正确.\033[0m")
                                    print("-------------------------------------")
                                    add_email = input("请输入用户的email:\n")
                        else:
                            print("年龄必须是数字.")

            elif action == "delete":
                name = input("请输入要删除的用户:\n")
                for u in RESULT:
                    if u[0] == name:
                        RESULT.remove(u)
                        print("成功删除用户{}".format(name))
                else:
                    print("该用户不存在")
            elif action == "update":
                name = input("请输入你要修改的用户名:\n")
                dict = {0: "name", 1: "age", 2: "tel", 3: "email"}
                for u in RESULT:
                    if u[0] == name:
                        r_index = RESULT.index(u)
                        info = input("请输入你要修改的用户信息:\n")
                        u_index = int(input("请输入你要修改的用户信息序号:(0:name, 1:age, 2:tel, 3:email)"))
                        u[u_index] = info
                        RESULT[r_index] = u
                        print("成功修改用户{}的{}为:{}".format(name, dict[u_index], info))
            elif action == "list":
                if len(RESULT) == 0:
                    print("没有用户数据")
                else:
                    name = input("请输入你要查找的用户名:\n")
                    for u in RESULT:
                        if u[0] == name:
                            print("用户名:{} 年龄:{} 电话:{} 邮箱:{}".format(u[0], u[1], u[2], u[3]))
                    else:
                        print("该用户不存在")
            elif action == "find":
                if len(RESULT) == 0:
                    print("没有用户数据.")
                else:
                    for u in RESULT:
                        print("用户名;{} 年龄:{} 电话:{} 邮箱:{}".format(u[0], u[1], u[2], u[3]))
                        print("****************************************************")
            elif action == "exit":
                sys.exit(0)
            else:
                print("invalid action.")
    else:
        print("用户名或者密码错误")
        INIT_FAIL_CNT += 1
print("\033[31m\nYou tried too many times, Terminal will exit.\033[0m")




