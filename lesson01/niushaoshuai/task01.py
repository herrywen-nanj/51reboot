#!/usr/bin/env python

m = 1
while m < 10:
    n = 1
    while n <= m:
        s = m * n
        if n == m :
            print(n,'*',m,'=',s,end="\n")
        else:
            print(n,'*',m,'=',s,',',end=" ")
        n = n + 1
    m = m +1
