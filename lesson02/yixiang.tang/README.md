# homework01： 字符串方法 和 列表方法 中文文档
## 字符串 (string)
#### 1. 基本语法 (string不能修改，只能赋值)
```python
name = 'monkey'
name = "monkey1"
name = '''monkey1'''
```

### 2. 特殊字符
#### a. 转义符 "\\"
###### 示例
```
print('\'monkey\'')
```
###### 输出
``` 
'monkey'
``` 
#### b. 换行符 "\n"
###### 示例
```
print("monkey\n abc")
```
###### 输出
``` 
monkey
 abc
``` 
#### c. tab格式符 "\t"
###### 示例
```
print('''mon \t key''')
```
###### 输出
``` 
monkey    key
``` 

### 3. 取值
#### a. 直接取值(常用)
###### 示例
```python
name = 'monkey'
print(name)
```
###### 输出
```
monkey
```
#### b. 依据字符串索引取值
索引取值范围: [-len(s), len(s)) 左闭右开
###### 示例
```python
name = 'monkey1'
print("name[0]: ", name[0])
print("name[-len(-5)]: ", name[-5])
print("name[len(s)]: ", name[len(name) - 1])
print("name[-len(s)]: ", name[-len(name)])

print('\n====== for 循环 string 索引取值 =====')
for i in range(len(name)):
    print(name[i])
```
###### 输出
```
name[0]: m
name[-len(-5)]: n
name[len(s)]: 1
name[-len(s)]: m

====== for 循环 string 索引取值 =====
m
o
n
k
e
y
1
```

### 4. 常用函数
#### a. count()方法
count() 用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
###### 语法
```
str.count(sub, start= 0,end=len(string))
```
###### 参数说明
```
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
```
###### 返回值
```
字符串在字符串中出现的次数
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print("str.count('n'): ", name.count('n'))
print("str.count('name'): ", name.count('name'))
```
###### 输出
```
str.count('n'):  2
str.count('name'):  1
```

#### b. startswith()方法
startswith() 检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。
###### 语法
```
str.startswith(str, beg=0,end=len(string))
```
###### 参数说明
```
str -- 检测的字符串
beg -- 可选参数用于设置字符串检测的起始位置
end -- 可选参数用于设置字符串检测的结束位置
```
###### 返回值
```
字符串以指定字符开头返回True，否则返回False。
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.startswith('my'))
print(name.startswith('is'))
print(name.startswith('name', 3, len(name)))
```
###### 输出
```
True
False
True
```

#### c. endswith()方法
endswith() 判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True
###### 语法
```
str.endswith(suffix[, start[, end]])
```
###### 参数说明
```
suffix -- 该参数可以是一个字符串或者是一个元组
start -- 开始位置。
end -- 结束位置。
```
###### 返回值
```
字符串含有指定的后缀返回True，否则返回False
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.endswith('!!!'))
print(name.endswith('is'))
print(name.endswith('sa si gi', 0, 19))
```
###### 输出
```
True
False
True
```

#### d. find()方法
find() 检测字符串中是否包含子字符串 
###### 语法
```
str.find(str, beg=0, end=len(string))
```
###### 参数说明
```
str -- 指定检索的字符串
beg -- 开始索引，默认为0
end -- 结束索引，默认为字符串的长度
```
###### 返回值
```
包含子字符串返回开始的索引值，否则返回-1
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.find('!!!'))
print(name.find('is'))
print(name.find('sa si gi', 0, 10))
```
###### 输出
```
19
8
-1
```

#### e. format()方法
format() 执行字符串的格式化操作, 它通过{}和:来代替传统%方式<br/>
摘录部分，尊重原创：https://blog.csdn.net/jpch89/article/details/84099277
###### 语法
```
.format
```
###### 参数说明
```
略
```
###### 返回值
```
返回字符串的副本，每个被替换与替换字段对应的参数值的字符串
```
###### 示例1:花括号内省略字段名，传递位置参数
```python
# 省略字段名传递位置参数
print('我叫{}，今年{}岁。'.format('sa si gi', 18))

# 花括号个数可以少于位置参数的个数
print('我爱吃{}和{}。'.format('香蕉', '苹果', '大鸭梨'))

# 花括号个数多于位置参数的个数则会报错
# print('我还吃{}和{}。'.format('西红柿'))
```
###### 示例1:输出
```
我叫sa si gi，今年18岁。
我爱吃香蕉和苹果。
"""
IndexError: tuple index out of range
"""
```
###### 示例2:过数字形式的简单字段名传递位置参数
```python
# 通过数字形式的简单字段名传递位置参数
print('身高{0}，家住{1}。'.format(1.8, '铜锣湾'))

# 数字形式的简单字段名可以重复使用。
print('我爱{0}。\n她今年{1}。\n{0}也爱我。'.format('阿香', 17))

# 体会把所有位置参数整体当成元组来取值
print('阿香爱吃{1}、{3}和{0}。'.format('榴莲', '臭豆腐', '皮蛋', '鲱鱼罐头', '螺狮粉'))
```
###### 示例2:输出
```
身高1.8，家住铜锣湾。
我爱阿香。她今年17。阿香也爱我。
阿香爱吃臭豆腐、鲱鱼罐头和榴莲。
"""
IndexError: tuple index out of range
"""
```

