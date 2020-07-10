def f(a, b, c, d, e, f):
    print(a, b, c, d, e, f)


args = (2, 3)
kwargs = {'d': 4, 'e': 5}

f(1, *args, **kwargs, f=6)
f(1, *args, f=6, d=4, e=5 )