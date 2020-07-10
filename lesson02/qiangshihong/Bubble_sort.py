#!/usr/bin/python
# -*- coding: UTF-8 -*-

ll = [3, 7, 2, 5, 20, 11]
i = 0

while i < len(ll)-1:
    for x in range(len(ll)-1-i):
        print(x)
        if ll[x] > ll[x+1]:
            ll[x],ll[x+1] = ll[x+1],ll[x]
            print(ll)
    i+=1
print(ll)



