

# 可变参数的位置参数
def optf1(x, y, z, *args, **kwargs):
    pass

def optf4(x, y, z, c=100, *args, **kwargs):
    print(x, y, z)
    print(c)
    print(args)
    print(kwargs)

def optf2(*args):
    print(args)

def optf3(**kwargs):
    print(kwargs)


# optf2(1, 2, 3, 4, 5, name="51reboot")
# optf3(name="51reboot")

# optf4(1, 2, 3, 4, 5, 6, a=1, b=2)

k = (5, 6, 7, 8)
kw = {'name' : '51reboot', 'age' : '5'}

optf4(1, 2, 3, 4, *k, **kw)

