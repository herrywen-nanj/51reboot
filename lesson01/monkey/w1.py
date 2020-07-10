
'''
init_val = 1
end_val = 9

while init_val <= end_val:
    print("1")
    init_val = init_val + 1

print("Over")
'''

'''
s = "1" * 9
print(s)

for x in s:
    print(x)
'''


init_val = 1
end_val = 9

while True:
    if init_val > end_val:
        # 退出当前循环 pass
        break
    print("1")
    init_val = init_val + 1

print("Over")