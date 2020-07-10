# 作业

## 1: 字符串方法 和 列表方法 
> 写成docstring中文文档README.md


### dir(str)  

.count  

统计元素在字符串出现的次数 

return int
```bash
str1 = "abcd"
print(str1.count("a"))
>>> 1
```

.startswith   

判断字符串是否以某个元素开头

return bool

```python
str1 = "abcd"
print(str1.startswith("a"))
>>> True

```

.endswith

判断字符串是否以某个元素结尾

return bool

```python
str1 = "abcd"
print(str1.endswith("s"))
>>> False

```

.find

查找元素是否在字符串内，有返回索引，没有返回-1

return int

```python
str1 = "abcd"
print(str1.find("b"))
print(str1.find("s"))
>>> 1
   -1

```
.format

字符串格式华输出
```python
print("hello,{}==={}".format("hhh", "xxx"))
>>> hello,hhh===xxx

```
.index

查找元素索引值，有返回当前索引，没有报错
```python
str1 = "abcd"
print(str1.index("s"))

>>> ValueError: substring not found
```

.isdigit

判断字符串内是否是数字，

return bool

```python
str1 = "abcd"
str2 = "123"

print(str1.isdigit())

print(str2.isdigit())

>>>
False
True

```
.islower

检测字符串是否由小写字母组成

return bool

```python
str1 = "abcd"
str2 = "123"
str3 = "ABCD"

print(str1.islower())

print(str2.islower())

print(str3.islower())
>>>
True
False
False

```

.isupper

检测字符串是否由大写字母组成

return bool

```python
str1 = "abcd"
str2 = "123"
str3 = "ABCD"

print(str1.isupper())

print(str2.isupper())

print(str3.isupper())

>>>
False
False
True


```
.join

将序列中的元素以指定的字符连接生成一个新的字符串

return 新的字符串

```python
str1 = "-"
seq = ("a", "b", "c")

print(str1.join(seq))
>>>

a-b-c

```
.ljust

方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串

return 新的字符串
```python
str1 = "abcd"

print(str1.ljust(10, "x"))
>>>
abcdxxxxxx

```
.lower

转换字符串中所有大写字符为小写。

return 新的字符串

```python
str1 = "aBcd"

print(str1.lower())
>>
abcd

```

.lstrip

截掉 string 左边的空格
```python
str1 = "   aBcd"

print(str1.lstrip())
>>>
aBcd

```
.replace
把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次

```python
str0 = "   aBaaaacd"
str1 = "a"
str2 = "x"

print(str0.replace(str1, str2, 2))
>>>
   xBxaaacd

```
.rjust

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

.split

返回一个包含各行作为元素的列表

```python
str0 = "   aBaaaacd"

print(str0.split())
print(str0.split("a"))
>>>
['aBaaaacd']
['   ', 'B', '', '', '', 'cd']

```

.strip

去除字符串左右的空格

.upper

转换 string 中的小写字母为大写

### dir(list)   
 
.append 

list添加元素

return  None

```python
l = ["a", "b", "c"]

print(l.append("b"))
print(l)
>>>
None
['a', 'b', 'c', 'b']

```

.count

元素在list中出现的次数

```python
l = ["a", "b", "c"]

print(l.count("b"))

>>> 1

```
.extend

连个list合并

.index

查找元素在list的index

.insert

指定位置插入元素

.pop  

删除最后一个元素

.remove

删除指定元素

.reverse

list 反转

.sort

list 排序
```

## 2: 用户管理系统
```bash
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add
    3.2 删 delete
    3.3 改 update
    3.4 查 list
    3.5 搜 find
3. 格式化输出   
```

## 3: 冒泡排序
```bash
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。

```
