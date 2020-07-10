# 作业

## 1: 用户管理系统 v2
```bash
1. 数据结构：列表 -> 字典；
2. 分页 display page 1 pagesize 5
3. 文件持久化
4. 异常处理
5. PrettyTable 优雅的格式化输出
6. 扩展：导出csv(可写可不写)
```

# 笔记

## range 用法

range(start,end)  # 没有start default 0， 从start到（end-1），start,end-->int 

#### 9*9乘法表

 ```python
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end=" ")

```

## PrettyTable

安装 pip3 install PrettyTable

```python
from prettytable import PrettyTable
# x=PrettyTable() # 创建表
#  按行/列添加数据：
#     tb.add_row( <llist> )
#     tb.add_column( <llist> )

x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
x.sortby = "Population" #排序字段
x.reversesort = True   # 排序
x.int_format["Area"] = "04d"  # 格式化数据
x.float_format = "6.1f" # 保留小书店一位
x.align["City name"] = "l" # Left align city names  ，左对齐
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)


```

## 字典
```python
# 元组可以当key
{(1,2,3):"元组可以当key"}
# 字典无序

dict.get() # 获取，key对应的value，没有返回指定值
dict.pop() # 删除指定元素key，不指定删除最后一个
dict.items()  #
dict.values() # 获取所有value，返回list
dict.keys()   # 获取所有key，返回list
dict.update()  # 更新 dict.update("age",18)
dict.copy()    # 浅拷贝
dict.clear()   # 清空字典
dict.setdefault() # 
dict.popitem()
dict.fromkeys()
dict.mro()

d={v:k for k,v in d.items()} # 字典推到式
```

## 异常处理
```python
s2="hello"
try:
    # int_num=int(s2) # ValueError
    1+"2" # TypeError
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
except Exception as  e:
    print(e)
else:
    print("所有异常都捕获不到走这里")
finally:
    print("最后走这个，总会执行")

```
## 文件操作
```python
# 写文件
open(file="文件名",mode='w',encoding=None,errors=None,newline=None,closefd=True)
fd=open("test.txt",'w')
fd.write("1\n")
fd.write("2\n")
fd.write("3\n")
fd.close()
# 读文件
f=open("text.txt","r")
data=f.read()

```


## 模块
```python
import os
import json
import sys

````

### 标准模块
### json
```python

import json

json.dumps() 
json.loads()

```
#### datetime

```python
import datetime
dtime=datetime.datetime.now() #当前时间
dtime.strftime("%Y-%m-d% %H:%M:%S") # 格式化时间


```

### 第三方模块




