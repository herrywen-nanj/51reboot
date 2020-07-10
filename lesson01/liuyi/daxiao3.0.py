import random
number=random.randint(1,100)
running=True
guess=int(input(" 请输入（1-100）的数字enter an integer:"))
s = 0
s1 = 6
while running:
    if guess == number :
        print("猜了",s,"次")
        print("猜对了")
        running=False
    elif s1 == 0:
        print("猜了", s, "次")
        print("游戏结束")
        running = False
    elif guess < number:
        print("小了")
        s=s+1
        s1 = s1-1
        guess = int(input("enter an integer:"))
    else:
        print("大了")
        guess = int(input("enter an integer:"))
        s=s+1
        s1= s1 -1

