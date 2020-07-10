#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1: 打印乘法口诀
提示：尝试print(‘monkey’)与print(‘monkey’, end=‘’)的区别
'''

# a = 1
# while a < 9:
#     b = 1
#     while b <= a:
#         print("%d*%d=%d\t"%(b,a,a*b),end="")
#         b = b+1
#     print()
#     a += 1


for x in range(1,10):
    for y in range(1,x+1):
        print(('{}x{}={} ').format(y,x,x*y),end='\t')
    print()







