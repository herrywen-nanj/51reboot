
import auth
import user
import logs
import sys


global about_sys
global sysName
global h
global model
global model_home
global model_level01
global sysConf
global users
global admins
global password

about_sys = '''
    lesson06新版用户管理系统... 
'''

# 系统名称
sysName = "用户管理"
h = "\n*=*=*=*=*=*=**=* {} *=**=*=*=*=*=*=*".format(sysName)
# 系统模块
model = {}
model_home = {}
# 模块应全部从model中获取，根据模块层级动态对应。应工时紧张，该处写死。
model_level01 = {1: "删除用户", 2: "修改用户", 3: "查询所有用户", 4: "搜索用户", 5: "导出用户信息csv格式"}

sysConf = {"register": 1, "home_setup": 1, "upgrade_user": 1, "ini_admin": 1}
# 普通用户
users = {}
# 管理员
admins = {}
# 隐藏密码
password = "666666"


class page(object):

    # 初始化系统
    def ini():
        # 初始化系统模块
        model[0] = '登录'
        model[1] = '注册'
        model[2] = '持久化数据'
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
        # 初始化管理用户 -- lesson3版本，文件中初始化用户信息
        if sysConf["ini_admin"] == 1:
            users["123"] = "123"
            users["234"] = "234"
            users["admin"] = "admin"
            admins["admin"] = "admin"

    # 以迭代器方式加载首页
    def home01(func):
        def wrapper(*args):
            print(h)
            model_key = sorted(args[1].keys())

            # 键入 模块 key 限定 int 类型
            for i in model_key:
                out = ("{:>5}{:<10}" .format(str(i) + ".", args[1][i]))
                print(out.center(len(h) - 3))

            print("exit".rjust(len(h)))
            print(" == ".center(len(h) + 2, "*"))
            input1 = input("请输入===>：")
            pass
            return func(input1, args[1], args[2])

        return wrapper

    # 通用进入相关页面
    @home01
    def print_model(inp, model, u):
        inp.strip()
        result = inp.isdigit()
        if result:
            pass
        else:
            if inp == "exit" and 100 in model:
                sys.exit(0)
            elif inp == "exit":
                return "exit"
            logs.error("只能输入数字，请重新输入：")
            return

        inp = int(inp)
        if inp in model.keys():
            if model[inp] == "登录":
                auth.auth.login()
                pass
            elif model[inp] == "注册":
                auth.auth.register()
                pass
            elif model[inp] == "关于":
                print(about_sys)
            elif model[inp] == "持久化数据":
                user.user.save_file()
                pass
            elif model[inp] == "导出用户信息csv格式":
                user.user.export_csv(u)
                pass
            elif model[inp] == "设置":
                print("功能缺失！")
            elif model[inp] == "退出系统":
                sys.exit(0)
            elif model[inp] == "删除用户":
                user.user.delete_user(u)
                pass
            elif model[inp] == "修改用户":
                user.user.update_user(u)
                pass
            elif model[inp] == "查询所有用户":
                user.user.list_user(u)
                pass
            elif model[inp] == "搜索用户":
                user.user.search_user(u)
                pass
        else:
            print("您的输入模块不存在，请重新输入：")
        input("输入任意字符回主页：")

