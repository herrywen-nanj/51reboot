# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 21:48
# @Author  : Joe
# @Site    : 
# @File    : 99乘法.py
# @Software: PyCharm
# @function: xxxxx


for i in range(1, 10):
    print("")
    for j in range(1, i+1):
        # print(j)
        print("%sx%s=%s" % (j, i, i*j), end=' ')
