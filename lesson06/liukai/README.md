### lesson6

#### 字符串内存地址
 ![image]('https://github.com/51reboot/xly1/blob/master/lesson06/liukai/WechatIMG39.png')

#### 深拷贝浅拷贝

Python中对象的赋值都是进行对象引用（内存地址）传递
使用copy.copy()，可以进行对象的浅拷贝，它复制了对象，但对于对象中的元素，依然使用原始的引用.
如果需要复制一个容器对象，以及它里面的所有元素（包含元素的子元素），可以使用copy.deepcopy()进行深拷贝
对于非容器类型（如数字、字符串、和其他'原子'类型的对象）没有被拷贝一说
如果元祖变量只包含原子类型对象，则不能深拷贝

#### 全局变量/局部变量生命周期

全局变量，函数外部，程序结束 ，生命周期结束。  
局部变量，在函数内，函数结束，生命周期结束

#### 变量作用域

LEGB , L局部作用域，E嵌套作用域，G全局作用域，B内置作用域   
局部作用域>嵌套作用域>全局作用域>内置作用域

```python

a=100

def change():
    # global a
    a=a+100
    print(a)

change()   #  会报错，,在局部修改全局的变量，需要先声明，加 global 
```

局部可以使用全局变量，但是修改全局变量修改加global

嵌套作用域

```python
a=100
def f1():
    a=200
    def f2():
        print(a)
    f2()

f1()

###############

a=100
def f1():

    a=200
    def f2():
        # global a  # 声明全局变量
        nonlocal  a  # 声明嵌套变量
        a+=20
        
        print(a)
    f2()

f1()

# >>> 120
# >>> 220  nonlocal  声明为嵌套变量

```
nonlocal  声明为嵌套变量

#### 闭包
在一个外函数中定义了一个内函数， 内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用

```python
def f1():
    num=100
    def f2():
        nonlocal num
        num+=100
        return num
    return f2
    
f=f1()
print(f())
print(f())
print(f())

# >>> 101
# >>> 102
# >>> 103

```

#### 装饰器
```python

def fun1(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)

    return wrapper
    
@fun1 #使用
def f2():
    pass

```

#### 可迭代对象

iter()

同dir()查看，实现了__iter__ 方法

#### 迭代器

  实现了__iter__  ，__next__ 方法
  
  range是迭代对象
  
#### 生成器

一种特殊的迭代器

生成器只需要yield

```python
def fditer():
    with open('/etc/passwd','r') as fd:
        for line in fd:
            yield line
            
for i in fditer():
    print(i)

```

### 多线程，多进程

https://github.com/467754239/python/tree/master/threads

os.fork  启一个进程
 
 multiprocessing 多进程
 
 gevent 启动携程
 
 GiL 全局解释器锁

同一时间内，cup能调度一个线程，

threading.Thread()  
th.start()  
th.join() 
th.setDaemon() 设置此线程是否被主线程守护回收，默认false不回收，需要在start方法前调用，这是为true相当与当前主席看出中注册
守护，当主线程结束时会将其一并回收

### 面向对象

类，对象

类型的特性：封装，继承，多态

```python
class People(object):
    # def __new__(cls)
    # def __del__(self ,*args) #析构函数 ，销毁一个对象时调用
    
    Name="123131"

    def __init__(self,name,age,height):  # 构建函数，定义类数学，初始化对象
        self.name=name
        self.__age=age # 私有属性
        self.height=height
        
    def say(self):
        return "my name is {},{} years old".format(self.name,self.__age)
        
    @classmethod
    def get_gae(cls):
        return cls.Name
        
    @property 
    def get_height(self):
        return self.height

  
  
p=People("lk",18,'140') # 事例化对象 默认调用__new__方法，
print(p.say())

print(People.get_gae())
print(p.get_height)

```

```python

class Cp(object):
    
    def __init__(self,age):
        self.age=age
        
    def __eq__(self, other):
        return self.age==other.age
        
    def __add__(self, other):
        return self.age+other.age
        
    def __str__(self):
        return  "xxxx"
    
    def __dir__(self):
        return []

x1=Cp(20)
x2=Cp(20)
print(x1==x2) #>>> True
print(x1+x2) #>>> 40
print(x1)   #>>>"xxxx"  __str__  
print(dir(x1))  # >>> []

```
对象比较运算符
```python

__cmp__ # 包含所有的比较情况  
__eq__  # 单一比较 等于  
__lt__  # 小于  
__gt__  # 大于   
__add__    
__sub__  
__mul__  
__div__    
__or__  
__and__ 
```
继承
```python

class Programmer(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Python(Programmer):
    def __init__(self):
        super().__init__()

```
 




