import random


def multiplication_table():
    """
    99乘法表
    :return: None
    """
    for i in range(1, 10):
        for f in range(1, 10):
            if f <= i:
                print("%s*%s=%s" % (i, f, i * f), end=" ")
        print(end="\n")


def guess_number():
    """
    猜数字
    :return: None
    """
    number = random.randint(0, 100)
    n = 6
    # print(number)
    for i in range(n):
        if n - i - 1 > 0:
            message = "您还有%s次机会" % (n - i - 1)
        else:
            message = "没有机会了,game over"
        g_number = input("输入你要猜的数数字:")
        if g_number.isdigit():
            if int(g_number) > number:
                print("大了," + message)
            elif int(g_number) < number:
                print("小了，" + message)
            else:
                print("你猜对了")
                break
        else:
            print("请输入数字," + message)


if __name__ == '__main__':
    print("--" * 10, "99乘法表", "--" * 10)
    multiplication_table()
    print("--" * 10, "猜数字", "--" * 10)
    guess_number()
