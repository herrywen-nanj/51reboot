

def optArg(a):
    return a[1]

#
#
# f = optArg
#
# t = ('a', 2)
#
#
# result = f(t)
# print(result)


dic = {'a' : 2, 'b' : 1, 'c' : 3}

ss = sorted(dic.items(), key=optArg, reverse=True)
print(ss)


