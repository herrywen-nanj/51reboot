for i in range(1, 10):  # 输入9行
    for j in range(1, i + 1): # 输出与行数相等的列
        print(str(j) + "x" + str(i) + "=" + str(i * j) + "\t", end=' ')
    print('')
