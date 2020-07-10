#encoding=utf8
import random
#生成100以内随机数，负值给变量random_num，设定计数器get_num
random_num = random.randint(0,100)
get_num = 0

#for 循环range方法限制6次
for i in range(6):
    #打印随机数值，方便调试
    print(random_num)
    num = int(input('请输入猜的数字: '))
    #随机数与输入数字比较，猜对直接退出，猜错继续循环计数器+1，并做提示
    if random_num == num:
        print('猜对了,程序退出')
        exit()
    elif random_num > num:
        print('猜小了')
        get_num += 1
    else:
        print('猜大了')
        get_num += 1
    print('当前已猜%s次，6次退出'%(get_num))
