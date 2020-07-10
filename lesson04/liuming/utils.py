#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  
# Author:       Aaron
# Date:         2019/5/27
# -------------------------------------------------------------------------------

import os
import csv
import json
import time
from prettytable import PrettyTable

# Default variable
TODAY = time.strftime('%Y-%m-%d', time.localtime())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 用户名密码文件所在路径
PASSWD_FILE_PATH = os.path.join(BASE_DIR, "passwd")
# 保存添加的用户信息文件所在路径
USER_INFO_FILE_PATH = os.path.join(BASE_DIR, "user_info.csv")
# 日志文件所在路径
LOG_FILE_PATH = os.path.join(BASE_DIR, "{}-u_m_s_demon_v3.log".format(TODAY))

# 用户信息储存字典
RESULT = {}
# 需要添加的用户信息字段
FIELDS = ["username", "age", "phone", "email"]


# 写日志模块
def create_logs():
    import logging

    # 其中有个name参数，默认值为root
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(filename=LOG_FILE_PATH, mode='a', encoding='utf-8')

    # 定义handler的输出格式formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)

    return logger


# 删库跑路模块
def drop_data():
    user_choice = input("\033[31m[CRITICAL]: 高能警告, 此操作删库跑路.(Y/N) >>:\033[0m").strip()
    if user_choice == "Y":
        RESULT.clear()
        save_csv()
        return True
    return None


# 字典嵌套转换为 列表嵌套字典 --> [{username: {field_name: value, }},]
# 转换后的格式主要为了方便 PTable模块操作
def dict_to_list(data_dict):
    """
    :param data_dict:
    :return:
    """
    res = []
    [res.append({k: v}) for k, v in data_dict.items()]
    return res


# 分页
def page(page_number, page_size):
    """

    :param page_number:
    :param page_size:
    :return: status
    """

    status = {
        "code": 0,
        "msg": "",
        "data": "",
    }

    if not RESULT:
        status["code"], status["msg"] = 4, "Data is empty，u can only choice add operation."
        return status

    start = (page_number - 1) * page_size
    end = page_number * page_size

    # 总数据长度
    data_length = len(RESULT)
    # 计算出最大可以输入的页码
    max_page_number = data_length // page_size + 1 if data_length % page_size else data_length // page_size
    # 输入的页码过大时打印提示，输出最后一页内容
    if page_number > max_page_number:
        # 重新获得当前页码
        page_number = max_page_number
        status["code"] = 4
        status["msg"] = "Page-number too big from you entered,  maximum page-number is {}.\nThe last page:\n".format(max_page_number)
        start = (max_page_number-1) * page_size
        end = max_page_number * page_size

    res = dict_to_list(RESULT)

    # 切片操作，获取当前页需要输出的行数
    status["data"] = res[start: end]
    status["msg"] = status["msg"] + "共[{}]页，当前第[{}]页.".format(max_page_number, page_number)
    return status


# 打印表格
def format_print(rows, fields=FIELDS):
    """

    :param fields: type is list --> [field_name_1, field_name_2， field_name_*]
    :param rows: [{user_name_1: {field_name_1: value, }}, {user_name_2: {field_name_1: value, }}]
    :return:
    """
    tb = PrettyTable()
    tb.field_names = fields

    for i_dict in rows:
        for user_name in i_dict:
            tb.add_row([i_dict[user_name][i] for i in FIELDS])

    return tb
    # print("\033[32m{}\n\033[0m".format(tb))


# 从文件中读取所有用户名密码
def query_all_user_info():
    """
    :return: type is a dict --> {"user_name_1": "password", user_name_2": "password"}
    """
    # 自动生成用户名密码文件; 防止默认文件被删除出现找不到文件错误
    with open(PASSWD_FILE_PATH, "w") as fd:
        user_pwd = [{"username":"lm", "password": "1", "role": "admin"},
                    {"username": "monkey", "password": "1", "role": "guest"}]
        fd.write(json.dumps(user_pwd))

    # 读取文件数据, 再json.loads反序列化字符串到内存
    with open(PASSWD_FILE_PATH) as fd:
        res = json.loads(fd.readline())

    return res


