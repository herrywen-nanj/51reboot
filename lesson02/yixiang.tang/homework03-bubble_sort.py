# 需求：
#     Python冒泡排序

x = [3, 7, 2, 5, 20, 11]
for i in range(len(x)):
    for j in range(len(x) - 1):
        if x[j] > x[j + 1]:
            x[j], x[j + 1] = x[j + 1], x[j]
print(x)
