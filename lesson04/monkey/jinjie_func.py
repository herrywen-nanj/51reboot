
'''
# 列表生成式
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

retadta = []
for i in arr:
    if i % 2 != 0:
        retadta.append(i)

print(retadta)

result = [ i for i in arr if i % 2 != 0]
print(result)
'''

# 字典生成式
d = {'a' : '1', 'b' : '2', 'c' : '3'}

optd = {}
for k, v in d.items():
    optd[v] = k
print(optd)

optd = { int(v)*2 : k for k, v in d.items() }
print(optd)

# 集合生成式

arr = [1, 2 ,3]

result = { x ** 2 for x in arr }
print(result)


# 元组生成式 -> 生成器
arr = [1, 2 ,3]

result1 = ( x ** 2 for x in arr )
print(result1)





