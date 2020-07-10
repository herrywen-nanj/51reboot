#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/112 14:51
# @Author  : 罗小贱
# @email: ljq906416@gmail.com
# @File    : 99乘法口诀
# @Software: PyCharm

for i in range(1,10):
     for j in range(1,i+1):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
     print (" ")

