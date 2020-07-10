<!--ts-->
   * [作业](#作业)
      * [1.1，字符串方法](#11字符串方法)
         * [.count](#count)
         * [.startswith](#startswith)
         * [.endswith](#endswith)
         * [.find](#find)
         * [.format](#format)
         * [.index](#index)
         * [.isdigit](#isdigit)
         * [.islower](#islower)
         * [.isupper](#isupper)
         * [.join](#join)
         * [.ljust](#ljust)
         * [.lower](#lower)
         * [.lstrip](#lstrip)
         * [.replace](#replace)
         * [.rjust](#rjust)
         * [.split](#split)
         * [.strip](#strip)
         * [.upper](#upper)
      * [1.2，列表方法](#12列表方法)
         * [.append](#append)
         * [.count](#count-1)
         * [.extend](#extend)
         * [.index](#index-1)
         * [.insert](#insert)
         * [.pop](#pop)
         * [.remove](#remove)
         * [.reverse](#reverse)
         * [.sort](#sort)
      * [2，用户管理系统](#2用户管理系统)
      * [3，冒泡排序](#3冒泡排序)

<!-- Added by: root, at: 2019-05-23T16:28+0800 -->

<!--te-->

# 作业

## 1.1，字符串方法

> 写成docstring中文文档README.md

>>> dir(str)  

```plain
python中字符串是不可变对象，所以所有修改和生成字符串的操作的实现方法都是从另一个内存片段中新生成一个字符串对象。
例如，'abc'.upper()将会在划分另一个内存片段，并将返回的ABC保存在此内存中。
```

### .count

**子串搜索**
```
返回字符串S中子串sub出现的次数，可以指定从哪里开始计算(start)以及计算到哪里结束(end)，索引从0开始计算，不包括end边界。
```
> S.count(sub[, start[, end]])

### .startswith

> S.startswith(prefix[, start[, end]])
```
判断字符串S是否是以prefix开头。
```
### .endswith

> S.endswith(suffix[, start[, end]])
```
检查字符串S是否以suffix结尾，返回布尔值的True和False。suffix可以是一个元组(tuple)。可以指定起始start和结尾end的搜索边界。
```
### .find

> S.find(sub[, start[, end]])
```
搜索字符串S中是否包含子串sub，如果包含，则返回sub的索引位置，否则返回"-1"。可以指定起始start和结束end的搜索位置。
```
### .format
```
> 使用 { 和 } 来标记变量将被替换的位置，并且可以提供详细的格式化指令，但你还需要提供要格式化的信息。
格式化输出
```

### .index

> S.index(sub[, start[, end]])
```
和find()一样，唯一不同点在于当找不到子串时，抛出ValueError错误。
```
### .isdigit

> S.isdigit()
```
测试字符串S是否是数字
```
### .islower

> S.islower()
```
判断是否小写,要求S中至少要包含一个字符串字符，否则直接返回False。
```
### .isupper

> S.isupper()
```
判断是否大写,要求S中至少要包含一个字符串字符，否则直接返回False。
```
### .join

> S.join(iterable)
```
将可迭代对象(iterable)中的元素使用S连接起来。注意，iterable中必须全部是字符串类型，否则报错。
```
### .ljust

> S.ljust(width[, fillchar])
```
ljust()使用fillchar填充在字符串S的右边，使得整体长度为width。
```
### .lower

> S.lower()
```
返回S字符串的小写
```
### .lstrip

> S.lstrip([chars])
```
分别是移除左边的字符char。如果不指定chars或者指定为None，则默认移除空白(空格、制表符、换行符)。

唯一需要注意的是，chars可以是多个字符序列。在移除时，只要是这个序列中的字符，都会被移除。
```
### .replace

> S.replace(old, new[, count])

```shell
>>> print('abcxyzoxy'.replace('xy','XY',1))
abcXYzoxy
>>> 
>>> print('abcxyzoxy'.replace('xy','XY',2)) 
abcXYzoXY
>>> print('abcxyzoxy'.replace('mm','XY',2))  
abcxyzoxy
```
```
将字符串中的子串old替换为new字符串，如果给定count，则表示只替换前count个old子串。如果S中搜索不到子串old，则无法替换，直接返回字符串S(不创建新字符串对象)。
```
### .rjust

> S.rjust(width[, fillchar])
```
ljust()使用fillchar填充在字符串S的左边，使得整体长度为width。如果不指定fillchar，则默认使用空格填充。如果width小于或等于字符串S的长度，则无法填充，直接返回字符串S(不会创建新字符串对象)。
```
### .split

> S.split(sep=None, maxsplit=-1)
```
根据sep对S进行分割，maxsplit用于指定分割次数，如果不指定maxsplit或者给定值为"-1"，则会从左向右搜索并且每遇到sep一次就分割直到搜索完字符串。如果不指定sep或者指定为None，则改变分割算法：以空格为分隔符，且将连续的空白压缩为一个空格。
```
### .strip

> S.strip([chars])
```
分别是移除左右两边的字符char。如果不指定chars或者指定为None，则默认移除空白(空格、制表符、换行符)。唯一需要注意的是，chars可以是多个字符序列。在移除时，只要是这个序列中的字符，都会被移除。
```
### .upper

> S.upper()
```
返回S字符串的大写格式。
```

## 1.2，列表方法 
>>> dir(list)    

### .append

在列表末尾添加元素

- append中添加的参数是作为一个整体
- append一次性只能添加一个元素

### .count

统计某个元素在列表中出现的次数

### .extend

在原列表追加另一个序列的中的多个值

```python
>>> name = list("scott")
>>> 
>>> name
['s', 'c', 'o', 't', 't']

>>> name.extend(list('xoyabc'))
>>> 
>>> name
['s', 'c', 'o', 't', 't', 't', 'i', 'g', 'e', 'r', 'x', 'o', 'y', 'a', 'b', 'c']
```

- 分片赋值

```python
>>> name = list("scott")
>>> 
>>> name
['s', 'c', 'o', 't', 't']
>>> name[len(name):] = list('tiger')
>>> name
['s', 'c', 'o', 't', 't', 't', 'i', 'g', 'e', 'r']
```

- 操作符”+”

```python
>>> name = list("scott")
>>> 
>>> test = list('xoyabc')
>>> 
>>> print (name+test)
['s', 'c', 'o', 't', 't', 'x', 'o', 'y', 'a', 'b', 'c']
```

### .index

从列表中找出某个值第一个（注意是第一个）匹配项的索引位置

```python
>>> name
['s', 'c', 'o', 't', 't']
>>> 
>>> name.index('t')
3
```

### .insert

用于将对象插入到列表中，两个参数，第一个是索引位置，第二个插入的元素对象。

```python
>>> name = list('xoyabc')     
>>> name
['x', 'o', 'y', 'a', 'b', 'c']
>>> name.insert(1, 'nihao') 
>>> name
['x', 'nihao', 'o', 'y', 'a', 'b', 'c']
```

### .pop

移除列表中的一个元素（最后一个元素），并返回该元素的值

```python
>>> name
['x', 'nihao', 'o', 'y', 'a', 'b', 'c']
>>> 
>>> 
>>> name.pop()
'c'
>>> 
>>> name
['x', 'nihao', 'o', 'y', 'a', 'b']
>>> 
```

### .remove

移除列表中某个值的第一匹配项。

- 如果有俩个相等的元素，就只是移除匹配的一个元素
- 如果某元素不存在某列表中，便会报错
- 一次性只能 移除一个元素。

```python
>>> name
['x', 'nihao', 'o', 'y', 'a', 'b']
>>> 
>>> name.remove('b')
>>> name
['x', 'nihao', 'o', 'y', 'a']

# 元素不存在，则报错
>>> name.remove('w')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
# 一次性只能 移除一个元素。
>>> name.remove('w', 'i')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (2 given)
```

### .reverse

将列表中的元素反转

```python
>>> name
['x', 'nihao', 'o', 'y', 'a']
>>> 
>>> 
>>> name.reverse()
>>> 
>>> name
['a', 'y', 'o', 'nihao', 'x']
```

### .sort

sort方法用于对列表进行排序，修改原列表，不会返回一个已排序的列表副本

```python
>>> name
['a', 'y', 'o', 'nihao', 'x']
>>> 
>>> 
>>> name.sort()
>>> 
>>> name
['a', 'nihao', 'o', 'x', 'y']
```


## 2，用户管理系统
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

```shell
[root@51reboot lesson02]# python homework_01_user_mgt_system.py
Please input your username: 11
Please input your password: 11
 username or password error,you have 5 times to input 
Please input your username: 11
Please input your password: 11
 username or password error,you have 4 times to input 
Please input your username: 11
Please input your password: 11
 username or password error,you have 3 times to input 
Please input your username: admin
Please input your password: 123456
Please input the action and info: add xiaoming 20 18212345678 1234@qq.com
add 'xiaoming 20 18212345678 1234@qq.com' succeed
Please input the action and info: add xiaohong 18 18233335678 6666@qq.com
add 'xiaohong 18 18233335678 6666@qq.com' succeed
Please input the action and info: add xiaohong 18 18233335678 6666@qq.com
'xiaohong 18 18233335678 6666@qq.com' is already added
Please input the action and info: find xiaohong
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaohong   |18  |18233335678   |6666@qq.com         
Please input the action and info: update xiaoming set age = 22
Please input the action and info: find xiaoming
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |22  |18212345678   |1234@qq.com         
Please input the action and info: update xiaoming set age=23          
Please input the action and info: find xiaoming
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |23  |18212345678   |1234@qq.com         
Please input the action and info: list
--------------------------------------------------------
|name       |age |Tel           |Email               
--------------------------------------------------------
|xiaoming   |23  |18212345678   |1234@qq.com         
--------------------------------------------------------
|xiaohong   |18  |18233335678   |6666@qq.com         
Please input the action and info: 
```


## 3，冒泡排序
```bash
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。

```

```shell
[root@51reboot lesson02]# ./bubble_sort.py  
第1次比较后的数组：
[3, 2, 5, 7, 11, 20]
第2次比较后的数组：
[2, 3, 5, 7, 11, 20]
第3次比较后的数组：
[2, 3, 5, 7, 11, 20]
第4次比较后的数组：
[2, 3, 5, 7, 11, 20]
第5次比较后的数组：
[2, 3, 5, 7, 11, 20]
```
