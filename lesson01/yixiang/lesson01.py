#!/usr/local/python36/bin/python3.6
print("hello!")

username = "小明!"
print(username)

num1 = 3
num2 = 2
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)

# ========== 基本输入输出，分隔线 ==========

num1 = input("Please input your num1:")
print("num1: ", num1)
num2 = input("Please input your num2:")
print("num2: ", num2)
print(num1, num2)
print("===== input默认为String类型输入，直接相加为字符串拼接 =====")
sum1 = num1 + num2
print("sum1 = num1 + num2", sum1)
print("===== input默认为String类型输入，需要类型转换int进行数值计算 =====")
sum1 = int(num1) + int(num2)
print("sum1 = int(num1) + int(num2)", sum1)
# 输出占位符
print("num1 value: {},num2 value: {}。" .format(num1, num2))

# ========== 变量类型判断，分隔线 ==========

b1 = True
b2 = 'hello'
b3 = "hello"
b4 = '''
hello
'''
print("b1 type: ", type(b1))
print("b2 type: ", type(b2))
print("b3 type: ", type(b3))
print("b4 type: ", type(b4))

# ========== 逻辑判断(and[且] or[或] not[非])，分隔线 ==========
a = "a"
b = "b"
b1 = "a"
a1 = "a"
print("a == b: {}" .format(a == b))
print("a == a1: {}" .format(a == a1))
print("a == a1: {}" .format(a == b1))
print("a is b: {}" .format(a is b))
print("a is b: {}" .format(a is not b))

# ========== if 流程控制，分隔线 ==========

score = input("请输入您的成绩：")
if int(score) >= 60:
    print("恭喜，您及格了！")
if int(score) < 10:
    print("哇，你真是个天才！")
else:
    print("您不及格！")

# ========== 循环(for, while) 相关关键字(break, pass, continue) 流程控制，分隔线 ==========
s = "0123456789"
array = {0, 1, 2, 3, 4, 5}
arr = range(0, 10)
# s 可以为任何对象。
for i in s:
    # end="" 输出后，以end中的内容结尾，默认以换行符结尾
    print(i, end=" ")
print("")

# 字符串重复拼接9次
s = "1" * 9
for i in s:
    print(i, end=" ")

# while
# while死循环
# while True:
#    print("死循环啦")




