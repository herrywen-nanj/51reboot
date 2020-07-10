
# 不可变的数据类型  str/tuple/int/bool/
# 可变的数据类型    list/dict/set

import copy

will = ["Will", 155589, "xxxx x", ["Python", "C#", "JavaScript"]]
# wilber = copy.copy(will)
# 浅拷贝会创建一个新的对象，这个例子中”wilber is not will”
willer = copy.deepcopy(will)

print(id(will))
print(id(willer))

print([id(x) for x in will])
print([id(x) for x in willer])


will[0] = "Wilber"  # update
will[3].append("CSS")   # add
print("-----------------------------")


print(id(will))
print(id(willer))

print([id(x) for x in will])
print([id(x) for x in willer])
print(will)
print(willer)




