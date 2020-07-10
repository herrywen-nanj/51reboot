import random

num = random.randint(0, 100)

# n = int(input("猜数字:"))
#print(num)

count = 0
while count < 5:
    count +=1
    n = int(input("猜数字:"))

    if n == num:
        print("猜对了")
        break
    elif n > num:
        print("猜大了")
    elif n < num:
        print("猜小了")
