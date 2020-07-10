# -*- coding:utf-8 -*-
# author: lyl

"""
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 13987654321 monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
3. 格式化输出
"""

# 标准模块
import sys
import getpass
import check
import add
import delete
import update
import find_list
import save_load
import logs

# 定义变量

INIT_FAIL_CNT = 0
MAX_FAIL_CNT = 6


while INIT_FAIL_CNT < MAX_FAIL_CNT:
    username = input("Please input your username: ")
    # 设置密码输入为非明文方式，IDE 下不可用
    password = getpass.getpass(prompt="Please input your password: ")
    # password = input("Please password: ")
    login_tag, role = check.user_login(username, password)
    if login_tag:
        # 如果输入无效的操作，则反复操作, 否则输入exit退出
        print("\033[1;32m{} 欢迎回来,你的身份是 {}\033[0m".format(username, role))
        check.display(role)
        while True:
            try:
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
                    logs.info(username, info_list)
                    add.user(info_list, role)
                elif action == "delete":
                    logs.info(username, info_list)
                    delete.user(info_list, role)
                elif action == "update":
                    logs.info(username, info_list)
                    update.user(info_list, role)
                elif action == "list":
                    logs.info(username, info_list)
                    find_list.list_user()
                elif action == "find":
                    logs.info(username, info_list)
                    find_list.find_user(info_list)
                elif action == "display":
                    logs.info(username, info_list)
                    find_list.pagesize(info_list)
                elif action == "save":
                    logs.info(username, info_list)
                    save_load.save_user(info_list)
                elif action == "load":
                    logs.info(username, info_list)
                    save_load.load_user(info_list, role)
                elif action == "login_out":
                    logs.info(username, info_list)
                    # 切换账号重置登录失败次数
                    INIT_FAIL_CNT = 0
                    break
                elif action == "exit":
                    sys.exit(0)
                else:
                    print("\033[1;31minvalid action.\033[0m")
            except KeyboardInterrupt as e:
                logs.error(e)
                print("\033[1;31m兄弟按Ctrl + C是不对的,真想退出请用exit\033[0m")
    else:
        # 带颜色
        print("\033[1;31musername or password error.\033[0m")
        logs.info(username, ['登录失败'])
        INIT_FAIL_CNT += 1

print("\033[1;31m\nInput {} failed, Terminal will exit.\033[0m".format(MAX_FAIL_CNT))
