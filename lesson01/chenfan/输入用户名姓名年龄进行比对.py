#!/bin/env python3
# -*- coding:utf-8 -*-

"""
输入用户名，性别，年龄 进行比对
author: chenfan
version:0.1
date:2019-04-29
"""

name = input("Pls enter your name: ")
age = int(input("Pls enter your age: "))
sex = input("Pls enter your sex<male/girl>: ")
if age > 18 and sex == "girl":
    print("你好 {} 女士，你的年龄高于18岁，可以进入".format(name))
elif age > 18 and sex == "male":
    print("你好{} 先生，你该出去交际了".format(name))
else:
    print("你好 {} ,你的年龄低于18岁，回家写作业去".format(name))