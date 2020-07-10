# 字符串方法  
### count方法:
用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置  
```python
str.count(sub, start= 0,end=len(string))
```
#### option:
* sub -- 搜索的子字符串
* start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
* end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
***

### startswith:
用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。  
```python
str.startswith(substr, beg=0,end=len(string));
```
#### option:  
* str -- 检测的字符串。
* substr -- 指定的子字符串。
* strbeg -- 可选参数用于设置字符串检测的起始位置。  
* strend -- 可选参数用于设置字符串检测的结束位置。
***

### endswith:
用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
```python
str.endswith(suffix[, start[, end]])
```
#### option:  
* suffix -- 该参数可以是一个字符串或者是一个元素。  
* start -- 字符串中的开始位置。  
* end -- 字符中结束位置。  
***

### find:
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
```python
str.find(str, beg=0, end=len(string))
```
#### option:
* str -- 指定检索的字符串
* beg -- 开始索引，默认为0。
* end -- 结束索引，默认为字符串的长度
***

### format:
增强了字符串格式化的功能。非常灵活，可指定位置，可不指定位置，可通过索引、字典设置参数
```python
"{} xxx".format("abc")
```

***
### index:
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
```python
str.index(str, beg=0, end=len(string))
```

#### option:
* str -- 指定检索的字符串
* beg -- 开始索引，默认为0。
* end -- 结束索引，默认为字符串的长度。
***

### isdigit:
检测字符串是否只由数字组成，返回True or False
```python
str.isdigit()
```

#### option:
无

-------------------------------------------------
### islower:
检测字符串是否由小写字母组成，返回True，只要字符串中包含一个大写字母都返回False
```python
str.islower()
```

#### option:
无
***

### isupper：
检测字符串是否由大写字母组成，返回True，只要字符串中包含一个小写字母都返回False
```python
str.isupper()
```

#### option:
无
***

### join:
用于将序列中的元素以指定的字符连接生成一个新的字符串。返回通过指定字符连接序列中元素后生成的新字符串。
```python
str.join(sequence)
```

#### option:
* sequence -- 要连接的元素序列

***

### ljust:
返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
```python
str.ljust(width[, fillchar])
```

#### option:
* width -- 指定字符串长度。
* fillchar -- 填充字符，默认为空格。
***

### lower:
转换字符串中所有大写字符为小写。返回转换后生成的字符串
```python
str.lower()
```

#### option:
无
***

### lstrip:
删除字符串左边的空格或指定字符。返回删除后生成的新字符串
```python
str.lstrip([chars])
```

#### option:
* chars --指定删除的字符
***

####replace:
把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。返回替换后的字符串
```python
str.replace(old, new[, max])
```

#### option:
* old -- 将被替换的子字符串。
* new -- 新字符串，用于替换old子字符串。
* max -- 可选字符串, 替换不超过 max 次
***

####rjust:
返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
```python
str.rjust(width[, fillchar])
```

#### option:
* width -- 指定填充指定字符后中字符串的总长度.
* fillchar -- 填充的字符，默认为空格。
***

### split:
通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num+1 个子字符串。返回分割后的字符串列表
```python
str.split(str="", num=string.count(str))
```

#### option:
* str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
* num -- 分割次数。默认为 -1, 即分隔所有。

***

### strip:
清除字符串左右两边的空格，等同于lstrip和rstrip同时执行。返回已清除的新字符串
```python
str.strip([chars])
```

#### option:
* chars -- 移除字符串头尾指定的字符序列。
***

### upper:
将字符串中的小写字母转为大写字母。返回小写字母转为大写字母的字符串。

```python
str.upper()
```

#### option:
无

***

# 列表
## 方法
### append:
用于在列表末尾添加新的对象。返回修改后的原列表
```python
list.append(obj)
```

#### option:
* obj -- 添加到列表末尾的对象
***

### count
统计某个元素在列表中出现的次数。返回元素在列表中出现的次数
```python
list.count(obj)
```

#### option
* obj -- 列表中统计的对象
***

### extend
用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
```python
list.extend(seq)
```

#### option
* seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
***

### index
用于从列表中找出某个值第一个匹配项的索引位置。返回查找对象的下标，如果没有找到对象则抛出异常
```python
list.index(obj)
```

#### option
* obj -- 查找对象
***

### insert:
用于将指定对象插入列表的指定位置。没返回值。谨慎使用，这会导致插入位置后的所有对象都重新插入一次
```python
list.insert(index, obj)
```

#### option
* index -- 对象obj需要插入的下标位置
* obj -- 要插入列表的对象。
***

### pop
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
```python
list.pop([index=-1])
```

#### option
* index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
***

### remove:
移除列表中某个值的第一个匹配项,没有返回值
```python
list.remove(obj)
```

#### option
* obj -- 列表中要移除的对象
***

### reverse
反向列表中元素。
```python
list.reverse()
```

#### option
无
***

### sort
对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。没有返回值
```python
list.sort( key=None, reverse=False)
```

#### option
* key -- 主要用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
* reverse -- 排序规则，reverse = True 降序，reverse = False 升序（默认）
***

### clear
清空列表
```python
list.clear()
```

#### option
无
***

### copy
复制列表，返回复制后的新列表
```python
list.copy()
```

#### option
无
***

## 函数
```python
len(list)   //列表元素个数
max(list)   //返回列表元素最大值
min(list)   //返回列表元素最小值
list(seq)   //将seq对象转换为列表

```


