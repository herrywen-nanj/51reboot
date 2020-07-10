# -*- coding:utf-8 -*-
# author: lyl
# 删除用户

import check
import json
import logs


def user(info_list, role):
    # 检查用户权限
    if role != 'admin':
        print("\033[1;31mpermission denied\033[0m")
        return
    # 检查用户输入内容
    if len(info_list) != 2:
        print("\033[1;31m输入有误，请检查输入内容 eg: delete monkey\033[0m")
        return
    # 检查用户是否存在
    result, message, user_id = check.user(info_list[1])
    if result is False:
        print(message)
        return
    elif result is None:
        return
    # 读取用户信息
    with open('user.txt', 'r') as user_fd:
        user_note = user_fd.read()
        if user_note == '':
            user_note = '{}'

    # 写入修改后信息
    try:
        user_dict = json.loads(user_note)
        user_dict.pop(message)
    except Exception as e:
        print("\033[1;31m 用户文件 user.txt存在异常，请手动修复\033[0m")
        logs.error(e)
        return


    # 读取ID信息
    with open('id_info.txt', 'r') as id_fd:
        try:
            id_note = id_fd.read()
            id_dict = json.loads(id_note)
        except Exception as e:
            logs.error(e)
            print("\033[1;31m id文件 id_info.txt存在异常，请手动修复\033[0m")
            return
    # 回收ID
    if len(id_dict['CAN_USE_ID']) == 0:
        id_list = [user_id]
        id_dict['CAN_USE_ID'] = id_list

    else:
        id_list = id_dict['CAN_USE_ID']
        id_list.append(user_id)
        id_dict['CAN_USE_ID'] = id_list

    with open('id_info.txt', 'w') as id_fd_rw:
        id_fd_rw.write(json.dumps(id_dict, indent=4))

    with open('user.txt', 'w+') as user_fd_rw:
        user_fd_rw.write(json.dumps(user_dict, indent=4))
        print("\033[1;32m用户{}删除成功\033[0m".format(message))
