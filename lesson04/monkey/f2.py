
# 定义一个函数
def f1():
    print("hello world.")
    return "51reboot", True

'''
如果return返回2+个值， 那么接收的变量就是元祖类型.
'''


# 执行指定函数
result, ok = f1()
print(result, ok)
