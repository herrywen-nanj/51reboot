#################字符串方法 和 列表方法###################

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


In [2]: s.count?                                                                                                                                                       
Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub in
string S[start:end].  Optional arguments start and end are
interpreted as in slice notation.
Type:      builtin_function_or_method

返回sub 在 s 里面出现的次数，如果 start 或者 end 指定则返回指定范围内 sub 出现的次数,返回类型是整形


In [3]: s.startswith?                                                                                                                                                  
Docstring:
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.
Type:      builtin_function_or_method

检查s是否是以 prefix开头，返回布尔值，是则返回 True，否则返回 False。如果start 和 end 指定值，则在指定范围内检查


In [4]: s.endswith?                                                                                                                                                    
Docstring:
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
Type:      builtin_function_or_method

检查s是否以 suffix结束，如果start或者end 指定则检查指定的范围内是否以suffix 结束，返回布尔值，如果是，返回 True,否则返回 False


In [5]: s.find?                                                                                                                                                        
Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      builtin_function_or_method

检测sub是否包含在 s 中，如果 start和 end 指定范围，则检查在指定范围内是否包含，如果包含返回开始的索引值，否则返回-1


In [6]: s.format?                                                                                                                                                      
Docstring:
S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
Type:      builtin_function_or_method

返回s格式化之后的字符串，使用args和kwargs替换，替换部分通过{}定义


In [7]: s.index?                                                                                                                                                       
Docstring:
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, 
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      builtin_function_or_method

检测sub是否包含在s 中，如果 start和 end 指定范围，则检查在指定范围内是否包含，如果包含返回开始的索引值，如果sub不在 s中会报一个ValueError异常

In [8]: s.isdigit?                                                                                                                                                     
Docstring:
S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      builtin_function_or_method

如果s只包含数字则返回 True 否则返回 False

In [9]: s.islower?                                                                                                                                                     
Docstring:
S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise.
Type:      builtin_function_or_method

如果s中包含至少一个区分大小写的字符，并且所有这些字符都是小写，则返回 True，否则返回 False


In [10]: s.isupper?                                                                                                                                                    
Docstring:
S.isupper() -> bool

Return True if all cased characters in S are uppercase and there is
at least one cased character in S, False otherwise.
Type:      builtin_function_or_method

如果s中包含至少一个区分大小写的字符，并且所有这些字符都是大写，则返回 True，否则返回 False


In [11]: s.join?                                                                                                                                                       
Docstring:
S.join(iterable) -> str

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      builtin_function_or_method

以s作为分隔符，将iterable中所有的元素合并为一个新的字符串In [15]: s.ljust?    
                                                                                                                                                  
Docstring:
S.ljust(width[, fillchar]) -> str

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

返回一个原字符串左对齐,并使用fillchar(默认为空格)填充至长度 width 的新字符串

In [20]: s.lower?                                                                                                                                                      
Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method

转换s中所有大写字符为小写,返回字符串

In [21]: s.lstrip?                                                                                                                                                     
Docstring:
S.lstrip([chars]) -> str

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

截掉 s左边的空格,返回字符串，如果chars指定了，删除左边指定的字符串

In [25]: s.replace?                                                                                                                                                    
Docstring:
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

把 s中的 old 替换成 new,如果 count 指定，则替换不超过 count 次

In [29]: s.rjust?                                                                                                                                                      
Docstring:
S.rjust(width[, fillchar]) -> str

Return S right-justified in a string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

返回一个原字符串右对齐,并使用fillchar(默认为空格)填充至长度 width 的新字符串

In [30]: s.split?                                                                                                                                                      
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method

以 sep 为分隔符切片 string，如果 maxsplit 有指定值，则仅分隔 maxsplit+ 个子字符串,如果sep没有定义，默认用空格分隔，返回列表

In [42]: s.strip?                                                                                                                                                      
Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

返回一个字符串，删除字符串左右空格，如果chars指定，删除s左右指定的chars字符


In [43]: s.upper?                                                                                                                                                      
Docstring:
S.upper() -> str

Return a copy of S converted to uppercase.
Type:      builtin_function_or_method

转换 s中的小写字母为大写,返回字符串


dir(list)    
.append
.count
.extend
.index
.insert
.pop
.remove
.reverse
.sort


In [2]: s.append?                                                                                                                                                      
Docstring: L.append(object) -> None -- append object to end
Type:      builtin_function_or_method

在列表末尾添加新的对象,返回空

In [3]: s.count?                                                                                                                                                       
Docstring: L.count(value) -> integer -- return number of occurrences of value
Type:      builtin_function_or_method

统计某个元素在列表中出现的次数

In [4]: s.extend?                                                                                                                                                      
Docstring: L.extend(iterable) -> None -- extend list by appending elements from the iterable
Type:      builtin_function_or_method

在列表末尾一次性追加另一个序列中的多个元素，返回为空

In [7]: s.index?                                                                                                                                                       
Docstring:
L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Type:      builtin_function_or_method

从列表中找出某个值第一个匹配项的索引位置,如果值不存在，抛出ValueError错误

