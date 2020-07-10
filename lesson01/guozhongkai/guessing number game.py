#!/usr/local/python36/bin/python3.6
#猜一个100以内的整数，6次机会，每次猜时，猜对了，大了，小了
#方法一
import random # 导入random（随机数）模块
i = 1
while i <= 6:
    num = input('请输入一个100以内的整数：')
    if int(num) == random.randint(0, 100): # 生成的随机数大于等于0且小于等于100
        print('猜对了')
    elif int(num) > random.randint(0, 100):
        print("猜大了")
    else:
        print('猜小了')
    i += 1 # i = i + 1

print()
print('game over')

'''
# 方法二
s = range(1, 7) # s = "123456"

for x in s:
    num = input('请输入一个100以内的整数：')
    if int(num) == random.randint(0, 100):
        print('猜对了')
    elif int(num) > random.randint(0, 100):
        print('猜大了')
    else:
        print('猜小了')

print()
print('game over')
'''
