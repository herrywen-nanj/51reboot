import random
c = 1
b = random.randint(0, 100)
while c < 7:
    a = int(input('请输入一个0到100的数字,有{}次机会: '.format(7 - c)))
    c = c + 1
    if a > 100 or a < 0:
        print('请按要求输入0-100的数字')
    elif a > b:
        print('猜大了,猜小点试试')
    elif a < b:
        print('猜小了,猜大点试试')
    elif a == b:
        print('真棒,猜对了')
        break
