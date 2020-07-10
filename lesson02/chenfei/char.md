---
title: python字符串常用内置参数详解
date: 2019-05-23 23:18
tags: python
---

capitalize(...)

```
	S.capitalize() -> string
	capitalize()方法返回S字符串的一个副本，只有它的第一个字母大写。
	例子:
		>>> a = "hello world"
		>>> print a
		hello world
		>>> a.capitalize()
		'Hello world'
```
center(...)

```
	S.center(width[, fillchar]) -> string
	返回一个原字符串居中,并使用空格填充至长度width的新字符串。默认填充字符为空格。
	例子：
		>>> Test = "My name is tyak"
		>>> print "test.center(20,'b') : ",test.center(20,'b')
		test.center(20,'b') :  bbMy name is tyak.bb
```
count(...)

```
    S.count(sub[, start[, end]]) -> int
    Python的string.count(str, begin=0, end=len(string)函数用于返回str在string中出现的次数
	string为待检测的字符串，如:s='this is a new technology,and I want to learn this.'
	参数1：str为待识别字符串，可以为串可以为字母但是要用引号包裹如str='this'或str='i'
	参数2：begin表示string的起始位置，第一个位置是0,默认第一个位置为None	
	参数3：end表示string的终止位置，最后一个位置是string的长度，默认最后一个位置为None
	例子：
       >>> tao="My name is yak.Tou, what's your name?"
		>>> print (tao.count('name',0,len(tao)))
		2
		>>> print (tao.count('name',6,len(tao)))
		1
```	
decode(...)

```
    以encoding指定的编码格式解码字符串。默认编码为字符串编码。
	 例子：
		 >>> h1="good morning"
		 >>> h1 = h1.encode('base64','strict')
		 >>> print "Encoded String: "+ h1
		 Encoded String: Z29vZCBtb3JuaW5n
		 >>> print "Encoded String: "+ h1.decode('base64','strict')
		 Encoded String: good morning
```

encode(...)

```

       编码,以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
		例子：
			>>> code="this is string example....wow!!!"
			>>> print "Encoded String: " + code.encode('base64','strict')
			Encoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=
```

endswith(...)

```
		如果字符串以指定的后缀结束，此方法返回true，否则返回False，也可以限制给定的指标开始和结束的匹配。
		str.endswith(suffix[, start[, end]])
		例子：
			>>> test1='this is string example....wow!!!'
			>>> succ="wow!!!"
			>>> print test1.endswith(succ)
			True
			>>> print test1.endswith(succ,20)
			True
			>>> succ="oo"
			>>> print test1.endswith(succ,20)
			False
```
expandtabs(...)

```
		把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
	    例子：
		   	>>> test="My name is\tstring taoyake,what's your name?"
			>>> print test
			My name is	string taoyake,what's your name?
			>>> print test.expandtabs();
			My name is      string taoyake,what's your name?
			>>> print test.expandtabs(2);
			My name is  string taoyake,what's your name?
```
find(...)

```
		检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

		语法：str.find(str, beg=0, end=len(string))
		例子：
			>>> test1="I come from chia."
			>>> test2="come"
			>>> print test1.find(test2)
			2
			>>> print test1.find(test2,10)
			-1
			>>> print test1.find(test2,2)
			2
```
format(...)

```
		S.format(*args, **kwargs) -> string
		格式化一个字符串的输出结果
		例子：
			>>> '{0},{1}'.format('hello','taokey')
			'hello,taokey'
			>>> '{},{}'.format('hi',19)
			'hi,19'
			>>> '{1},{0},{1}'.format('hi','taokey')
			'taokey,hi,taokey'
			>>> '{},{},{}'.format('hi','taokey','pl')
			'hi,taokey,pl'
```
index(...)

```
	    S.index(sub [,start [,end]]) -> int
	    检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
	    语法：
	    str.index(str, beg=0, end=len(string))
	    参数
		str -- 指定检索的字符串
		beg -- 开始索引，默认为0。
		end -- 结束索引，默认为字符串的长度。

	   例子:		
			>>> str1 = "this is string example....wow!!!";
			>>> str2 = "exam";
			>>> print str1.index(str2)
			15
			>>> print str1.index(str2,10)
			15
			>>> print str1.index(str2,30)
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			ValueError: substring not found
```
isalnum(...)

```
		S.isalnum() -> bool
		Python isalnum() 方法检测字符串是否由字母和数字组成。	
		语法：
			str.isalnum()
		例子：
			>>> str1="beautiful"
			>>> print str1.isalnum()
			True
			>>> str1="beautiful girl"
			>>> print str1.isalnum()
			False
			>>> str1="beautiful111"
			>>> print str1.isalnum()
			True
			>>> str1="beautiful111..."
			>>> print str1.isalnum()
			False
```
isalpha(...)

```
		S.isalpha() -> bool
		Python isalpha() 方法检测字符串是否只由字母组成
		例子：
			>>> str1="beautiful111"
			>>> print str1.isalpha()
			False
			>>> str1="beautiful"
			>>> print str1.isalpha()
			True
```
isdigit(...)

```
		S.isdigit() -> bool
		Python isdigit() 方法检测字符串是否只由数字组成。
		例子：
			>>> print str1.isdigit()
			True
			>>> str1="123456abc"
			>>> print str1.isdigit()
			False
```
islower(...)

```
       S.islower() -> bool
       检测字符串是否由小写字母组成。
		例子：
			>>> test1='taoyake'
			>>> print test1.islower()
			True
			>>> test1='Taokey'
			>>> print test1.islower()
			False
```
isspace(...)

