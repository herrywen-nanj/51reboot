#encoding=utf8
'''
for循环外循环从9变到1，内循环从1变到9，外循环一次，内循环一圈
f格式化输出方法之一，:2得出结果为2位优化显示，end取消换行，外循环正常换行
'''
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(f'{j} * {i} = {i*j:2}',end=' ')
    print()
