# 需求：
#     简单的用户管理系统

import sys

about_sys = '''
    系统角色：普通用户 管理员 
    系统配置, 缺省:
            用户自注册：开
          主页设置入口：开 
          用户升级渠道：开 
            内置管理员：开

    系统第一期，工期紧张，可配项有限，客官见谅...
'''

# 系统名称
sysName = "用户管理"
h = "\n*=*=*=*=*=*=**=* {} *=**=*=*=*=*=*=*".format(sysName)
# 系统模块
model = {}
model_home = {}
# 模块应全部从model中获取，根据模块层级动态对应。应工时紧张，该处写死。
model_level01 = {1: "删除用户", 2: "修改用户", 3: "查询所有用户", 4: "搜索用户"}

sysConf = {"register": 1, "home_setup": 1, "upgrade_user": 1, "ini_admin": 1}
# 普通用户
users = {}
# 管理员
admins = {}
# 隐藏密码
password = "666666"


# 初始化系统
def ini():
    # 初始化系统模块
    model[0] = '登录'
    model[1] = '注册'
    model[98] = '关于'
    model[99] = '设置'
    model[100] = '退出系统'
    # 初始化 home
    for i in model.keys():
        flag = True
        if sysConf["register"] == 0 and model[i] == "注册":
            flag = False
        if sysConf["home_setup"] == 0 and model[i] == "设置":
            flag = False

        if flag:
            model_home[i] = model[i]

    # 初始化管理用户
    if sysConf["register"] == 1:
        users["123"] = "123"
        users["admin"] = "admin"
        admins["admin"] = "admin"


# 欢迎页
def home01(model):
    print(h)
    model_key = sorted(model.keys())

    # 键入 模块 key 限定 int 类型
    for i in model_key:
        out = ("{}. {}".format(i, model[i])).rjust(8)
        print(out.center(len(h) - 3))

    print("exit".rjust(len(h)))
    print(" == ".center(len(h) + 2, "*"))
    return input("请输入===>：")


def login():
    input_info = input("请输入用户名/密码：")
    info = input_info.split("/")
    if len(info) != 2:
        print("您的输入格式错误，请按照：用户名/密码")
        return
    if info[0] not in users or info[1] != users[info[0]]:
        print("您输入的用户名或密码错误!")
        return

    if info[0] in admins:
        model_level01[1] = "删除用户"
        model_level01[3] = "查询所有用户"
    else:
        if 3 in model_level01.keys():
            model_level01.pop(1)
            model_level01.pop(3)

    while True:
        in1 = home01(model_level01)
        op = print_model(in1, model_level01, info[0])
        if op == "exit":
            return


def register():
    input_info = input("请输入您注册的用户名/密码：")
    info = input_info.split("/")
    if len(info) != 2:
        print("您的输入格式错误，请按照：用户名/密码")
        retry = input("重试(y), 回到主页面(other)")
        if retry == "y":
            return register()
        return
    if info[0] in users.keys():
        print("您注册的用户已经存在！")
        return
    users[info[0]] = info[1]
    print("注册成功！")


def delete_user(user):
    if user in admins.keys():
        print(" 查看所有用户 ".center(len(h), "*"))
        for i in users.keys():
            out = "userName: {}".format(i).ljust(10)
            print(out.center(len(h)))
    input_info = input("请输入您需要删除的用户：")
    if input_info not in users.keys():
        print("该用户不存在！")
        return
    users.pop(input_info)
    print("删除成功！")


def update_user(user):
    if user in admins.keys():
        print(" 查看所有用户 ".center(len(h), "*"))
        for i in users.keys():
            out = "userName: {}".format(i).ljust(10)
            print(out.center(len(h)))
        input_info = input("请输入您需要修改的用户名：")
        if input_info not in users.keys():
            print("该用户不存在！")
            return
    else:
        input_info = user

    users[input_info] = input("请输入新的密码：")
    print("修改成功！")


def list_user(user):
    if user in admins.keys():
        print(" 查看所有用户 ".center(len(h), "*"))
        for i in users.keys():
            out = "userName: {}".format(i).ljust(10)
            print(out.center(len(h)))
    else:
        print("非管理员不能查看所有用户信息")


def search_user(user):
    input_info = input("请输入您需要搜索的用户名：")
    if input_info not in users.keys():
        print("您输入的用户不存在！")
        return

    print(" 搜索用户 ".center(len(h), "*"))
    if user in admins.keys():
        out = "userName: {}, password: {}".format(input_info, users[input_info]).ljust(10)
    else:
        out = "userName: {}".format(input_info).ljust(10)
    print(out.center(len(h)))


# 通用进入相关页面
def print_model(inp, model, user):
    inp.strip()
    result = inp.isdigit()
    if result:
        pass
    else:
        if inp == "exit" and 100 in model:
            sys.exit(0)
        elif inp == "exit":
            return "exit"
        print("只能输入数字，请重新输入：")
        return

    inp = int(inp)
    if inp in model.keys():
        if model[inp] == "登录":
            login()
        elif model[inp] == "注册":
            register()
        elif model[inp] == "关于":
            print(about_sys)
        elif model[inp] == "设置":
            print("功能缺失！")
        elif model[inp] == "退出系统":
            sys.exit(0)
        elif model[inp] == "删除用户":
            delete_user(user)
        elif model[inp] == "修改用户":
            update_user(user)
        elif model[inp] == "查询所有用户":
            list_user(user)
        elif model[inp] == "搜索用户":
            search_user(user)
    else:
        print("您的输入模块不存在，请重新输入：")
    input("输入任意字符回主页：")


# 程序主入口
if __name__ == '__main__':
    ini()

    while True:
        in1 = home01(model_home)
        print_model(in1, model_home, "")





