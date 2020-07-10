#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  
# Author:       Aaron
# Date:         2019/5/27
# -------------------------------------------------------------------------------
"""
需求说明:
v2版数据结构: {"username1": {"field1": "value1", "field2": "value2", " field3": "value3", "field4": "value4"}, }
FIELDS: ["username", "age", "phone", "email"]
"""

import os
import csv
import json
import time
from prettytable import PrettyTable

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASSWD_FILE = os.path.join(BASE_DIR, "passwd")    # 用户名密码文件所在路径
USER_INFO_FILE = os.path.join(BASE_DIR, "user_info.csv")  # 保存添加的用户信息文件所在路径
FIELDS = ["username", "age", "phone", "email"]


# 字典嵌套转换为 列表嵌套字典 --> [{username: {field_name: value, }},]
# 转换后的格式主要为了方便 Ptable模块操作
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
    max_page_number = data_length // page_size + 1 if data_length % page_size else data_length / page_size
    # 输入的页码过大时打印提示，输出最后一页内容
    if page_number > max_page_number:
        status["code"] = 4
        status["msg"] = "Page-number too big from you entered,  maximum page-number is {}.\nThe last page:".format(max_page_number)
        start = (max_page_number-1) * page_size
        end = max_page_number * page_size

    res = dict_to_list(RESULT)

    # 切片操作，获取当前页需要输出的行数
    status["data"] = res[start: end]
    return status


# 打印表格
def format_print(rows, fields=FIELDS):
    """

    :param fields: type is list --> [field_name_1, field_name_2， field_name_*]
    :param rows: [{user_name_1: {field_name_1: value, }}, {user_name_2: {field_name_1: value, }}]
    :return:
    """
    x = PrettyTable()
    x.field_names = fields

    for i_dict in rows:
        for user_name in i_dict:
            x.add_row([i_dict[user_name][i] for i in FIELDS])

    print("\033[32m{}\n\033[0m".format(x))


# 从文件中读取所有用户名密码
def query_all_user_info():
    """
    :return: type is a dict --> {"user_name_1": "password", user_name_2": "password"}
    """
    # 自动生成用户名密码文件; 防止默认文件被删除出现找不到文件错误
    with open(PASSWD_FILE, "w") as fd:
        user_pwd = {"lm": "1", "monkey": "大佬带我飞"}
        fd.write(json.dumps(user_pwd))

    # 读取文件数据, 再json.loads反序列化字符串到内存
    with open(PASSWD_FILE) as fd:
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
    if not RESULT:
        status["code"] = 4
        status["msg"] = "小老弟，都是空的你导出个锤锤!"
        return status

    with open(USER_INFO_FILE, 'w', newline="") as f2:
        fieldnames = FIELDS
        cw = csv.DictWriter(f2, fieldnames=fieldnames)
        # 将fieldnames 写入到第一行
        cw.writeheader()
        for i in RESULT:
            cw.writerow(RESULT[i])

    status["msg"] = "导出成功，文件位置:{}".format(USER_INFO_FILE)
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
    result = {}

    with open(USER_INFO_FILE, 'r') as f:
        cr = csv.DictReader(f)
        # print(type(cr), cr)
        for row in cr:
            name_key, age_key, phone_key, email_key = FIELDS
            username = row[name_key]

            # 字典第一层
            result[username] = {}
            # 字典第二层嵌套
            result[username][name_key], result[username][age_key], result[username][phone_key], \
                result[username][email_key] = row[name_key], row[age_key], row[phone_key], row[email_key]
        # print(result)

    if result:
        status["data"] = result
    else:
        status["code"] = 1
        status["msg"] = "[ERROR]: 导入失败"

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
# 根据数据结构变化，查看下是否需要优化
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
        user_info_d = {FIELDS[i]: data_list[i] for i in range(len(FIELDS))}
        # print("user_info_d --> ", user_info_d)
        RESULT[data_list[0]] = user_info_d

        # 为了 PTable准备的数据格式
        rows = [{data_list[0]: user_info_d}]
        self.status["code"], self.status["msg"], self.status["data"] = 0, "[Success]: add ok.", rows
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

        if index in RESULT:
            # 删除用户
            RESULT.pop(index)

            # 打印时间，配合审计功能可以直接写日志
            time_format = '%Y-%m-%d %X'
            today = time.strftime(time_format, time.localtime())
            self.status["code"], self.status["msg"] = 0, "{}\t[Success]: delete '{}' success.".format(today, index)
            return self.status
        # 用户不存在的情况
        else:
            self.status["code"], self.status["msg"] = 1, "[ERROR]: user '{}' don't exist, u needn't to delete.".format(
                index)
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
            self.status["msg"] = "[Success]: update '{}' success,change {}'s value to '{}'".format(
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
        self.status["data"] = rows

        return self.status

    # 列出所有数据
    def list(self):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，add a new user,please."
            return self.status

        res = dict_to_list(RESULT)
        self.status["code"], self.status["data"] = 0, res
        return self.status


# 从本地csv文件读取已有用户信息数据
user_info_dict = load_csv()
RESULT = {} if user_info_dict["code"] else user_info_dict["data"]


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

