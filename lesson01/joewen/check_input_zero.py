# -*- coding: utf-8 -*-
# @Time    : 2019-05-11 00:29
# @Author  : Joe
# @Site    : 
# @File    : check_input_zero.py
# @Software: PyCharm
# @function: xxxxx

total = 0
numbers = input("输入多个数字，以空格隔开:")
my_list = numbers.split(" ")

if str(0) in my_list:
    exit()
else:
    for i in my_list:
        total += int(i)
    maxnumber = max(my_list)
    print("总和：%s" % total)
    print("最大值：%s" % maxnumber)
