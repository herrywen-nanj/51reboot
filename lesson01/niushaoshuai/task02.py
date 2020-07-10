#!/usr/bin/env python

import random
i = random.randint(0,100)
times = 0
while times < 6:
    n = int(input())
    if n > i:
        print('大了')
    elif n < i:
        print('小了')
    else:
        print('猜对了')
        break
    times = times + 1
else:
    print('次数用完了')
