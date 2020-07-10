

'''
d = {'age': 12, 'tel': '132xxx'}


d1 = {}

for k, v in d.items():
    # print(k, v)
    d1[v] = k


d1 = {v :k for k, v in d.items()}


print(d1)
'''


d = {'x' : 1, 'x2' : 5, 'x3' : 10}

d1 = {k : v*2 for k, v in d.items()}
print(d1)


