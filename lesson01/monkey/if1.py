
# 及格分数线
good_score = 60

'''
A 大于90
B 大于等于80 小于90
C 大于等于60 小于80
D 小于60

>
>=
<
<=
!=
== 比较
'''

score = input("请输入你的语文分数: ")
if int(score) >= good_score:
    print("你的语文分数及格了。")
    print("恭喜恭喜")
else:
    print("你的语文分数不及格。")
    print("好好学习")

