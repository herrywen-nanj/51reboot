arg = [3,7,2,5,20,11]
for i in range(len(arg)-1):
    for j in range(len(arg)-1-i):
        if arg[j] > arg[j + 1]:
            arg[j], arg[j + 1] = arg[j + 1], arg[j]

print (arg)