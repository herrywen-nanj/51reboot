import random

print("====== 猜字游戏 ======")
ran = random.randint(0,100)
for i in range(6):
    input1 = int(input("请输入您猜的数字: "))
    if ran == input1:
        print("恭喜您，猜对了")
        break
    if input1 < ran:
        print("小了")
    elif input1 > ran:
        print("大了")
    if i == 5:
        print("很遗憾，您没有机会了！")

