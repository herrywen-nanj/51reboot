# _*_ encoding:utf-8 _*_
__author__ = 'sunzhaohui'
__date__ = '2019-05-12 18:17'

import random

'''
2: 猜数游戏
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了

提示：生成随机数的方法
import random
random.randint(0, 100)
'''

#第一种方法
'''
chance_times = 6
random_number = random.randint(0,100)

while chance_times > 0:
    input_number = int(input('猜一个100以内的整数,当前有{}次机会:'.format(chance_times)))
    if input_number == random_number:
        print('猜对了')
        break
    elif input_number > random_number:
        print('大了')
    else:
        print('小了')
    chance_times = chance_times - 1
'''

#第二种方法
random_number = random.randint(0,100)
print(random_number)
for i in ('654321'):
    input_number = int(input('猜一个100以内的整数,当前有{}次机会:'.format(i)))
    if input_number == random_number:
        print('猜对了')
        break
    elif input_number > random_number:
        print('大了')
    else:
        print('小了')


