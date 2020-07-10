def second(lt):
    #先去重
   lt1 = []
   for i in lt:
     if i not in  lt1:
        lt1.append(i)
   for j in lt1:
        a.append(j)
        a.sort()
        return  a[-2]
a = [1,2,3,4,5,8,8,555,666,555,66,9]
print(second(a))
