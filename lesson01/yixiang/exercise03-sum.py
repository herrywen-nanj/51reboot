# 需求：
#     输入6个数字
#     输出，求和
sum = 0
for i in range(5):
    sum += int(input("Please input number: "))
print("sum: ", sum)


# 需求：
#     计算1到100的和
sum = 0
for i in range(100):
    sum += i + 1
print("1+...+100 =", sum)


# 需求：
#     输入n个数，知道输入0结束
max = 0
sum = 0
while True:
    in1 = int(input("Please input number: "))
    if in1 == 0:
        break
    sum += in1
    if max < in1:
        max = in1
print("sum: ", sum)
print("max:", max)

