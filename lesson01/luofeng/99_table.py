#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-05-18
# Filename: 99_table.py
# Describe:
#*******************************************

# 正方形九九乘法表
for n in range(1,10):
    # python3 print() 函数支持 end 参数，python2 不支持, 默认值 end = '\n'
    for m in range(1,10):
        print('{} * {} = {}'.format(n, m, n*m), end='\t')
    print('')

# 左上三角形九九乘法表
for n in range(1,10):
    # python3 print() 函数支持 end 参数，python2 不支持, 默认值 end = '\n'
    for m in range(n,10):
        print('{} * {} = {}'.format(n, m, n*m), end='\t')
    print('')

# 左下三角形九九乘法表
for n in range(1,10):
    # python3 print() 函数支持 end 参数，python2 不支持, 默认值 end = '\n'
    for m in range(1,n+1):
        print('{} * {} = {}'.format(n, m, n*m), end='\t')
    print('')