# 封装csv文件导入操作
def save_csv():
    """
    :return:
    """

    status = {
        "code": 0,
        "msg": "",
        "data": "",
    }
    # 禁止空字典导出
    # if not RESULT:
    #     status["code"] = 4
    #     status["msg"] = "小老弟，都是空的你导出个锤锤!"
    #     return status

    with open(USER_INFO_FILE_PATH, 'w', newline="") as f2:
        fieldnames = FIELDS
        cw = csv.DictWriter(f2, fieldnames=fieldnames)
        # 将fieldnames 写入到第一行
        cw.writeheader()
        for i in RESULT:
            cw.writerow(RESULT[i])

    status["msg"] = "save success，file path:{}".format(USER_INFO_FILE_PATH)
    return status


# 封装导出csv操作
def load_csv():
    """
    :return:
    """

    status = {
        "code": 0,
        "msg": "",
        "data": "",
    }
    _result = {}

    # 文件不存在自动创建
    if not os.path.exists(USER_INFO_FILE_PATH):
        with open(USER_INFO_FILE_PATH, 'w') as f:
            f.write("\n")

    with open(USER_INFO_FILE_PATH, 'r') as f:
        cr = csv.DictReader(f)
        # print(type(cr), cr)
        for row in cr:
            name_key, age_key, phone_key, email_key = FIELDS
            username = row[name_key]

            # 字典第一层
            _result[username] = {}
            # 字典第二层嵌套
            _result[username][name_key], _result[username][age_key], _result[username][phone_key], \
                _result[username][email_key] = row[name_key], row[age_key], row[phone_key], row[email_key]
    # print("_result -> ", _result)

    # 全局RESULT字典 为空则自动更新为csv文件存在的用户数据
    if _result and not RESULT:
        RESULT.update(_result)
        status["code"] = 0
        status["msg"] = "[INFO]: load success."
        status["data"] = dict_to_list(_result)
        return status
    # 判断内存中的数据和硬盘导入数据是否一致
    elif _result and _result != RESULT:
        while True:
            user_choice = input("\033[36mThe operation will overwrite the user data already in memory. "
                                "recommend to save your data first.\n"
                                "Please confirm whether to execute again.(Y/N)>>: ").strip()

            if user_choice == "" or user_choice == "N"or user_choice == "n":
                status["code"] = 4
                status["msg"] = "[INFO]: cancel loading"
                return status
            elif user_choice == "Y" or user_choice == "y":
                # print("_result", _result)
                RESULT.update(_result)
                status["code"] = 0
                status["msg"] = "[INFO]: load success"
                status["data"] = dict_to_list(_result)
                return status
            else:
                print("\033[31mYou entered error, please try again.")
    # csv文件和全局RESULT都为空 或者数据都一致 不需要更新
    else:
        status["code"] = 4
        status["msg"] = "[INFO]: 完全一致，兄dei别瞎玩."
        return status


# 根据用户名查询一条用户记录
def get_one(name):
    """

    :param name: str
    :return: {}
    """
    if not RESULT:
        return

    if name in RESULT:
        user_info = RESULT[name]
        return user_info


