#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/112 15:20
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 猜数游戏
# @Software: PyCharm

import random
sum = 0
guess = random.randint(0,100)
while sum <= 6:
    input_number = int(input('请输入一个0-100的整数:'))
    if input_number > guess:
        print('你猜的数字比实际的大','输入的数字和实际的数字分别是',input_number,guess)
        sum += 1
    elif input_number < guess:
        print('你猜的数字比实际的小','输入的数字和实际的数字分别是',input_number,guess)
        sum += 1
    else:
        print('你猜对了')
        exit()