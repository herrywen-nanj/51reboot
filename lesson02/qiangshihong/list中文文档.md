**.append** 
------
```
描述: L.append(object) -> None 
#将对象追加到结尾
类型:      builtin_function_or_method

##实例:
list = []          ## 空列表
list.append('Google')   ## 使用 append() 添加元素
list.append('Runoob')
print(list)
#以上实例输出结果：
['Google', 'Runoob']
```   
**.count**
------
```
描述:  L.count(value) -> integer 
#返回值的出现次数
Type:      builtin_function_or_method

##实例:
list = [123,'q',456,123,'rrr',123]
print(list.count(123))
#以上实例输出结果：
3
```  
**.extend** 
------
```
描述:  L.extend(iterable) -> None 
#用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
Type:      builtin_function_or_method

##实例:
l1 = [123,456,789]
l2= ['q','rrr','mm']
l1.extend(l2)
print(l1)
#以上实例输出结果：
[123, 456, 789, 'q', 'rrr', 'mm']
``` 
**.index** 
------
```
描述: L.index(value, [start, [stop]]) -> integer 
#返回值的第一个索引. 
#如果该值不存在, 抛错 ValueError
类型:      builtin_function_or_method

##实例:
aList = [123, 'ccc', 'aaa', 'abc']
print(aList.index( 'aaa' ))
#以上实例输出结果：
2
``` 
**.insert** 
------
```
描述: L.insert(index, object) 
#在索引之前插入对象
类型:      builtin_function_or_method

##实例:
aList = [123, 'aaa', 'bbb', 'abc']
aList.insert( 3, 2019)
print(aList)
#以上实例输出结果：
[123, 'aaa', 'bbb', 2019, 'abc']
``` 
**.pop**
------
```
描述:
L.pop([index]) -> item 
#删除并返回索引处的项 (默认值为最后一个)。
#如果列表为空或索引超出范围,抛错 IndexError 
类型:      builtin_function_or_method

##实例:
list1 = ['Google', 'Baidu', 'Taobao']
list_pop=list1.pop(1)
print(list_pop)
print(list1)
#以上实例输出结果：
Baidu
['Google', 'Taobao']
```  
**.remove** 
------
```
描述:
L.remove(value) -> None 
#移除列表中某个值的第一个匹配项
#如果该值不存在, 抛错 ValueError
类型:      builtin_function_or_method

##实例:
aList = [123, 'aaa', 'bbb', 'ccc', 'ddd']
aList.remove('bbb')
print(aList)
#以上实例输出结果：
[123, 'aaa', 'ccc', 'ddd']
``` 
**.reverse**
------
```
描述: L.reverse() 
#反向列表中元素
类型:      builtin_function_or_method 

##实例:
aList = [123, 'aaa', 'bbb', 'ccc', 'ddd']
aList.reverse()
print(aList)
#以上实例输出结果：
['ddd', 'ccc', 'bbb', 'aaa', 123]
```
**.sort**  
------
```
描述: L.sort(key=None, reverse=False) -> None 
#对原列表进行排序
类型:      builtin_function_or_method

##实例:
aList = [12, 100, 88, 0]
aList.sort()
print(aList)
aList.sort(reverse=True)
print(aList)
#以上实例输出结果：
[0, 12, 88, 100]
[100, 88, 12, 0]

##以下实例演示了通过指定列表中的元素排序来输出列表：
def takeSecond(elem):
    return elem[1]
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
print('排序列表：', random)
#以上实例输出结果如下：
排序列表：[(4, 1), (2, 2), (1, 3), (3, 4)]
```
