# -*- coding: utf-8 -*-
# @Time    : 2019-05-10 23:49
# @Author  : Joe
# @Site    : 
# @File    : 6sum.py
# @Software: PyCharm
# @function: xxxxx

sums = 0
times = 1
while True:
    number = input("输入第%s数字：" % times)
    if number.isdigit():
        times += 1
        sums += int(number)
    else:
        print("输入的不是数字请重新输入!")
    if times > 6:
        break
print("6个数的总和：%s" % sums)
