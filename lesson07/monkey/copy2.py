
import copy

will = ["Will", 28, ["Python", "C#", "JavaScript"]]

# 浅拷贝会创建一个新的对象
wilber = copy.copy(will)

print(id(wilber))
print(id(will))

print([id(ele) for ele in will])
print([id(ele) for ele in wilber])

will[0] = "Wilber"
will[2].append("CSS")

print(id(wilber))
print(id(will))

# 为什么第一层字符串改变了
# 因为字符串无法修改，如果修改其实就是重新申请、创建内存
# 那为什么子对象的地址没有变化呢
print([id(ele) for ele in will])
print([id(ele) for ele in wilber])

