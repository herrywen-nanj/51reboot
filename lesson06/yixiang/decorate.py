

# 装饰器
def decorate1(func):

    def wrapper(*args, **kwargs):
        # 装饰器 主体逻辑
        print("调用函数前执行了decorate1，args: {}, kwargs: {}" .format(args, kwargs))
        pass
        # 执行被注解函数执行位置
        func(args[0], args[1])

    return wrapper


# 装饰器
def decorate2(func):

    def wrapper(*args, **kwargs):
        # 执行被注解函数执行位置
        func(args[0], args[1])

        # 装饰器 主体逻辑
        print("调用函数后执行了decorate1，args: {}, kwargs: {}" .format(args, kwargs))
        pass

    return wrapper


# 启动装饰器
@decorate1
def f1(name, age):
    print("hello, my name is {} age {}" .format(name, age))


# 启动装饰器
@decorate2
def f2(name, age):
    print("hello, my name is {} age {}" .format(name, age))


# 程序主入口
if __name__ == '__main__':
    print("----- 我是华丽的开始符 ------")
    f1("小明", 12)
    print("----- 我是华丽的分隔符 ------")
    f2("小明", 18)

