



s = "123456"
ssum = 0

for x in s:
    # print(input("Please input num{}: ".format(x)))
    num = input("Please input num{}: ".format(x))
    # print("[Debug] x:{}, num:{}, ssum:{}".format(x, num, ssum))
    ssum = ssum + int(num)
    # print("[Debug] ssum: {}".format(ssum))

print("ssum: {}".format(ssum))