```
       S.isspace() -> bool
       检测字符串是否只由空格组成。
		例子：
			>>> test2='Taokey'
			>>> print test2.isspace()
			False
			>>> test2='  '
			>>> print test2.isspace()
			True
```
istitle(...)

```
       S.istitle() -> bool
       检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
       例子：
			>>> h1='My English Name Is Taokey'
			>>> print h1.istitle()
			True
			>>> h1='My English name is taokey'
			>>> print h1.istitle()
			False
```
isupper(...)

```
       S.isupper() -> bool
       检测字符串中所有的字母是否都为大写。
       例子：
			>>> test='HELLO TAOKEY'
			>>> print test.isupper()
			True
			>>> test='hello taokey'
			>>> print test.isupper()
			False
```
join(...)

```
       S.join(iterable) -> string
       将序列中的元素以指定的字符连接生成一个新的字符串。
       例子:
			>>> a1="|"
			>>> seq = ("a","b","c")
			>>> print a1.join(seq)
			a|b|c        
```
 replace(...)
 
```
      S.replace(old, new[, count]) -> string
      把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 		max次。
	   参数：
			old -- 将被替换的子字符串。
			new -- 新字符串，用于替换old子字符串。
			max -- 可选字符串, 替换不超过max次
	   例子：
			>>> str = "this is string example....wow!!! this is really string"
			>>> print str.replace("is", "was");
			thwas was string example....wow!!! thwas was really string
			>>> print str.replace("is", "was", 3)
			thwas was string example....wow!!! thwas is really string
```
rfind(...)

```
    S.rfind(sub [,start [,end]]) -> int
	 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。
	 参数:
		str -- 查找的字符串
		beg -- 开始查找的位置，默认为 0
		end -- 结束查找位置，默认为字符串的长度。
	 例子：
		 >>> str = "this is really a string example....wow!!!"
		 >>> substr = "is"
		 >>> print str.rfind(substr)
		 5
		 >>> print str.rfind(substr, 0, 10)
		 5
		 >>> print str.rfind(substr, 10, 0)
		 -1
		 >>> print str.find(substr)
		 2
		 >>> print str.find(substr,0,10)
		 2
		 >>> print str.find(substr,10,4)
		 -1
	 
```
rindex(...)

```
	S.rindex(sub [,start [,end]]) -> int
	Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异	常，你可以指定可选参数[beg:end]设置查找的区间。
	参数：
		str -- 查找的字符串
		beg -- 开始查找的位置，默认为0
		end -- 结束查找位置，默认为字符串的长度。
	例子：
		>>> str1 = "this is string example....wow!!!"
		>>> str2 = "is"
		>>> print str1.rindex(str2)
		5
		>>> print str1.index(str2)
		2
```
split(...)

```
      S.split([sep [,maxsplit]]) -> list of strings
      Python split()通过指定分隔符对字符串进行切片，如果参数num 有指定值，则仅分隔 num 个		子字符串
      参数
		  str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
		  num -- 分割次数。
	  语法：  
		>>> str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
		>>> print str.split( )
		['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
		>>> print str.split(' ', 1 );
		['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
```
rstrip(...)

```
      S.rstrip([chars]) -> string or unicode
      Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格).
	   语法：
	     str.rstrip([chars])
      参数：
	     chars -- 指定删除的字符(默认为空格)
      例子：
			>>> str="chars -- 指定删除的字符（默认为空格）"
			>>> str="     this is string example....wow!!!     "
			>>> print str.rstrip()
			     this is string example....wow!!!
			>>> str="00000this is string example....wow!!!00000"
			>>> print str.rstrip('0')
			00000this is string example....wow!!!
```

splitlines(...)

```
      S.splitlines(keepends=False) -> list of strings
      Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列		表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
		语法：
			str.splitlines([keepends])
		参数：
			keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包			含换行符，如果为 True，则保留换行符。
		例子：
			>>> str1 = 'ab c\n\nde fg\rkl\r\n'
			>>> print str1.splitlines()
			['ab c', '', 'de fg', 'kl']
			>>> str2 = 'ab c\n\nde fg\rkl\r\n'
			>>> print str2.splitlines(True)
			['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```				

  title(...)
  
```
        S.title() -> string
        Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为		  小写(见 istitle())
		例子：
			>>> str = "this is string example....wow!!!"
			>>> print str.title()
			This Is String Example....Wow!!!
```
translate(...)

```
    	S.translate(table [,deletechars]) -> string
    	Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要		过滤掉的字符放到 del 参数中。
    语法：
    	str.translate(table[, deletechars])
    参数：
		table -- 翻译表，翻译表是通过maketrans方法转换而来。
		deletechars -- 字符串中要过滤的字符列表。
	返回值：
		返回翻译后的字符串。		
	例子：
		>>> from string import maketrans
		>>> intab = "aeiou"
		>>> outtab = "12345"
		>>> trantab = maketrans(intab, outtab)
		>>> str = "this is string example....wow!!!"
		>>> print str.translate(trantab)
		th3s 3s str3ng 2x1mpl2....w4w!!!
		>>> str = "this is string example....wow!!!";
		>>> print str.translate(trantab, 'xm')
		th3s 3s str3ng 21pl2....w4w!!!
```

zfill(...)

```
        S.zfill(width) -> string
        Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
    	 语法：    
          str.zfill(width)
       参数：
     	  width -- 指定字符串的长度。原字符串右对齐，前面填充0。
      例子：
			>>> str = "this is string example....wow!!!"
			>>> print str.zfill(40)
			00000000this is string example....wow!!!
			>>> print str.zfill(50)
			000000000000000000this is string example....wow!!!     
```


