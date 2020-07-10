#!/bin/bin/env python
# -*- coding: utf-8 -*-
# __auhtor__: will_xue
# Date: 2019-05-17
# Email: xuegqcto@aliyun.com

"""
1. 猜一个100以内的整数
2. 6次机会
3. 每次猜时，猜对了，大了，小了
"""
import random
num = random.randint(0, 100)

count = 1
while True:
    txt = input('请输入一个整数，最多连续猜6次，请珍惜机会 :')
    txt_int = int(txt)

    if count < 6:
        if txt_int < num:
            print('猜小了，现在是第{}次，当前随机数是：{}, '.format(count, num))
        elif txt_int == num:
            print('猜对了，现在是第{}次，当前随机数是:{}'.format(count, num))
            break
        else:
            print('猜大了，现在是第{}次，当前随机数是：{}, '.format(count, num))
    else:
        print('太笨了，6次机会已经用完！')
        break

    count += 1