"""
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。
"""

#从左到右，数组中相邻的两个元素进行比较，将较大的放到后面
lt = [3, 7, 2, 5, 20, 11]
n = len(lt)
for x in range(n-1):
    for y in range(n-1-x):
        if lt[y] > lt[y+1]:
            lt[y],lt[y+1] = lt[y+1],lt[y]
print(lt)

# 或者利用sorted()方法排序， reverse=False升序 或 reverse=True降序
print(sorted(lt, reverse=False))