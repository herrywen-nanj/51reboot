
# 不可变的数据类型  str/tuple/int/bool/
# 可变的数据类型   list/dict/set

'''
a = [2] # 8
arr = [2]int
a.append(2)
a.append(x)
a.append(3)

'''

a = list(range(100))

will = ["Will", 28, ["Python", "C#", "JavaScript"]]
wilber = will


print(id(will))
print(id(wilber))

print([id(x) for x in will])
print([id(x) for x in wilber])

print("-----------------------------")

will[0] = "Wilber"  # update
# will[2].append("CSS")   # add
will[2].extend(a)

print(id(will))
print(id(wilber))

print([id(x) for x in will])
print([id(x) for x in wilber])



