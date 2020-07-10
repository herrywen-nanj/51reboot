#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auth : xuegqcto@aliyun.com

# 冒泡排序

"""
索引取值，解包法赋值
"""
l1 = [1, 28, 9, 21, 12, 33, 22, 10]

for i in range(len(l1)-1):
    if l1[i] > l1[i+1]:
        l1[i], l1[i+1] = l1[i+1], l1[i]

print(l1)


"""
索引取值，两两比较，临时数值暂存值，A、B交换法
"""
l1 = [1, 28, 9, 21, 12, 33, 22, 10]
tmp = 0

for i in range(len(l1)-1):
    if l1[i] > l1[i+1]:
        tmp = l1[i]
        l1[i] = l1[i+1]
        l1[i+1] = tmp

print(l1)




l1 = [1, 28, 9, 21, 12, 33, 22, 10]

for i in range(len(l1)):
    for j in range(len(l1)-i-1):
        if l1[j] > l1[j + 1]:
            l1[j], l1[j + 1] = l1[j + 1], l1[j]
print(l1)




