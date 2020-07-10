#!/usr/bin/env python
###############################
# function: 9x9 multiplication table
# author: dhl
# date:	2019-05-16
# env: python3
###############################

print("< 九九乘法表 >")
for i in range(1,10):
    for j in range(1,i+1):
        print('%dx%d=%2d' %(i,j,i*j), end=' ')
    print(' ')
     
