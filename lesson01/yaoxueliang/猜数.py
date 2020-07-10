import random
rand = random.randint(0, 100)

print('随机数字为:', rand)

guess = int(input('请输入一个1-100之间的数字（猜对有奖励哦）：'))

i = 1

while i <= 6:

    i += 1


    if 100 > guess > rand:
        print('大了大了，再来')

    elif  guess >= 1 and guess < rand:
        print('小了小了，再来')

    elif guess == rand:
        print()
        print('猜对啦，恭喜！给你一个大嘴巴子！啪！')
        exit()

    else:
        print()
        print('你猜的数字超过范围了，请重来')

    guess = int(input('请输入一个1-100之间的数字（猜对有奖励哦）：'))

print()
print('你太笨啦，这都猜不到，去死吧，突突突！')

