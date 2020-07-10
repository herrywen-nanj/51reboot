list = [3, 7, 2, 5, 20, 11]
for for_list_range in range(len(list)):
    for list_range_len in range(len(list) - 1):
        if list[list_range_len] > list[list_range_len + 1]:
            tmp = list[list_range_len]
            list[list_range_len] = list[list_range_len + 1]
            list[list_range_len + 1] = tmp
print([list])