#### f. index()方法
index() 检测字符串中是否包含子字符串
###### 语法
```
str.index(str, beg=0, end=len(string))
```
###### 参数说明
```
str -- 指定检索的字符串
beg -- 开始索引，默认为0
end -- 结束索引，默认为字符串的长度
```
###### 返回值
```
包含子字符串返回开始的索引值，否则抛出异常
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.find('!!!'))
print(name.find('is'))
print(name.find('sa si gi', 0, 10))
```
###### 输出
```
19
8
"""
File "H:/51reboot-vm/lesson2/test.py", line 4, in <module>
    print(name.index('sa si gi', 0, 10))
ValueError: substring not found
"""
```

#### g. isdigit()方法
isdigit() 检测字符串是否只由数字组成
###### 语法
```
str.isdigit()
```
###### 参数说明
```
无
```
###### 返回值
```
字符串只包含数字则返回 True 否则返回 False
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.isdigit())
name = '456'
print(name.isdigit())
```
###### 输出
```
False
True
```

#### h. islower()方法
islower() 检测字符串是否由小写字母组成
###### 语法
```
str.islower()
```
###### 参数说明
```
无
```
###### 返回值
```
字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
```
###### 示例
```python
name = 'My'
print(name.islower())
name = 'my'
print(name.islower())
name = '456'
print(name.islower())
```
###### 输出
```
False
True
False
```

#### i. isupper()方法
isupper() 检测字符串中所有的字母是否都为大写
###### 语法
```
str.isupper()
```
###### 参数说明
```
无
```
###### 返回值
```
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
```
###### 示例
```python
name = 'MY'
print(name.isupper())
name = 'My'
print(name.isupper())
name = '456'
print(name.isupper())
```
###### 输出
```
True
False
False
```

#### j. join()方法
join() 用于将序列中的元素以指定的字符连接生成一个新的字符串
###### 语法
```
str.join(sequence)
```
###### 参数说明
```
sequence -- 要连接的元素序列
```
###### 返回值
```
返回通过指定字符连接序列中元素后生成的新字符串
```
###### 示例
```python
x = '-'
seq = ('sa', 'si', 'gi')
print(x.join(seq))
```
###### 输出
```
sa-si-gi
```

#### k. ljust()方法
ljust() 使字符串变成指定长度的左对齐
###### 语法
```
str.ljust(width[, fillchar])
```
###### 参数说明
```
width -- 指定字符串长度
fillchar -- 填充字符，默认为空格
```
###### 返回值
```
返回左对齐字符串, 并用空格填充至指定长度的新字符串, 如果指定的长度小于原字符串的长度则返回原字符串
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.ljust(10, '0'))
print(name.ljust(30, '0'))
```
###### 输出
```
my name is sa si gi!!!
my name is sa si gi!!!00000000
```

#### l. rjust()方法
rjust() 使字符串变成指定长度的右对齐
###### 语法
```
str.rjust(width[, fillchar])
```
###### 参数说明
```
width -- 指定填充指定字符后中字符串的总长度
fillchar -- 填充的字符，默认为空格
```
###### 返回值
```
返回右对齐字符串, 并用空格填充至指定长度的新字符串, 如果指定的长度小于原字符串的长度则返回原字符串
```
###### 示例
```python
name = 'My Name Is Sa Si Gi!!!'
print(name.rjust(10))
print(name.rjust(30))
print(name.rjust(30, '0'))
```
###### 输出
```
My Name Is Sa Si Gi!!!
        My Name Is Sa Si Gi!!!
00000000My Name Is Sa Si Gi!!!
```


#### m. lower()方法
lower() 转换字符串中所有大写字符为小写
###### 语法
```
str.lower()
```
###### 参数说明
```
无
```
###### 返回值
```
返回将字符串中所有大写字符转换为小写后生成的字符串
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.lower())
name = 'My Name Is Sa Si Gi!!!'
print(name.lower())
name = 'MY NAME IS SA SI GI!!!'
print(name.lower())
```
###### 输出
```
my name is sa si gi!!!
my name is sa si gi!!!
my name is sa si gi!!!
```

