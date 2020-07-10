import random


"""
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了

提示：生成随机数的方法
import random
random.randint(0, 100)
"""

rand = random.randint(0,100)
count = 1
while True:
    if count > 6:
        print("6次机会已经用完 结束")
        break
    num = int(input("Pelase Input Num: "))

    if num > rand:
        print("大了")
    elif num < rand:
        print("小了")
    elif num == rand:
        print("猜对了")
        print("游戏结束!")
        break
    #每猜一次 加1
    count += 1