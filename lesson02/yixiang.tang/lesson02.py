#!/usr/local/python36/bin/python3.6

# ========== 字符串基本操作，分隔线 ==========
# string不能修改，只能赋值
# 从左往右依次为：0,1,2,3,...,n-1
# 从右往左依次为：-1,-2,-3,...,-n
# 下标取值范围： [-len(s), len(s)) 【- len(s) <= s.index < len(s)】
name = 'monkey \''
print(name)
name = "mon \n key"
print(name)
name = '''mon \t key'''
print(name)
name = "monkey"
print("name[0]: {}, name[4]: {}, name[5]: {}" .format(name[0], name[4], name[5]))
print("name[-1]: {}, name[-2]: {}" .format(name[-1], name[-2]))
# print("name[6]: {}", name[6]) 'monkey' #无6下标，报错
# name[0] = '1' print(name) #String不能修改，只能赋值


name = "monkey zxz"
print(len(name))
print("name:{} \nmin(name): {}, max(name):{}".format(name, min(name), max(name)))
print('m' in name)
print('hello' in name)
print("name.find('m') return index: {}" .format(name.find("z")))
print("name.find('m', 1) return index: {}" .format(name.find("z", 2)))

print('====== for 打印string =====')
for i in range(len(name)):
    print(name[i])

print('====== while中的else将在不满足while循环条件时，执行一次 =====')
i = 0
while i < len(name):
    print("i: {}, name: {}" .format(i, name[i]))
    i += 1
else:
    print(name)

print("\n========== list, 分隔线 ==========")
# ========== list, 分隔线 ==========
x = [2, 3.14, 'hello world', True]
print(x)
# 删除x中的value值
x.remove(2)
print(x)
# pop获取第一个元素，并从list中删除
i = x.pop(0)
print("i: {}, x: {}".format(i, x))
# append 追加一个值
x.append("add")
print(x)
# reverse() 反转集合
x.reverse()
print("reverse(): ", x)
# index() 返回值所在index索引的下标
x = [5, 12, 32, 4, 2, 10, 25]
print("x: {}, index(2): {}" .format(x, x.index(32)))
# count() 统计列表中value的出现次数
x.append(2)
print("x: {}, count(2): {}" .format(x, x.count(2)))
x.append(2)
print("x: {}, count(2): {}" .format(x, x.count(2)))


print("\n ===== sort =====")
x = [5, 12, 32, 4, 2, 10, 25]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

print("\n ===== sorted =====")
s = "68301897889713"
# sorted 排序并返回一个新的集合
l1 = sorted(s)
print("升序: 原始列表：{}\n最终列表：{}" .format(s, l1))
s1 = "".join(l1)
print("升序: 原始列表：{}\n最终列表：{}" .format(s, s1))
# 反正升序列表，则变成降序列表
l1.reverse()
s2 = "".join(l1)
print("降序: 原始列表：{}\n最终列表：{}" .format(s, s2))

print("\n ===== extend([]) =====")
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = []
for i in range(len(l1)):
    l3.extend([l1[i], l2[i]])
print(l3)


print("\n ===== 切片(语法：list[start:end:sep]， 遵循左闭右开原则), 分隔线  =====")
# 切片的 start > len(s)，则slice为空。
l1 = [1, 2, 3, 4, 5, 6]
s = l1[10: 1]
print("原始集合: {}", l1)
print("切片：", s)
# 切片的 |startIndex| < |endIndex|, 无论正负，最后若开始索引位置在结束索引位置之后,则切片为空
s = l1[-2: 4]
print("切片 l1[-2: 4]：", s)
s = l1[-10: 4]
print("切片 l1[-10: 4]：", s)
# 从下标为1的开始，以len(l1)结束，每隔2切一次
s = l1[1::2]
print("切片 l1[1::2]：", s)

print("\n========== list函数 分隔线 ==========")
x = [1, 2, 3, 4, 5, 6, 10, 35, -1]
print(len(x))
print(max(x))
print(min(x))



