### 字符串常用方法

```python
字符串常用的方法：
dir(str)
.count
.startswith
.endswith
.find
.format
.index
.isdigit
.islower
.isupper
.join
.ljust
.lower
.lstrip
.replace
.rjust
.split
.strip
.upper
```





#### 1.count

```python
In [10]: str.count?                                                                                                
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      method_descriptor

#返回sub在S中出现的次数，返回类型为整形，可以指定start,end范围，表示返回指定范围内sub出现的次数
```





#### 2.startswith

```python
In [11]: str.startswith?                                                                                           
Docstring:
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.
Type:      method_descriptor
    
#检查字符串是否是以 prefix 开头，是则返回 True，否则返回 False。如果start 和 end 指定值，则在指定范围内检查.
```





#### 3.endswith

```python
Docstring:
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
Type:      method_descriptor
#检查字符串是否是以 suffix 结尾，是则返回 True，否则返回 False。如果start 和 end 指定值，则在指定范围内检查.
```



#### 4.find

```python
In [13]: str.find?                                                                                
Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      method_descriptor
    
#检测 sub 是否包含在 S 中，如果 strt 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
```



#### 5.format

```python
In [14]: str.format?                                                                              
Docstring:
S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
Type:      method_descriptor
    
#返回s格式化之后的字符串，使用args和kwargs替换，替换部分通过{}定义
```



#### 6.index

```python
Docstring:
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, 
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      method_descriptor

    
    	
#跟find()方法一样，只不过如果sub不在 S中会报一个异常.
```



#### 7.isdigit

```python
In [16]: str.isdigit?                                                                             
Docstring:
S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      method_descriptor

#如果 string 只包含数字则返回 True 否则返回 False.
```

#### 8.islower

```python
Docstring:
S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise.
Type:      method_descriptor
    
#如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
```



#### 9.isupper

```python
In [18]: str.isupper?                                                                             
Docstring:
S.isupper() -> bool

Return True if all cased characters in S are uppercase and there is
at least one cased character in S, False otherwise.
Type:      method_descriptor

#如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
```



#### 10.join

```python
In [19]: str.join?                                                                                
Docstring:
S.join(iterable) -> str

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      method_descriptor

#以S作为分隔符,将 iterable 中所有的元素(的字符串表示)合并为一个新的字符串
```



#### 11.ljust

```python
In [20]: str.ljust?                                                                               
Docstring:
S.ljust(width[, fillchar]) -> str

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      method_descriptor

#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
```

#### 12.lower

```python
In [22]: str.lower?                                                                               
Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      method_descriptor
    
#转换 string 中所有大写字符为小写.
```



#### 13.lstrip

```python
In [23]: str.lstrip?                                                                              
Docstring:
S.lstrip([chars]) -> str

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      method_descriptor
   
#截掉 string 左边的空格
```



#### 14.replace

```python
In [24]: str.replace?                                                                             
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      method_descriptor

#把 string 中的 old 替换成 new,如果 count 指定，则替换不超过 count 次.
```

#### 15.rjust

```python
In [25]: str.rjust?                                                                               
Docstring:
S.rjust(width[, fillchar]) -> str

Return S right-justified in a string of length width. Padding is
done using the specified fill character (default is a space).
Type:      method_descriptor

#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
```

#### 16.split

```python
In [26]: str.split?                                                                               
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      method_descriptor

#以 sep 为分隔符切片 string，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串
```



#### 17.strip

```python
In [27]: str.strip?                                                                               
Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      method_descriptor
    
#在 string 上执行 lstrip()和 rstrip()
```

#### 18.upper

```python
In [28]: str.upper?                                                                               
Docstring:
S.upper() -> str

Return a copy of S converted to uppercase.
Type:      method_descriptor

#转换 string 中的小写字母为大写
```



### 列表常用方法

```python
>>> dir(list)    
.append
.count
.extend
.index
.insert
.pop
.remove
.reverse
.sort
```



#### 1.append

```python
Docstring: L.append(object) -> None -- append object to end
Type:      method_descriptor
    
#在列表末尾添加新的对象
```



#### 2.count

```python
Docstring: L.count(value) -> integer -- return number of occurrences of value
Type:      method_descriptor
    
#统计某个元素在列表中出现的次数
```



#### 3.extend

```python
Docstring: L.extend(iterable) -> None -- extend list by appending elements from the iterable
Type:      method_descriptor
   
#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
```



#### 4.index

```python
Docstring:
L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Type:      method_descriptor

#从列表中找出某个值第一个匹配项的索引位置    
```



#### 5.insert

```python
Docstring: L.insert(index, object) -- insert object before index
Type:      method_descriptor
    
#将对象插入列表
```



#### 6.pop

```python
Docstring:
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
Type:      method_descriptor
    
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
```



#### 7.remove

```python
Docstring:
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
Type:      method_descriptor
 
#移除列表中某个值的第一个匹配项
```



#### 8.reverse

```python
Docstring: L.reverse() -- reverse *IN PLACE*
Type:      method_descriptor
    
#反向列表中元素
```



#### 9.sort

```python
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      method_descriptor

#对原列表进行排序,升序
```

