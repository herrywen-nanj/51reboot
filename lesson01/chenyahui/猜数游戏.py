#_author:Administrator
#date:2019/5/17 0017

import random
number=random.randint(1,100)
for i in range(1,7):
    guess_number=int(input('please enter your number:'))
    if guess_number<number:
        print('小了')
    elif guess_number>number:
        print('大了')
    else:
        break
if guess_number==number:
    print('猜对了 ')
print('zhe random number is',number)