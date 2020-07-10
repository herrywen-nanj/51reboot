#!/usr/local/bin/python3 -V
"""
打印乘法口诀
author:zhangjie
date:2019-04-29
"""
#方法一:
#for i in range(1,10):
#    for j in range(1,i+1):
#        print(i,'*',j,'=',i*j,"\t", end="")
#    print()
#

#方法二:
for i in range(1,10):
    for j in range(1,i+1):
        print('{} * {} = {}\t'.format(i,j,i*j,),end='')
    print("")
