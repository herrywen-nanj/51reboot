'''

-[3,7,2,5,20,11]
'''

array = [3,7,2,5,20,11]
for i in range(len(array)):
    for j in range(i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
