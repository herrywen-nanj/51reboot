### 字符串函数
```
In [1]: s1 = "www.51reboot.com"                                           # 统计字符出现的次数                      
In [2]: print(s1.count('ww')                           
1

In [3]: print(s1.count('w'))                                                                            
3
# 判断字符串中是否全是数字
In [4]: s1.isdigit()                                                    Out[4]: False

In [5]: s2='123'                                                    
In [6]: s2.isdigit()                             
Out[6]: True

In [35]: str2=1                                                         
In [36]: str2.isdigit()                                      
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-36-759af1eb6f78> in <module>
----> 1 str2.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'


# 判断是否全是小写
In [7]: s1.islower()                                                                                    
Out[7]: True

In [8]: s2.islower()                                                                                    
Out[8]: False

In [9]: s3="ABCD"                                                                                       
# 判断是否全是大写
In [10]: s3.isupper()                                                                                   
Out[10]: True

In [11]: s3="ABCd"                                                                                      

In [12]: s3.isupper()                                                                                   
Out[12]: False

# 字符替换
In [13]: s3.replace('BD','e')                                                                           
Out[13]: 'ABCd'

In [14]: s3.replace('BC','e')                                                                           
Out[14]: 'Aed'

In [15]: s1                                                                                             
Out[15]: 'www.51reboot.com'

# 判断字符串是否以指定字符开始
In [16]: s1.startswith('w')                                                                             
Out[16]: True

In [17]: s1.startswith('w1')                                                                            
Out[17]: False

# 判断字符串是否以指定字符结尾
In [18]: s1.endswith('com')                                                                             
Out[18]: True

In [19]: s1.endswith('com1')                                                                            
Out[19]: False

In [20]: s4="  www.51reboot.com"                                                                        

In [21]: s4.strip()                                                                                     
Out[21]: 'www.51reboot.com'

In [22]: s4.lstrip()                                                                                    
Out[22]: 'www.51reboot.com'

In [23]: s4.rstrip()                                                                                    
Out[23]: '  www.51reboot.com'

```

### 字符串format方法
```
In [58]: with open(FILENAME) as fd: 
    ...:     for line in fd: 
    ...:         lineArr = line.split(':') 
    ...:         print('{:<10} {:^} {:>30} {:>30}'.format(lineArr[0],lineArr[2],lineArr[5],lineArr[6])) 
    ...:
    
# :^ 居中显示
# :< 左对齐
# :> 右对齐
# 以上{}中的数字表示为该匹配到字符串预留的位数
```
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/format-duiqi.png?raw=true)

### 字符串 == is  比较

- is 是比较两个对象的内存地址是否相同
- == 是比较两个对象的值是否相等

![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/str%3D%3Dis-1.png?raw=true)

![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/str%3D%3Dis-2.png?raw=true)

###### 总结：python给小整数和不带空格的字符串开了小灶


### 赋值、深拷贝、浅拷贝
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E8%B5%8B%E5%80%BC.png?raw=true)

![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E6%B5%85%E6%8B%B7%E8%B4%9D.png?raw=true)

![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E6%B7%B1%E6%8B%B7%E8%B4%9D.png?raw=true)

### 变量生命周期
- 生命周期定义
```
变量从被创建到被系统回收的过程
```
- 局部变量的生命周期
  - 局部变量在函数执行时才被创建，函数执行结束后局部变量被系统回收
  - 局部变量在生命周期内，可以用来存储函数内部的临时使用的数据
- 全局变量的生命周期
  - 程序运行时开始创建，程序退出时销毁
 
### 变量的作用域
- 介绍
```
在Python程序中创建，改变，查找变量名时，都是在一个保存变量名的空间中进行，我们称之为命名空间。也叫作用域
```


- 分类：
  - 全局：在函数外部定义
  - 局部：在函数内部定义

- LEGB法则
  - L local局部作用域 ---> b = 0
  - E （Enclosing functionlocale） 嵌套作用域  --->函数嵌套，外层函数的局部变量作为内层函数的全局变量
  - G （Globalmodule）全局作用域 global
  - B Buildin python内置模块的作用域
