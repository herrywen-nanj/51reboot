#!/usr/local/python36/bin/python3.6
#打印乘法口诀
s = range(1, 10)
for i in s:
    print()
    for j in s:
        if j <= i:
            p = j * i
            print(j,'x',i,'=',p,end='  ')
