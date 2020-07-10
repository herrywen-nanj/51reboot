## 字符串常见操作

1）Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      builtin_function_or_method

中文翻译：

返回 str在start和end之间 在 mystr里面出现的次数

用法：

```
mystr.count(str, start=0, end=len(mystr))
```

![1558748699456](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558748699456.png)

2）Docstring:
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.
Type:      builtin_function_or_method

中文翻译：

检查字符串是否是以 obj 开头, 是则返回 True，否则返回 False

用法：

```
mystr.startswith(obj)
```

![1558748967755](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558748967755.png)

3）Docstring:
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
Type:      builtin_function_or_method

中文翻译：

检查字符串是否以obj结束，如果是返回True,否则返回 False.

用法：

```
mystr.endswith(obj)
```

![1558749515382](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558749515382.png)

4）Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      builtin_function_or_method

中文翻译：

检测 str 是否包含在 mystr中，如果是返回开始的索引值，否则返回-1

用法：

```
mystr.find(str, start=0, end=len(mystr))
```

![1558749850645](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558749850645.png)

5）Docstring:
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, 
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      builtin_function_or_method

中文翻译：

跟find()方法一样，只不过如果str不在 mystr中会报一个异常.

用法：

```
mystr.index(str, start=0, end=len(mystr)) 
```

![1558750234693](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558750234693.png)

6）Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

中文翻译：

把 mystr 中的 str1 替换成 str2,如果 count 指定，则替换不超过 count 次.

用法：

```
mystr.replace(str1, str2,  mystr.count(str1))
```

![1558751074152](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558751074152.png)

7）Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method

中文翻译：

以 str 为分隔符切片 mystr，如果 maxsplit有指定值，则仅分隔 maxsplit 个子字符串

用法：

```
mystr.split(str=" ", 2)   
```

![1558751512976](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558751512976.png)

8）Docstring:
S.capitalize() -> str

Return a capitalized version of S, i.e. make the first character
have upper case and the rest lower case.
Type:      builtin_function_or_method

中文翻译：

把字符串的第一个字符大写

用法：

```
mystr.capitalize()
```

![1558751672043](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558751672043.png)

9）Docstring:
S.title() -> str

Return a titlecased version of S, i.e. words start with title case
characters, all remaining cased characters have lower case.
Type:      builtin_function_or_method

中文翻译：

把字符串的每个单词首字母大写

用法：

```python
>>> a = "hello itcast"
>>> a.title()
'Hello Itcast'
```

10）Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method

中文翻译：

转换 mystr 中所有大写字符为小写

用法：

```
mystr.lower()      
```

![1558751892789](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558751892789.png)

11）Docstring:
S.upper() -> str

Return a copy of S converted to uppercase.
Type:      builtin_function_or_method

中文翻译：

转换 mystr 中的小写字母为大写

用法：

```
mystr.upper()    
```

![1558752047419](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558752047419.png)

12）Docstring:
S.ljust(width[, fillchar]) -> str

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

中文翻译：

返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串

用法：

```
mystr.ljust(width) 
```

![1558752161657](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558752161657.png)

13）Docstring:
S.rjust(width[, fillchar]) -> str

Return S right-justified in a string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

中文翻译：

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串

用法：

```
mystr.rjust(width) 
```

![1558752516728](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558752516728.png)

14）Docstring:
S.center(width[, fillchar]) -> str

Return S centered in a string of length width. Padding is
done using the specified fill character (default is a space)
Type:      builtin_function_or_method

中文翻译：

返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

用法：

```
mystr.center(width)   
```

![1558752673326](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558752673326.png)

15）Docstring:
S.lstrip([chars]) -> str

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

中文翻译：

删除 mystr 左边的空白字符

用法：

```
mystr.lstrip()
```

![1558752873262](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558752873262.png)

16）Docstring:
S.rstrip([chars]) -> str

Return a copy of the string S with trailing whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

中文翻译：

删除 mystr 字符串末尾的空白字符

用法：

```
mystr.rstrip()   
```

