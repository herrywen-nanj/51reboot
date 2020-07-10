#!/usr/local/python36/bin/python3.6
#-*- coding: utf-8 -*-
'''
Author: WangXiaoyun
'''
#九九乘法表
for i in range(1,10):
    for j in range(1,10):
        sum = i * j
        if i >= j:
          print('%d * %d = %d' % (i,j,sum),end='  ')
    print ('')