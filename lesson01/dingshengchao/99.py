num1 = "123456789"
num2 = "123456789"
for m in num1:
    intm = int(m)
    for n in num2:
        intn = int(n)
        print("{}x{}={}".format(intm,intn,intm*intn),end = " ")
    print()
