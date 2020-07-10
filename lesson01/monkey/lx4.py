

'''
需求：
1. 输入分数，评等级
2. 输出
如果分数>= 90, 评分是A.
如果分数>= 80, 小于90, 评分是B.
如果分数>= 70, 小于80, 评分是C.
如果分数>= 60, 小于70, 评分是D.
如果分数<  60, 评分是E.
输出：your score is <80>, get <B>.
'''

score = input("输入分数: ")

score_int = int(score)
score_level = ""


if score_int >= 90:
    score_level = "A"
elif score_int >= 80 and score_int < 90:
    score_level = "B"
elif score_int >= 70 and score_int < 80:
    score_level = "C"
elif score_int >= 60 and score_int < 70:
    score_level = "D"
elif score_int < 60:
    score_level = "E"

print("your score is <{}>, get <{}>".format(score_int, score_level))