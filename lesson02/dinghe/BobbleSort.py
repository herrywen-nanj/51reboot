#!/bin/python


# 冒泡排序
list = [3, 6, 1, 2, 7, 9, 5]

# 循环的次数 当前列表从长度减1
for i in range(len(list) - 1):
    # 从第一个值比较到最后一个值，循环i次
    for j in range(len(list) - 1):
        # 如果值比下一个的值大,两者交换位置
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

# 打印排序后的列表
print(list)
