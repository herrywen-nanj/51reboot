for num1 in range(1,10):
    for num2 in range(1,num1+1):
        print('{} * {} = {}'.format(num1,num2,(num1 * num2)),end='\t')
    print('')


num1 = 1
while num1 < 10:
    num2 = 0
    while num2 < num1 + 1:
        print('{} * {} = {}'.format(num1, num2, (num1 * num2)),end='\t')
        num2 += 1
    print('')
    num1 += 1
