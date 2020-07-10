#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了

提示：生成随机数的方法
import random
random.randint(0, 100)
'''

import random

num = random.randint(0,100)
print(num)

def func(coun):
    while True:
        try:
            if coun > 6:
                print('结束了，你没有机会了。')
                break
            else:
                val = input(('请输入第{}个数值：').format(coun))
                coun = coun + 1
                if int(val) > num:
                    print('sorry，你猜的数字大于正确值，祝你好运。')
                    continue
                elif int(val) < num:
                    print('sorry，你猜的数字小于正确值，祝你好运。')
                    continue
                elif int(val) == num:
                    print('good，恭喜你猜对了！')
                    return
        except ValueError:
            print('Error：请正确填写数字')

if __name__ == '__main__':
    func(1)