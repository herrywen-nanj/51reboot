# for 猜数字

import random

real_number=random.randint(1,100)

for cnt in range(1,7):
    print ('总共有6次机会，这是第{}次机会: '.format(cnt))
    input_number=int(input('please enter your number:'))
    if input_number < real_number:
        print('猜小了')
    elif input_number > real_number:
        print('猜大了')
    elif input_number == real_number:
        print('猜对了 ')
        break
        print('zhe random number is',input_number)
    else:
        break