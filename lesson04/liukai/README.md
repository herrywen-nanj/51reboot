#### 1 序列化

json 和 pickle

JSON 只能出来基本数据类型， Pickle 可以出来所有python数据类型，

json.dumps()  序列化之后是字符串， pickle.dumps() 序列化后是二进制


#### 集合

集合内数据必须是不可以变的，无序的，元素不重复,可修改

{1,2,3,4,5}

空集合 set()

可循环的都是可迭代的

操作：add clear pop remove difference 差集 intersection 交集 union 并集

#### 内置函数

sum enumerate|range random

sum 求和: sum([1,2,3,4,5])

enumerate|range 

enumerate 去列表索引，

for i,v in enumerate(Array):
    print(i,v)

sum(list(range(1,101)))

sum(list(range(0,101,2)))

random 随机

r=random,random() 生成0-1之间浮点数

r=random.uniform(1,100) 指定范围内的浮点数

r=random.randint(1,100)生成范围内的整数

### 文件操作

fd=open('file','rb') #byte

fd.read(size=-1,/) # 全部读完

fd.read(10)  # 读10个字节

fd.readline()  读一行

fd.readlines()  返回list,每一行是list的一个元素

#### 文件指针

fd.fileno()  返回一个整型的文件描述符
fd.tell() #  当前文件指针位置
fd.seek(5，1)  #移动到指定指针

### 内置函数

time

time.ctime()

time.localtime()

time.sleep(3)

datetime

datetime.now() 当前时间

datetime.now().strftime()'%Y

datetime.datetime,now()+datetime.timedelta(days=1)

os 

os.path.exists() 判断文件是否存在

os.path.isfile()  判断是否是问题

os.path.isdir()  判断是否是目录

os.path.abspath() 获取文件绝对路径

os.path.join(dir,filename) 拼接

os.listdir('/usr/local)   相当于 ls

os.walk('/usr/local/')  返回 dirpath ,dirnames,filename 

os。getsize（） 返回文件大小





logger





### 函数 

def 函数名(arg):
        函数题

函数名，函数参数，返回值

def f1():
    s="hello"
    return s
    

位置参数 
 
def opt(x,y):

     return x+y

关键字参数，

def opt(x=2,z=3):

    return z-y
    
def f3(x,y,z=100):

    return x+y+z 

f3(1,2)

可变参数

def f1(*args):

    print(args)
    
def d2(**kwargs):

    print(kwargs)
    
    
*tuple,**dict ，用*，** 解包

你们函数

lamdba  

f=lamdba x,y:x+y

s=f(2,3)

排序 sorted

sorted(dict.items(),key=lambda x:x[1],reverse=True)


#### 列表生成式

[x  for x in arr if x % 2 != 0]


#### 字典生成式

{k:v for k,v in d.items()}

#### 集合生成式

arr=[1,2,3]

{x**2 for x in arr}

#### 元组生成器

（x**2 for x in arr）


### 作业

把第三天作业用def实现






    
   











