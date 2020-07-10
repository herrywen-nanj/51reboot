
# 及格分数线
good_score = 60
low_score = 10

# 第一版
score = input("请输入你的语文分数: ")
if int(score) >= good_score:
    print("你的语文分数及格了。")
    print("恭喜恭喜")
elif int(score) < low_score: # elif --> else + if
    print("你可以放弃学习了.")
else:
    print("你的语文分数不及格。")
    print("好好学习")


# 第二版
score = input("请输入你的语文分数: ")
if int(score) >= good_score:
    print("你的语文分数及格了。")
    print("恭喜恭喜")
else:
    if int(score) < low_score:
        print("你可以放弃学习了.")
    else:
        print("你的语文分数不及格。")
        print("好好学习")

