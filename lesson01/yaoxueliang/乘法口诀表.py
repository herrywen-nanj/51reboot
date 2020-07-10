row = range(1, 10)
col = range(1, 10)



for y in col:
    print()
    for x in range(1,y+1):
        print(x, '*', y, '=', y*x, end=' ')