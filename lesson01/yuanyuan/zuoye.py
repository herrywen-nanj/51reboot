
#打印乘法口诀表

#预定义循环
s = "123456789"
z = "123456789"

for x in s:
   for y in z:
      if y > x:
         continue
      else:
         sum = int(y) * int(x)
         print('{}X{}={}'.format(y,x,sum),end=" ")
   print()
   


#猜数游戏

#导入随机数
import random
num = random.randint(0,100)

s = '123456'

for x in s:
   a = int(input("猜一个100以内的整数："))
   if a == num:
      print("猜对了")
      break
   elif a > num:
      print("大了")
   elif a < num:
      print("小了")
print("游戏结束")
