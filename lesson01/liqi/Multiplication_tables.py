for i in range(1,10):
    for a in range(1,i+1):
	# 关键字 end 可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
        print('{} * {} = {} '.format(i,a,i*a),end='')
    print()
