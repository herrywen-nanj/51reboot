'''
需求：冒泡排序
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。
'''

x = [3, 7, 2, 5, 20, 11]

for i in range(len(x)):
    for j in range(i):
        if x[j] > x[i]:
            x[j],x[i] = x[i],x[j]
print(x)
