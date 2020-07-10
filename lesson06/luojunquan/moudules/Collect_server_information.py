#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 17:51
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : agent.py
# @Software: PyCharm

import logging,time,os
from luojunquan.moudules.db import Sql_Util
from luojunquan.utils.log_utils import Logs
import psutil

logger = logging.getLogger(__name__)
log = Logs()
sql_util = Sql_Util()

class Collect_Server_Information(object):

    def execute_cmd(self,cmd):
        _fh = os.popen(cmd)
        _cxt = _fh.read()
        _fh.close()
        return _cxt

    #获取IP
    def get_ip(self):
        # _cmd = "ifconfig eth0|grep inet|head -1|awk -F':' '{print $2}'|awk '{print $1}'"
        # _cmd =  "curl members.3322.org/dyndns/getip"
        '''
        _cmd = "ip a|grep eth0|grep inet|awk '{print $2}'|awk -F'/' '{print $1}'"
        _cxt = self.execute_cmd(_cmd)
        return str(_cxt.split(':')[-1]).strip()
        :return:
        '''
        dic = psutil.net_if_addrs()
        for ad in dic:
            snlist = dic[ad]
            for sn in snlist:
                if sn.family.name in 'AF_INET' and sn.address != '127.0.0.1':
                    return sn.address


                    #获取CPU使用率
    def collect_cpu(self):
        _cmd = "top -b -n 1|grep Cpu|awk '{print $2}'|cut -f 1 -d '.'"
        _cxt = self.execute_cmd(_cmd)
        return float(_cxt.split('%')[0])

    #获取主机名
    def collect_hostname(self):
        _hostname = "cat /etc/sysconfig/network|grep HOSTNAME|awk -F'=' '{print $2}'"
        _host = self.execute_cmd(_hostname)
        return (_host.split()[0])

    #获取内存使用率
    def collect_ram(self):
        _free = "free -m | sed -n '2p' | awk '{print $3}'"
        _total = "free -m | sed -n '2p' | awk '{print $2}'"
        _cmd_free = self.execute_cmd(_free)
        _cmd_total = self.execute_cmd(_total)
        return 100 * float(_cmd_free) / float(_cmd_total)

    def collect(self):
        _rt = {}
        _rt['ip'] = self.get_ip()
        _rt['cpu'] = self.collect_cpu()
        _rt['ram'] = self.collect_ram()
        _rt['hostname'] = self.collect_hostname()
        _rt['time'] = time.strftime('%Y-%m-%d %H:%M:%S')
        real_time = time.strftime('%Y-%m-%d %H:%M:%S')
        data = (self.get_ip(),self.collect_cpu(),self.collect_ram(),self.collect_hostname(),real_time)
        sql_insert = "insert into server_information(ip,cpu_tilization,ram,hostname,real_datetime) values (%s,%s,%s,%s,%s);"
        sql_util.db_insert(sql_insert,data)