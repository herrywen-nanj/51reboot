# -*- coding:utf-8 -*-
# author: lyl

sort = [3, 7, 2, 5, 20, 11]

for i in range(len(sort)):
    # 判断索引是否超出范围
    if i+1 < len(sort):
        for n in range(i+1, len(sort)):
            if sort[i] > sort[n]:
                sort[i], sort[n] = sort[n], sort[i]
print(sort)
