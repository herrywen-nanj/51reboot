
**.count**   
------
```
S.count（sub [，start [，end]]） - > int 
#返回 sub 在 S 里面出现的次数，如果 start 或者 end 指定则返回指定范围内 sub 出现的次数  

返回子字符串sub的非重叠出现次数  
string S [start：end]。可选参数start和end是  
解释为切片表示法。
类型：builtin_function_or_method 

##实例:


以上实例输出结果：

```


**.startswith**  
------
```
S.startswith(prefix[, start[, end]]) -> bool 
#检查字符串是否是以 prefix 开头，是则返回 True，否则返回 False。如果start 或者 end 指定值，则在指定范围内检查.

如果S以指定的前缀开头，则返回True，否则返回False。  
通过start(可选)，测试S从该位置开始。  
使用end（可选），停止比较该位置的S.  
前缀也可以是要尝试的字符串元组。  
类型：builtin_function_or_method  
```
**.endswith**   
------
```
S.endswith(suffix[, start[, end]]) -> bool 
#检查字符串是否以 suffix 结束，如果start 或者 end 指定值，则在指定范围内检查. 

如果S以指定的后缀结束，则返回True，否则返回False。   
通过start(可选)，测试S从该位置开始。   
使用end（可选），停止比较该位置的S.   
后缀也可以是要尝试的字符串元组。   
类型：builtin_function_or_method   
```
**.find**    
------
``` 
S.find(sub[, start[, end]]) -> int   
#检测 sub 是否包含在 S 中，如果 start 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1. 

返回S中找到子字符串sub的最小索引值，   
这样sub包含在S [start：end]中。可选的   
参数start和end被解释为切片表示法。   

失败时返回-1。  
类型：builtin_function_or_method  
```
**.format**    
------
``` 
S.format(*args, **kwargs) -> str  
#格式化字符串

使用args和kwargs中的替换返回S的格式化版本。  
替换由大括号（'{'和'}'）标识。  
类型:      builtin_function_or_method  
```
**.index**    
------
```
S.index(sub[, start[, end]]) -> int  
#跟find()方法一样，只不过如果sub不在S中会报一个异常.  

返回S中找到子字符串sub的最小索引值，  
这样sub包含在S [start：end]中。可选的  
参数start和end被解释为切片表示法。  

找不到子字符串时引发ValueError。  
类型:      builtin_function_or_method  
```
**.isdigit**    
------
``` 
S.isdigit() -> bool  
#如果 S 只包含数字则返回 True 否则返回 False.  

如果S中的所有字符都是数字，则返回True 和 S中至少有一个字符，否则为False。  
类型:      builtin_function_or_method  
```
**.islower**    
------
```
S.islower() -> bool  
#如果 S 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False  

如果S中的所有套接字符都是小写且存在，则返回True 和 S中至少有一个套接字符，否则为False。  
类型:      builtin_function_or_method  
```
**.isupper**    
------
```  
S.isupper() -> bool  
#如果 S 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

如果S中的所有套接字符都是大写且存在，则返回True 和 S中至少有一个套接字符，否则为False。  
类型:      builtin_function_or_method  
```
**.join**    
------
```
S.join(iterable) -> str  
$ 以 S 作为分隔符，将列表 iterable 中所有的元素(的字符串表示)合并为一个新的字符串  
类型:      builtin_function_or_method  
```
.**ljust**    
------
```
S.ljust(width[, fillchar]) -> str  
#返回一个原字符串左对齐,并使用指定的填充字符填充至长度为width 的新字符串（默认为空格）。  
类型:      builtin_function_or_method  
```
.**rjust**  
------
``` 
S.rjust(width[, fillchar]) -> str  
#返回一个原字符串右对齐,并使用指定的填充字符填充至长度为width 的新字符串（默认为空格）。  
类型:      builtin_function_or_method  
```
**.lower**    
------
``` 
S.lower() -> str  
#转换 S 中所有大写字符为小写.  
类型:      builtin_function_or_method  
```
**.upper**    
------
``` 
S.upper() -> str  
#转换 S 中所有小写字符为大写.  
类型:      builtin_function_or_method  
```
**.strip**    
------
```
S.strip([chars]) -> str  
#在 S 上执行 lstrip()和 rstrip()  
移除字符串 S 前后空格. 如果给出了字符而不是 "无", 请删除字符中的字符。  

类型:      builtin_function_or_method  
```
**.lstrip**   
------
```
S.lstrip([chars]) -> str  
#截掉 string 左边的空格 

返回字符串S的副本，删除S左边的空格。  
如果指定了chars和非空，则删除chars中的字符。  
类型:      builtin_function_or_method  
```
**.replace**   
------
``` 
S.replace(old, new[, count]) -> str  
#把 S 中的 old 替换成 new,如果 count 指定，则替换不超过 count 次. 

返回包含所有子字符串的S副本,老被新的取代。如果可选参数count是给定，只替换第一次计数。  
类型:      builtin_function_or_method  
```
**.split**    
------
``` 
S.split(sep=None, maxsplit=-1) -> list of strings  
#以 sep 为分隔符切片 S，如果 maxsplit 有指定值，则仅分隔 maxsplit + 1 个子字符串 

返回 S 中的单词列表, 使用 sep 作为表达式分隔符字符串。 如果给出最大分裂, 最多只能进行最大分裂分离。  
如果没有指定 sep 或为 "无", 则任何作色的空白字符串都是分隔符, 空字符串从结果中删除。  

类型:      builtin_function_or_method  
```
