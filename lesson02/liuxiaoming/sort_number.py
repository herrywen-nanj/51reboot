number = [3, 7, 30, 5, 20, 11]
for i in range(len(number)):
    for j in range(i + 1, len(number)):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]

print(number)
