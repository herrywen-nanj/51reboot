import random

title = '''
You have six chances. If you typed incorrectly, you have one chance to subtract.
'''
print(title)



judge = True
count = 6
random_num = random.randint(0, 100)

while judge:
    number = input('input your number：')

    count -= 1
    if count == 0:
        print('random_num is {}'.format(random_num))
        judge = False
        continue
    try:
        number = int(number)
    except ValueError as e:
        print('Please input int,not str or other, chcance: {}'.format(count))
    else:
        print('Your number is {}, '.format(number),end=' ')
        if number == random_num:
            print('Bingo, {}, you are right! The number is {}'.format(number,random_num))
            agein = input('Do you want to play it again? (y/n)')
            if agein == 'y':
                count = 6
                random_num = random.randint(0, 100)
                continue
            elif agein == 'n':
                judge = False
                continue
            else:
                print('y or n')
        else:
            print('You can only type it again, chcance: {}'.format(count))

