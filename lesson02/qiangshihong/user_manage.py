#!/usr/bin/python
'''
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
'''

help_info = '''---------------------------------------------
命令：
>增: add monkey 12 132xxx monkey@51reboot.com
>删: delete monkey
>改: update monkey set age = 18
>查: list
>搜: find monkey
---------------------------------------------
'''

import sys
import getpass   #用于隐藏用户输入的字符串，常用来接收密码

# 定义变量
RESULT = []
USERID = []
NEW_USERID = 1
INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6
USERINFO = ("51reboot","123456")
FIELDS = ['id', 'username', 'age', 'tel', 'email']
RESULT.append(FIELDS)
flag = False

def get_id(RESULT_length):
    global NEW_USERID,ADD_USERID
    ADD_USERID = ''
    if int(RESULT_length) > 0:
        last_id = int(RESULT[RESULT_length][0])
        if last_id < len(RESULT):
            NEW_USERID = str(last_id + 1)
            return NEW_USERID

        else:
            for x in range(1,len(RESULT)):
                if x != int(RESULT[x][0]):
                    ADD_USERID = str(x)
                    return ADD_USERID
                else:
                    pass

    else:
        NEW_USERID = str(NEW_USERID)
        return NEW_USERID

def get_info(user_info,*args):
    global flag,inx
    for i in RESULT:
        if user_info == i[1]:
            flag = True
            inx = RESULT.index(i)
            return inx,flag
        else:
            flag = False
def add_user(info_list):
    while len(info_list) == 5:
        length = len(RESULT) - 1
        get_info(info_list[1])
        # 判断用户是否存在, 如果用户存在，提示用户已经存在， 不在添加
        if flag == False:
            get_id(length)
            #判断id完整性，优先分配低数值
            if len(ADD_USERID.strip()) == 0:
                info_list[0] = NEW_USERID
                RESULT.append(info_list)
            else:
                info_list[0] = ADD_USERID
                RESULT.insert(int(ADD_USERID),info_list)
            # 打印结果信息
            return("\033[1;32mAdd {} succ.\033[0m\n".format(info_list[1]))
        else:
            return ("\033[5;31m{} already exists.\033[0m\n".format(info_list[1]))
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: add [{}] [{}] [{}] [{}]\033[0m\n").format(FIELDS[1], FIELDS[2], FIELDS[3], FIELDS[4])
def del_user(info_list):
    while len(info_list) == 2:
        get_info(info_list[1])
        if flag:
            RESULT.pop(inx)
            return ("\033[5;31m{}\033[0m has been deleted.\n".format(info_list[1]))
            break
        else:
            return "\033[5;31m{} does not exist.\033[0m\n".format(info_list[1])
    else:
        return ("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: delete | del [{}]\033[0m\n").format(FIELDS[1])
def find_info(info_list):
    while len(info_list) == 2:
        get_info(info_list[1])
        if flag:
            print("|{} |{} |{} |{}|\n".format(FIELDS[0].ljust(5), FIELDS[1].ljust(10),FIELDS[2].ljust(3), FIELDS[3].ljust(11),FIELDS[4].ljust(20), end="\t"))
            print("|{} |{} |{} |{}|".format(RESULT[inx][0].ljust(5),RESULT[inx][1].ljust(10),RESULT[inx][2].ljust(3),RESULT[inx][3].ljust(11),RESULT[inx][4].ljust(20), end="\t"))
            break
        else:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1])
    else:
        print("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: find [{}]\033[0m\n".format(FIELDS[1]))
def update_info(info_list):
    while len(info_list) == 6:
        get_info(info_list[1])
        if flag and info_list[3] in FIELDS:
            iny = FIELDS.index(info_list[3])
            RESULT[inx][iny] = info_list[5]
            return "{} {} was changed to {}.".format(info_list[1],info_list[3],info_list[5], end="\t")
            break
        if info_list[3] not in FIELDS:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[3])
        else:
            return "\033[1;31;43m{} does not exist!\033[0m\n".format(info_list[1])
    else:
        return("\033[1;31mInput Error！\033[0m\n\033[5;33;42mUsage: update [{}] set [ {}|{}|{} ] = [ Target field ]\033[0m\n").format(FIELDS[1],FIELDS[2],FIELDS[3],FIELDS[4])

def main():
    # 如果输入无效的操作，则反复操作, 否则输入exit退出
    while True:
        try:
            # 业务逻辑
            info = input("\033[1;35mPlease input your operation: \033[0m")
            # string -> list
            info_list = info.split()
            action = info_list[0]
            if action == "add":
                res = add_user(info_list)
                print(res)
            elif action == "delete" or action == "del":
                # .remove
                res = del_user(info_list)
                print(res)
            elif action == "find":
                find_info(info_list)
            elif action == "update":
                res = update_info(info_list)
                print(res)
            elif action == "list":
                # 如果没有一条记录， 那么提示为空
                if (len(RESULT)) == 1:
                    print("\033[1;31mEmpty.Please add user information!\033[0m")
                else:
                    for i in RESULT:
                        #定义字符串长度为?，字符对齐到左边，默认填充空格
                        print("|{} |{} |{} |{} |{}|".format(i[0].ljust(5), i[1].ljust(10), i[2].ljust(3), i[3].ljust(11), i[4].ljust(20)), end="\t")
                        print()
                        print("-".ljust(59,'-'))
            elif action == "help" or action == "h":
                print(help_info)
            elif action == "exit":
                sys.exit(0)
            else:
                print("\033[1;36m输入错误，请输入 help 查看帮助！\033[0m\n")
        except IndexError:
            print('\033[1;36mError：list index out of range.\033[0m\n')

def checkuser(username,password):
    if username == USERINFO[0] and password == USERINFO[1]:
        return True
    else:
        return False

if __name__ == "__main__":
    while INIT_FAIL_CNT < MAX_FAIL_CNT:
        username = input("Please input your username: ")
        password = getpass.getpass("Please input your password: ")   #输入密码不可见
        if checkuser(username, password):
            print("\033[1;36mLogin Suceesfully.\033[0m")
            main()
        else:
            INIT_FAIL_CNT += 1
            if INIT_FAIL_CNT < MAX_FAIL_CNT:
                print("\033[5;35musername or password error！\033[0m\n还剩 {} 次机会.".format(MAX_FAIL_CNT - INIT_FAIL_CNT))
    else:
        print("\n\033[1;31mBye-bye, Input {} failed.\033[0m".format(MAX_FAIL_CNT))
