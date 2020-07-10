import copy

a = [1,2,3,4,['a','b']]  #原始对象



c = copy.copy(a)

# a.append(5)
a[4].append('c')

print(a, id(a))
print(c, id(c))