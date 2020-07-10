
def optf(x, y, z):

    print("x = {}".format(x))
    print("y = {}".format(y))
    print("z = {}".format(z))

# 执行参数时的参数
# 位置参数   positional argument
# 关键字参数 key=value  keyword argument
# 执行函数时， 位置参数一定要放在关键字参数前面
# positional argument follows keyword argument
optf(1, y=2, z=3)