#### n. upper()方法
upper() 转换字符串中所有小写字符为大写字母
###### 语法
```
str.upper()
```
###### 参数说明
```
无
```
###### 返回值
```
返回将字符串中所有小写字符转换为大写后生成的字符串
```
###### 示例
```python
name = 'my name is sa si gi!!!'
print(name.upper())
name = 'My Name Is Sa Si Gi!!!'
print(name.upper())
name = '123456'
print(name.upper())
```
###### 输出
```
MY NAME IS SA SI GI!!!
MY NAME IS SA SI GI!!!
123456
```

#### o. lstrip()方法
lstrip() 用于截掉字符串左边的空格或指定字符
###### 语法
```
str.lstrip([chars])
```
###### 参数说明
```
chars --指定截取的字符
```
###### 返回值
```
返回截掉字符串左边的空格或指定字符后生成的新字符串
```
###### 示例
```python
name = '       My Name Is Sa Si Gi!!!'
print(name.lstrip())
name = '0000000My Name Is Sa Si Gi!!!'
print(name.lstrip('0'))
```
###### 输出
```
My Name Is Sa Si Gi!!!
My Name Is Sa Si Gi!!!
```

#### p. replace()方法
replace() 把字符串中的 old（旧字符串） 替换成 new(新字符串)
###### 语法
```
str.replace(old, new[, max])
```
###### 参数说明
```
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
```
###### 返回值
```
返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串
```
###### 示例
```python
name = 'My Name Is Sa Si Gi!!!'
print(name.replace(' ', '-'))
print(name.replace(' ', '-', 2))
```
###### 输出
```
My-Name-Is-Sa-Si-Gi!!!
My-Name-Is Sa Si Gi!!!
```

#### q. split()方法
split() 把字符串进行指定次数的切片
###### 语法
```
str.split(str="", num=string.count(str))
```
###### 参数说明
```
str -- 分隔符，默认为空格
num -- 分割次数
```
###### 返回值
```
返回分割后的字符串列表
```
###### 示例
```python
name = 'My Name | Is Sa Si Gi!!!'
print(name.split())
print(name.split('|'))
print(name.split(maxsplit=3))
print(name.split(' ', 4))
```
###### 输出
```
['My', 'Name', '|', 'Is', 'Sa', 'Si', 'Gi!!!']
['My Name ', ' Is Sa Si Gi!!!']
['My', 'Name', '|', 'Is Sa Si Gi!!!']
['My', 'Name', '|', 'Is', 'Sa Si Gi!!!']
```

#### r. strip()方法
strip() 用于移除字符串头尾指定的字符
###### 语法
```
str.strip([chars])
```
###### 参数说明
```
chars -- 移除字符串头尾指定的字符，默认为空格
```
###### 返回值
```
返回移除字符串头尾指定的字符生成的新字符串
```
###### 示例
```python
name = '     My Name | Is Sa Si Gi!!!'
print(name.strip())
name = '00000My Name | Is Sa Si Gi!!!00000'
print(name.strip('0'))
```
###### 输出
```
My Name | Is Sa Si Gi!!!
My Name | Is Sa Si Gi!!!
```



## 列表 (list)
#### 1. 基本语法 
```python
x = []
x = [2, 3.14, 'hello world', True]
```

### 2. 取值
#### a. 索引取值(常用)
索引取值范围: [-len(list), len(list)) 左闭右开
###### 示例
```python
x = [2, 3.14, 'hello world', True]
print("索引取值", x[1])
print("索引取值", x[-2])
print("索引取值", x[len(x) -1])
print("索引取值", x[- len(x)])

print('\n====== for 循环 x 列表取值 =====')
for l in x:
    print(l)
```
###### 输出
```
索引取值 3.14
索引取值 hello world
索引取值 True
索引取值 2

====== for 循环 x 列表取值 =====
2
3.14
hello world
True
```

#### b. 切片取值
###### 语法
```
list[start:end:step]
```
###### 参数
```
start -- 开始位置索引，默认为0
end -- 结束位置索引，默认为列表长度
step -- 每次执行索引步调，默认为1
```
###### 示例
```python
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
```
###### 输出
```
原始集合: {} [1, 2, 3, 4, 5, 6]
切片： []
切片 l1[-2: 4]： []
切片 l1[-10: 4]： [1, 2, 3, 4]
切片 l1[1::1]： [2, 3, 4, 5, 6]
```

### 3. 常用函数
#### a. append()方法
append() 用于在列表末尾添加新的对象
###### 语法
```
list.append(obj)
```
###### 参数说明
```
obj -- 添加到列表末尾的对象
```
###### 返回值
```
无返回值, 但是会修改原来的列表
```
###### 示例
```python
x = [2, 3.14, 'hello world', True]
print(x)
x.append(3)
print(x)
```
###### 输出
```
[2, 3.14, 'hello world', True]
[2, 3.14, 'hello world', True, 3]
```

