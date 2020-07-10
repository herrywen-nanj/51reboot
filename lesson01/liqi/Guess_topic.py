import random
# 随机生成数字
shu = random.randint(0,100)
for x in range(0,6):
    put = int(input('please:'))
    print(shu)
    if put == shu:
        print('猜对了')
        print(shu)
        break
    elif put > shu:
        print('大了')
    else:
        print('小了')
    if x == 5:
        print('猜题结束')
