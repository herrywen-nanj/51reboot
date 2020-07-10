# Python3-字符串使用详解

## 安装ipython

```shell
vagrant@localhost ~]$ sudo /usr/local/python36/bin/pip3 install ipython
```

## 运行ipython

```shell
[vagrant@localhost ~]$ ipython
Python 3.6.8 (default, May  6 2019, 03:31:49) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:                                                            
```

## 常用内置函数

### find

```python
In [3]: s = "haha"                                                                                                                                                     
In [4]: s.find?      #获取帮助                                                                                                                                                Docstring:
#使用方法:s.find(sub,start[,end]) 返回是整数类型
S.find(sub[, start[, end]]) -> int
也可以这么理解s.find(sub[,start=0[,end=len(S)]])
sub:是指定的字符串
start:默认是从0开始
end:要大于 start 小于等于len(s)

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.
#执行失败返回-1
Return -1 on failure.
Type:      builtin_function_or_method
例子：
In [55]: s                                                                        
Out[55]: 'hello  world   world all world'
In [56]: s.find("hello") #查找hello位置
Out[56]: 0 #得出第0索引就是要找的
In [57]: s.find("hello",1)  #找出索引第一以后的hello,因为1以后没有所以返回-1                     Out[57]: -1
In [58]: s.find("world")
Out[58]: 7
#看一下索引第7个事什么鬼
In [59]: s[7]
Out[59]: 'w' #说明world 是从第7个开始的
In [68]: s.find("world",8) #从第8个开始
Out[68]: 15 #第15个就是world 的开始
In [69]: s[15]                        
Out[69]: 'w'
end:怎么使用                                                  
```

### count

```python
Docstring:
S.count(sub[, start[, end]]) -> int#其实使用方法和find很相似，差别就是一个返回所在位置，一个统计出现此处
Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      builtin_function_or_method #内置函数
例子：
In [72]: s                               
Out[72]: 'hello  world   world all world' 
In [73]: s.count("world")                #统计world总共出现次数
Out[73]: 3
In [74]: s.count("world",8)             #从第八个以后world 出现的次数 
Out[74]: 2
In [75]: s.count("world",82)             #如果超出范围或者字符串不存在的话不会报错，会返回0
Out[75]: 0
```

### endswith

```
In [76]: s.endswith?                                                                                                                        
Docstring:
S.endswith(suffix[, start[, end]]) -> bool # 返回布尔
Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.

如果字符串以指定的后缀结尾返回 True ，否则返回 Falsesuffix can also be a tuple of strings to try.
Type:      builtin_function_or_method
例子：
Out[78]: 'hello  world   world all world'
In [79]: suffix='ld'
In [80]: s.endswith(suffix)
Out[80]: True
In [81]: suffix='ldd'
In [82]: s.endswith(suffix)
Out[82]: False
In [91]: suffix='lo'
In [92]: s.endswith(suffix,0,5)
Out[92]: True
```

### format

```
In [93]: s.format?                                                                                                                                                     
Docstring:
S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
Type:      builtin_function_or_method

字符串的格式化方法分为两种，分别为占位符(%)和format方式。占位符方式在Python2.x中用的比较广泛，随着Python3.x的使用越来越广，format方式使用的更加广泛

可以参考

https://www.cnblogs.com/lvcm/p/8859225.html
```

### isdigit

```
isdigit() 方法检测字符串是否只由数字组成。

In [97]: s.isdigit?                                                                                                                                                    
Docstring:
S.isdigit() -> bool  #返回布尔值

Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

例子：

In [97]: s.isdigit?                                                                                                                                                    
Docstring:
S.isdigit() -> bool
Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method
In [98]: str = "123456";                                                                                                                                               
In [99]: str.isdigit()                                                                                                                                                 
Out[99]: True
In [100]: str = "ha";                                                                                                                                                  
In [101]: str.isdigit()                                                                                                                                                
Out[101]: False
In [102]: str = "ha01";                                                                                                                                                
In [103]: str.isdigit()                                                                                                                                                
Out[103]: False
```

### islower

