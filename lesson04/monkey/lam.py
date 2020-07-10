
# def ssum(x, y):
#     return x + y
#
# s = ssum(2, 3)
# print(s)


# lambda [arg1 [,arg2,.....argn]]:expression
# f = lambda x, y:x + y
# print(f)
# s = f(2, 3)
# print(s)

dic = {'a' : 2, 'b' : 1, 'c' : 3}
print(dic)
print(dic.items())

# def keyf(arg):
#     return arg[1]

keyf2 = lambda x:x[1]

# ss = sorted(dic.items(), key=lambda x:x[1], reverse=True)
ss = sorted(dic.items(), key=keyf2, reverse=True)
print(ss)