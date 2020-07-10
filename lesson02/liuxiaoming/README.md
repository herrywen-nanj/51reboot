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

```python
str.count(sub, start=0, end=len(str))

>>>>s = "aaabbb345"
>>>>s.count("a")
3
```
### .startswith

```python
str.startswith(prefix, start=0, end=len(str))

>>>>s.startswith("a")
True
```

### .endswith

```python
str.endswith(suffix, start=0, end=len(str))

>>>>s.endswith("a")
False
```
### .find

```python
str.find(sub, start=0, end=len(str))

>>>>s.find("b")
3
```

### .format

```python
>>>>"{}, {}, {}".format(s[2], s[6], s[8])
a, 3, 5
```

### .index

```python
str.index(sub, start=0, end=len(str))

>>>>s.index("4")
7
```

### .isdigit
```python
str.isdigit()

>>>>s.isdigit()
False
```


### .islower
```python
str.islower()

>>>>s.islower()
True
```

### .isupper
```python
str.isupper()

>>>>s.isupper()
False
```

### .join
```
str.join(iterable)
```

### .upper

> S.upper()
```
>>>>s.upper()
AAABBB345
```
### .lower
```pythonh
str.lower()

>>>>s.lower()
aaabbb345
```

### .lstrip
```
str.lstrip(chars)
```

### .replace
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
```python
str.ljust(width, fillchar)

>>>>s.ljust(20, ".")
aaabbb345...........
```

### .rjust
> S.rjust(width, fillchar)
```python
>>>>s.rjust(20, ".")
...........aaabbb345
```
### .split

```
 S.split(sep=None, maxsplit=-1)
 
 >>>>s = "abcdefg"
 >>>> s.split(sep="b")
 ['a', 'cdefg']
```
### .strip

> S.strip([chars])
```

```

## 1.2，列表方法 
>>> dir(list)    

### .append



### .extend

```python
>>> name = list("teed")
>>> 
>>> name
['t', 'e', 'e', 'd']

>>> name.extend(list('5421'))
>>> 
>>> name
['t', 'e', 'e', 'd', '5', '4', '2', '1']
```


### .insert

```python
>>> name.insert(1, 'SB') 
>>> name
['t', 'SB', 'e', 'e', 'd', '5', '4', '2', '1']
```

### .pop
```python
>>> name.pop()
'1'
>>> 
>>> name
['t', 'SB', 'e', 'e', 'd', '5', '4', '2']
>>> 
```

### .remove
```python
>>> name.remove('SB')
>>> name
['t', 'SB', 'e', 'e', 'd', '5', '4', '2', '1']

>>> name.remove('w')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>>
>>> name.remove('w', 'i')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: remove() takes exactly one argument (2 given)
```

### .reverse

```python

>>> name.reverse()
>>> name
['t', 'SB', 'e', 'e', 'd', '5', '4', '2', '1']
```

### .sort


```python
>>> name.sort()
>>> name
['t', 'SB', 'e', 'e', 'd', '5', '4', '2', '1']