- 搜索变量名优先级：局部作用域 > 嵌套作用域 > 全局作用域 > 内置作用域
- 变量由内到外，先找自己的作用域的变量，然后上级寻找，仍未找到报错NameError

### global nolocal
- 如果内部函数有引用外部函数的同名变量或者全局变量,并且对这个变量有修改.那么python会认为它是一个局部变量。
```
In [140]: def global_test(): 
     ...:     gcount += 1 
     ...:     print(gcount) 
     ...: global_test()                                                                                 
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
<ipython-input-140-62191078ed67> in <module>
      2     gcount += 1
      3     print(gcount)
----> 4 global_test()

<ipython-input-140-62191078ed67> in global_test()
      1 def global_test():
----> 2     gcount += 1
      3     print(gcount)
      4 global_test()

UnboundLocalError: local variable 'gcount' referenced before assignment

```
- 呈上，声明全局变量，如果在局部要对全局变量修改，需要在局部也要先声明该全局变量：
```
gcount = 0#第一行定义了一个全局变量，（可以省略global关键字）

def global_test():
    global gcount#在内部函数中申明gcount为全局变量
    gcount +=1
    print (gcount)#打印的值为全局变量值为1
global_test()
print gcount#打印的值为全局变量值为1

output: 
1
1
```
- 在局部如果不声明全局变量，并且不修改全局变量。则可以正常使用全局变量：
```
In [139]: gcount = 0                                                                                    
In [141]: def global_test(): 
     ...:     #gcount += 1 
     ...:     print(gcount) 
     ...: global_test()                                                                         
0
```

- nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量
  - 简而言之，nonlocal的作用：在一个函数中调用另一个函数的私有化变量
```
def make_counter(): 
    count = 0 
    def counter(): 
        nonlocal count 
        count += 1 
        return count 
    return counter 

def make_counter_test(): 
    mc = make_counter() 
    print(mc())
    print(mc())
    print(mc())

make_counter_test()
```

- global 当在全局调用，即非函数体内，在局部之外调用的变量
```
def scope_test():
    def do_local():
        spam = "local spam" #此函数定义了另外的一个spam字符串变量，并且生命周期只在此函数内。此处的spam和外层的spam是两个变量，如果写出spam = spam + “local spam” 会报错
    def do_nonlocal():
        nonlocal  spam #其它函数或作用域内可以调用这里申明的spam变量
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"#global全局变量在函数体内或者作用域内不可调用，仅可在全局调用
    spam = "test spam"
    do_local()
    print("After local assignmane:", spam)
    do_nonlocal()
    print("After nonlocal assignment:",spam)
    do_global()
    print("After global assignment:",spam)

scope_test()
print("In global scope:",spam)
outputs: 
After local assignmane: test spam#私有变量在函数外不可调用，故spam依旧是test spam
After nonlocal assignment: nonlocal spam#scope_test()函数体内调用的spam是nonlocal spam
After global assignment: nonlocal spam#scope_test()函数体内调用的spam是nonlocal spam
In global scope: global spam#跳出scope_test()函数之外，为全局变量故spam是global spam
```

- 函数1申明的全局变量q若要在函数2中修改，必须在函数2中再次申明全局变量q，表示修改外部的全局变量q
```
def add_b():
    global  b
    b = 0
    def do_global():
        global  b
        b = b + 1
        print(b)
    do_global()
    print(b)
add_b()
outputs:
1
1
```

### 变量作用域总结
- def class lambda 是 改变变量作用域的代码段
- 在if - elif -else, for-else,while,try-except等关键字的语句块中并不会产生作用域

### 闭包
```
在一个外函数中定义一个内函数
内函数里运用了外函数的临时变量
并且外函数的返回值时内函数的引用
```
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E9%97%AD%E5%8C%85%E5%87%BD%E6%95%B0.png?raw=true)

### 装饰器
- 装饰器参数介绍1
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E8%A3%85%E9%A5%B0%E5%99%A8.png?raw=true)

- 装饰器参数介绍2
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/%E8%A3%85%E9%A5%B0%E5%99%A8-2.png)

