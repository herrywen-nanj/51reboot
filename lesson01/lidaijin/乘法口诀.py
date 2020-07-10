for i in range(1,10):
    for num in range(1,i+1):
        results = i * num
        print("{} * {} = {}".format(num,i,results),end="\t")
    print()

