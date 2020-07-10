"""
猜数游戏
1、猜一个100以内的整数
2、6次机会
3、每次猜时，猜对了，大了，小了
提示：生成随机数的方法
import random
random.randint(0,100)
"""
# import random
# ran = random.randint(0,100)
# guess = 0
# x = 0
# while guess != ran:
#     while x < 6:
#         x = x + 1
#         num = input("请输入数字:")
#         guess = int(num)
#         if guess > ran:
#             print("猜大了")
#         else:
#             print("猜小了")
#     if x == 6:
#         print("6次机会已猜完，over")
#         break
#
# if guess == ran:
#     print("猜对了！")

import random
num = random.randint(0,100)
count = 0
while count <= 5:
    count += 1
    nums = int(input("请输入数字："))
    if nums > num:
        print("猜大了")
    elif nums < num:
        print("猜小了")
    elif nums == num:
        print("猜对了")
print("正确的数是{}".format(num))