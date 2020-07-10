[TOC]

## 用户管理系统

```
1. 登录认证；
2. 增删改查和搜索
    3.1 增 add           # add monkey 12 132xxx monkey@51reboot.com
    3.2 删 delete        # delete monkey
    3.3 改 update        # update monkey set age = 18
    3.4 查 list          # list
    3.5 搜 find          # find monkey
    3.6 分页             # display
    3.7 存储 save        # save
    3.8 加载 load        # load
    3.9 退出 exit        # exit
3. 格式化输出
4. 日志记录
```

### 技术点

**难点**

```
输入信息 字符串 -> 列表
分页 字典-> 列表
```


#### 函数返回值传入

```
info,ok = fuction()
info 为 返回的信息
ok 为 Bool值，可以进行判断
```

#### 分页

```
分页的业务逻辑，不是很明白，所以直接写的比较简单粗暴一点了
只是将字典转换为了列表
```

#### 日志

```
只做了部分的日志
```
