#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  other public function
# Author:       Aaron
# Date:         2019/7/4
# -------------------------------------------------------------------------------
import logging
import configparser
import pymysql
from prettytable import PrettyTable
from settings import LOG_FILE_PATH, PASSWD_FILE_PATH, DB_CONN_INFO, RESULT, FIELDS, SESSION


# 判断登录状态和执行权限的装饰器
def auth(role: str):
    def decorate(func):
        def wrapper(*func_args, **func_kwargs):
            # 根据传入的role参数是否是admin 和 是否和session中的一致判定是否有执行权限
            # 也可换一种思路实现，维护一个全局字典，id数字对应角色名，根据id大小判定调用权限
            if SESSION["role"] != "admin" and role != SESSION["role"]:
                print("\033[31mu don't have permission to do it!\n\033[0m")
                return None

            func(*func_args, **func_kwargs)
        return wrapper
    return decorate


# Create log directory and write logfile
def create_logs():
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


# Formatted output
def print_table(rows):
    """
    :param rows: {user_name_1: {field_name_1: value, }, user_name_2: {field_name_1: value, }} or
    [{field_name_1: value, }, {field_name_1: value, }, ]
    :return:
    """
    tb = PrettyTable()
    tb.field_names = FIELDS
    # 传入的数据类型为: [{},{}]
    if isinstance(rows, list):
        for d_user_info in rows:
            tb.add_row([d_user_info[k] for k in FIELDS])
    # 传入的数据是RESULT内存中的数据类型
    elif isinstance(list(rows.values())[0], dict):
        for d_user_info in list(rows.values()):
            tb.add_row([d_user_info[k] for k in FIELDS])
    else:
        tb.add_row([rows[k] for k in FIELDS])

    return tb
    # print("\033[32m{}\n\033[0m".format(tb))


# Paging function
def page(page_number, page_size, data=RESULT):
    status = {
        "status": 0,
        "msg": "",
        "data": "",
    }

    if not data:
        status["status"], status["msg"] = 4, "Data is empty，u can only choice add operation."
        return status

    if isinstance(data, dict):
        data = list(data.values())

    start = (page_number - 1) * page_size
    end = page_number * page_size

    # 总数据长度
    data_length = len(data)
    # 计算出最大可以输入的页码
    max_page_number = data_length // page_size + 1 if data_length % page_size else data_length // page_size
    # 输入的页码过大时打印提示，输出最后一页内容
    if page_number > max_page_number:
        # 重新获得当前页码
        page_number = max_page_number
        status["status"] = 4
        status["msg"] = "Page-number too big from you entered,  maximum page-number is {}.\nThe last page:\n".format(max_page_number)
        start = (max_page_number-1) * page_size
        end = max_page_number * page_size

    # 切片操作，获取当前页需要输出的行数
    status["data"] = data[start: end]
    status["msg"] = status["msg"] + "共[{}]页，当前第[{}]页.".format(max_page_number, page_number)
    return status


