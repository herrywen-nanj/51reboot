# -*- coding: utf-8 -*-

import random

a = 69

for i in range(6):
    b = random.randint(0,100)
    if b > a:
        print("大了")
    if b < a:
        print("小了")
    if b == a:
        print("对了")


