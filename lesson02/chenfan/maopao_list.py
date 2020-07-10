#!/bin/env python3
# -*- coding:utf-8 -*-
# 没有调试

"""
冒泡排序
"""
rlist = [3, 7, 2, 5, 20, 11]

for j in range(len(rlist)):
    for i in range(j, len(rlist)):
        if rlist[j] > rlist[i]:
            rlist[j], rlist[i] = rlist[i], rlist[j]

	print(rlist)
