# -*- coding:utf-8 -*-
# author: lyl
import json
import check
import logs

title = ['id', 'name', 'age', 'tel', 'email']
user_tem = {}
user_list = []


def write_id(note_info, tag):
    with open('id_info.txt', 'w+') as id_fd:
        # 对id文件进行处理
        if tag == "USED":
            id_list = note_info['CAN_USE_ID']
            id_list.remove(id_list[0])
            note_info["CAN_USE_ID"] = id_list

            if note_info["CAN_USE_ID"] is None:
                note_info["CAN_USE_ID"] = []
        else:
            note_info["MAX_ID"] = note_info["MAX_ID"] + 1

        # 格式化写入id格式
        new_id_info = json.dumps(note_info, indent=4)
        id_fd.write(new_id_info)


def write_uer(user_message):
    with open('user.txt', 'r+') as fd:
        note = fd.read()
        # 如果用户表为空，则手动赋值，避免loads报错
        if note == '':
            note = '{}'
    try:
        # 初始化用户信息
        dict1 = json.loads(note)
    except Exception as e:
        print("\033[1;31m用户文件 user.txt 存在异常，请手动修复\033[0m")
        logs.error(e)
        return [False, None]
    # 判断用户是否存在
    if user_message[1] in dict1.keys():
        return [False, "\033[1;31m用户{}已存在，添加失败！！\033[0m".format(user_message[1])]
    # 拼凑插入字典的value
    for i in range(len(title)):
        user_tem[title[i]] = user_message[i]
    dict1[user_message[1]] = user_tem
    # 格式化数据，并写入
    str1 = json.dumps(dict1, indent=4)
    with open('user.txt', 'w') as fd:
        fd.write(str1)
        return [True, "\033[1;32m用户{}添加成功\033[0m".format(user_message[1])]


def user(user_info, role, tag=None):
    # 检查用户权限
    if role != 'admin':
        print("\033[1;31mpermission denied\033[0m")
        return
    if len(user_info) != 5:
        print("\033[1;31m输入有误，eg: add monkey 18 13987654321 12345@qq.com\033[0m")
        return
    # 检测用户输入的年龄、手机号、邮箱是否合法
    check_result = check.input_args(username=user_info[1], age=user_info[2], phone=user_info[3], mail=user_info[4])
    if check_result is not True:
        print("\033[1;31m用户\033[0m" + "\033[1;31m{}\033[0m".format(user_info[1]) + "\033[1;31m添加失败,\033[0m" +
              check_result)
        return
    # 检测可用id 表是否为空，如果有则取对应的值如果没有则选用MAX_ID + 1的值做id
    with open('id_info.txt', 'r+') as id_fd:
        try:
            id_dict = json.loads(id_fd.read())
        except Exception as e:
            print("\033[1;31m id文件 id_info.txt存在异常，请手动修复\033[0m")
            logs.error(e)
            return
        if len(id_dict['CAN_USE_ID']) > 0:
            # 增加id字段
            user_info.insert(1, id_dict['CAN_USE_ID'][0])
            # 增加用户信息
            user_list.append(user_info[1:])
            tag = 'USED'
        else:
            user_info.insert(1, id_dict['MAX_ID'])
            tag = 'MAX'

    result = write_uer(user_info[1:])
    if result[0]:
        write_id(id_dict, tag)
        print(result[1])
    elif result[1] is None:
        pass
    else:
        print(result[1])

