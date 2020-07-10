
for x in range(1, 10):
    for y in range(1, x+1):
        print('{} * {} = {}\t'.format(y, x, y*x), end='')
        if y == x:
            print('\n')


