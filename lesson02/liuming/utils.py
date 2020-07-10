#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  抽出公用模块
# Author:       Aaron
# Date:         2019/5/19
# -------------------------------------------------------------------------------
"""
根据视频要求重新改写作业
数据结构: [[user_info],[user_info]]
FIELDS: ["username", "age", "phone", "email"]
多写一个方法，针对通过 name获取记录
"""
FIELDS = ["username", "age", "phone", "email"]
RESULT = []


# 封装增删改查操作
class DataOperate(object):
    # 定义增删查改的返回数据格式
    status = {
        "code": 0,  # 状态码反应操作成果或者失败；失败又分为1和4俩种，用于区分不同级别
        "msg": "",
    }

    # 添加，可批量添加数据到列表
    def add(self, data_list):
        """
        :param data_list: type is list
        :return: {}
        """
        # 验证用户是否已存在
        user_info = get_one(data_list[0])
        if user_info:
            self.status["code"], self.status["msg"] = 1, \
                "Fail: user '{}' already exist, add operation is failing.".format(data_list[0])
            return self.status

        # 添加操作
        RESULT.append(data_list)
        self.status["code"], self.status["msg"] = 0, "Success: add ok."
        return self.status

    # 通过name直接 remove 用户信息
    def delete(self, index):
        """

        :param index: string
        :return: {}
        """
        # 处理没有数据的情况
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status

        for u in RESULT:
            if index == u[0]:
                # 删除用户
                RESULT.remove(u)
                self.status["code"], self.status["msg"] = 0, "Success: delete '{}' success.".format(index)
                return self.status
        # 用户不存在的情况
        else:
                self.status["code"], self.status["msg"] = 1, "Error: user '{}' don't exist, u needn't to delete.".format(index)
                return self.status

    # 通过id更新数据列表
    def update(self, data_list):
        """
        update user_name set age = 18
        :param data_list: type is list --> ["username", "set", "field_name", "=", "value"]
        :return: {}
        """
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status

        # list -> [(index, item), (index, item), ...]
        fields_info = list(enumerate(FIELDS))
        for u in RESULT:
            if data_list[0] == u[0]:
                # 获取需要更新的索引位置
                u_index = RESULT.index(u)
                index = [field_info[0] for field_info in fields_info if data_list[2] == field_info[1]][0]

                # 更新操作
                RESULT[u_index][index] = data_list[4]
                self.status["code"] = 0
                self.status["msg"] = "Success: update '{}' success,change {}'s value to '{}'".format(
                        data_list[0], data_list[2], data_list[4])
                return self.status
        else:
            self.status["code"], self.status["msg"] = 0, \
                "Fail: don't find any record which name is '{}'.".format(data_list[0])
            return self.status

    # 可通过用户名（精确）查找， 切片（范围）查找
    def find(self, *args):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，u can only choice add operation."
            return self.status
        elif len(args) < 1:
            self.status["code"], self.status["msg"] = 1, "Error:  takes exactly 1 argument (0 given)."
            return self.status

        # 范围查询
        user_lists = []     # 查询的结果列表
        if len(args) >= 2:
            start, stop = args
            if int(start) > len(RESULT) - 1:
                self.status["code"], self.status["msg"] = 1, "Error: Index exceeds list length"
                return self.status
            user_lists.extend(RESULT[int(start):int(stop)])
        # 精确索引查找
        else:
            username = args[0]
            for k, u in enumerate(RESULT):
                user_info = [i for i in u if username == u[0]]
                if user_info:
                    user_lists.append(user_info)

        # 处理查找的结果为空的情况
        if not user_lists:
            self.status["code"], self.status["msg"] = 4, "You don't get anything."
        else:
            self.status["code"], self.status["msg"] = 0, user_lists

        return self.status

    # 列出所有数据
    def list(self):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["code"], self.status["msg"] = 4, "Data is empty，add a new user,please."
            return self.status

        self.status["code"], self.status["msg"] = 0, RESULT
        return self.status


# 根据用户名查询一条用户记录
def get_one(name):
    if not RESULT:
        return

    for user_info in RESULT:
        if name == user_info[0]:
            return user_info


