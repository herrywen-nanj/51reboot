

import random


randomNum = random.randint(0, 100)
int_cnt = 1
max_cnt = 6

while True:
    if int_cnt > max_cnt:
        print("游戏结束, 随机数为{}.".format(randomNum))
        break

    num = input("Please input your num: ")
    num_int = int(num)
    if num_int > randomNum:
        print("猜大了")
    elif num_int < randomNum:
        print("猜小了")
    else:
        print("猜对了, 随机数为{}.".format(randomNum))
        break
    int_cnt += 1
