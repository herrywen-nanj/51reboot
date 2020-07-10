lans = ['python', 'go', 'go', 'java', 'c', 'python', 'ruby', 'python']
dic = {}

for lan in lans:
    print(">>>>>> dic: {}".format(dic))
    if lan not in dic:
        print(lan, 1)
        dic[lan] = 1
    else:
        before_value = dic[lan] # dic['python'] -> 1
        after_value = before_value + 1
        # d['python'] = 2 + 1
        dic[lan] = after_value  # 修改
        print("xxxxxxxxxxxxxxxx lan: {}, count: {}".format(lan, after_value))
    input()

print(dic)
