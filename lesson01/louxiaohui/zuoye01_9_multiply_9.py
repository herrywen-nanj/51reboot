#!/usr/bin/env python
# -*- coding: utf-8 -*-
# desc: 9 multiply by 9
# method 1
num = 9
for i in range(1,num+1):
    for j in range(1,i+1):
        product = j * i
        # {:<3} 左对齐，乘积占3个占位符
        print ("{}*{}={:<3} " .format(j, i, product), end='')
    # 第二层循环结束时换行，即乘数与被乘数相等时
    print (end='\n')

# method 2
m1 = 1
t_value = 9
while m1 <= t_value:
    m2 = 1
    while m2 <= m1:
        # 乘数与被乘数相等时,换行
        if m2 == m1:
            end_str = '\n'
        else:
            end_str = ''
        product = m2 * m1
        # 格式化输出，乘积占3个占位符
        print ("{}*{}={:<3} " .format(m2, m1, product), end=end_str)
        m2 += 1
    m1 += 1
