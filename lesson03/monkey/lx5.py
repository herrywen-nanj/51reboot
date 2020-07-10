lans = ['python', 'go', 'go', 'java', 'c', 'python', 'ruby', 'python']
dic = {}

for lan in lans:
    dic[lan] = dic.get(lan, 0) + 1  # 赋值
    print(">>>>>> dic: {}".format(dic))
    input()

print(dic)
