import random
randnum = random.randint(0,100)
count = 1
while count <= 6:
    num = int(input("请输入你要猜测的1-100间的数字："))
    if num > randnum:
        print("大了")
    elif num < randnum:
        print("小了")
    else:
        print("猜对了")
        break
    count += 1



