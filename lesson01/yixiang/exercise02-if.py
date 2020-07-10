# 需求：
#     输入分数，评等级
#     输出，your score is <80>, get a grade <B>


score = int(input("Please input your score: "))
level = 'E'
if score > 89:
    level = 'A'
elif score > 79:
    level = 'B'
elif score > 69:
    level = 'C'
elif score > 59:
    level = 'D'

print("your score is {}, get a grade {}" .format(score, level))
