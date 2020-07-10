import random

ans_number = random.randint(0, 100)
times = 1

while times <= 6:
    left = 6 - times
    times += 1
    number = int(input("请输入一个数字："))
    if number > ans_number:
        print('数字太大了,重新猜一次吧,你还有{}次机会.'.format(left))

    elif number < ans_number:
        print('数字太小了,重新猜一次吧,你还有{}次机会.'.format(left))
    else:
        print("恭喜你,猜对了!!,数字是{}".format(ans_number))
        break
if left == 0:
    print("你已经使用完了6次机会了,游戏结束了!")



