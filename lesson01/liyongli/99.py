# -*- coding:utf-8 -*-
# author: lyl

for i in range(1, 10):
    for n in range(1, i+1):
        # 使用制表符让输出对齐
        print("%d * %d = %d " % (i, n, i*n), end='\t')
    print()

