


d = [3, 7, 2, 5, 20, 11]

d_len = len(d)

'''
for i in range(0, d_len):
    for j in range(i+1, d_len):
        if d[i] > d[j]:
            d[i], d[j] = d[j], d[i]
'''


'''
冒泡排序
每相邻的2个数比较，每次比较次数为 长度-1，一轮比较下来，会有一个最大值。
那么这个最大值下次就可以不在比较了。

'''
for i in range(0, d_len-1):
    for j in range(d_len-1-i):
        print(d[j], d[j+1])
        if d[j] > d[j+1]:
            d[j], d[j+1] = d[j+1], d[j]

print(d)
