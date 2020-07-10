
def f1():
    num = 100

    def f2():
        nonlocal num
        # print("num: {}".format(num))
        num += 1
        return num

    return f2


f = f1()
# print(f)
print(f())
print(f())
print(f())

print("--------------")
def func1():
    num = 100
    num += 1
    return num


print(func1())
print(func1())
print(func1())