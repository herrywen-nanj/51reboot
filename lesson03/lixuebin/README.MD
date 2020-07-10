# 第三次作业

## 功能实现:

1. 将列表转换为字典
2. 分页 --> 根据page和pagesize 进行分页并优雅输出 --> 对分页数量进行判断,超出后提示
3. 持久化数据 --> 默认在数据更改后会自动持久化, 导入数据和清空数据会询问是否永久保存
4. 异常处理 --> 对整个程序的所有操作异常处理
5. 优雅格式化输出 --> 从登陆后的命令提示界面到列表查询,到分页,全部优雅格式化输出
6. 支持导出数据到csv --> 支持自定义/默认路径和文件名 --> 导出后判断文件是否存在 --> 提示成功或失败
7. 记录登陆日志 --> 登陆成功 --> log/login.log  登陆失败 --> log/loginFail.log
8. 记录操作日志 --> 对add, update, delete, clear, export, import操作进行记录
9. 统计用户数量
10. 清空用户 --> 临时清空 --> 可以reload加载 --> 询问是否永久清空 --> 直接修改文件永久清空
11. 支持从cvs中导入数据 --> 文件存在 --> 文件格式校验 --> 重复数据校验

## 用法描述和命令

| Serial | Description | Command |
| :------: | ----------- | ------- |
| 1 | Add user info | add username age tel email |
| 2 | Delete user | delete username |
| 3 | Update user info | update username set (age\|tel\|email) = new value          |
| 4 | Find user info | find username |
| 5 | Show tables | list |
| 6 | Pagination display | display page 1 pagesize 5 |
| 7 | Count of users | count |
| 8 | Clear users table | clear |
| 9 | Reload when temporarily emptied | reload |
| 10 | Export csv file | export [path/filename].Default "csv/UserData+unixtime.csv" |
| 11 | From csv file import data | import "path/filename" |

```
+--------+---------------------------------+------------------------------------------------------------+
| Serial | Description                     | Command                                                    |
+--------+---------------------------------+------------------------------------------------------------+
|   1    | Add user info                   | add username age tel email.                                |
|   2    | Delete user                     | delete username.                                           |
|   3    | Update user info                | update username set (age|tel|email) = new info.            |
|   4    | Find user info                  | find username.                                             |
|   5    | Show tables                     | list.                                                      |
|   6    | Pagination display              | display page 1 pagesize 5.                                 |
|   7    | Count of users                  | count.                                                     |
|   8    | Clear users table               | clear.                                                     |
|   9    | Reload when temporarily emptied | reload.                                                    |
|   10   | Export csv file                 | export [path/filename].Default "csv/UserData+unixtime.csv" |
|   11   | From csv file import data       | import "path/filename"                                     |
+--------+---------------------------------+------------------------------------------------------------+

```

## 课堂笔记

****

### 第三课
- range()函数

  ```
  range是Python内置函数,只接受数字
  range(stop)					# 默认start从0开始
  range(start, stop)			# 指定start从start开始
  range(start, stop[, step])	# 可以指定step步长
  ```



- prettytable
    地址: https://github.com/jazzband/prettytable

  ```
  格式化输出的第三方库,直接输出表格

  x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
  x.add_row(["Adelaide",1295, 1158259, 600.5])
  x.add_row(["Brisbane",5905, 1857594, 1146.4])
  x.add_row(["Darwin", 112, 120900, 1714.7])
  x.add_row(["Hobart", 1357, 205556, 619.5])
  x.add_row(["Sydney", 2058, 4336374, 1214.8])
  x.add_row(["Melbourne", 1566, 3806092, 646.9])
  x.add_row(["Perth", 5386, 1554769, 869.4])
  ```

- 字符串方法

  - join和split

    ```
    join()将可迭代对象按指定字符转换为字符串
    " | ".join("hello", "world")
    "hello | world"

    split()将字符串按指定的字符转换为列表
    L = ["hello", "world"]

    ```


#### 字典

- 定义: 字典是一种可变容器,可存储任意类型的对象
- 字典的每个键值对用冒号分隔,没个对之间,用逗号分隔,整个字典使用花括号{}
- 字典的key键必须是唯一的
- 值是任意数据类型
- key键必须是不可变元素,例如数字,字符串,元组 但是list列表是可变的不可以当键
- 如果字典里没有键的访问数据,会报错
- 字典是无序的





#### 操作

- 定义字典

  ```
  d = {"name":"zhangsan",'age':18}
  ```

- 访问字典

  ```
  1. 字典名字加中括号[key]对字典进行访问
  	d['name']
  	zhangsan
  2. 使用get()方法进行访问
  	get()方法对字典进行访问
  	d.get('name'[,返回值])
  	返回值可以定义,默认是None,如果列表中存在这个键值对则返回值,如果键值对不存在,则返回定义的返回值,默认None

  	此方法在http里用的较多,参数可选设置默认值

  ```

- 修改字典

  ```
  1. 使用d['key'] = '新值'对字典进行修改
  2. 使用d.update({'name':'liubei'})进行修改
  ```

- 删除字典

  ```
  1.d.pop(key[, 值]) 根据指定的键删除值,并返回这个值,如果没有找到key,并且没有指定返回值,则报KeyError异常,如果键没找到,给定了值,则会给出指定的值

  2.del语句删除
  	del d['name'] 删除name键
  ```

  ​

#### 方法

```
d.keys()  打印所有的key

d.values() 打印所有的value

d.items() 将字典里的键值对当成元组组成一个列表

for 对字典进行循环时, 只循环key 需要对值进行循环

python支持多变量赋值
```

#### 字典推导式

将for循环放进字典里



#### 错误和异常

- 错误语法错误,影响程序运行,不能被编译
- 异常是运行时发生的错误

### 捕获异常

```
try:
	语句
except:
	语句
except ValueError:
	print("value error")
except IndexError:
	print(index error)
except Exception as e: # Exception捕获全局错误
	print(e)
else:
	print("success")
	#如果没有异常,则会走else语句
finally:
	print("It is finally")
	#无论如何都会始终运行的语句



当多个异常类型需要捕获可以写做
except (ValueError,IndexError):


# 异常捕获,使用try:except语句进行捕获.用来防止程序正常运行时退出.使用except对错误类型进行,判断.Exception是全局错误类型.
```



## 文件读写

- 打开文件
  - `fd = open("filename", "w") # w写,r读`
- 操作文件
  - 读
    - `fd.read()`
  - 写
    - 写操作值能接收字符串类型
    - `fd.write("1\n")`
- 关闭文件
  - `fd.close()`

### 常用模块

#### 标准模块

- **json**

  ```
  json.dumps()	将列表转换为字符串

  json.loads()	将json.dumps()写入的字符串转换为列表


  json.dump("",fp)		将数据以序列化的形式写入文件,文件是必须存在的
  json.load(fp)		读数据
  ```

- **os**

- **sys**

- **datetime**

  ```
  现在时间: nowtime = datetime.datetime.now()
  将日期转成字符串: nowtime.strftime(%Y-%m-%d %T)
  ```

![脑图](xmind/Python-3.png)




