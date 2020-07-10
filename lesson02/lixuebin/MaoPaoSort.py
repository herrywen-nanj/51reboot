'''
冒泡排序算法:
    比较相邻的两个数字大小
    然后变换位置
    相同的数字不变换位置
    是一种稳定的排序算法
'''
L = [78, 13.56, 6, 2, 3, 8, 9, 4, 16, 54, 21]

i = 0

while True:
    if i >= len(L)-1:                       #判断i>列表长度就重新赋值为0
        i = 0
    else:
        while i < len(L):
            if L[i] > L[i+1]:
                L.insert(i+1,L.pop(i))
                i+=1
                print(L)
                if i >= len(L)-1:           #当判断i>=列表长度时,此时没有次索引值,所以退出到上一层循环,使i重新赋值为0
                    break
            else:

                i+=1
                if i >= len(L)-1:
                    break
                else:
                    continue
