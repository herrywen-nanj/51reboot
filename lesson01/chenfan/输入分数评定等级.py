#!/bin/env python3
# -*- coding:utf-8 -*-
#
"""
输入分数，评定等级
author: chenfan
version: 0.1
data: 2019-04-29
"""

score = int(input("Pls enter your score: "))
if score >= 90:
    print("Your score is {} and grate is A".format(score))
elif  80 <= score < 90:
    print("Your score is {} and grate is B".format(score))
elif 70 <= score < 80:
    print("Your score is {} and grate is C".format(score))
elif 60 <= score < 70:
    print("Your score is {} and grate is D".format(score))
else:
    print("Your score is {}, and grate is E".format(score))



