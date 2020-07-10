#!/bin/env python3
# -*- coding:utf-8 -*-

"""
计算1到100的和
author: chenfan
version: 0.1
date: 2019-04-29
"""

count = 0
nums = 0
num = 0
while num <= 99:
    num += 1
    count += 1
    nums += num
    if count == 100:
        break

print(nums)
