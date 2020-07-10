import random      # 导入随机数模块

print('\n——————猜数字游戏——————\n')
random = random.randint(1, 100)  # 生成1到10之间的随机数
print("请输入1~100之间的任意一个数：")
count = 0;
while count < 6:
    guess = input()  # 获取输入的数字
    if int(guess)!=0 and int(guess) < random:  # 若猜测的数字小于基准数，则提示用户输入的数太小，并让用户重新输入
        print('太小，请重新输入：')
    if int(guess)!=0 and int(guess) > random:  # 若猜测的数字大于基准数，则提示用户输入的数太大，并让用户重新输入
        print('太大，请重新输入：')
    if int(guess) == random:  # 输入的数字与随机数相同时，用户猜对数字，获得成功，游戏结束
        print('恭喜你，你赢了，猜中的数字是：', random)
        print('\n———————游戏结束———————')
        count = 6
    else:
        count += 1
        print("请重新输入", 6 - count, "times")
