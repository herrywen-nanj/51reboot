
'''
乘法口诀
'''

'''
# 方式1
retlist = range(1, 10)

for i in retlist:
    for j in range(1, i+1):
        # print(i, j, end="")
        print("{} * {} = {}".format(j, i, i * j), end=" ")
    print()
'''


# 方式2
i = 1

while i < 10:
    j = 1
    while j < i+1:
        print("{} * {} = {}".format(j, i, i * j), end=" ")
        j += 1
    i += 1
    print()