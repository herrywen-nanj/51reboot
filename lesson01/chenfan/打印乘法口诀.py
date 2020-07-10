#!/bin/env python3
# -*- coding:utf-8 -*-

"""
打印乘法口诀
author: chenfan
version: 0.2
date: 2019-04-29
"""

for i in range(1,10):
    # print(i)
    for j in range(1, i+1):
        print( "{} * {} = {:<2}".format(j, i, i *j), end="\t")
    print()
