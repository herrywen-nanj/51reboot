import copy

a = [{1, 2, 3, "hello world"}, 'world', ['www', '51reboot'], 'com', 100, (1, 2, 3)]
# b = a.copy()    # b = copy.copy(a)
b = copy.deepcopy(a)
# print(a, id(a))
# print(b, id(b))


a[2].append("http")


# for x in a:
#     print(id(x), end=",")
#
# print("\n")
#
# for x in b:
#     print(id(x), end=",")
#
# print()

# a[2].append(".com")
# a[0] = 100
# a.append("http")
#
#
print(a)
for x in a:
    print(id(x), end=",")

print("\n")

print(b)
for x in b:
    print(id(x), end=",")

print("\n")

