#!/usr/local/python36/bin/python3.6
# 需求
# 打印列表中的最大数字和最小数字
# [5, 12, 32, 4, 2, 10, 25]

x = [5, 12, 32, 4, 2, 10, 25]
max, min
for i in range(len(x)):
    if i == 0:
        max, min = x[i], x[i]
    if x[i] > max:
        max = x[i]
    if x[i] < min:
        min = x[i]
print("Max: {}, Min: {}" .format(max, min))


# 需求
# 移动列表的最大数字到最后
# 原始列表：[5, 12, 32, 4, 2, 10, 25]
# 最终列表：[5, 12, 4, 2, 10, 25，32]

x = [5, 12, 32, 4, 2, 10, 25]
for i in range(len(x) -1):
    if x[i] > x[i + 1]:
        a = x[i + 1]
        x[i + 1], x[i] = x[i], a
print(x)


# 需求
# 移动列表的最大数字到中间
# 原始列表：[5, 12, 32, 4, 2, 10, 25]
# 最终列表：[5, 12, 4, 2, 10, 25，32]

x = [5, 12, 32, 4, 2, 10, 25]
for i in range(len(x) -1):
    if x[i] > x[i + 1]:
        a = x[i + 1]
        x[i + 1], x[i] = x[i], a
x.insert(len(x) // 2, x.pop(-1))
print(x)


# 需求
# 求两个列表中重复的元素的列表
# 原始列表：[1, 2, 5, 7, 11]
#         [2, 15, 3, 7]
x1 = [1, 2, 5, 7, 11]
x2 = [2, 15, 3, 7]
x = []
for i in x1:
    if i in x2:
        x.append(i)
print(x)


# 需求
# 求重复元素的个数
# [13, 60, 96, 78, 21, 88, 22, 64, 52, 60, 60, 13]
x1 = [13, 60, 96, 78, 21, 88, 22, 64, 52, 60, 60, 13]
x2 = []
for i, v in enumerate(x1):
    x = x1.pop(i)
    if x in x1:
        x2.append(x)
print("重复元素的个数: {}" .format(len(x2)))




