


s2 = 'hello'

try:
    int_num = int(s2)
    print(int_num)
except ValueError:
    print("string to int error.")
except Exception as e:
    print(e)

