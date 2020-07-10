## 1、 用户管理系统 v5
```bash
1. 支持配置文件管理方式 
- ConfigParser
2. 存储方式 由文件 改成 数据库
- PyMySQL
```

## 注释

- 用户管理修改：当用户不输入直接回车，则该选项还是延续以前的。
- 用户管理添加的用户程序里做了用户名唯一的判定，所以增加和删除、修改都是以用户名为唯一点。
- 程序中对手机号、性别、电子邮件、年龄都做了判定。保证其符合常理。

### 实现效果

- 用户管理系统执行添加和显示

![image](https://github.com/luojunquan/Image/blob/master/images/1.png?raw=true)

- 用户管理系统执行修改

![image](https://github.com/luojunquan/Image/blob/master/images/%E4%BF%AE%E6%94%B9.png?raw=true)

- 用户管理系统执行删除

![image](https://github.com/luojunquan/Image/blob/master/images/%E5%88%A0%E9%99%A4.png?raw=true)

- 主机信息搜集入数据库

![image](https://github.com/luojunquan/Image/blob/master/images/server_information.png?raw=true)

- 用户信息数据库图

![image](https://github.com/luojunquan/Image/blob/master/images/users.png?raw=true)


