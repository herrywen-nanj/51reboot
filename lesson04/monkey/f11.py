


def optArgSort(iterableItem, reverse=True):
    vs = []
    for k, v in  iterableItem:
        vs.append(v)

    retdata = []
    if reverse:
        vs.sort()
    else:
        vs.sort(reverse=True)
    for i in vs:
        for k, v in iterableItem:
            if v == i:
                retdata.append((k, v))
    return retdata




dic = {'a' : 2, 'b' : 1, 'c' : 3}

result = optArgSort(dic.items(), reverse=False)
print(result)
