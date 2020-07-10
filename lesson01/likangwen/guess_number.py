import random

num = random.randint(0, 100)
guess_num = int(input("Please input a number start guess number game:"))
n = 1
while n < 6:
    n += 1
    if guess_num > num:
        guess_num = int(input("输入数值比随机数值大，继续输入:"))
    elif guess_num < num:
        guess_num = int(input("输入数值比随机数值小，继续输入:"))
    else:
        print("恭喜你，输入对了，猜数数字是{}".format(num))
        break

if n == 6:
    print("很遗憾次数已用完")
