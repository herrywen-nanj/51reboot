#!/usr/bin/python
# -*- coding: UTF-8 -*-

init = 1
sum = 0
max_num = 0

while True:
    # 循环6次
    if init < 7:
        str = input(('请输入第{}个数字：').format(init))
        # 当前数字
        current_num = int(str)
        # 总和等于本次+上次数字的和
        sum = current_num + sum
        init = init + 1
        # 如果当前值大于最大值
        if current_num > max_num:
            max_num = current_num
        else:
            max_num = max_num
    else:
        break

print(('总和为：{},最大值为：{}').format(sum,max_num))