![1558753017209](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753017209.png)

17）Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

中文翻译：

删除mystr字符串两端的空白字符

用法：

```python
>>> a = "\n\t itcast \t\n"
>>> a.strip()
'itcast'
```

18）Docstring:
S.rfind(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      builtin_function_or_method

中文翻译：

类似于 find()函数，不过是从右边开始查找.

用法：

```
mystr.rfind(str, start=0,end=len(mystr) )
```

![1558753231896](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753231896.png)

19）Docstring:
S.rindex(sub[, start[, end]]) -> int

Return the highest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      builtin_function_or_method

中文翻译：

类似于 index()，不过是从右边开始.

用法：

```
mystr.rindex( str, start=0,end=len(mystr))
```

![1558753334264](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753334264.png)

20）Docstring:
S.partition(sep) -> (head, sep, tail)

Search for the separator sep in S, and return the part before it,
the separator itself, and the part after it.  If the separator is not
found, return S and two empty strings.
Type:      builtin_function_or_method

中文翻译：

把mystr以str分割成三部分,str前，str和str后

用法：

```
mystr.partition(str)
```

![1558753538379](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753538379.png)

21）Docstring:
S.rpartition(sep) -> (head, sep, tail)

Search for the separator sep in S, starting at the end of S, and return
the part before it, the separator itself, and the part after it.  If the
separator is not found, return two empty strings and S.
Type:      builtin_function_or_method

中文翻译：

类似于 partition()函数,不过是从右边开始.

用法：

```
mystr.rpartition(str)
```

![1558753634057](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753634057.png)

22）Docstring:
S.splitlines([keepends]) -> list of strings

Return a list of the lines in S, breaking at line boundaries.
Line breaks are not included in the resulting list unless keepends
is given and true.
Type:      builtin_function_or_method

中文翻译：

按照行分隔，返回一个包含各行作为元素的列表

用法：

```
mystr.splitlines()  
```

![1558753809684](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753809684.png)

23）Docstring:
S.isalpha() -> bool

Return True if all characters in S are alphabetic
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

中文翻译：

如果 mystr 所有字符都是字母 则返回 True,否则返回 False

用法:

```
mystr.isalpha()  
```

![1558753965973](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558753965973.png)

24)Docstring:
S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

中文翻译：

如果 mystr 只包含数字则返回 True 否则返回 False.

用法：

```
mystr.isdigit() 
```

![1558754084756](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558754084756.png)

25）Docstring:
S.isalnum() -> bool

Return True if all characters in S are alphanumeric
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

中文翻译：

如果 mystr 所有字符都是字母或数字则返回 True,否则返回 False

用法：

```
mystr.isalnum()  
```

![1558754216129](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558754216129.png)

26）Docstring:
S.isspace() -> bool

Return True if all characters in S are whitespace
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

中文翻译：

如果 mystr 中只包含空格，则返回 True，否则返回 False.

用法：

```
mystr.isspace()   
```

![1558754340048](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558754340048.png)

27）Docstring:
S.join(iterable) -> str

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      builtin_function_or_method

中文翻译：

mystr 中每个字符后面插入str,构造出一个新的字符串

用法：

```
mystr.join(str)
```

![1558754514380](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558754514380.png)

## 列表常见操作

## <1>添加元素("增"append, extend, insert)

1）append

Docstring: L.append(object) -> None -- append object to end
Type:      builtin_function_or_method

通过append可以向列表添加元素

demo:

![1558754881478](C:\Users\liusfgood\AppData\Roaming\Typora\typora-user-images\1558754881478.png)

2)extend

Docstring: L.extend(iterable) -> None -- extend list by appending elements from the iterable
Type:      builtin_function_or_method

通过extend可以将另一个集合中的元素逐一添加到列表中

demo:

```python
>>> a = [1, 2]
>>> b = [3, 4]
>>> a.append(b)
>>> a
[1, 2, [3, 4]]
>>> a.extend(b)
>>> a
[1, 2, [3, 4], 3, 4]
```