```
In [105]: s.islower?  

slower() 方法检测字符串是否由小写字母组成。                                                                                                                                                 Docstring:
S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise.
Type:      builtin_function_or_method

例子：

In [106]: s                                                                                                                                                            
Out[106]: 'hello  world   world all world'
In [107]: s.islower()                                                                                                                                                  
Out[107]: True

In [109]: a="HAHAH S"
In [112]: a.islower()                                                                                                                                                  
Out[112]: False
In [113]: b="Hello"
In [114]: b.islower()                                                                                                                                                  
Out[114]: False
```

### join

```
In [115]: s.join?                                                                                                                                                      
Docstring:
S.join(iterable) -> str#返回字符串

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      builtin_function_or_method

例子：

In [116]: s1="-"                                                                                                                                                       
In [117]: s2=""                                                                                                                                                        
In [118]: s3="#"                                                                                                                                                       
In [119]: s                                                                                                                                                            
Out[119]: 'hello  world   world all world'
In [120]: s1.join(s)                                                                                                                                                   
Out[120]: 'h-e-l-l-o- - -w-o-r-l-d- - - -w-o-r-l-d- -a-l-l- -w-o-r-l-d'
In [121]: s2.join(s)                                                                                                                                                   
Out[121]: 'hello  world   world all world'
In [122]: s3.join(s)                                                                                                                                                   
Out[122]: 'h#e#l#l#o# # #w#o#r#l#d# # # #w#o#r#l#d# #a#l#l# #w#o#r#l#d'
In [123]: s4="@"     
In [124]: s4.join(s)                                                                                                                                                   
Out[124]: 'h@e@l@l@o@ @ @w@o@r@l@d@ @ @ @w@o@r@l@d@ @a@l@l@ @w@o@r@l@d'
```

### ljust

In [141]: s.ljust?                                                                                                                                                     
Docstring:
S.ljust(width[, fillchar]) -> str

```
str.ljust(width[, fillchar])
width -- 指定字符串长度。
fillchar -- 填充字符，默认为空格
```

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

例子：

```
In [142]: s
Out[142]: 'hello  world   world all world'
In [143]: s.ljust(59,"*")
Out[143]: 'hello  world   world all world*****************************'
```



### lower

```
In [148]: s.lower? 
Python lower() 方法转换字符串中所有大写字符为小
Docstring:
S.lower() -> str
Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method
例子：
In [149]: s="HELLO"
In [150]: s
Out[150]: 'HELLO'
In [151]: s.lower()
Out[151]: 'hello'
```

### lstrip

- ```
  lstrip() 方法用于截掉字符串左边的空格或指定字符。
  语法
  ​```
  str.lstrip([chars])
  ​```
  - chars --指定截取的字符。
  - 返回截掉字符串左边的空格或指定字符后生成的新字符串
    In [156]: s
    Out[156]: 'HELLO'
    In [157]: s.lstrip("HE")
    Out[157]: 'LLO'
  ```
  
  ### capitalize

```
In [10]: s.capitalize?Docstring:
S.capitalize() -> str #返回字符串
Return a capitalized version of S, i.e. make the first character
have upper case and the rest lower case. #将字符串的首字母大写，其他的都会变成小写的
Type:      builtin_function_or_method
例子如下：
In [11]: s = "nihao  zhongguo"
In [12]: s1=s.capitalize()
In [13]: print(s1)
Nihao  zhongguo
```

### split

```
In [14]: s.split?
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings 
maxsplit:分割次数。-1是指分割所有
#返回一个list
Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method
例子：
In [15]: str = "this is string example....wow!!!"
In [16]: print(str.split())
['this', 'is', 'string', 'example....wow!!!']
In [18]: print(str.split("i"))
['th', 's ', 's str', 'ng example....wow!!!']
In [19]: print(str.split("i"))
['th', 's ', 's str', 'ng example....wow!!!']
In [20]: print(str.split("i",1))
['th', 's is string example....wow!!!']
In [21]: print(str.split("w",1))
['this is string example....', 'ow!!!']
In [22]: print(str.split("w"))
['this is string example....', 'o', '!!!']
In [23]: a= str.split()
In [24]: type(a)
Out[24]: list
```

