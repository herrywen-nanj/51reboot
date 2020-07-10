def bubble_sort3(arr):
    for j in range(len(arr)-1, 0, -1):
        count = 0
        for i in range(0, j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1
        if count == 0:
            return

arr = [1, 3, 4, 67, 8, 34, 51]
bubble_sort3(arr)
print(arr)