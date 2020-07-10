import copy

a = {"hello worldxxx": [1,2,3]}
# b = a
# b[1].append(4)
# print(a, id(a))



b = copy.copy(a)
a['hello worldxxx'].append("aaa")
# a['2'] = "123je"
print(a, id(a))
print(b, id(b))

for k1, v1 in a.items():
    print(id(k1), id(v1))

for k2, v2 in b.items():
    print(id(k2), id(v2))

# print(a)
# for k1, v1 in a.items():
#     print(id(k1), id(v1))
#
# print(b)
# for k2, v2 in b.items():
#     print(id(k2), id(v2))
