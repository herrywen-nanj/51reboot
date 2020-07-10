import functools

def decorate(func):

    def wrapper():
        '''
        add print
        :return:
        '''

        print("www.51reboot.com")

        func()

        print("2014.08 51reboot start")

    # return wrapper
    return functools.wraps(func)(wrapper)

@decorate
def f1():
    '''
    logic f1
    :return:
    '''
    print("hello world")
    with open("/etc/passwd") as fd:
        print(fd.read())


print(f1.__doc__)
print(f1.__name__)

# f = decorate(f1)
# f()