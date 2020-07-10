'''
1.猜一个100以内的整数
2.6次机会
3.每次猜时，猜对了，大了，小了

提示：生成随机数的方法
import random
random.randint(0, 100)
'''
import random

#2.随机生成一个数字
computer = random.randint(0,100)
i = 0
#3.判断你的输入是否正确
while i < 6:
	
	#1.提示并获取你要输入的数字
	num = int(input("请输入您要猜的数字："))
	if num == computer:
		print("恭喜您，答对了！！")
	elif num > computer:
		print("很抱歉，您输入的数字大了！")
	elif num < computer:
		print("很抱歉，您输入的数字小了！")
	i = i + 1
print("正确的数字是%d"%computer)
