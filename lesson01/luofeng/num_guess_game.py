#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-05-18
# Filename: num_guess_game.py
# Describe:
#*******************************************

import random

# 猜字的总次数
count_total = 6

# 游戏开始
for count in range(0, 6):
    count_total = count_total - 1

    # 谜底， 随机数，默认 int 类型
    riddle_num = random.randint(0, 100)

    guess_num = int(input('请输入一个100以内的数字: '))
    if guess_num > 100:
        print("\033[0m数字不能大于100，剩余 {} 次机会，请重新输入\033[0m".format(count_total))
        continue

    if guess_num == riddle_num:
        print("\033[32m真厉害，{} 次就猜中了，佩服佩服\033[0m".format(count))

    elif guess_num > riddle_num:
        print("\033[31m抱歉，猜大了，还有 {} 次机会，加油 !!!\033[0m".format(count_total))

    else:
        print("\033[31m抱歉，猜小了，还有 {} 次机会，加油 !!!\033[0m".format(count_total))

    # 判断用户剩余次数
    if not count_total:
        msg = '''\033[33m非常抱歉，猜字游戏结束, 英雄请重新来过 !!!\033[0m'''
        print(msg)
