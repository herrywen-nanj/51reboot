#task01 冒泡
x = [1000,3, 7, 2, 2,5, 20, 11,10,100,34,45,99]
i = 0
while i < len(x):
    for k,v in enumerate(x):
        if k == 0:
            continue
        m = v
        n = x[k-1]
        if m < n:
            x[k-1],x[k] = m,n
    i = i + 1 
print(x)
