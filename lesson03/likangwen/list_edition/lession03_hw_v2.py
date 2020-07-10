import sys
import getpass
import json
from prettytable import PrettyTable
import pandas

# 定义变量
RESULT = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
# USERINFO = ("admin", "123456")
USERINFO = ("a", "a")
FIELDS = ['username', 'age', 'tel', 'email']
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
        RESULT.extend(data)
    except Exception:
        pass

# 持久化
def save():
    fd = open('kw.txt', 'w')
    fd.write(json.dumps(RESULT))
    fd.close()

# 添加用户函数
def add(info_list):
    try:
        username = info_list[0]
    except Exception:
        return "\033[0m请输入正确格式\033[0m \n{}".format(FORMAT)
        # return "请输入正确格式"

    if username and len(info_list)==4:
        if username not in [u[0] for u in RESULT]:  # 检查用户是否不存在
            RESULT.append(info_list)
            # 保存添加到文件
            save()
            return "{}用户添加成功".format(username)
        else:
            return "{}用户已存在，需要修改请使用update方法".format(username)
    else:
        return "参数有误，请输出正确参数"

# 分页
def display(info_list):
    if 'page' in info_list and 'pagesize'  in info_list:
        page_num = info_list[info_list.index('page') + 1]
        pagesize_num = info_list[info_list.index('pagesize') + 1]
        if page_num.isdigit() and pagesize_num.isdigit():
            end = int(pagesize_num) * int(page_num)
            return RESULT[end-int(pagesize_num):end]
        else:
            print("请输入正确的page与pagesize，格式：display page 1 pagesize 5")
    else:
        print("请输入正确的page与pagesize，格式：display page 1 pagesize 5")

# 报错为csv文件
def export(info_list):
    file_name = "kw"
    if len(info_list):
        file_name = info_list.pop(0)
    pd = pandas.DataFrame(columns=FIELDS, data=RESULT)
    pd.to_csv('{}.csv'.format(file_name), encoding='utf_8_sig') # 防止中文乱码

# 删除用户函数
def delete(info_list):
    for user_list in RESULT:
        if user_list[0] == info_list[0]:
            FIELDS.pop(user_list)
            return "{}用户删除成功".format(info_list[0])
    return "删除失败，用户列表查无{}此用户".format(info_list[0])

# 修改用户函数
def update(info_list):
    for user_list in RESULT:
        if user_list[0] == info_list[0]:
            copy_user_list = user_list  # 拷贝一份
            location_index = info_list.index("=")   # 获取 = 在哪个位置
            key_name = info_list[location_index - 1]   # 获取要修改的参数，如age，username等
            if key_name in FIELDS:
                print(key_name)
                key_location = FIELDS.index(key_name)   # 获取要修改的参数在列表对应的位置
                user_list[key_location] = info_list[location_index + 1] # 修改参数
                RESULT[RESULT.index(copy_user_list)] = user_list
                # 数据保存到文件
                save()
                return "{}用户修改成功".format(username)
            else:
                return "{}，无此字段参数".format(key_name)


    return "{}用户修改失败，用户列表查无此用户".format(username)

# 打印成表格的函数
def pretable(ret_list):
    x = PrettyTable()
    x.field_names = FIELDS
    for user_list in ret_list:
        x.add_row(user_list)
    print(x)

# 按需打印用户函数
def list(ret_list=None):
    if ret_list:
        # 此处给find调用，当传来的ret有序列，打印
        # for user_list in ret_list:
        #     print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format(user_list[0],user_list[1],user_list[2],user_list[3]))
        pretable(ret_list)
    else:
        # for user_list in RESULT:
        #     print("{:^10}\t{:^10}\t{:^10}\t{:^10}".format(user_list[0], user_list[1], user_list[2], user_list[3]))  # 格式限定符规定打印格式
        pretable(RESULT)

# 查找用户函数
def find(info_list):
    find_list = []
    for user_list in RESULT:
        # 判断查找的用户是否存在于列表里
        if user_list[0] == info_list[0]:
            find_list.append(FIELDS)
            find_list.append(user_list)
            return find_list
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
                ret = add(info_list)
                print(ret)
            elif action == "delete":
                ret = delete(info_list)
                print(ret)
            elif action == "update":
                ret = update(info_list)
                print(ret)
            elif action == "list":
                list(info_list)
            elif action == "find":
                ret = find(info_list)
                if ret:
                    list(ret)
            elif action == "exit":
                sys.exit(1)
            elif action == "display":
                ret = display(info_list)
                if ret:
                    list(ret)
            elif action == "export":
                export(info_list)
            else:
                print("Syntax error")
                print(FORMAT)
    else:
        print("账号或密码错误")
        INIT_FAIL_CNT += 1

print("密码错误次数超过6次, 系统退出")