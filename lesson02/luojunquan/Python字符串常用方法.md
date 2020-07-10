- 测试字符串
```
In [1]: mystring = 'test string'
In [2]: mystring
Out[2]: 'test string'
```
- 查看字符串有哪些方法
```
dir(mystring)
```
- count统计某个字符串出现的次数
```
In [3]: mystring.count('t')
Out[3]: 3
```
- startwith查看字符串是以什么开头的，返回布尔值
```
In [4]: mystring.startswith('t')
Out[4]: True
In [5]: mystring.startswith('e')
Out[5]: False
```
- endwith查看字符串是以什么结尾的，返回布尔值
```
In [6]: mystring.endswith('t')
Out[6]: False
In [7]: mystring.endswith('g')
Out[7]: True
```
- find检查字符串中是否有字符，指定开始与结尾，不存在返回-1
```
In [9]: mystring.find('e') #返回索引
Out[9]: 1
In [10]: mystring.find('n',0,5)
Out[10]: -1
In [11]: mystring.find('t',0,5)
Out[11]: 0
```
- format格式化输出
```
In [12]: 'hello {} string'.format('is')
Out[12]: 'hello is string'
```
- index查找字符串索引位置
```
In [13]: mystring.index('n')
Out[13]: 9
```
- isdigit检查是不是数字组成，返回布尔值
```
In [14]: mystring.isdigit()
Out[14]: False
In [15]: '123'.isdigit()
Out[15]: True
```
- islower检查是不是小写，返回布尔值
```
In [16]: mystring.islower()
Out[16]: True
```
- isupper检查是不是大学，返回布尔值
```
In [17]: 'HI'.isupper()
Out[17]: True
```
- join链接字符串
```
In [18]: str = '-'
In [19]: s=('H','e','l','l','o')
In [21]: str.join(s)
Out[21]: 'H-e-l-l-o'
```
- ljust检查字符串左对齐，默认使用空格填充至指定长度的新字符串
```
In [24]: mystring.ljust(15,'!')
Out[24]: 'test string!!!!'
```
- lower将字符串转换为小写
```
In [25]: 'HELLO'.lower()
Out[25]: 'hello'
```
- lstrip 将去掉字符串左边空格，或指定字符
```
In [26]: '  hello word'.lstrip()
Out[26]: 'hello word'
```
- replac将字符串右对齐，默认使用空格填充至指定长度的新字符串
```
In [27]: mystring.replace('n','A')
Out[27]: 'test striAg'
```
- split将字符串切分，返回列表
```
In [28]: mystring.rjust(15,'!')
Out[28]: '!!!!test string'
```
- strip去除指定字符,(但必须是从开头开始的单子字母或者字符)
```
In [33]: mystring.strip('te')
Out[33]: 'st string'
```
- upper将字符串变为大写
```
In [34]: 'hello word'.upper()
Out[34]: 'HELLO WORD'
```