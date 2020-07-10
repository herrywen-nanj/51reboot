
'''
1: 打印乘法口诀
提示：尝试print(‘monkey’)与print(‘monkey’, end=‘’)的区别
'''

#第一种方法
#'''
#变量竖
vertical = 1
#变量横
cross = 1
while cross <= 9:
    #变量 i
    i = 1
    while vertical <= 9:
        #i与数的乘积
        vectors = i * vertical
        if i < cross:
            print("{} x {} = {}   ".format(i, vertical, vectors), end='')
        else:
            print("{} x {} = {}   ".format(i, vertical, vectors))
            vertical = vertical + 1
            break
        i = i + 1
    cross = cross + 1
#'''

#第二种方法
#变量竖
vertical = 1
#变量横
cross = 1
for c in '123456789':
    i = 1
    for v in '123456789':
        vectors = i * vertical
        if i < cross:
            print("{} x {} = {}   ".format(i, v, vectors), end='')
        else:
            print("{} x {} = {}   ".format(i, v, vectors))
            vertical = vertical + 1
            break
        i = i + 1
    cross = cross + 1

