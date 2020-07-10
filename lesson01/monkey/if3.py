

x1 = input("x1>>> ") # 70

x1_int = int(x1)

if x1_int > 90:
    print("good")
else:
    if x1_int > 80 and x1_int <= 90:
        print("ok")
    else:
        print("Failed")

print("Over")