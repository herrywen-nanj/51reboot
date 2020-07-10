#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-06-15
# Filename: utils.py
# Describe:
#*******************************************

import csv
import json
from logzero import logger

def save_audit_log(**kwargs):
    '''保存用户操作记录'''

    try:
        audit_log_file = kwargs.get('audit_log_file', 'user_oper_audit.log')
        oper_audit_msg = kwargs.get('oper_audit_msg')

        with open(audit_log_file, 'a') as f:
            f.write(oper_audit_msg + '\n')
            #logger.info('user actions have been successfully recorded.')

    except Exception as e:
            logger.info('wirte error',e)


def save_data_to_csv(**kwargs):
    '''将数据写入csv文件'''

    out_data = {}

    try:
        csv_file = kwargs.get('csv_file')#, 'default.csv')
        column_name   = kwargs.get('column_name', [])
        userdata = kwargs.get('userlist')

        with open(csv_file, 'w') as f:
            fhandler = csv.DictWriter(f, column_name)
            fhandler.writeheader()
            fhandler.writerows(userdata)

        out_data.update({
            "status": 0,
            "msg": "Success",
            "data": True
        })

        return json.dumps(out_data)

    except Exception as e:
        logger.error('write error', e)
        out_data.update({
            "status": 0,
            "msg": "Success",
            "data": True
        })

        return json.dumps(out_data)

def read_data_in_file(**kwargs):
    '''读取文件的数据'''

    out_data = {}

    try:
        filename = kwargs.get('filename')
        with open(filename, 'r') as f:
            userdata = f.readlines()

        out_data.update({
            "status": 0,
            "msg": "Success",
            "data": userdata
        })

        return json.dumps(out_data)

    except Exception as e:
        out_data.update({
            "status": 1,
            "msg": "Read user data error",
            "data": "nli"
        })

        return json.dumps(out_data)

def write_data_to_file(**kwargs):
    '''写数据到文件中'''

    out_data = {}

    try:
        filename = kwargs.get('filename')
        userdata = kwargs.get('userdata')

        with open(filename, 'a+') as f:
            for data in userdata:
                f.write(json.dumps(data)+'\n')

        out_data.update({
            "status": 0,
            "msg": "Success",
            "data": True
        })

        return json.dumps(out_data)

    except Exception as e:
        out_data.update({
            "status": 1,
            "msg": "data write error",
            "data": False
        })

        return  json.dumps(out_data)
