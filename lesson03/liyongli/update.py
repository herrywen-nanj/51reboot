# -*- coding:utf-8 -*-
# author: lyl
import check
import json
import logs


def user(info_list, role):
    # 检查用户权限
    if role != 'admin':
        print("\033[1;31mpermission denied\033[0m")
        return
    # 检查用户输入内容
    # update monkey set age = 18
    if len(info_list) != 6:
        print("\033[1;31m输入长度有误，请检查输入内容 eg: update monkey set age = 18\033[0m")
        return
    if info_list[2] != 'set' or info_list[4] != '=':
        print("\033[1;31m输入长度有误，请检查输入内容 eg: update monkey set age = 18\033[0m")
        return
    # 检查用户是否存在
    result, message, user_id = check.user(info_list[1])
    if result is False:
        print(message)
        return
    elif result is None:
        return
    if info_list[3] not in ['username', 'age', 'tel', 'email']:
        print("\033[1;31m更新字段有误，请检查\033[0m")
        return

    tag = check.user_input(tag=info_list[3], check_world=info_list[-1])
    if tag:
        with open('user.txt', 'r') as user_fd:
            user_note = user_fd.read()
            if user_note == '':
                user_note = '{}'
            try:
                user_dict = json.loads(user_note)
            except Exception as e:
                print("\033[1;31m id文件 user.txt存在异常，请手动修复\033[0m")
                logs.error(e)
                return
            user_dict[info_list[1]][info_list[3]] = info_list[-1]
        with open('user.txt', 'w') as user_fd_rw:
            user_fd_rw.write(json.dumps(user_dict, indent=4))
            print("\033[1;32m用户{} {}修改成功\033[0m".format(info_list[1], info_list[3]))
    else:
        print(tag)
