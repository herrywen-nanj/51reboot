#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 17:51
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : agent.py
# @Software: PyCharm

import logging,time,os
from db import connect
from log_utils import Logs
logger = logging.getLogger(__name__)

def execute_cmd(cmd):
    _fh = os.popen(cmd)
    _cxt = _fh.read()
    _fh.close()
    return _cxt

#获取IP
def get_ip():
    _cmd = "ifconfig eth0|grep inet|head -1|awk -F':' '{print $2}'|awk '{print $1}'"
    # _cmd =  "curl members.3322.org/dyndns/getip"
    _cxt = execute_cmd(_cmd)
    return str(_cxt.split(':')[-1]).strip()

#获取CPU使用率
def collect_cpu():
    _cmd = "top -b -n 1|grep Cpu|awk '{print $2}'|cut -f 1 -d '.'"
    _cxt = execute_cmd(_cmd)
    return float(_cxt.split('%')[0])

#获取主机名
def collect_hostname():
    _hostname = "cat /etc/sysconfig/network|grep HOSTNAME|awk -F'=' '{print $2}'"
    _host = execute_cmd(_hostname)
    return (_host.split()[0])

#获取内存使用率
def collect_ram():
    _free = "free -m | sed -n '2p' | awk '{print $3}'"
    _total = "free -m | sed -n '2p' | awk '{print $2}'"
    _cmd_free = execute_cmd(_free)
    _cmd_total = execute_cmd(_total)
    return 100 * float(_cmd_free) / float(_cmd_total)

log = Logs()
def collect():
    _rt = {}
    _rt['ip'] = get_ip()
    _rt['cpu'] = collect_cpu()
    _rt['ram'] = collect_ram()
    _rt['hostname'] = collect_hostname()
    _rt['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
    real_time = time.strftime('%Y-%m-%d %H:%M:%S')
    data = (get_ip(),collect_cpu(),collect_ram(),collect_hostname(),real_time)
    conn = connect()
    cur = conn.cursor()
    sql_insert = "insert into server_information(ip,cpu_tilization,ram,hostname,real_datetime) values (%s,%s,%s,%s,%s);"
    try:
       cur.execute(sql_insert,data)
       log.info('服务器信息增加成功{}'.format(data))
       conn.commit()
    except Exception as e:
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    _msg = collect()