- 装饰器参数介绍3
![image](https://github.com/niushaoshuai/stand_file/blob/master/youdao-pic/%E8%A3%85%E9%A5%B0%E5%99%A8-3.png?raw=true)

- 装饰器实战1
```
这个函数的作用在于可以给任意可能会hang住的函数添加超时功能，这个功能在编写外部API调用 、网络爬虫、数据库查询的时候特别有用

import signal, functools #下面会用到的两个库
 
class TimeoutError(Exception):      # 定义一个Exception，后面超时抛出 
    pass 

def timeout(seconds, error_message = 'Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
      
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)        # 为信号绑定一个处理函数.
            signal.alarm(seconds)                                 # 多长时间触发SIGALRM信号.
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)                                   # 取消SIGALRM信号，不在继续抛出异常.
            return result
        return functools.wraps(func)(wrapper)
    return decorated
使用：

@timeout(5) # 限定下面的slowfunc函数如果在5s内不返回就强制抛TimeoutError Exception结束.
def slowfunc(sleep_time):
  import time
  time.sleep(sleep_time) #这个函数就是休眠sleep_time秒.

slowfunc(3) #sleep 3秒，正常返回 没有异常.


slowfunc(10) #被终止 

## 输出 
---------------------------------------------------------------------------
TimeoutError                              Traceback (most recent call last)
```
- 装饰器实战2
```
摘录 知乎pc大神
有时候出于演示目的或者调试目的，我们需要程序运行的时候打印出每一步的运行顺序 和调用逻辑。类似写bash的时候的bash -x调试功能,然后Python解释器并没有 内置这个时分有用的功能，那么我们就“自己动手，丰衣足食”。

import sys,os,linecache
def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call": 
            return localtrace
        return None
        
    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace 
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print "{}({}): {}".format(  bname,
                                        lineno,
                                        linecache.getline(filename, lineno).strip('\r\n')),
        return localtrace
        
    def _f(*args, **kwds):
        sys.settrace(globaltrace)
        result = f(*args, **kwds)
        sys.settrace(None)
        return result
    return _f
使用：

@trace
def xxx():
  print 1
  print 22
  print 333

xxx() #调用 

## 输出 
<ipython-input-4-da50741ac84e>(3):     print 1 # @trace 的输出 
1
<ipython-input-4-da50741ac84e>(4):     print 22 # @trace 的输出 
22
<ipython-input-4-da50741ac84e>(5):     print 333 # @trace 的输出 
33
```

```
# 什么时候使用装饰器.
如果你想对一个"原始函数"或"原始类"在不改变原有代码的情况下对其进行增加新功能，你可以考虑使用装饰器.

# 装饰器的特点
装饰器接收一个原始函数并返回一个被装饰后的函数
函数可以以参数的形式传递给装饰器
装饰器用@符号来声明

# 装饰器的应用场景
flask框架中路由的设定就是通过装饰器完成的。
flask框架中写后台程序时，判断用户是否需要登录，也可以用装饰器来完成。
```

### 可迭代对象
- 定义:
```
凡是返回一个迭代器（实现了__iter_方法_）的对象都可以称为可迭代对象
它并不是指某种具体的数据类型
```
- 语法:
```
iter（iterable）->迭代器
ITER（Callable，Sentinel）->迭代器
从对象中获取迭代器。在第一种形式中，参数必须
提供自己的迭代器，或者是序列。
在第二种形式中，调用被调用，直到它返回sentinel。
```
### 迭代器
- 定义:
  - 任何同时实现了__iter__ 和__next__方法的对象都是迭代器
  - __iter__返回迭代器自身，__next__返回容器的下一个值，如果容器中没有更多元素了，则跑出StopIteration异常
  - 迭代器是一种带状态的对象

- range是可迭代对象

### 生成器
- 生成器是Python最吸引人的特性之一
- 生成器是一种特殊的迭代器
- 生成器和迭代器的区别：
  - 生成器一定是迭代器，但迭代器不一定是生成器
  - 迭代器要同时实现__iter__和__next__方法，但生成器只需要一个yield关键字即可

### 多进程、多线程、协程
- 引入GIL概念
```
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing 
Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. 
(However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)

GIL(Global Interpreter Lock) 全局解释器锁 阻止Python.
阻止原生线程并发执行Python字节码，因为cPython内存不是线程安全的。多线程序列化阻止它的并发.
```
- 为什么要有GIL
```
由于物理上得限制，各CPU厂商在核心频率上的比赛已经被多核所取代。为了更有效的利用多核处理器的性能，就出现了多线程的编程方式，而随之带来的就是线程间数据一致性和状态同步的困难。
Python当然也逃不开，为了利用多核，Python开始支持多线程。而解决多线程之间数据完整性和状态同步的最简单方法自然就是加锁。 于是有了GIL这把超级大锁
```
- GIL的影响
```
很多人的概念里CPython就是Python，也就想当然的把GIL归结为Python语言的缺陷。所以这里要先明确一点：GIL并不是Python的特性，Python完全可以不依赖于GIL
CPYTHON的实现GIL的方式添加一个防止多线程并发执行机器码的一个Mutex，乍一看就是个BUG般存在的全局锁嘛
GIL无疑就是一把全局排他锁。毫无疑问全局锁的存在会对多线程的效率有不小影响。甚至就几乎等于Python是个单线程的程序。
```

### 多线程 多进程 协程相关的原理概念
- 核心
  - 线程是调度的基本单位
  - 进程是资源管理的基本单位
- 资源
  - 内存
  - 信号处理
  - 文件描述符
  - 进程锁
  - socket
  - ...
  ```
  进程与资源通信，线程与cpu通信
  操作系统分配的资源都是进程，进程中的线程共享进程中的资源
  操作系统调度线程而非进程
  一个进程下的所有线程共享同一个地址空间资源
  ```
### 地址空间资源
- 内存资源
- 文件描述符fd
- 共享代码
- 进程用户ID(UID)与线程组ID(PGID)

### 并发与并行的区别
```
单核也可以并发，但是单核不能并行，只有多核才能并行
```

### 线程轻量
- 内存占用开销小
- 灵活上下文切换
  - 用户态线程 协程 不参与内核的上下文切换

### 多线程模块threading - 适用于IO密集型
![image](https://raw.githubusercontent.com/niushaoshuai/stand_file/master/youdao-pic/threading.png)

### 计算机的任务有两种IO和计算
```
# 分类
IO密集型   -> 有读有写，比如爬虫.
计算密集型   -> 计算排序.

# 阐释两类
(1)为什么IO密集型能够利用多线程？
下一个线程有效的利用了上一个线程的等待IO的时间，伪并发，要比单线程高很多.

(2)计算密集型
执行效率非常低
CPU要比IO快很多很多，因此几乎没有等待上个线程的等待时间，创造线程还需要时间等.
CPU密集型任务：多线程效率往往比单线程还低.

(2.1) 解决计算密集型计算的方法
1. 通过ctypes来解决，绕过了GIL的限制.
2. 多进程的方式 multiprocessing
```

### 多进程模块multiprocessing -适用于计算密集型
```
文件描述符 file descriptor
在linux内，对所有设备或者文件的操作都是通过文件描述符进行的.

多进程 主进程fork子进程 子进程继承主进程的文件描述符(文件位置、偏移量)
```
```
import multiprocessing as mp
def job(q):
    res = 0
    for i in range(1000):
        res += i + i ** 2 + i ** 3
    q.put(res)

if __name__ == '__main__':
    # 设置队列
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))  # 注意当参数只有一个时，应加上逗号
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    # q,<class 'multiprocessing.queues.Queue'>
    # 依次从队列中取值
    res1 = q.get()
    res2 = q.get()
    print(res1 + res2)
```
### 协程

```
协程不同于线程，线程是抢占式的调度，而协程是协同式的调度，协程需要自己做调度。

协程没有线程的安全问题，一个进程可以同时存在多个协程，但是只有一个协程是激活的，而且协程的激活和休眠又程序员通过编程来控制，
而不是操作系统控制的，

协程是用户空间线程，操作系统其存在一无所知，所以需要用户自己去调度，用来执行协程多任务非常合适

Python3.4中，引入了asyncio包，这个包提供了关于事件循环的实现，这就使得在Python中使用协程实现高并发成为可能
```
