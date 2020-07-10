import sys
import getpass
import json
from prettytable import PrettyTable
import pandas

# 定义变量
RESULT = {}

INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
# USERINFO = ("admin", "123456")
USERINFO = ("a", "a")
FIELDS = ['name', 'age', 'tel', 'email']
# RESULT.append(FIELDS)

FORMAT = """
====================================================================
1.表字段格式
username age tel email
2. 增删改查和搜索
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
    2.6 分页  display    # display page 1 pagesize 5
    2.7 保存csv格式，可跟上名称，否则默认     # export csvname  
====================================================================
"""

# 读取文件里的数据
def load():
    fd = open('kw.txt', 'r')
    # 异常处理如果文件里面不存在任何内容，那么什么都不做
    try:
        data = json.load(fd)
        RESULT.update(data)
    except Exception:
        pass

# 持久化
def save():
    fd = open('kw.txt', 'w')
    fd.write(json.dumps(RESULT))
    fd.close()

# 添加用户函数
def add(info_list):
    USER_MSG = {}
    if len(info_list):
        try:
            USER_MSG['name'] = info_list[0]
            USER_MSG['age'] = info_list[1]
            USER_MSG['tel'] = info_list[2]
            USER_MSG['email'] = info_list[3]
        except Exception:
            pass
        finally:
            RESULT[USER_MSG['name']] = USER_MSG
            save()
            print("添加用户成功")
    else:
        print("\033[0m请输入正确格式\033[0m {}".format("add monkey 12 132xxx monkey@51reboot.com"))

# 分页
def display(info_list):
    print("因为字典的无序性，字典的分页排序是无意义的")

#  保存为csv文件
def export(info_list):
    data_list = []
    file_name = "kw"
    if len(info_list):
        file_name = info_list.pop(0)

    if len(RESULT):
        pt_fields = list(list(RESULT.values())[0].keys())
        for u_k, u_v in RESULT.items():
            data_list.append(list(u_v.values()))
            pd = pandas.DataFrame(columns=pt_fields, data=data_list)
            pd.to_csv('{}.csv'.format(file_name), encoding='utf_8_sig') # 防止中文乱码
    else:
        print("数据为空，请添加数据")

# 删除用户函数
def delete(info_list):
    for u_k, u_v in RESULT.items():
        if u_k == info_list[0]:
            RESULT.pop(u_k)
            save()
            return "{}用户删除成功".format(info_list[0])
    return "删除失败，用户列表查无{}此用户".format(info_list[0])

# 修改用户函数
def update(info_list):
    for u_k, u_v in RESULT.items():
        if u_k == info_list[0]:
            try:
                location_index = info_list.index("=")   # 获取 = 在哪个位置
                key_name = info_list[location_index - 1]   # 获取要修改的参数，如age，username等
                value_name = info_list[location_index + 1]  # 获取要修改的参数的值

                if key_name in FIELDS:
                    if key_name == "name":
                        RESULT[value_name] = RESULT.pop(u_k)  #修改外层key(name)的名称，保持外层和里面的name名称是一致的
                    u_v[key_name] = value_name  # 修改里层的字典对应的key的value
                    # 数据保存到文件
                    save()
                    return "{}用户修改成功".format(value_name)
                else:
                    return "{}，无此字段参数".format(key_name)

            except Exception:
                return "请输入正确的参数"

    return "{}用户修改失败，用户列表查无此用户".format(info_list[0])

# 打印成表格的函数
def pretable(ret_dict):
    if len(ret_dict):
        pt_fields = list(list(ret_dict.values())[0].keys())
        x = PrettyTable()
        x.field_names = pt_fields
        for u_k, u_v in ret_dict.items():
            x.add_row(list(u_v.values()))
        print(x)
    else:
        print("暂无数据，请添加数据。")

# 按需打印用户函数
def user_list(ret_dict=None):
    if ret_dict:
        pretable(ret_dict)
    else:
        pretable(RESULT)

# 查找用户函数
def find(info_list):
    find_list = []
    for u_k, u_v in RESULT.items():
        # 判断查找的用户是否存在于列表里
        if u_k == info_list[0]:
            # return u_v
            return {u_k:u_v}
    print("用户列表查无{}此用户".format(info_list[0]))

while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    password = input("Please input your password: ")
    # password = getpass.getpass("Please input your password: ")
    if username == USERINFO[0] and password == USERINFO[1]:
        # 提示增删改查操作
        print(FORMAT)
        # 读取文件里面的内容
        load()
        while True:
            info = input("Please input your operation: ").lower()
            if not info:    # 当直接回车时不会报错
                continue
            info_list = info.split()

            try:    # 异常处理
                action = info_list.pop(0)
            except:
                pass

            if action == "add":
                add(info_list)
            elif action == "delete":
                ret = delete(info_list)
                print(ret)
            elif action == "update":
                ret = update(info_list)
                print(ret)
            elif action == "list":
                user_list(info_list)
            elif action == "find":
                ret = find(info_list)
                if ret:
                    user_list(ret)
            elif action == "exit":
                sys.exit(1)
            elif action == "display":
                ret = display(info_list)
                if ret:
                    user_list(ret)
            elif action == "export":
                export(info_list)
            elif action.lower() == "h" or action.lower() == "help":
                print(FORMAT)

            else:
                print("Syntax error")
                print(FORMAT)
    else:
        print("账号或密码错误")
        INIT_FAIL_CNT += 1

print("密码错误次数超过6次, 系统退出")