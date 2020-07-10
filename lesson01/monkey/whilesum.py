

max_val = 0
ssum = 0

while True:
    num = input("Please input: ")
    num_int = int(num)
    if num_int == 0:
        break
    ssum = ssum + num_int

    if num_int > max_val:
        max_val = num_int

print(max_val)
print(ssum)
