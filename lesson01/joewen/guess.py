# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 23:39
# @Author  : Joe
# @Site    : 
# @File    : guess.py
# @Software: PyCharm
# @function: xxxxx


import random

times = 1
while times <= 6:
    number = int(input("times:%s input number:" % times))
    gennumber = random.randint(0, 100)
    print("生成数字: %s" % gennumber)
    if number == gennumber:
        print("猜对了")
    elif number > gennumber:
        print("大了")
    else:
        print("小了")
    times += 1
