# 猜六次数字并打印正确与否

import random

num = random.randint(0, 100)
#print(num)

a = 0
b = 6

while a < b:
    c = b - (a+1)
    guessNum = int(input("Please enter the number you guessed: "))
    if guessNum > num:
        print("You guessed it was big! You still have {} chances.".format(c))
    elif guessNum < num:
        print("You guessed it was small! You still have {} chances.".format(c))
    else:
        print("You guessed right. This number is {}".format(num))
        break
    a = a + 1
print()
print("This true Num is {}".format( num ))
