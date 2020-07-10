#!/usr/bin/env python
# -*- encoding:utf8 -*-
#*******************************************
# Author: LuoFeng
# Date: 2019-05-25
# Filename: maopao_sort.py
# Describe:
#*******************************************

nums = [1, 2, 23, 234, 56, 232, 98, 1001, 112]

for i in range(len(nums) - 1):
    for j in range(len(nums) -i -1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print(nums)


