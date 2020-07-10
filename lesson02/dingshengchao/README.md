# dir(str)  字符串方法
## - .count


Docstring:
S.count(sub[, start[, end]]) -> int

Return the number of non-overlapping occurrences of substring sub instring S[start:end].  Optional arguments start and end are interpreted as in slice notation.

Type:      method_descriptor

返回整数型，返回子字符串出现的次数

## - .startswith
Docstring:
S.startswith(prefix[, start[, end]]) -> bool

Return True if S starts with the specified prefix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
prefix can also be a tuple of strings to try.

Type:      method_descriptor

返回布尔值，用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
## - .endswith
Docstring:
S.endswith(suffix[, start[, end]]) -> bool

Return True if S ends with the specified suffix, False otherwise.
With optional start, test S beginning at that position.
With optional end, stop comparing S at that position.
suffix can also be a tuple of strings to try.
Type:      method_descriptor

用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
## - .find
Docstring:
S.find(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found,
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Return -1 on failure.
Type:      method_descriptor

方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

## - .format
Docstring:
S.format(*args, **kwargs) -> str

Return a formatted version of S, using substitutions from args and kwargs.
The substitutions are identified by braces ('{' and '}').
Type:      method_descriptor

通过字符串中的花括号 {} 来识别替换字段 replacement field，从而完成字符串的格式化。

## - .index
S.index(sub[, start[, end]]) -> int

Return the lowest index in S where substring sub is found, 
such that sub is contained within S[start:end].  Optional
arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.
Type:      method_descriptor

如果包含子字符串返回开始的索引值，否则抛出异常。
检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内
## - .isdigit
Docstring:
S.isdigit() -> bool

Return True if all characters in S are digits
and there is at least one character in S, False otherwise.
Type:      method_descriptor

检测字符串是否只由数字组成
如果字符串只包含数字则返回 True 否则返回 False

## - .islower
Docstring:
S.islower() -> bool

Return True if all cased characters in S are lowercase and there is
at least one cased character in S, False otherwise.
Type:      method_descriptor

检测字符串是否由小写字母组成。
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
## - .isupper
Docstring:
S.isupper() -> bool

Return True if all cased characters in S are uppercase and there is
at least one cased character in S, False otherwise.
Type:      method_descriptor

检测字符串中所有的字母是否都为大写。
如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
## - .join
Docstring:
S.join(iterable) -> str

Return a string which is the concatenation of the strings in the
iterable.  The separator between elements is S.
Type:      method_descriptor

用于将序列中的元素以指定的字符连接生成一个新的字符串。
返回通过指定字符连接序列中元素后生成的新字符串。
## - .ljust
S.ljust(width[, fillchar]) -> str

Return S left-justified in a Unicode string of length width. Padding is
done using the specified fill character (default is a space).
Type:      method_descriptor

返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

## - .lower
Docstring:
S.lower() -> str

Return a copy of the string S converted to lowercase.
Type:      builtin_function_or_method

转换字符串中所有大写字符为小写
返回将字符串中所有大写字符转换为小写后生成的字符串。
## - .lstrip
Docstring:
S.lstrip([chars]) -> str

Return a copy of the string S with leading whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

用于截掉字符串左边的空格或指定字符。
返回截掉字符串左边的空格或指定字符后生成的新字符串。
## - .replace
S.replace(old, new[, count]) -> str

Return a copy of S with all occurrences of substring
old replaced by new.  If the optional argument count is
given, only the first count occurrences are replaced.
Type:      builtin_function_or_method

把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
## - .rjust
S.rjust(width[, fillchar]) -> str

Return S right-justified in a string of length width. Padding is
done using the specified fill character (default is a space).
Type:      builtin_function_or_method

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
## - .split
Docstring:
S.split(sep=None, maxsplit=-1) -> list of strings

Return a list of the words in S, using sep as the
delimiter string.  If maxsplit is given, at most maxsplit
splits are done. If sep is not specified or is None, any
whitespace string is a separator and empty strings are
removed from the result.
Type:      builtin_function_or_method

通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符
返回分割后的字符串列表。
## - .strip
Docstring:
S.strip([chars]) -> str

Return a copy of the string S with leading and trailing
whitespace removed.
If chars is given and not None, remove characters in chars instead.
Type:      builtin_function_or_method

用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
## - .upper
Docstring:
S.upper() -> str

Return a copy of S converted to uppercase.
Type:      builtin_function_or_method

将字符串中的小写字母转为大写字母。返回字符串

# dir(list)   列表方法
## .append
Docstring: L.append(object) -> None -- append object to end
Type:      method_descriptor

在列表末尾添加新的对象。
该方法无返回值，但是会修改原来的列表。

## .count
Docstring: L.count(value) -> integer -- return number of occurrences of value
Type:      method_descriptor

用于统计某个元素在列表中出现的次数。
返回元素在列表中出现的次数
## .extend
Docstring: L.extend(iterable) -> None -- extend list by appending elements from the iterable
Type:      method_descriptor

用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
该方法没有返回值，但会在已存在的列表中添加新的列表内容。


## .index
L.index(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.
Type:      method_descriptor

从列表中找出某个值第一个匹配项的索引位置。
该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。

## .insert
Docstring: L.insert(index, object) -- insert object before index
Type:      method_descriptor

用于将指定对象插入列表的指定位置。
该方法没有返回值，但会在列表指定位置插入对象。
## .pop
L.pop([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.
Type:      method_descriptor

于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

## .remove
Docstring:
L.remove(value) -> None -- remove first occurrence of value.
Raises ValueError if the value is not present.
Type:      method_descriptor

用于移除列表中某个值的第一个匹配项
没有返回值
## .reverse
Docstring: L.reverse() -- reverse *IN PLACE*
Type:      method_descriptor

用于反向列表中元素。
该方法没有返回值，但是会对列表的元素进行反向排序。
## .sort
Docstring: L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
Type:      method_descriptor

用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。