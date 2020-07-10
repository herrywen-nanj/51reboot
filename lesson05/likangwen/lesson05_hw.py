import sys
from prettytable import PrettyTable
import pandas
import logging
import dbutils

# 定义变量
# RESULT = {'kw25': {'tel': '10086', 'age': 20, 'username': 'kw25', 'email': 'kw15@qq.com'}, 'kw28': {'tel': '10086', 'age': 20, 'username': 'kw28', 'email': 'kw8@qq.com'}}
RESULT = {}
# USERINFO = ("admin", "123456")
USERINFO = ("a", "a")
FIELDS = ('username', 'age', 'tel', 'email')
# RESULT.append(FIELDS)

FORMAT = """
====================================================================
    2.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    2.2 删 delete        # delete monkey
    2.3 改 update        # update monkey set age = 18
    2.4 查 list          # list
    2.5 搜 find          # find monkey
    2.6 分页  display    # display page 1 pagesize 5
    2.7 保存csv格式，可跟上名称，否则默认     # export csvname  
    2.8 帮助文档         # 'h' or 'help'    
===================================================================
"""

# 日志函数
def User_log(msg):
    logging.basicConfig(level=logging.DEBUG,
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    logging.debug(msg)


# 读取数据库里的数据
def load():
    sql = "select * from users"
    msg, ok = dbutils.sqlOperation(sql, seek=True)
    if ok:
        for u in msg:
            RESULT[u[1]] = dict(zip(FIELDS, u[1:])) #读取数据库的数据并报错到RESULT字典里面
        return 'opration success'

    else:
        return 'sql data is empty'

# 保存到数据库
def save():
    for k,v in RESULT.items():
        print(v.keys())
        find_sql = "select * from users where username='{}'".format(k)
        msg,ok = dbutils.sqlOperation(find_sql, seek=True)     # 查找用户是否存在，不存在则创建
        if not ok:
            sql = "insert into users{} values{}" .format(str(tuple(v.keys())).replace("'",""), tuple(v.values()))    # 生成对应的sql语句
            print(sql)
            try:
                msg, ok = dbutils.sqlOperation(sql)
            except Exception as e:
                return e
        else:
            continue
    return msg

# 添加用户函数
def add(info_list):
    USER_MSG = {}
    if len(info_list) == 4:
        username = info_list[0]
        if username in RESULT:
            print("用户已存在，请重新添加")
        else:
            RESULT[username] = dict(zip(FIELDS, info_list))
            User_log("user {} add success" .format(username))
            print("添加用户成功")
    else:
        print("请输入正确格式, {}".format("add monkey 12 132xxx monkey@51reboot.com"))

# 分页
def display(info_list):
    if len(info_list) >= 2 and len(info_list) <= 4:

        pagesize = 5
        if len(info_list) == 2:
            if info_list[0] == "page":
                pagesize = 5
            else:
                print("请重新输入查询语句")
        else:
            if info_list[0] == "page" and info_list[2] == "pagesize":
                pagesize = int(info_list[-1])
            else:
                print("请重新输入查询语句")

        page = int(info_list[1])
        data = []
        for k, v in RESULT.items():
            data.append(v.values())
        end = page * pagesize

        pretable(data[end-pagesize: end], FIELDS=v.keys())

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
            # 操作数据库
            sql = "delete from users where username='{}'".format(u_k)
            dbutils.sqlOperation(sql)
            User_log("user {} delete success".format(u_k))
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
                    if key_name == "username":
                        RESULT[value_name] = RESULT.pop(u_k)  #修改外层key(name)的名称，保持外层和里面的name名称是一致的
                    u_v[key_name] = value_name  # 修改里层的字典对应的key的value
                    # 操作数据库
                    if key_name == 'age':
                        sql = "update users set {}={} where username='{}'".format(key_name, value_name, info_list[0])
                    else:
                        sql = "update users set {}='{}' where username='{}'".format(key_name, value_name, info_list[0])
                    dbutils.sqlOperation(sql)
                    # 数据保存到文件
                    #save()
                    return "{}用户修改成功".format(value_name)
                else:
                    return "{}，无此字段参数".format(key_name)

            except Exception:
                return "请输入正确的参数"

    return "{}用户修改失败，用户列表查无此用户".format(info_list[0])

# 打印成表格的函数
def pretable(data, FIELDS=FIELDS):
    if len(data):
        if type(data) == dict:
            pt_fields = list(list(data.values())[0].keys())
            x = PrettyTable()
            x.field_names = pt_fields
            for u_k, u_v in data.items():
                x.add_row(list(u_v.values()))
            print(x)
        elif type(data) == list:
            x = PrettyTable()
            x.field_names = FIELDS
            for user_list in data:
                x.add_row(user_list)
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


def main():
    INIT_FAIL_CNT = 0
    MAX_FAIL_CNT = 6

    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        print("******此为缓存到文件操作版本******")
        username = input("Please input your username: ")
        password = input("Please input your password: ")
        # password = getpass.getpass("Please input your password: ")
        if username == USERINFO[0] and password == USERINFO[1]:
            # 提示增删改查操作
            print("输入'h'或者 'help'查看帮助文档")

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

                elif action == "display":
                    ret = display(info_list)
                    if ret:
                        user_list(ret)
                        
                elif action == "export":
                    export(info_list)
                    
                elif action == "load":
                    load()
                    
                elif action == "save":
                    msg = save()
                    print(msg)
                    
                elif action.lower() == "h" or action.lower() == "help":
                    print(FORMAT)

                elif action == "haha":
                    print(RESULT)
                    
                elif action == "exit":
                    sys.exit(1)
                    
                else:
                    print("Syntax error")
                    print(FORMAT)
        else:
            print("账号或密码错误")
            INIT_FAIL_CNT += 1

    print("密码错误次数超过6次, 系统退出")

"""
def main():
    msg = save()
    print(msg)
"""

if __name__ == '__main__':
    main()