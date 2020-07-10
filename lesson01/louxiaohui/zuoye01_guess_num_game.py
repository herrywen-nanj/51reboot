#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

print ("*****************************************************************")
print ("欢迎来玩猜数字游戏，请输入一个100以内的整数，你共有6次机会。")
print ("*****************************************************************")
count = 6
chance_num = 1
#num = 56
num = random.randint(0, 100)


while chance_num <= 6:
    num_in = int(input("请输入第{}个数字：" .format(chance_num)))
    if num_in == num:
        print ("恭喜你，猜对了,你真厉害")
        break
    elif num_in > num:
        print ("很遗憾，猜大了")
    else:
        print ("很遗憾，猜小了")
    if chance_num == 6:
        print ("很遗憾，你猜了6次也没猜对，游戏结束")
    chance_num += 1
print ("正确数字是{}" .format(num))
