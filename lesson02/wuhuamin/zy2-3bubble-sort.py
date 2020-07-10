# arr = [7, 4, 3, 67, 34, 1, 8]
#
# def bubble_sort(arr):
#     n = len(arr)
#     for j in range(0, n - 1):
#         for i in range(0, n - 1 - j):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#
#
# bubble_sort(arr)
# print(arr)  # [1, 3, 4, 7, 8, 34, 67]

#冒号排序
#list1 = [3, 7, 2, 5, 20, 11]

def bubble_sort(lis):
    n = len(lis)
    #print(n)
    for i in range(n):
        for j in range(n-i-1):
            print(j,j+1)
            # if lis[j] > lis[j+1]:
            #     lis[j],lis[j+1] = lis[j+1],lis[j]
lis = [3, 7, 2, 5, 20, 11]
bubble_sort(lis)

print(lis)