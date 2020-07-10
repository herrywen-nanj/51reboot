
will = ["Will", 28, ["Python", "C#", "JavaScript"]]

# 赋值
wilber = will

print(id(wilber))
print(id(will))

print([id(ele) for ele in will])
print([id(ele) for ele in wilber])

will[0] = "Wilber"
will[2].append("CSS")

print(id(wilber))
print(id(will))

print([id(ele) for ele in will])
print([id(ele) for ele in wilber])

