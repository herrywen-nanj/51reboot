#-*- coding:utf-8 -*-
from subprocess import Popen, PIPE
import re
import platform
import psutil
import datetime
import ipaddress


"""
主机信息搜集
hostname、private_ip, public_ip, cpu、mem、disk、manufacturer、real_datetime、os
"""

# 获取时间
def getDatetime():
    return datetime.datetime.now()

# 获取磁盘
def getDisk():
    d = psutil.disk_usage('/')
    disk = round(d.total / 1024 / 1024 / 1024)
    return "{}G".format(disk)

# 获取内存
def getMem():
    m = psutil.virtual_memory()
    mem = round(m.total / 1024 / 1024 / 1024)
    return "{}G".format(mem)

# 获取制造商
def getManufacturer():
    p = Popen('dmidecode -s system-manufacturer', stdout=PIPE, shell=True)
    manufacturer = p.stdout.read().decode(encoding='utf-8').strip()
    return manufacturer

# 获取CPU核数
def getCPU():
    count = psutil.cpu_count()
    return count


# 获取系统版本
def getOS():
    o = platform.dist()
    os  = '_'.join(o)
    return os

# 获取主机名
def getHostname():
    p = Popen('hostname', stdout=PIPE, shell=True)
    hostname = p.stdout.read().decode(encoding='utf-8').strip()
    return hostname

# 获取IP地址
def getIP():
    IP_list = []
    p = Popen('ifconfig', stdout=PIPE, shell=True)
    data = p.stdout.read().decode(encoding='utf-8').split('\n\n')
    for lines in data:
        if lines.startswith('lo'):
            continue
        if lines:
            regex = r'inet (.*) \ netmask'
            ip = re.findall(regex, lines)
            IP_list.append(ip[0])
    return IP_list

# 使用psutil获取IP地址
def get_IP():
    IP_list = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                IP_list.append(item[1])
    return IP_list



# 检测分类
def testIP(ip):
    if ipaddress.ip_address(ip).is_private:
        return True

# IP分类
def sortIP(ip_list, Dict):
    private=0
    public=0
    for ip in ip_list:
        if testIP(ip):
            Dict['private_ip{}'.format(private)] = ip
            private += 1
        else:
            Dict['public_ip{}'.format(public)] = ip
            public += 1


def main():
    HostInfo = {}
    # sortIP(getIP(), HostInfo)
    sortIP(get_IP(), HostInfo)
    HostInfo['hostname'] = getHostname()
    HostInfo['cpu'] = getCPU()
    HostInfo['mem'] = getMem()
    HostInfo['disk'] = getDisk()
    HostInfo['manufacturer'] = getManufacturer()
    HostInfo['real_datetime'] = getDatetime()
    HostInfo['os'] = getOS()

    for k in HostInfo.keys():
        print("{}: {}".format(k, HostInfo[k]))


if __name__ == '__main__':
    main()