<!--ts-->
 ```python
print('hello')
```
# 作业

## 字符串方法
### dir(str)  
```
>dir(str)
```
### .count
```统计字符串出现的总次数```
```python
str.count(sub, start=0, end=len(str))

>>>>s = "aaabbb"
>>>>s.count("a")
3
```
### .startswith
```判断字符串开头是否为某个字符，返回布尔值```
```python
str.startswith(prefix, start=0, end=len(str))

>>>>s.startswith("a")
True
```

### .endswith
```判断字符串末尾是否为某个字符，返回布尔值```
```python
str.endswith(suffix, start=0, end=len(str))

>>>>s.endswith("a")
False
```
### .find，当无法查找到对应值的时候则会返回-1
```查找字符串的索引位置，默认返回第一次出现的```
```python
str.find(sub, start=0, end=len(str))

>>>>s.find("b")
3
```

### .format,该方法不止用于字符串，也可用于列表
```字符串格式化方法,使用format("参数")来替换字符串中的{}标识的元素```
```python
>>>>"{}, {}, {}".format(s[2], s[6], s[8])
a, 3, 5
```
```列表示例
In [23]: b = [ 'a','b','c','d',1 ,2 ,3 ,4]                                                                                                                                                                  

In [24]: "我需要的这个字符串是{},还有是{},最后一个是{}".format(b[0],b[1],b[2])                                                                                                                              
Out[24]: '我需要的这个字符串是a,还有是b,最后一个是c'
```
### .index
```当查找成功时,index()方法与find()方法相同,返回最小的索引值```
```python
str.index(sub, start=0, end=len(str))

>>>>s.index("4")
7
```

### .isdigit
```如果str中的所有字符都是数字并且至少有一个字符是数字时,返回True,否则返回False```
```python
str.isdigit()

>>>>s.isdigit()
False
```


### .islower
```如果字符串中全为小写返回True,有大小写或者大写否则返回False```
```python
str.islower()

>>>>s.islower()
True
```

### .isupper
``` 如果字符串中全为大写返回True,有大写或者大小写字符返回False```
```python
str.isupper()

>>>>s.isupper()
False
```

### .join,不止用于字符串，大多用于列表的拼接
```方法用于将序列中的元素以指定的字符连接生成一个新的字符串```

```
str1 = "-";
seq = ("a", "b", "c"); # 字符串序列
print(str1.join(seq));
输出:a-b-c



### .upper
```Python upper() 方法将字符串中的小写字母转为大写字母。```
> S.upper()
```
In [67]: a = "AAAAAAAAAAAAAAAAAAAaBBBBBBBBBBBBBBBCCCCCm"
In [69]: a.upper()                                                                                                                                                                                        
Out[69]: 'AAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBCCCCCM'
```

### .lower
```Python lower() 方法将字符串中的大写字母转为小写字母。```
```pythonh
str.lower()

In [67]: a = "AAAAAAAAAAAAAAAAAAAaBBBBBBBBBBBBBBBCCCCCm"                                                                                                                                                    
In [68]: a.lower()                                                                                                                                                                         
Out[68]: 'aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbcccccm'
```

### .lstrip
```Python lstrip() 方法用于截掉字符串左边的空格或指定字符。```
```
str.lstrip(chars)
In [65]: c                                                                                                                                                                                                  
Out[65]: 'aaaaaaaaaabbbbbbbbbbbccccccccc'

In [66]: c.lstrip('a')                                                                                                                                                                                  
Out[66]: 'bbbbbbbbbbbccccccccc'
```

### .replace
```Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。```
```python
str.replace(old, new, count)
>>> print('abcxyzoxy'.replace('xy','XY',1))
abcXYzoxy
>>> 
>>> print('abcxyzoxy'.replace('xy','XY',2)) 
abcXYzoXY
>>> print('abcxyzoxy'.replace('mm','XY',2))  
abcxyzoxy
```

### .ljust
```Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。```
```python
a.rjust(width, fillchar)
In [76]: a = "这是左对齐测试！！"                                                                                                                                                                           

In [77]: a.ljust(50,'*')     #50是字符的宽度，*是填充的字符串                                                                                                                                                                                   
Out[77]: '这是左对齐测试！！*****************************************'
```

### .rjust
```rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。```
> S.rjust(width, fillchar)
```python
In [78]: a = "这是有对齐测试!!!!"                                                                                                                                      
In [79]: a.rjust(100,'*')                                                                                                                                                               
Out[79]: '*****************************************************************************************这是有对齐测试!!!!'
```


### .split
```Python split() 通过指定分隔符对字符串进行切片，返回值类型为列表```
```
a.split('char',num)
char是指定的分割符
num是指定的分割次数
In [85]: a = "this#is#test#html#this#is#is" 
In [86]: a.split('#')                                                                                                                                                                                       
Out[86]: ['this', 'is', 'test', 'html', 'this', 'is', 'is']

In [87]: a.split('#',1)                                                                                                                                                                                     
Out[87]: ['this', 'is#test#html#this#is#is']
```
### .strip
```Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。```
> a.strip([chars])
```
eg:
In [91]: a = "    adajsdkjasd adasdas ^^^thsi        "                                                                                                                                                      
In [92]: a.strip()                                                                                                                                                                                          
Out[92]: 'adajsdkjasd adasdas ^^^thsi'
```

## 1.2，列表方法 
>>> dir(list)    

### .append
```在列表末尾,添加新的对象```
a = ["1",21,True]
a.append(5)
print(a)
>>> ['1', 21, True, 5]


### .extend
扩展列表,一次性追加另一个序列的多个值,用新列表扩展原来的列表
```python
a = ['1', 21, True, 5, 21]
b = [3,4,5]
a.extend(b)
print(a)
>>> ['1', 21, True, 5, 21, 3, 4, 5]
```


### .insert
将指定对象插入列表指定位置
```python
a = ['1', 21, True, 5, 21, 3, 4, 5]
b = [3,4,5]
a.insert(1,b)
print(a)
>>> ['1', [3, 4, 5], 21, True, 5, 21, 3, 4, 5]
```

### .pop
```python
a = ['1', [3, 4, 5], 21, True, 5, 21, 3, 4, 5]
a.pop(1)  //删除索引值是1的元素
print(a)
>>> ['1', 21, True, 5, 21, 3, 4, 5]
```

### .remove
```按值来删除列表中的第一次匹配的元素```
```python
a = ['1', 21, True, 5, 21, 3, 4, 5]
a.remove(5)
print(a)
>>> ['1', 21, True, 21, 3, 4, 5]


### .reverse
反向排序列表元素
```python

a = ['1', 21, True, 21, 3, 4, 5]
a.reverse()
print(a)
>>> [5, 4, 3, 21, True, 21, '1']
```

### .sort
对于原列表进行排序，默认从小到大

```python
b = [4, 2, 5]
b.sort()
print(b)
>>> [2, 4, 5]

