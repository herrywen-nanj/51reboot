#!/usr/bin/python
# -*- coding: UTF-8 -*-
#一共六次机会，猜随机数，猜对即刻退出。
import random
result = random.randint(0,100)
count = 1
while count <= 6:
    your_answer = int(input("please input your answer:"))
    count += 1
    if result == your_answer:
        print("恭喜你猜对了")
        break
    elif result > your_answer:
        print("你猜小了!请继续努力")
    else:
        print("你猜大了点！请继续努力")
else:
    print("你的机会使用完毕，请重新运行!")
