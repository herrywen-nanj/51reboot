# -*- coding:utf-8 -*-
# author: lyl

"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys
import getpass
import re

# 定义变量
RESULT = []
FIND_LIST = []
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6

USERINFO = {
    '51reboot': {
        "password": "123456",
        "role": "admin"
    },
    '52reboot': {
        "password": "123456",
        "role": "user"
    }
}

FIELDS = ['username', 'age', 'tel', 'email', 'id']
MAX_ID = 1
CAN_USE_ID = []

FIND_LIST.append(FIELDS)
RESULT.append(FIELDS)
phone_add = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 172, 178, 182, 183, 184, 187, 188, 198,
             130, 131, 132, 145, 155, 156, 166, 171, 175, 176, 185, 186, 133, 149, 153, 173, 177, 180, 181, 189, 191,
             199]
mail_pattern = re.compile(r'([a-zA-Z0-9]([a-zA-Z0-9_]+)(\@))[a-zA-Z0-9]([a-zA-Z0-9_]+)\.(([a-z]+))')


# 定义功能函数
# 检测用户登录
def check_user_login(user_name, pass_word):
    if user_name not in USERINFO.keys() or USERINFO[user_name]['password'] != pass_word:
        return False
    return True


# 检测用户登录
def check_user_permission(user_name):
    return USERINFO[user_name]['role']


# 检测用户是否存在
def check_user(name):
    for i in RESULT:
        if i[4] != "id":
            if str(i[4]) == name:
                return True
        if name == i[0]:
            return True
    return False


# 检查用户更新用户更新字段
def check_input(tag, check_world=None):
    return {
        'username': lambda: 0 if check_world is None else check_input_type(),
        'age': lambda: 1 if check_world is None else check_input_type(age=check_world),
        'tel': lambda: 2 if check_world is None else check_input_type(phone=check_world),
        'email': lambda: 3 if check_world is None else check_input_type(mail=check_world),
    }[tag]()


# 检查用户输入内容是否有误
def check_input_type(age=None, phone=None, mail=None):
    if age is not None:
        if not age.isdigit():
            return "\033[1;31m年龄有误\033[0m"
    if phone is not None:
        if len(phone) != 11:
            return "\033[1;31m手机号有误\033[0m"
        # 提取用户输入手机号的前三位,并转化为int类型
        head = int(''.join(list(phone[:3])))
        if head not in phone_add:
            return "\033[1;31m手机号有误,暂不支持虚拟运营商!!!\033[0m"
    if mail is not None:
        # 粗略写的正则，凑活着用
        m = mail_pattern.match(mail)
        if m is None:
            return "\033[1;31m邮件格式有误 eg: xxx@xxx.com\033[0m"
    return True


# 增加用户
def add(infolist, user_name, user_id):  # 之所以写infolist是因为如果定义成info_list 不符合PEP8规范
    # add monkey 12 13987654321 monkey@51reboot.com
    # 检测用户输入，长度必须为5，个字段分别为：动作、姓名、年龄、手机号、邮箱
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    if len(infolist) != 5:
        return "\033[1;31m输入有误，请检查输入内容 eg: add monkey 12 132xxx monkey@51reboot.com\033[0m"
    tag = check_input_type(age=infolist[2], phone=infolist[3], mail=infolist[4])
    if tag is not True:
        return tag
    name = infolist[1]
    if check_user(name):
        return "\033[1;31m添加失败{}已存在\033[0m".format(name)
    user_info = infolist[1:]
    user_info.append(user_id)
    RESULT.append(user_info)

    return True


# 删除用户
def delete(infolist, user_name):
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    # delete monkey
    if len(infolist) != 2:
        return "\033[1;31m输入有误，请检查输入内容 eg: delete monkey\033[0m"
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                user_id = RESULT[i][4]
                RESULT.remove(RESULT[i])
                return [user_id, "\033[1;32;40m用户{}删除成功\033[0m".format(name)]
    return "\033[1;31m用户{}删除失败，无此用户\033[0m".format(name)


