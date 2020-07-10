import json

# ValueError 异常捕获
s = "hello"
try:
    int_s = int(s)
    print(int_s)
except ValueError:
    print("string can't cast int")
except Exception as e:
    print(e)

# TypeError 异常捕获
try:
    print(1 + "2")
except TypeError:
    print("string + int error")
except Exception as e:
    print(e)

print("==============json 操作==============")
# json 操作
map = {"hello": "123", "world": "he"}
# 对象转json
json1 = json.dumps(map)
print(json1)
# json转对象
json2 = json.loads(json1)
for i in json2:
    print(i)

print("==============文件操作==============")
# 文件操作
# 写文件
fd = open("file_test.txt", 'w')

fd.write("1\n")
fd.write("2\n")
fd.write("3\n")
fd.write("hello world\n")

s = "A\nB\nC\nhello\n"
fd.write(s)

fd.close()

# 读文件
fd = open("file_test.txt", 'r')
data = fd.read()
print(data)

fd.close()
