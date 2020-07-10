# -*- coding:utf-8 -*-
# author: lyl

import random

random_number = random.randint(0, 100)


for i in range(6):
    # 检测用户输入内容
    try:
        number = int(input("你猜是多少: "))
    except ValueError as e:
        print("输入有误，错误详情: {}".format(e))
        break
    if random_number == number:
        print("猜对了")
        break
    elif number > random_number:
        print("猜大了")
    else:
        print("猜小了")
