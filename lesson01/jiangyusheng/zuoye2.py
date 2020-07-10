import random,sys
_Number = random.randint(0,100)
_Counter = 0

while True:
    _Num = int(input('请输入一个整数: '))
    if _Num > _Number:
        print('大了.')
        _Counter += 1
        if _Counter > 5:
            sys.exit('Sorry, {} 次都没猜对唉,不和你玩了,Bye!'.format(_Counter))
    elif _Num < _Number:
        print('小了.')
        _Counter += 1
        if _Counter > 5:
            sys.exit('Sorry, {} 次都没猜对唉,不和你玩了,Bye!'.format(_Counter))
    else:
        sys.exit('恭喜你，猜对了.')