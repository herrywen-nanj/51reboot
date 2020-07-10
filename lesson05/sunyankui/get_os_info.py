# coding: utf-8
from subprocess import Popen, PIPE

def os_cpu_model():
    with open('/proc/cpuinfo') as fd:
        items = fd.readlines()
        for line in items:
            if line.startswith('model name'):
                cpu_model = line.split(':')[1]
                break
        return cpu_model

def os_cpu_num():
    with open('/proc/cpuinfo') as fd:
        items = fd.readlines()
        num = 0
        for line in items:
            if line.startswith('processor'):
                num = num + 1
        return num

def os_mem():
    with open('/proc/meminfo') as fd:
        items = fd.readlines()
        for line in items:
            if line.startswith('MemTotal'):
                mem = line.split()[1] + ' ' + line.split()[2]
        return mem

def os_version():
    with open('/etc/issue') as fd:
        os_ver = fd.read().split('\n')[0]
    return os_ver

def os_hostname():
    with open('/etc/sysconfig/network') as fd:
        data = fd.read().split('\n')[1]
        os_name = data.split('=')[1]
    return os_name

def os_ip():
    p = Popen(['ifconfig'], stdout = PIPE, stderr = PIPE)
    data = p.stdout.read().decode('utf8').split('\n\n')

    for lines in data:
        if lines.startswith('lo'):
            continue
        if lines:
            ip = lines.split('\n')[1].split()[1].split(':')[1]
            break
    return ip


def os_manufacturer():
    p = Popen(['dmidecode --type system'], stdout=PIPE, shell=True)
    manufacturer = p.stdout.read().decode('utf8').split(':')[1].split('.')[0]
    return manufacturer

def os_info():
    host_info = {}
    host_info['ip'] = os_ip()
    host_info['manufacturer'] = os_manufacturer()
    host_info['hostname'] = os_hostname()
    host_info['version'] = os_version()
    host_info['cpu_num'] = os_cpu_num()
    host_info['mem'] = os_mem()
    host_info['cpu_model'] = os_cpu_model()

    for key in host_info.keys():
        print("%s: %s" % (key, host_info[key]))

if __name__ == '__main__':
    msg = os_info()