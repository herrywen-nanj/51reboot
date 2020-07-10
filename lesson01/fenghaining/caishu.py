import random
num=random.randint(0,100)
print('随机数为：%s'%num)
for i in range(1,7):
    tmp = int(input('第%s次猜数，请输入:'%i ))
    if tmp <num:
        print('猜小了')
    elif tmp >num:
        print('猜大了')
    else:
        print('猜对了')
        exit()