# 封装增删改查操作
class DataOperate(object):
    # 定义增删查改的返回数据格式
    status = {
        "code": 0,  # 状态码反应操作成果或者失败；失败又分为1和4俩种，用于区分不同级别
        "msg": "",
        "data": "",
    }

    # 添加
    def add(self, data_list):
        """
        :param data_list: type is list
        :return: {}
        """
        # 验证用户是否已存在
        user_info = get_one(data_list[0])
        if user_info:
            self.status["code"], self.status["msg"] = 1, \
                "[FAIL]: user '{}' already exist, add operation is failing.".format(data_list[0])
            return self.status

        # 添加操作
        # user_info_d = {FIELDS[i]: data_list[i] for i in range(len(FIELDS))}
        user_info_d = dict(zip(FIELDS, data_list))
        # print("user_info_d --> ", user_info_d)
        RESULT[data_list[0]] = user_info_d

        # 为了 PTable准备的数据格式
        rows = [{data_list[0]: user_info_d}]
        self.status["code"], self.status["msg"], self.status["data"] = 0, "[INFO]: add ok.", rows
        return self.status

    # 通过username直接删除用户信息
    def delete(self, index):
        """

        :param index: string
        :return: {}
        """
        # 处理没有数据的情况
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status

        # 删除用户
        is_succ = RESULT.pop(index, None)
        # 用户不存在的情况
        if not is_succ:
            self.status["code"], self.status["msg"] = 1, "[ERROR]: user '{}' don't exist, u needn't to delete.".format(
                index)
        # 删除成功
        else:
            time_format = '%Y-%m-%d %X'
            today = time.strftime(time_format, time.localtime())
            self.status["code"], self.status["msg"] = 0, "{}\t[Success]: delete '{}' success.".format(today, index)
        return self.status

    # 通过username为索引更新数据字典
    def update(self, data_list):
        """
        update user_name set field_name = value
        update user_name set age = 18
        :param data_list: type is list --> ["username", "set", "field_name", "=", "value"]
        :return: {}
        """
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status

        username, field_name, value = data_list[0], data_list[2], data_list[4]
        # 处理用户名不存在情况
        if username not in RESULT:
            self.status["code"], self.status["msg"] = 4, \
                "[FAIL]: don't find any record which name is '{}'.".format(username)
            return self.status

        # 处理字段输入错误
        if field_name not in FIELDS:
            self.status["code"], self.status["msg"] = 1, \
                "[ERROR]: field '{}' doesn't exist".format(field_name)
            return self.status
        # 处理修改用户名字段，但已存在同用户名的情况
        elif field_name == FIELDS[0] and value in RESULT:
            self.status["code"], self.status["msg"] = 1, \
                "[ERROR]: user '{}' already exist, can't change {} field to {}".format(username, field_name, username)
            return self.status

        # 修改用户名字段
        if field_name == FIELDS[0]:
            temp_dict = RESULT[username]
            temp_dict[field_name] = value
            res = self.delete(username)
            if res["code"] != 0:
                self.status["code"] = 1
                self.status["msg"] = "update {}'s field [{}] failed."
            RESULT[username] = temp_dict

        # 修改非username字段的数据
        else:
            RESULT[username][field_name] = value
            self.status["code"] = 0
            self.status["msg"] = "[INFO]: update '{}' success,change {}'s value to '{}'".format(
                username, field_name, value)
        return self.status

    # 可通过用户名作为关键字查找
    def find(self, username):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status
        # 未输入要查找的用户
        elif not username:
            self.status["code"], self.status["msg"] = 1, "[ERROR]:  takes exactly 1 argument (0 given)."
            return self.status
        # 用户名不存在
        elif username not in RESULT:
            self.status["code"], self.status["msg"] = 4, \
                "[INFO]: User '{}' doesn't exist, u need to add first.".format(username)
            return self.status

        # 从字典查找到用户并重新拼接数据结构
        rows = [{username: RESULT[username]}]
        self.status["code"] = 0
        self.status["msg"] = "[INFO]: Find {} rows of records".format(len(rows))
        self.status["data"] = rows

        return self.status

    # 列出所有数据
    def list(self):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，add a new user,please."
            return self.status

        res = dict_to_list(RESULT)
        self.status["code"], self.status["msg"], self.status["data"] = 0, "[INFO]: list all user info", res
        return self.status


if __name__ == "__main__":
    # all_user_dict = query_all_user_info()
    # print(all_user_dict)

    # save_csv()
    # load_csv()

    # 打印
    # print("user_info_dict -- >", user_info_dict)
    # print("RESULT -->", RESULT)

    # # 测试分页模块
    # res = page(3, 2)
    # if res["code"] and res["code"] == 4:
    #     print("\033[34m{}\033[0m".format(res["msg"]))
    #
    # format_print(res["data"])
    pass