# 更新用户
def update(infolist, user_name):
    # ['username', 'age', 'tel', 'email']
    # update monkey set age = 18
    if check_user_permission(user_name) == 'user':
        return "\033[1;31mpermission denied\033[0m"
    if len(infolist) != 6 or infolist[2] != 'set' or infolist[3] not in ['username', 'age', 'tel', 'email'] or \
            infolist[4] != "=":
        return "\033[1;31m输入有误，请检查输入内容 eg: update monkey set age = 18\033[0m"

    tag = check_input(infolist[3], check_world=infolist[5])
    if tag is not True:
        return tag
    name = infolist[1]
    if check_user(name):
        for i in range(len(RESULT)):
            if name == RESULT[i][0]:
                result_tag = check_input(info_list[3])
                RESULT[i][result_tag] = infolist[5]
        return "\033[1;32;40m用户{}更新成功\033[0m".format(name)
    return "\033[1;31m用户{}更新失败，无此用户\033[0m".format(name)


# 精确查找
def find(user_name):
    if check_user(user_name):
        for i in range(len(RESULT)):
            if user_name == RESULT[i][0] or user_name == str(RESULT[i][4]):
                return RESULT[i]
    return False


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    # 设置密码输入为非明文方式，IDE 下不可用
    password = getpass.getpass(prompt="Please input your password: ")
    login_tag = check_user_login(username, password)
    if login_tag:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        print("\033[1;32;40m来了老弟\033[0m")
        while True:
            # 业务逻辑
            info = input("Please input your operation: ")
            # string -> list
            info_list = info.split()
            # 检测用户是否输入内容
            try:
                action = info_list[0]
            except IndexError:
                print("\033[1;31m兄弟什么都不输入几个意思?\033[0m")
                continue
            if action == "add":
                # 检测可用id 表是否为空，如果有则取对应的值如果没有则选用MAX_ID + 1的值做id
                if len(CAN_USE_ID) > 0:
                    result = add(info_list, username, CAN_USE_ID[0])
                    id_tag = False
                    CAN_USE_ID.remove(CAN_USE_ID[0])
                else:
                    result = add(info_list, username, MAX_ID)
                    id_tag = True
                if result is True:
                    print("\033[1;32;40m用户{}添加成功\033[0m".format(info_list[1]))
                    if id_tag:
                        MAX_ID += 1
                else:
                    print(result)
            elif action == "delete":
                # .remove
                result = delete(info_list, username)
                try:
                    delete_user_id = result[0]
                    CAN_USE_ID.append(delete_user_id)
                    result = result[1]
                except IndexError:
                    pass
                print(result)
            elif action == "update":
                result = update(info_list, username)
                print(result)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if len(RESULT) == 1:
                    print("no user ,if you have permission ,you can add it")
                else:
                    for x in RESULT:
                        # 突然想加个id功能，如果加到前面就会重写一堆东西，所以还是简单的改下输出吧
                        print("{} {} {} {}".format(x[4], x[0], x[1], x[2], x[3]), end="\t")
                        print()
                        print("-" * 50)
            elif action == "find":
                result = find(info_list[1])
                if result is False:
                    print("\033[1;31m用户不存在\033[0m")
                else:
                    FIND_LIST.append(result)
                    for x in FIND_LIST:
                        print("{} {} {} {}".format(x[4], x[0], x[1], x[2], x[3]), end="\t")
                        print()
                        print("-" * 50)
                    # 避免多次查询数据重复
                    FIND_LIST.remove(result)
            elif action == "login_out":
                # 切换账号重置登录失败次数
                INIT_FAIL_CNT = 0
                break
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[1;31minvalid action.\033[0m")
    else:
        # 带颜色
        print("\033[1;31musername or password error.\033[0m")
        INIT_FAIL_CNT += 1

print("\033[1;31m\nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
