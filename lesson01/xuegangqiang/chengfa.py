#!/bin/bin/env python
# -*- coding: utf-8 -*-
# __auhtor__: will_xue
# Date: 2019-05-12
# Email: xuegqcto@aliyun.com

# 打印乘法口诀

for i in range(1, 10):
    for j in range(1, 10):
        if j > i:
            break
        print(j, "*", i, "=", i * j, end="\t")
        j = j + 1
    print()
    i += 1