3)insert

Docstring: L.insert(index, object) -- insert object before index
Type:      builtin_function_or_method

insert(index, object) 在指定位置index前插入元素object

demo:

```python
>>> a = [0, 1, 2]
>>> a.insert(1, 3)
>>> a
[0, 3, 1, 2]
```

## <2>修改元素("改")

修改元素的时候，要通过下标来确定要修改的是哪个元素，然后才能进行修改

demo:

```python
   #定义变量A，默认有3个元素
    A = ['xiaoWang','xiaoZhang','xiaoHua']

    print("-----修改之前，列表A的数据-----")
    for tempName in A:
        print(tempName)

    #修改元素
    A[1] = 'xiaoLu'

    print("-----修改之后，列表A的数据-----")
    for tempName in A:
        print(tempName)
```

结果：

```
  -----修改之前，列表A的数据-----
    xiaoWang
    xiaoZhang
    xiaoHua
    -----修改之后，列表A的数据-----
    xiaoWang
    xiaoLu
    xiaoHua
```

## <3>查找元素("查"in, not in, index, count)

所谓的查找，就是看看指定的元素是否存在

#### in, not in

python中查找的常用方法为：

- in（存在）,如果存在那么结果为true，否则为false
- not in（不存在），如果不存在那么结果为true，否则false

demo：

```python
    #待查找的列表
    nameList = ['xiaoWang','xiaoZhang','xiaoHua']

    #获取用户要查找的名字
    findName = input('请输入要查找的姓名:')

    #查找是否存在
    if findName in nameList:
        print('在字典中找到了相同的名字')
    else:
        print('没有找到')
```

说明：

> in的方法只要会用了，那么not in也是同样的用法，只不过not in判断的是不存在
>
> #### index, count
>
> index和count与字符串中的用法相同
>
> ```python
> >>> a = ['a', 'b', 'c', 'a', 'b']
> >>> a.index('a', 1, 3) # 注意是左闭右开区间
> Traceback (most recent call last):
>   File "<stdin>", line 1, in <module>
> ValueError: 'a' is not in list
> >>> a.index('a', 1, 4)
> 3
> >>> a.count('b')
> 2
> >>> a.count('d')
> 0
> ```

## <4>删除元素("删"del, pop, remove)

列表元素的常用删除方法有：

- del：根据下标进行删除

- pop：删除最后一个元素

- remove：根据元素的值进行删除

  demo:(del)

  ```python
   movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']
  
      print('------删除之前------')
      for tempName in movieName:
          print(tempName)
  
      del movieName[2]
  
      print('------删除之后------')
      for tempName in movieName:
          print(tempName)
  ```

结果：

```
  ------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    指环王
    霍比特人
    速度与激情
```

demo:(pop)

```python
 movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

    print('------删除之前------')
    for tempName in movieName:
        print(tempName)

    movieName.pop()

    print('------删除之后------')
    for tempName in movieName:
        print(tempName)
```

结果：

```
------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
```

demo:(remove)

```python
movieName = ['加勒比海盗','骇客帝国','第一滴血','指环王','霍比特人','速度与激情']

    print('------删除之前------')
    for tempName in movieName:
        print(tempName)

    movieName.remove('指环王')

    print('------删除之后------')
    for tempName in movieName:
        print(tempName)
```

结果:

```python
  ------删除之前------
    加勒比海盗
    骇客帝国
    第一滴血
    指环王
    霍比特人
    速度与激情
    ------删除之后------
    加勒比海盗
    骇客帝国
    第一滴血
    霍比特人
    速度与激情
```

## <5>排序(sort, reverse)

sort方法是将list按特定顺序重新排列，默认为由小到大，参数reverse=True可改为倒序，由大到小。

reverse方法是将list逆置。

```python
>>> a = [1, 4, 2, 3]
>>> a
[1, 4, 2, 3]
>>> a.reverse()
>>> a
[3, 2, 4, 1]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a.sort(reverse=True)
>>> a
[4, 3, 2, 1]
```