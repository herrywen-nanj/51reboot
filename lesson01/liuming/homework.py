#!/usr/bin/env python
# -*-encoding:utf-8-*-
# -------------------------------------------------------------------------------
# Name:         homework.py
# Description:  玩一下
# Author:       Aaron
# Date:         2019/5/13
# -------------------------------------------------------------------------------

import random


def nine_nine_multiplication():
    """
    俩个循环一个控制列数，一个控制行数

    循环1-9赋值给 second
        循环1, second+1, 赋值给first
            打印print("first x second=product", end="")
        print()
    :return: nine-nine multiplication
    """
    for second in range(1, 10):
        for first in range(1, second+1):
            print("{}x{}={:<4}  ".format(first, second, first*second), end="")
        print()


def guess_number():
    """
    random.randint(0, 100)生成一个一百以内的数，赋值给random_number
    设置一个最大尝试次数，赋值给max_try
    while max_try:
        input提示用户输入数字
        猜中，恭喜并退出循环
        猜错，提示大了或小了，并减少一次尝试次数
        print打印剩余的尝试次数
    """
    random_number = random.randint(0, 100)
    # print(random_number)
    max_try = 6
    print("\033[36m【Are you ready?】\n【Game Start】\033[0m")
    while max_try:
        try:
            user_input = int(input("Please input number what you think is the most probable >>: "))
            if user_input == random_number:
                print("\033[36mCongratulations, you are right\033[0m")
                break
            elif user_input < random_number:
                print("\033[31mError, the number of you entered is too small.\033[0m")
            else:
                print("\033[31mError, the number of you entered is too big.\033[0m")

        except ValueError:
            print("\033[31mError,you entered isn't a number.\033[0m")

        max_try -= 1
        word = "chances" if max_try > 1 else "chance"
        print("\033[33mYou only have {} {}.\033[0m".format(max_try, word))


if __name__ == "__main__":
    nine_nine_multiplication()
    guess_number()