#### b. count()方法
count() 统计某个元素在列表中出现的次数
###### 语法
```
list.count(obj)
```
###### 参数说明
```
obj -- 列表中统计的对象
```
###### 返回值
```
元素在列表中出现的次数
```
###### 示例
```python
x = [3, 3.14, 'hello world', True, 3]
print(x.count(2))
print(x.count(3))
```
###### 输出
```
0
2
```

#### c. extend()方法
extend() 用于在列表末尾一次性追加另一个序列中的多个值
###### 语法
```
list.extend(seq)
```
###### 参数说明
```
seq -- 元素列表
```
###### 返回值
```
元素在列表中出现的次数
```
###### 示例
```python
x1 = [3, 3.14, 'hello world', True, 3]
x2 = [2, 2, 1, 3]
x2.extend(x1)
print(x1)
print(x2)
```
###### 输出
```
[3, 3.14, 'hello world', True, 3]
[2, 2, 1, 3, 3, 3.14, 'hello world', True, 3]
```

#### d. index()方法
index() 用于从列表中找出某个值第一个匹配项的索引位置
###### 语法
```
list.index(obj)
```
###### 参数说明
```
obj -- 查找的对象
```
###### 返回值
```
返回查找对象的索引位置，如果没有找到对象则抛出异常
```
###### 示例
```python
x1 = [3, 3.14, 'hello world', True, 3]
print(x1.index(3))
print(x1.index('hello world'))
print(x1.index(2))
```
###### 输出
```
0
2
"""
ValueError: 2 is not in list
"""
```

#### e. insert()方法
insert() 用于从列表中找出某个值第一个匹配项的索引位置
###### 语法
```
list.insert(index, obj)
```
###### 参数说明
```
index -- 对象 obj 需要插入的索引位置
obj -- 要插入列表中的对象
```
###### 返回值
```
没有返回值，但会在列表指定位置插入对象
```
###### 示例
```python
x1 = [3, 3.14, 'hello world', True, 3]
x1.insert(2, "add")
print(x1)
```
###### 输出
```
[3, 3.14, 'add', 'hello world', True, 3]
```

#### f. pop()方法
pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
###### 语法
```
list.pop([index])
```
###### 参数说明
```
index -- 可选参数，默认值：-1
```
###### 返回值
```
返回从列表中移除的元素对象
```
###### 示例
```python
x1 = [3, 3.14, 'hello world', True, 3]
x1.pop()
print(x1)
x1.pop(1)
print(x1)
```
###### 输出
```
[3, 3.14, 'hello world', True]
[3, 'hello world', True]
```

#### f. remove()方法
remove() 移除列表中某个值的第一个匹配项
###### 语法
```
list.remove(obj)
```
###### 参数说明
```
obj -- 列表中要移除的对象
```
###### 返回值
```
没有返回值但是会移除列表中的某个值的第一个匹配项
```
###### 示例
```python
x1 = [3, 3.14, 'hello world', True, 3]
x1.remove(3)
print(x1)
x1.remove(True)
print(x1)
```
###### 输出
```
[3.14, 'hello world', True, 3]
[3.14, 'hello world', 3]
```

#### g. reverse()方法
reverse() 反向列表中元素
###### 语法
```
list.reverse()
```
###### 参数说明
```
无
```
###### 返回值
```
没有返回值，但是会对列表的元素进行反向排序
```
###### 示例
```python
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(x1)
x1.reverse()
print(x1)
```
###### 输出
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1]
```

#### h. sort()方法
sort() 对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
###### 语法
```
list.sort(key=None, reverse=False)
```
###### 参数说明
```
key -- 进行比较的元素
reverse -- 排序规则，reverse = True 降序，reverse = False 升序（默认）
```
###### 返回值
```
没有返回值，但是会对列表的对象进行排序
```
###### 示例
```python
x1 = [1, 6, 4, 7, 0, -1, 5, 8, 9]
x1.sort()
print("x1.sort(): ", x1)
x1.sort(reverse=True)
print("x1.sort(reverse=True): ", x1)

x1 = ['s', 'b', 'q', 'l', 'p']
x1.sort()
print("\nx1.sort(): ", x1)
x1.sort(reverse=True)
print("x1.sort(reverse=True): ", x1)
```
###### 输出
```
x1.sort():  [-1, 0, 1, 4, 5, 6, 7, 8, 9]
x1.sort(reverse=True):  [9, 8, 7, 6, 5, 4, 1, 0, -1]

x1.sort():  ['b', 'l', 'p', 'q', 's']
x1.sort(reverse=True):  ['s', 'q', 'p', 'l', 'b']
```


