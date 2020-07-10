#!/usr/bin/python
# -*- coding: UTF-8 -*-
for i in range(1,10):
    for j in range(1,i+1):
        # 默认python3中的print是换行的，加end可以控制结尾字符，空为不换行
        print('{} * {} = {} '.format(i,j,i*j),end='')
    #j循环结束就换行
    print()
