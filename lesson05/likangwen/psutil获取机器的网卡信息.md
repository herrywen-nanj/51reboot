

##### 使用psutil来获取机器的IP地址
```
#coding=utf-8
import psutil
#获取网卡名称和其ip地址，不包括回环

netcard_info = []
info = psutil.net_if_addrs()
for k,v in info.items():
    for item in v:
        if item[0] == 2 and not item[1]=='127.0.0.1':
            print(k, item[1])
```

上面比较有疑问的就是item[0] == 2这个判断了。因为在ipython直接查看info的话，是一个字典对象。而且根本就没有等于2的元素。
```
In [7]: print(info)                                                                                                        
{'lo': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='00:00:00:00:00:00', netmask=None, broadcast=None, ptp=None)], 'eth0': [snicaddr(family=<AddressFamily.AF_INET: 2>, address='172.16.0.15', netmask='255.255.240.0', broadcast='172.16.15.255', ptp=None), snicaddr(family=<AddressFamily.AF_PACKET: 17>, address='52:54:00:a7:ab:a0', netmask=None, broadcast='ff:ff:ff:ff:ff:ff', ptp=None)]}
```

如果使用dumps把字典转换成json格式的话，那么上面的判断就好理解了
```
In [1]: import psutil                                                                                                      

In [2]: from json import dumps                                                                                             

In [3]: info = psutil.net_if_addrs()                                                                                       

In [4]: print(dumps(info, indent=4))                                                                                       
{
    "lo": [
        [
            2,
            "127.0.0.1",
            "255.0.0.0",
            null,
            null
        ],
        [
            17,
            "00:00:00:00:00:00",
            null,
            null,
            null
        ]
    ],
    "eth0": [
        [
            2,
            "172.16.0.15",
            "255.255.240.0",
            "172.16.15.255",
            null
        ],
        [
            17,
            "52:54:00:a7:ab:a0",
            null,
            "ff:ff:ff:ff:ff:ff",
            null
        ]
    ]
}
```