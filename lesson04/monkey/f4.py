
def optf1(x, y):
    # print(x)
    # print(y)
    if x:
        print("51reboot ", y)
    else:
        print("err")


def optfsum(x, y):
    return x + y

def optfdiv(x, y):
    return x - y

# 位置参数
s = optfdiv(3, 2)
print(s)

s = optfdiv(y=3, x=2)
print(s)