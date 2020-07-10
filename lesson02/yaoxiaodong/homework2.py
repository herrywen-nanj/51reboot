data = [3, 7, 2, 5, 20, 11]

num = len(data)

for one in range(num-1):
    for two in range(num-one-1):
        if data[two] > data[two+1]:
            data[two],data[two+1] = data[two+1],data[two]
print(data)
