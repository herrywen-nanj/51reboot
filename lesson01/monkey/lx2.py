

'''
需求：
1. 输入用户名，性别、年龄
2. 输出：你好XXX先生(女士)，您的年龄低于(高于)18岁，(不)可以进入.
'''

username = input("输入用户名: ")
sex = input("输入性别 [man | woman]: ")
age = input("输入年龄: ")

mid_age = 18
var_sex = ""
var_age = ""
var_enter = ""

'''
if sex == "man":
    var_sex = "先生"
elif sex == "woman":
    var_sex = "女士"
'''

if sex == "man":
    var_sex = "先生"
else:
    if sex == "woman":
        var_sex = "女士"


if int(age) > mid_age:
    var_age = "高于"
    var_enter = ""
elif int(age) < mid_age:
    var_age = "低于"
    var_enter = "不"

# Version1
print("你好", username, var_sex, ",", "您的年龄", var_age, "18岁, ", var_enter, "可以进入.")


# Version2 字符串格式化
print("你好{}{}，您的年龄{}18岁，{}可以进入.".format(username, var_sex, var_age, var_enter))
