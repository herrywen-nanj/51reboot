#及格分数线
# good_socre = 60
#
# score = input("请输入你的语文分数: ")
# if int(score)>=good_socre:
#     print("你的成绩及格了！")
# else:
#     print("你的成绩不及格了！")
#
#
# #及格分数线
# a = 66
# c = 10
# b = input("请输入你的成绩：")
# if int(b)>=a:
#     print("你的成绩合格了！")
# elif int(b) < c:
#     print("你可以放弃了！")
# else:
#     print("你的成绩不合格！")



# s = num1 + emp + num2
# print(s)
# ####
# username = "kk"
# age = 20
# sex = "男"
# print("你的名字叫",username,"年龄是",age,"性别是",sex,"。")




# s = input("请输入你的名字：")
# age = input("请输入你的年龄：",)
# sex = input("请输入你的性别：")
#
# if int (age)<18:
#     print("你好",s,"先生(女士)","你的年龄低于18岁,不能进去。")
# elif int (age)>18:
#     print("你好",s,"先生(女士)","你的年龄大于18岁,能进去。")
#




# a = eval(input("请输入你的分数："))
# if a >= 90: print("your score is" ,a,"评分是A")
# elif a >= 80 < 90: print("your score is",a,"评分是B")
# elif a >= 70 < 80: print("your score is" ,a,"评分是C")
# elif a >= 60 < 70: print("your score is" ,a,"评分是D")
# elif a < 60: print("your score is" ,a,"评分是E")

# s = "1" * 9
# print(s)
# for x in s:
# print(x)

for i in range(1,10):
    for j in range(1,10):
        sum = i * j
        if i >= j:
          print('%d * %d = %d' % (i,j,sum),end='  ')
    print ('')