# Operate password file， write and read
class ConfigOperator(object):
    def __init__(self, file_path, section, s_key=None):
        """
        :param file_path: File path which store DB info.
        :param section:
        :param s_key:
        """
        self.file_path = file_path
        self.section = section
        self.s_key = s_key

    # read and parse the configuration of storing DB info
    def read_config(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(self.file_path, encoding="utf-8")

        if not config.sections():
            return "configuration is empty.", False

        if config.has_section(self.section) and config.has_option(self.section, self.s_key):
            user_info = {"username": self.s_key, "password": config.get(self.section, self.s_key)}
            admin_members = config.get("groups", "admin")
            user_info["role"] = "admin" if user_info["username"] in admin_members else "guest"
            return user_info, True
        else:
            return "User doesn't exist.", False

    # Parse and write the configuration of storing DB info
    def write_conf(self):
        config = configparser.ConfigParser(allow_no_value=True)
        config.read(self.file_path, encoding='utf-8')

        # add node(section)
        if not config.has_section(self.section):
            config.add_section(self.section)
        if not config.has_section("groups"):
            config.add_section("groups")

        # add key and value(option)
        if not config.options(self.section):
            config.set(self.section, 'lm', "1")
            config.set(self.section, 'aaron', "2")
            config.set(self.section, 'monkey', "1")

        if not config.options("groups"):
            config.set("groups", 'admin', "lm, aaron")
            config.set("groups", 'guest', "monkey")

        config.write(open(self.file_path, 'w'))


# Encapsulate related operation about database
class DB(object):
    # Format of function return
    result = {
        "status": 0,
        "msg": "",
        "data": "",
    }

    # Establish a connection to the database
    def _connection(self):
        self.conn = pymysql.connect(
            host=DB_CONN_INFO["host"],
            port=DB_CONN_INFO["port"],
            user=DB_CONN_INFO["user"],
            passwd=DB_CONN_INFO["passwd"],
            db=DB_CONN_INFO["db"],
        )
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def _close_db(self):
        self.cursor.close()
        self.conn.close()

    def insert(self, table_name, data):
        try:
            # 建立连接
            self._connection()

            # 开始准备sql执行
            _fields = ["username", "age", "phone", "email"]
            sql = "insert into {}({}) values({});".format(
                table_name, ",".join(["{}".format(fd) for fd in _fields]), ",".join(["'{}'".format(i) for i in data])
            )
            # print("sql: ", sql)
            res = self.cursor.execute(sql)
            # 插入语句执行失败不会报错, 只能通过返回值(res受影响的行数)判断
            if res:
                self.result["status"], self.result["msg"], self.result["data"] = 0, "insert success.", ""
            else:
                self.result["status"], self.result["msg"], self.result["data"] = 1, "insert fail.", ""
        except Exception as e:
            self.result["status"], self.result["msg"], self.result["data"] = 1, e, ""
        finally:
            # 关闭连接
            self._close_db()
        return self.result

    def delete(self, table_name, data):
        try:
            # 建立连接
            self._connection()
            # print("delete 方法被调用,self.cursor --> {}\tself.conn--> {}".format(self.cursor, self.conn))

            # 开始准备sql执行
            sql = "delete from {} where username='{}';".format(table_name, data)
            # print("sql: ", sql)
            res = self.cursor.execute(sql)
            # print("执行sql返回的结果: ", res)
            self.result["status"], self.result["msg"], self.result["data"] = 0, "delete success.", ""
        except Exception as e:
            self.conn.rollback()
            self.result["status"], self.result["msg"], self.result["data"] = 1, e, ""
        finally:
            # 关闭连接
            self._close_db()
        return self.result

    def select(self, table_name, fields="*"):
        try:
            # 建立连接
            self._connection()
            # print("select 方法被调用,self.cursor --> {}\tself.conn--> {}".format(self.cursor, self.conn))

            # 开始准备sql执行
            if isinstance(fields, list):
                fields = ",".join(fields)

            sql = "select {} from {};".format(fields, table_name)
            # print("sql: ", sql)
            res = self.cursor.execute(sql)
            # print("执行sql返回的结果: ", res)
            rows = self.cursor.fetchall()
            self.result["status"], self.result["msg"], self.result["data"] = 0, "query all of user success.", rows
        except Exception as e:
            self.result["status"], self.result["msg"], self.result["data"] = 1, e, ""
        finally:
            # 关闭连接
            self._close_db()

        return self.result

    def update(self, table_name, data, where):
        try:
            # 建立连接
            self._connection()
            # print("update 方法被调用,self.cursor --> {}\tself.conn--> {}".format(self.cursor, self.conn))

            # 开始准备sql执行
            sql = "update {} set {} where username='{}';".format(
                table_name, ",".join(["{}='{}'".format(k, data[k]) for k in data.keys()]), where)
            # print("sql: ", sql)
            res = self.cursor.execute(sql)
            # print("执行sql返回的结果: ", res)
            self.result["status"], self.result["msg"], self.result["data"] = 0, "update success.", ""
        except Exception as e:
            self.result["status"], self.result["msg"], self.result["data"] = 1, e, ""
        finally:
            # 关闭连接
            self._close_db()

        return self.result

    def get_one(self, table_name, where):
        try:
            # 建立连接
            self._connection()
            # print("get_one 方法被调用,self.cursor --> {}\tself.conn--> {}".format(self.cursor, self.conn))

            # 开始准备sql执行
            sql = "select * from {} where username='{}';".format(table_name, where)
            # print("sql: ", sql)
            res = self.cursor.execute(sql)
            # print("执行sql返回的结果: ", res)
            row = self.cursor.fetchone()
            self.result["status"] = 0 if row else 4
            self.result["msg"], self.result["data"] = "query info of [{}] success.".format(where), row
        except Exception as e:
            self.result["status"], self.result["msg"], self.result["data"] = 1, e, ""
        finally:
            # 关闭连接
            self._close_db()
        return self.result


# Encapsulate related operation about memory data
class MemoryData(object):
    status = {
        "status": 0,  # 状态码反应操作成功或者失败；失败又分为1和4俩种，用于区分不同级别
        "msg": "",
        "data": "",
    }

    def add(self, data_list):
        """
        :param data_list: type is list
        :return: {}
        """
        # 验证用户是否已存在
        res = self.get_one(data_list[0])
        # print("user_info", res)
        if res["status"] == 0:
            self.status["status"], self.status["msg"] = 1, \
                "[FAIL]: user '{}' already exist, add operation is failing.".format(data_list[0])
            return self.status

        # 添加操作
        user_info_d = dict(zip(FIELDS, data_list))
        RESULT[data_list[0]] = user_info_d

        self.status["status"], self.status["msg"], self.status["data"] = 0, "[INFO]: add ok.", user_info_d
        return self.status

    def delete(self, index):
        """
        :param index: string
        :return: {}
        """
        # 处理没有数据的情况
        if not RESULT:
            self.status["status"], self.status["msg"] = 4, "[FAIL]: Data is empty，u can only choice add operation."
            return self.status

        # 删除用户
        is_succ = RESULT.pop(index, None)
        # 用户不存在的情况
        if not is_succ:
            self.status["status"], self.status["msg"] = \
                1, "[ERROR]: user '{}' don't exist, u needn't to delete.".format(index)
        # 删除成功
        else:
            self.status["status"], self.status["msg"] = \
                0, "[Success]: delete '{}' success.".format(index)
        return self.status

    # 通过username为索引更新数据字典
    def update(self, data_list):
        """
        :param data_list: type is list --> ["username", "set", "field_name", "=", "value"]
        :return: {}
        """
        if not RESULT:
            self.status["status"], self.status["msg"], self.status["data"] = \
                4, "[FAIL]: Data is empty，u can only choice add operation.", ""
            return self.status

        username, field_name, value = data_list[0], data_list[2], data_list[4]
        # 处理用户名不存在情况
        if username not in RESULT:
            self.status["status"], self.status["msg"], self.status["data"] = \
                4, "[FAIL]: don't find any record which name is '{}'.".format(username), ""

            return self.status

        # 处理字段输入错误
        if field_name not in FIELDS:
            self.status["status"], self.status["msg"], self.status["data"] = \
                1, "[ERROR]: field '{}' doesn't exist".format(field_name), ""
            return self.status

        # 处理修改用户名字段，但已存在同用户名的情况
        if field_name == FIELDS[0] and value in RESULT:
            self.status["status"], self.status["msg"], self.status["data"] = \
                1, "[ERROR]: user '{}' already exist, can't change {} field to {}".format(
                    username, field_name, username
                ), ""
            return self.status

        # 修改用户名字段
        if field_name == FIELDS[0]:
            temp_dict = RESULT[username]
            temp_dict[field_name] = value
            res = self.delete(username)
            if res["status"] != 0:
                self.status["status"] = 1
                self.status["msg"] = "[ERROR]: update {}'s field [{}] failed."
                return self.status
            RESULT[username] = temp_dict
        # 修改非username字段的数据
        else:
            RESULT[username][field_name] = value

        self.status["status"] = 0
        self.status["msg"] = "[INFO]: update '{}' success,change {}'s value to '{}'".format(
            username, field_name, value)
        self.status["data"] = RESULT[username]
        return self.status

    # 可通过用户名作为关键字查找
    def find(self, username):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["status"], self.status["msg"] = 4, "[FAIL]: Data is empty，u can only choice add operation."
            return self.status

        # 用户名不存在
        if username not in RESULT:
            self.status["status"], self.status["msg"] = 4, \
                "[FAIL]: User '{}' doesn't exist, u need to add first.".format(username)
            return self.status

        # 从字典查找到用户并重新拼接数据结构
        row = RESULT[username]
        self.status["status"] = 0
        self.status["msg"] = "[INFO]: Find success"
        self.status["data"] = row

        return self.status

    # 列出所有数据
    def list(self):
        # 验证数据列表是否不为空
        if not RESULT:
            self.status["status"], self.status["msg"] = 4, "[FAIL]: Data is empty，add a new user,please."
            return self.status

        self.status["status"], self.status["msg"], self.status["data"] = 0, "[INFO]: list all user info", RESULT
        return self.status

    def get_one(self, name):
        """

        :param name: str
        :return: {}
        """
        if not RESULT:
            self.status["status"], self.status["msg"] = 4, "Data is empty，add a new user,please."
            return self.status

        if name in RESULT:
            user_info = RESULT[name]
            self.status["status"], self.status["msg"], self.status["data"] = \
                0, "[INFO]: list info of [{}]".format(name), user_info
        else:
            self.status["status"], self.status["msg"], self.status["data"] = \
                4, "[FAIL]: User '{}' doesn't exist, u need to add first.".format(name), ""
        return self.status


if __name__ == "__main__":
    pass

