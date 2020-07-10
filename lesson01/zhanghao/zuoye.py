'''
需求：
打印乘法口诀
'''
# Version1
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %2d" % (j,i,j*i),end='  ')
    print('')

# Version2
i = 1
while i < 10:
    for j in range(1,i+1):
        print("%d * %d = %2d" % (j,i,j*i),end='  ')
    print('')
    i = i + 1

'''
需求：
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了
'''

import random
secret = random.randint(0,100)
n = 0
while True :
    n = n + 1
    temp = input("请输入第{}次你猜的数字：".format(n))
    guess = int(temp)
    if guess > secret:
        print("第{}次猜大了".format(n))
    elif guess < secret:
        print("第{}次猜小了".format(n))
    else:
        print("第{}次猜对了".format(n))
    if n == 6:
        print("游戏结束")
        break
