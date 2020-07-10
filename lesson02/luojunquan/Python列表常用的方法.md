- 查看类别有哪些方法
```
mylist=['h','e','l','l','o']
dir(mylist)
```
- append列表中追加内容
```
In [37]: mylist.append('word')
In [38]: mylist
Out[38]: ['h', 'e', 'l', 'l', 'o', 'word']
```
- extend追加内容，但是不会出现列表嵌套结构(会把一个字符串分开)，append会嵌套
```
In [43]: mylist.extend('word')
In [44]: mylist
Out[44]: ['h', 'e', 'l', 'l', 'o', 'word', 'w', 'o', 'r', 'd']
```
- count统计列表中元素出现的次数
```
In [39]: mylist.count('o')
Out[39]: 1
In [40]: mylist
Out[40]: ['h', 'e', 'l', 'l', 'o', 'word']
```
- index返回索引位置（返回第一个）
```
In [45]: mylist.index('o')
Out[45]: 4
```
- insert插入内容，指定索引位置（嵌套的形式）
```
In [47]: mylist.insert(4,'WORD')
In [48]: mylist
Out[48]: ['h', 'e', 'l', 'l', 'WORD', 'o', 'word', 'w', 'o', 'r', 'd']
```
- pop删除列表内容，按照索引位置，返回删除信息
```
In [50]: mylist.pop(4)
Out[50]: 'WORD'
In [51]: mylist
Out[51]: ['h', 'e', 'l', 'l', 'o', 'word', 'w', 'o', 'r', 'd']
```
- remove移除列表内容，不返回删除信息
```
In [53]: mylist.remove('word')
In [54]: mylist
Out[54]: ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'd']
```
- reverse反转列表
```
In [55]: mylist.reverse()
In [56]: mylist
Out[56]: ['d', 'r', 'o', 'w', 'o', 'l', 'l', 'e', 'h']
```
- sort排序
```
In [57]: mylist.sort()
In [58]: mylist
Out[58]: ['d', 'e', 'h', 'l', 'l', 'o', 'o', 'r', 'w']
```