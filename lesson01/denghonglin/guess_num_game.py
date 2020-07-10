#!/usr/bin/env python
###############################
# function: Number guessing game
# author: dhl
# date:	2019-05-16
# env: python3
###############################

import random

secret = random.randint(1,10)
count = 0

while count < 6:
    temp = input("猜猜今日幸运数字，请输入（1-100）:")
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("恭喜你猜对，但没有奖励^_^")
            print("总共猜了【{}】次".format(count))
            break
        else:
            if guess > secret:
                print("兄弟，大啦，继续...")
            else:
                print("嘿，小啦，再猜...")
    else:
        print("输入有误，请输入数字.")
    count += 1
print("无聊,Game Over! T_T")
           





