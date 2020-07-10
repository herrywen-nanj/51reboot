#_author:Administrator
#date:2019/5/17 0017

for first_number in range(1,10):
    for second_number in range(1,10):
        if first_number>=second_number:
            print('{}*{}={}'.format(second_number,first_number,first_number*second_number),end=' ')
    print()