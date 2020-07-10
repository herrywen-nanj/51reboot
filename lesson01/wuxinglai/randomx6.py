import os
import random
print('''
游戏规则说明:系统随机生成1-100的数字，你有6次机会猜中机会；6次之后自动退出！''')
username = input("Player name:")
target = random.randint(1,100)
i = 0
while i <= 5:
      i=i+1
      num  = int(input("Please guess the number:"))
      if num == target:
              print("恭喜 {}同学猜对了!".format(username))
              break
      elif num > target:
              print("猜大了")
      elif num < target:
              print("猜小了")
      if i == 6:
         print('抱歉 {}你的6次机会已经用完!'.format(username))
