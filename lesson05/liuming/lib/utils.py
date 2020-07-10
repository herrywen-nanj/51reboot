#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         utils.py
# Description:  other public function
# Author:       Aaron
# Date:         2019/6/24
# -------------------------------------------------------------------------------
import logging
import configparser
from prettytable import PrettyTable
from settings import LOG_FILE_PATH, PASSWD_FILE_PATH


# read and parse the configuration of storing DB info
def read_config(filename, section, key=None):
    """
    :param filename: file path which store DB info.
    :param section:
    :param key:
    :return:
    """
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(filename, encoding="utf-8")

    if not config.sections():
        return "configuration is empty.", False

    if key:
        print("section --> ", config.has_section(section))
        if config.has_section(section) and config.has_option(section, key):
            return dict(config.get(section, key)), True
        else:
            return "", False
    return dict(config[section]), True


# Parse and write the configuration of storing DB info
def write_conf(file_name, section):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(file_name, encoding='utf-8')

    # add node(section)
    if not config.has_section(section):
        config.add_section(section)

    # add key and value(option)
    if not config.options(section):
        config.set(section, 'aaron', "1")
        config.set(section, 'monkey', "1")
        config.write(open(file_name, 'w'))


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
def format_print(rows):
    """
    :param rows: [{user_name_1: {field_name_1: value, }}, {user_name_2: {field_name_1: value, }}]
    :return:
    """
    tb = PrettyTable()
    if isinstance(rows, dict):
        tb.field_names = rows.keys()
        tb.add_row(rows.values())
    else:
        tb.field_names = rows[0].keys()
        for i_dict in rows:
            data = [i_dict[k] for k in i_dict.keys()]
            tb.add_row(data)

    return tb
    # print("\033[32m{}\n\033[0m".format(tb))


# Color and record logs based on status codes
def msg_operation(status_dict: dict):
    msg, data = status_dict.get("msg", None), status_dict.get("data", None)

    # 格式化输出
    if status_dict["status"] == 0:
        # 记录日志
        log.info(msg)

        print("\033[32m{}\033[0m".format(msg))
        if data:
            res = format_print(rows=data)
            print("\033[32m{}\n\033[0m".format(res))
    elif status_dict["status"] == 4:
        print("\033[34m{}\033[0m\n".format(msg))
        if data:
            res = format_print(rows=data)
            print("\033[32m{}\n\033[0m".format(res))
    else:
        print("\033[31m{}\033[0m\n".format(msg))


# Paging function
def page(data, page_number, page_size):
    status = {
        "status": 0,
        "msg": "",
        "data": "",
    }

    if not data:
        status["status"], status["msg"] = 4, "Data is empty，u can only choice add operation."
        return status

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


log = create_logs()


if __name__ == "__main__":
    pass

