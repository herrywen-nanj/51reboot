#!/usr/local/bin/python3.6
#冒泡排序
list = [3, 7, 2, 5, 20, 11]
print(list)

def dubble_sort(list):
    count = len(list)
    for i in range(0,count):
        for j in range(i+1,count):
            if list[i] > list[j]:
                list[i],list[j] = list[j],list[i]
    return list
print(dubble_sort(list))
