#!/usr/bin/env python
###############################
# function: login_system
# author: dhl
# date:	2019-05-24
# env: python3
###############################

list_data = [3, 7, 2, 5, 20, 11]

def bubble_sort(data):
    for i in range(len(list_data)-1,0,-1):
        count = 0
        for j in range(0,i):
            if list_data[j] > list_data[j+1]:
                list_data[j],list_data[j+1] = list_data[j+1],list_data[j]
                count += 1
        if count == 0:
            return

bubble_sort(list_data)
print(list_data)