In [8]: s.insert?                                                                                                                                                      
Docstring: L.insert(index, object) -- insert object before index
Type:      builtin_function_or_method

在指定索引之前插入一个对象到列表

In [9]: s.pop?                                                                                                                                                         
Docstring:
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
Type:      builtin_function_or_method

移除列表中的一个元素（默认最后一个元素），并且返回该元素的值,如果列表为空或者指定的索引超出范围抛出IndexError错误

In [10]: s.remove?                                                                                                                                                     
Docstring:
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
Type:      builtin_function_or_method

移除列表中第一个匹配到的值,如果value不存在，抛ValueError异常

In [11]: s.reverse?                                                                                                                                                    
Docstring: L.reverse() -- reverse *IN PLACE*
Type:      builtin_function_or_method

反向列表中元素

In [12]: s.sort?                                                                                                                                                       
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      builtin_function_or_method

对原列表进行默认升序排序，返回空










#############用户管理系统############


1. 登录认证：6次失败退出


[root@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：1
Please input your password：1
username or password error.
Please input your username：2
Please input your password：2
username or password error.
Please input your username：3
Please input your password：3
username or password error.
Please input your username：4
Please input your password：4
username or password error.
Please input your username：5
Please input your password：5
username or password error.
Please input your username：6
Please input your password：6
username or password error.

Input 6 times failed,Terminal will exit.
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#



2. 增删改查和搜索



2.1 增 add
add monkey 20 188xxx monkey@51reboot.com
add pear 24 159xxx pear@51reboot.com
add apple 39 137xxx appley@51reboot.com


[root@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：51reboot
Please input your password：123456
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
Add user monkey success.
Please input your operation：add pear 24 159xxx pear@51reboot.com
Add user pear success.
Please input your operation：add apple 39 137xxx appley@51reboot.com
Add user apple success.
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
用户 monkey 已存在，无需添加.
Please input your operation：add pear 24 159xxx pear@51reboot.com
用户 pear 已存在，无需添加.
Please input your operation：add apple 39 137xxx appley@51reboot.com
用户 apple 已存在，无需添加.
Please input your operation：exit
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#



2.2 删 delete 
delete monkey
delete pear
delete apple


[root@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：51reboot
Please input your password：123456
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
Add user monkey success.
Please input your operation：add pear 24 159xxx pear@51reboot.com
Add user pear success.
Please input your operation：add apple 39 137xxx appley@51reboot.com
Add user apple success.
Please input your operation：delete monkey
Delete user monkey success.
Please input your operation：delete pear
Delete user pear success.
Please input your operation：delete apple
Delete user apple success.
Please input your operation：delete monkey
用户 monkey 不存在.
Please input your operation：delete pear
用户 pear 不存在.
Please input your operation：delete apple
用户 apple 不存在.
Please input your operation：exit
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#



2.3 改 update
update monkey set age = 30  # update monkey 30 188xxx monkey@51reboot.com
update pear set age = 40    # update pear 40 159xxx pear@51reboot.com


ot@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：51reboot
Please input your password：123456
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
Add user monkey success.
Please input your operation：add pear 24 159xxx pear@51reboot.com
Add user pear success.
Please input your operation：update monkey 30 188xxx monkey@51reboot.com
Update monkey update success.
Please input your operation：update pear 40 159xxx pear@51reboot.com
Update pear update success.
Please input your operation：exit
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#



2.4 查 list


[root@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：51reboot
Please input your password：123456
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
Add user monkey success.
Please input your operation：add pear 24 159xxx pear@51reboot.com
Add user pear success.
Please input your operation：add apple 39 137xxx appley@51reboot.com
Add user apple success.
Please input your operation：list
 username 	   age    	   tel    	  email   	
--------------------------------------------------
  monkey  	    20    	  188xxx  	monkey@51reboot.com	
--------------------------------------------------
   pear   	    24    	  159xxx  	pear@51reboot.com	
--------------------------------------------------
  apple   	    39    	  137xxx  	appley@51reboot.com	
--------------------------------------------------
Please input your operation：exit
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#



2.5 搜 find



ot@izj6cg7tzgh6chp30m1s4hz lesson02]# python usermanager.py 
Please input your username：51reboot
Please input your password：123456
Please input your operation：add monkey 20 188xxx monkey@51reboot.com
Add user monkey success.
Please input your operation：add pear 24 159xxx pear@51reboot.com
Add user pear success.
Please input your operation：find monkey
 username 	   age    	   tel    	  email   	
--------------------------------------------------
  monkey  	    20    	  188xxx  	monkey@51reboot.com	
--------------------------------------------------
Please input your operation：find pear
 username 	   age    	   tel    	  email   	
--------------------------------------------------
   pear   	    24    	  159xxx  	pear@51reboot.com	
--------------------------------------------------
Please input your operation：exit
[root@izj6cg7tzgh6chp30m1s4hz lesson02]#




####################冒泡排序#####################

'''
需求：
- [3, 7, 2, 5, 20, 11]

将列表通过冒泡排序的方式实现排序。
'''

[2, 3, 5, 7, 11, 20]
