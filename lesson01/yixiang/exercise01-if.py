# 需求：
#     输入姓名，性别，年龄
#     输出，你好xxx先生(女士)，您的年龄低于(高于)18岁，可以(不能)进入


username = input("请输入您的姓名：")
age = input("请输入您的年龄：")
sex = input("请输入您的性别：")

a = '先生' if sex == '男' or sex == 'man' else '女士'
b = '年满' if int(age) >= 18 else '不满'
c = '可以' if int(age) >= 18 else '不能'

print("您好{}{}, 您{}18岁, {}进入。" .format(username, a, b, c))

