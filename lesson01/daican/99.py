'''
打印乘法口诀表
提示：尝试print('monkey')与print('monkey', end='')的区别
'''

x = 0
y = 0

for x in range(1,10):
    for y in range(1,10):
        a = x*y
        print("{}*{}={:<2} ".format(x, y, a), end=" ")
    print("")


