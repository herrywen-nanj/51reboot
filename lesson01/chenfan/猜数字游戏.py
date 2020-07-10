#!/bin/env python3
# -*- coding:utf-8 -*-

"""
猜数字游戏
猜一个100以内的随机数，6次机会
author: chenfan
version: 0.1
date: 2019-04-29
"""

import random
num = random.randint(0, 100)
count = 0
while count <= 5:
    count += 1
    nums = int(input("Pls enter a nums: "))
    if nums == num: print("Bingo you are right")
    elif nums > num: print("Your input num {} is too big".format(nums))
    else: print("Your input num {} is too little".format(nums))

print("U R loser,正确的数字是:%d" % num)
