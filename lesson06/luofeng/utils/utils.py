#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-07-06
# Filename: utils.py
# Describe:
#*******************************************

def save_data_to_csv(**kwargs):
    '''将数据写入csv文件'''

    out_data = {}

    try:
        csv_file = kwargs.get('csv_file', 'default.csv')
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
