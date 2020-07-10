



a = 100

def f1():
    a = 200

    def f2():
        # gloal a
        nonlocal a
        a += 20
        print(a)

    f2()

f1()