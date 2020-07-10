import copy

a = {"1": [1,2,3]}
b = a.copy()    # 浅拷贝


# print(a, id(a))
# print(b, id(b))

# a['1'].append('4')
a[2] = "hello wrold"

for k1, v1 in a.items():
    print(k1, v1, id(k1), id(v1))

for k2, v2 in b.items():
    print(k2, v2, id(k2), id(v2))
